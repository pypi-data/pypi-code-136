import re
from rats.core.RATS_CONFIG import splitchar, dfpath, packagepath, packet_format_dictionary, LLCEDB, LLCEDBFormat
import rats.core.topoparser as topo
import pandas as pd
import numpy as np
from rats.core.errors import RatsError
import pyarrow as pa
import pyarrow.parquet as pq
import json
import datetime


class RatsParser:
    meta_key = 'Waters_RATS_visualiser'
    metadata = {'parse_completed_without_error': False,
                'gds_protocol_version': 0,
                'gds_packet_format': {},
                'errors': False,
                'log': '',
                }
    dataframe: pd.DataFrame
    gds_protocol_version: int
    different_to_n_dataframes: int = 0  # USED IN SESSION DATA TRACKER
    packet_format: None

    def __init__(self, filepath=None, data_directory=packagepath / dfpath, formats: dict = packet_format_dictionary):

        self.filepath = filepath
        self.filename = filepath.split(splitchar)[-1].split('.')[0]

        self.data_directory = data_directory
        self.packet_format_dictionary = formats

    def _determine_LLC_bit_format(self):
        """In this function, there will be the capability to read topo files and report on the format of the
        LLC rats input... for now this is delegated to the RATS_CONFIG file"""
        pass

    def _create_partitioned_dataframe(self):
        """
        Takes the .txt file and reads it into a dataframe where every line has an associated packet number.
        outputs a dataframe with two columns; 'packet_number' and bytes. all the bytes for a single packet
        will be joined up downstream
        """
        regex_match_for_validity = re.compile('[$]') # would be possible to use this if the inter-packet verbiage was not present.. change $ to relevant characters
                                                     # i.e. if the files take on only the ICS format, use '[^A-Za-z0-9-]'
        series_stream = []
        with open(self.filepath, 'r') as f:
            # Create a list of every line in the .txt file
            line = f.readline()
            while line:

                if regex_match_for_validity.match(line):
                    self.metadata[
                        'log'] += f'{datetime.datetime.now()}: The text file has some unexpected characters ' \
                                  f'in it\n'
                    raise RatsError
                series_stream.append(line.strip())
                line = f.readline()

        packet_separator = ['-', ']', ':']
        # lines in the .txt file which start with these characters can be rejected - might add to config later
        df = pd.DataFrame(series_stream, columns=['bytes'])
        df = df[~df['bytes'].str.contains('|'.join(packet_separator))]
        # Use dataframe filtering to reject any line which contains one of the characters in reject_characters
        df['index_count'] = df.index.values
        deltas = df['index_count'].diff()[1:]
        gaps = deltas[deltas > 1]
        # Where the difference in the index is greater than 1, a new packet started
        packet_number_dictionary = {gaps.index.values[i]: i + 1 for i in range(len(gaps.index.values))}
        # gaps.index.values[i] is an index to the line on which the individual packets started
        # i iterates and yields the actual packet number to be mapped to the main dataframe
        # This is hard to explain....
        df['packet_number'] = df.index.map(packet_number_dictionary)
        df.reset_index(inplace=True)
        df.fillna(method='ffill', inplace=True)
        # each line of the dataframe, at the first line of each packet, has an iterative integer. This ffill method
        # propagates the packet number so that each line, which represents a line in the .txt file, is labelled
        # with the correct packet number
        df['packet_number'].fillna(0, inplace=True)
        # ffill might leave line 0 with a NaN value, so make sure it's 0
        df.drop('index_count', axis=1, inplace=True)
        try:
            self.metadata['gds_protocol_version'] = int(df['bytes'].iloc[0].split()[0], 16)
            self.metadata['gds_packet_format'] = self.packet_format_dictionary[self.metadata['gds_protocol_version']]
            self.packet_format = self.packet_format_dictionary[self.metadata['gds_protocol_version']]
        except KeyError:
            self.metadata['log'] += f'{datetime.datetime.now()}: GDS protocol version: ' \
                                    f'{int(df["bytes"].iloc[0].split()[0], 16)} not found in available formats\n'
            raise RatsError

        self.metadata[
            'log'] += f'{datetime.datetime.now()}: GDS format identified as {self.metadata["gds_protocol_version"]}\n'
        self.metadata['log'] += f'{datetime.datetime.now()}: _create_partitioned_dataframe function completed\n'
        self.dataframe = df

        # =============================================================================================================

    def _separate_header_and_data(self):

        input_bytes = self.packet_format['DATA']

        def __operation(df):
            """
            To be used on a groupby object, i.e.: GroupByObject.apply(_partition_packet_data)
            expects a dataframe constructed from only one packet of data, and splits the packet into
            the header bytes and the datastream, returning a dataframe with those columns

            # need to raise a RatsError at the appropriate point
            """
            data = df.bytes.tolist()
            stream = ' '.join(data).split()
            counter = 0
            packet_dictionary = {}
            for field in self.packet_format:
                if field == 'DATA':
                    if not stream[counter:]:
                        self.metadata[
                            'log'] += f'{datetime.datetime.now()}: Failed to partition the header from the full ' \
                                      f'data stream\n'
                        raise RatsError

                    active_edb_flags = f"{packet_dictionary['ACTIVE_EDBS']:032b}"[::-1] # padded to max of 32 bits..
                    flaglist = [i for i, x in enumerate(active_edb_flags) if x == '1']
                    bytes = [stream[counter:][i:i + input_bytes] for i in range(0, len(stream[counter:]), input_bytes)]

                    bytes = [''.join(i) for i in bytes]

                    bytes = [np.array(bytes[i:i + len(flaglist)]) for i in range(0, len(bytes), len(flaglist))]

                    # check for dropped data here and pad if required...
                    bytes_padding_check = [len(i) == len(flaglist) for i in bytes]
                    bytes_padding_check = [i for i, x in enumerate(bytes_padding_check) if x == False]


                else:
                    if not stream[counter:counter + self.packet_format[field]]:
                        # If there are any bytes missing from the header
                        self.metadata['log'] += f"Could not fill the specified packet header for packet {df.name}\n"
                        raise RatsError
                    bytes = stream[counter:counter + self.packet_format[field]]
                    # do conversions here, maybe...
                    if field != 'TIME_STAMP':
                        bytes = int(''.join(bytes), 16)
                    else:
                        bytes = ' '.join(bytes)

                packet_dictionary[field] = bytes
                counter += self.packet_format[field]

            packet_dictionary['ACTIVE_EDBS'] = flaglist
            return pd.DataFrame.from_records([packet_dictionary])

        try:
            self.dataframe = self.dataframe.groupby('packet_number').apply(__operation)
            self.dataframe = self.dataframe.droplevel(level='packet_number')
            self.dataframe.reset_index(inplace=True, drop=True)
            self.metadata['log'] += f'{datetime.datetime.now()}: _separate_header_and_data function completed\n'
        except Exception:
            self.metadata['log'] += f'{datetime.datetime.now()}: _separate_header_and_data function failed\n'
            raise RatsError


    def _assign_samples_to_edbs(self):
        """
        Takes a dataframe which has been partitioned into header fields and a data stream and breaks up the
        datastream, then assigns the samples to the correct EDBs

        """

        # This will generate the number and 'ID' of each EDB which is active on the RATS inputs
        def __operate(df):
            df = df.copy()
            df = df.explode('DATA')

            packet_timestamp_milliseconds = int(df['TIME_STAMP'].str.split().str.join('').iloc[0][:8], 16)
            packet_timestamp_microseconds = int(df['TIME_STAMP'].str.split().str.join('').iloc[0][-4:], 16) >> 6
            packet_start_time = packet_timestamp_microseconds + (packet_timestamp_milliseconds * 1000)
            number_of_samples = len(
                df['DATA'].values)
            sample_rate = df['SAMPLE_RATE'].iloc[0]  # fetch sample rate
            propagated_time_column = [packet_start_time + (i * sample_rate) for i in range(number_of_samples)]
            df['TIME_STAMP'] = propagated_time_column

            df['SAMPLE'] = [i for i in range(number_of_samples)]
            df = df.explode(['ACTIVE_EDBS', 'DATA'])

            for bit in LLCEDBFormat:
                # have an issue here.. need to further subdivide into packets, maybe drop packet duplicates
                if 'BIT' not in bit.name:
                    df[bit.name] = np.where(df['ACTIVE_EDBS'] == LLCEDB,
                                            df['DATA'].apply(int, base=16)
                                            .apply(bin).str[2:].str.zfill(16).str[15 - bit.value], None)

                    df[bit.name] = df[bit.name].ffill()
                    df[bit.name] = df[bit.name].astype(np.int8)
            df = df[df['ACTIVE_EDBS'] != LLCEDB]

            df.rename(columns={'index': 'rats_sample'})
            return df

        try:
            self.dataframe = self.dataframe.groupby('LLC_COUNT').apply(__operate)
            self.dataframe.reset_index(inplace=True, drop=True)

            self.dataframe = self.dataframe.drop('SAMPLE_RATE', axis=1)
            self.dataframe.reset_index(inplace=True, drop=True)
            self.dataframe['TIME_STAMP'] = self.dataframe['TIME_STAMP'] - \
                                           self.dataframe['TIME_STAMP'].iloc[0]
            self.metadata['log'] += f'{datetime.datetime.now()}: _assign_samples_to_edbs function completed\n'
        except Exception:
            self.metadata['log'] += f'{datetime.datetime.now()}: _assign_samples_to_edbs function failed\n'
            raise RatsError

    def _find_outliers(self):
        """
        A hash of the sequence of samples recorded for every individual edb is produced per-function.
        e.g. each edb will be sampled for every instance of a single function, possibly multiple times.
        If you take those samples and make a hash, the sample data and the order of the sample data is encoded.
        The requirement to encode the order of sample data is so that a reverse scan will be registered as a different
        value to a forward scan, for instance.

        Any instance of an EDB producing a hash which is not the mode of the hash values for a particular function will
        be labelled as anomalous.
        """
        def __operate(df):
            sip_df = df[df['SIP'] == 1]  # make sure to only select for the scan data
            hash_list = [hash(' '.join([str(llc) for llc in frame['DATA'].tolist()])) for llc, frame in
                         sip_df.groupby(['LLC_COUNT'])]
            hash_per_llc = pd.Series(hash_list, index=sip_df['LLC_COUNT'].unique())
            hash_mode = pd.Series(hash_per_llc).mode()

            df['hash'] = df['LLC_COUNT'].map(hash_per_llc.to_dict())
            df['filter'] = hash_mode.values[0]
            df['hash'] = df['hash'].fillna(0)
            df['filter'] = np.where(df['hash'] == 0, 0, df['filter'])
            df['anomalous'] = np.where(df['hash'] != df['filter'], 1, 0)

            if 1 in df['anomalous'].values:
                packets = df[df['anomalous'] == 1]['LLC_COUNT'].unique()
                self.metadata['log'] += f'{datetime.datetime.now()}: ANOMALY DETECTED in function: {df.name[0]}, ' \
                                        f'LLC interval(s): {packets},  ' \
                                        f'EDB: {df.name[1]}\n'
                self.metadata['errors'] = True

            df['anomalous'] = df['anomalous'].astype('category')
            return df

        self.dataframe = self.dataframe.groupby(['FUNCTION', 'ACTIVE_EDBS']).apply(
            __operate)
        # this groups by function and EDB, so the output should be an anomalous set..
        self.dataframe.drop(['hash', 'filter'], axis=1, inplace=True)
        self.metadata['log'] += f'{datetime.datetime.now()}: _find_outliers function completed\n'

    def _scale_and_rename_rats_inputs(self):

        active_edbs = self.dataframe['ACTIVE_EDBS'].unique()
        df = self.dataframe.copy()

        def _scale_twos_comp_values(dataframe):
            """
            Generic function to take a dataframe with column; Packet.DATA.name and work out the twos complement
            values.
            This is applied to a groupby object in self._scale_and_rename_rats_inputs
            """
            input_bytes = self.packet_format['DATA']

            def to_int(x):
                x = int(x, input_bytes * 8)
                if (x & (1 << (input_bytes * 8 - 1))) != 0:  # if sign bit is set
                    x = x - (1 << input_bytes * 8)  # compute negative value...

                return x

            dataframe['DATA'] = dataframe['DATA'].apply(to_int)

            dataframe['DATA'] = ((dataframe.maximum - dataframe.minimum) *
                                (dataframe['DATA'] / (2 ** (input_bytes * 8)))) + \
                                ((dataframe.maximum - dataframe.minimum) / 2) + dataframe.minimum

            dataframe.drop(['minimum', 'maximum'], axis=1, inplace=True)

            return dataframe

        try:
            instance_name = self.filename.split('_')[-1].split('.')[0].split('(')[0].replace('-',
                                                                                            '_')
            datasheet_identifier = self.filename.split('_')[-1].split('.')[0].split('(')[1][:-1]
            topodata = topo.extractscale(datasheet_identifier, active_edbs)

            df['minimum'] = df['ACTIVE_EDBS'].map(topodata['minimum'])
            df['maximum'] = df['ACTIVE_EDBS'].map(topodata['maximum'])
            df['units'] = df['ACTIVE_EDBS'].map(topodata['units']).astype('category')
            df['board'] = instance_name
            df['board'] = df['board'].astype('category')
            df = df.groupby(['ACTIVE_EDBS']).apply(_scale_twos_comp_values)

            df['ACTIVE_EDBS' + '_id'] = df['ACTIVE_EDBS'].map(
                topodata['descriptions']).astype('category')

            self.metadata['log'] += f'{datetime.datetime.now()}: Data scaled against topology and EDS files ' \
                                    f'successfully\n'

        except Exception as e:
            df['board'] = 'UNDEFINED - UNABLE TO PARSE TOPOLOGY DATA'
            df['board'] = df['board'].astype('category')
            df['units'] = 'N/A'
            df['units'] = df['units'].astype('category')
            df['minimum'] = -1
            df['maximum'] = 1

            df = df.groupby(['ACTIVE_EDBS']).apply(_scale_twos_comp_values)
            df['ACTIVE_EDBS' + '_id'] = df['ACTIVE_EDBS'].astype('category')

            self.metadata['log'] += f'{datetime.datetime.now()}: Failed to parse topography files and datasheets\n'

        df['ACTIVE_EDBS'] = df['ACTIVE_EDBS'].astype('category')

        for field, value in self.packet_format.items():
            type = value * 8
            if field == 'TIME_STAMP':
                if type == 8:
                    df[field] = df[field].astype(np.int8)
                elif type == 16:
                    df[field] = df[field].astype(np.int16)
                elif type == 32:
                    df[field] = df[field].astype(np.int32)
                elif type > 32:
                    df[field] = df[field].astype(np.int64)
            elif field in df.columns and field != 'DATA':
                df[field] = df[field].astype('category')

        for llc in LLCEDBFormat:
            if 'BIT' in llc.name:
                pass
            else:
                df[llc.name] = df[llc.name].astype('category')
        self.dataframe = df

    def save_dataframe(self):
        # construct a parquet file which contains the metadata and the dataframe. much, much heavier than a feather file
        # but can store more info about how the file was processed and when. Also stores the parameters passed to the
        # parser in the self.metadata, now that they're stored as dictionaries.
        table = pa.Table.from_pandas(self.dataframe)
        default_table_meta = table.schema.metadata
        custom_meta = json.dumps(self.metadata)
        combined_meta = {self.meta_key.encode(): custom_meta.encode(), **default_table_meta}
        table = table.replace_schema_metadata(combined_meta)
        pq.write_table(table, f'{self.data_directory / self.filename}.parquet', compression='GZIP')

    def load_dataframe(self):
        # use this function to load in old frames and associated metadata - no good pure pandas way to do this yet
        print(self.data_directory / self.filename)
        table = pq.read_table(f'{self.data_directory / self.filename}.parquet')
        meta_json = table.schema.metadata[self.meta_key.encode()]
        self.dataframe = table.to_pandas()  # no specific column loading, but this method preserves metadata so...
        self.metadata = json.loads(meta_json)
        self.gds_protocol_version = int(self.metadata['gds_protocol_version'])

    def rescale_data(self):
        # starting on a function to re-scale the data against a new set of topo files...
        self.load_dataframe()
        self._scale_and_rename_rats_inputs()
        self.save_dataframe()

    def report_metadata(self):
        for key, item in self.metadata.items():
            print(key, ':', item)

    def parse(self, test=False):
        try:
            self.load_dataframe()
            if 'anomalous' in self.dataframe.columns:  # might not be if the frame failed to parse
                if 1 in self.dataframe.anomalous.values:
                    self.status_message = 'There seems to be some anomalous data in this file'

        except FileNotFoundError:
            try:
                if '.txt' not in self.filepath:
                    self.filepath = self.filepath + '.txt'
                self._create_partitioned_dataframe()
                self._separate_header_and_data()
                print(self.dataframe.head())
                self._assign_samples_to_edbs()

                self._find_outliers()
                self._scale_and_rename_rats_inputs()
                self.metadata['date_created'] = str(datetime.datetime.now().strftime("%d%b%y, %H:%M:%S"))
                self.metadata['parse_completed_without_error'] = True
                if not test:
                    self.save_dataframe()
                self.metadata['parse_completed_without_error'] = True

            except RatsError:
                self.metadata['log'] += 'There was an error while parsing this file, ' \
                                        'so a generic, empty dataframe was created \n'
                self.packet_format = self.packet_format_dictionary[list(self.packet_format_dictionary.keys())[0]]
                self.dataframe = pd.DataFrame(columns=[column for column, value in self.packet_format.items()])
                self.metadata['parse_completed_without_error'] = False
                if not test:
                    self.save_dataframe()



parser = RatsParser(r'C:\Users\uksayr\OneDrive - Waters Corporation\Desktop\ratsAug24\Sample003_20220824T131305_TBAR-ION-GUIDE-3(5-3)')
# parser = RatsParser(r'C:\Users\uksayr\OneDrive - Waters Corporation\Desktop\ratsAug24\Sample003_20220824T131305_TBAR-ION-GUIDE-2(4-3)')
parser.parse(test=True)

