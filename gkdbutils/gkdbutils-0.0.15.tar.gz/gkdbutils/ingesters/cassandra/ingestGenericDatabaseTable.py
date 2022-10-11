#!/usr/bin/env python
"""Ingest Generic Database tables using multi-value insert statements and multiprocessing.

Usage:
  %s <configFile> <inputFile>... [--fileoffiles] [--table=<table>] [--tableDelimiter=<tableDelimiter>] [--bundlesize=<bundlesize>] [--nprocesses=<nprocesses>] [--nfileprocesses=<nfileprocesses>] [--loglocationInsert=<loglocationInsert>] [--logprefixInsert=<logprefixInsert>] [--loglocationIngest=<loglocationIngest>] [--logprefixIngest=<logprefixIngest>] [--columns=<columns>] [--types=<types>] [--skiphtm] [--nullValue=<nullValue>] [--fktable=<fktable>] [--fktablecols=<fktablecols>] [--fktablecoltypes=<fktablecoltypes>] [--fkfield=<fkfield>] [--fkfrominputdata=<fkfrominputdata>] [--racol=<racol>] [--deccol=<deccol>] [--flattenheader] [--headerlength=<headerlength>] [--headerdelimiter=<headerdelimiter>] [--headerprefix=<headerprefix>] [--rownumcolumn=<rownumcolumn>]
  %s (-h | --help)
  %s --version

Options:
  -h --help                                Show this screen.
  --version                                Show version.
  --fileoffiles                            Read the CONTENTS of the inputFiles to get the filenames. Allows many thousands of files to be read, avoiding command line constraints.
  --table=<table>                          Target table name.
  --tableDelimiter=<tableDelimiter>        Table delimiter (e.g. \\t \\s ,) where \\t = tab and \\s = space. Space delimited assumes one or more spaces between fields [default: \\s]
  --bundlesize=<bundlesize>                Group inserts into bundles of specified size [default: 1]
  --nprocesses=<nprocesses>                Number of processes to use per ingest file. Warning: nprocesses x nfileprocesses should not exceed nCPU. [default: 1]
  --nfileprocesses=<nfileprocesses>        Number of processes over which to split the files. Warning: nprocesses x nfileprocesses should not exceed nCPU. [default: 1]
  --loglocationInsert=<loglocationInsert>  Log file location [default: /tmp/]
  --logprefixInsert=<logprefixInsert>      Log prefix [default: inserter]
  --loglocationIngest=<loglocationIngest>  Log file location [default: /tmp/]
  --logprefixIngest=<logprefixIngest>      Log prefix [default: ingester]
  --columns=<columns>                      List of columns, comma separated, no spaces. If blank, assumes all columns of the input data.
  --types=<types>                          PYTHON column types in the same order as the column headers.
  --skiphtm                                Don't bother calculating HTMs. They're either already done or we don't need them. (I.e. not spatially indexed data.)
  --nullValue=<nullValue>                  Value of NULL definition (e.g. NaN, NULL, \\N, None) [default: \\N]
  --fktable=<fktable>                      Cassandra has a flat schema, so join to another table file via a foreign key (e.g. exposures).
  --fktablecols=<fktablecols>              The valid columns in the foreign key table we want to use - comma separated, no spaces (e.g. expname,object,mjd,filter,mag5sig,zp_mag,fwhm_px,exptime,detem).
  --fktablecoltypes=<fktablecoltypes>      The valid (python) column types in the foreign key table we want to use - comma separated, no spaces (e.g. str,str,float,str,float,float,float,float,float).
  --fkfield=<fkfield>                      Foreign key field [default: expname]
  --fkfrominputdata=<fkfrominputdata>      Foreign key from input data. If set to filename it will use the datafile filename as the key [default: filename]
  --racol=<racol>                          Column that represents the RA [default: ra]
  --deccol=<deccol>                        Column that represents the Declination [default: dec]
  --flattenheader                          Flatten a headed file.
  --headerlength=<headerlength>            Does the file we are reading have a header [default: 0]
  --headerdelimiter=<headerdelimiter>      Delimiter of header values [default: =]
  --headerprefix=<headerprefix>            Header comment prefix [default: #]
  --rownumcolumn=<rownumcolumn>            Generate a rownum column if one doesn't exist.

Examples:
  %s config_cassandra.yaml 01a58464o0535o.dph --fktable=/Users/kws/atlas/dophot/all_co_exposures.tst --fkfield=expname --fktablecols=mjd,expname,exptime,filter,mag5sig --types=float,float,float,int,int,float,float,float,float,float,float,float,float,float,float,float,float,float --fktablecoltypes=float,str,float,str,float --table=atlasdophot --racol=RA --deccol=Dec

  %s /home/kws/config_cassandra_atlas.yaml /home/kws/atlas/dophot/ingest/parallel_machine_ingest_test/remaining_batch/exposures_around_galactic_centre_10degrees_20210219_cleaned_hko_only_second_attempt_db1 --fileoffiles --fktable=/home/kws/atlas/dophot/all_co_exposures.tst --fkfield=expname --fktablecols=mjd,expname,exptime,filter,mag5sig --types=float,float,float,int,int,float,float,float,float,float,float,float,float,float,float,float,float,float --fktablecoltypes=float,str,float,str,float --table=atlas_detections --racol=RA --deccol=Dec --nprocesses=8 --nfileprocesses=4 --loglocationIngest=/home/kws/cassandra_ingest_logs/db1/cassandra_ingest/galactic_centre_hko/ --loglocationInsert=/home/kws/cassandra_ingest_logs/db1/cassandra_ingest/galactic_centre_hko/

  %s /Users/kws/config_cassandra.yaml /Users/kws/lasair/cassandra/load-old-data/noncandidates/file_of_files_to_ingest.txt --fileoffiles --types=str,float,float,int,int,float,float,float,int --table=test_noncandidates --tableDelimiter=, --nprocesses=11 --nfileprocesses=1 --skiphtm

  %s /Users/kws/config_cassandra_atlas.yaml /tmp/ddc/atlas/diff/01a/59860/01a59860o0765o.ddc --table=atlas_ddc --columns=OBS,OBJ,FILT,MJD,TEXP,APFIT,MAGZPT,SKYMAG,MAG5SIG,PA,CLOUD,RAHEAD,DECHEAD,det_id,RA,Dec,mag,dmag,x,y,major,minor,phi,det,chi/N,Pvr,Ptr,Pmv,Pkn,Pno,Pbn,Pcr,Pxt,Psc,Dup,WPflx,dflx --types=str,str,str,float,float,float,float,float,float,float,float,float,float,int,float,float,float,float,float,float,float,float,float,int,float,float,float,float,float,float,float,float,float,float,int,float,float --flattenheader --headerlength=37 --racol=RA --deccol=Dec --rownumcolumn=det_id

  %s /Users/kws/config_cassandra_atlas.yaml /tmp/inputddcfiles.txt --fileoffiles --table=atlas_ddc --columns=OBS,OBJ,FILT,MJD,TEXP,APFIT,MAGZPT,SKYMAG,MAG5SIG,PA,CLOUD,RAHEAD,DECHEAD,det_id,RA,Dec,mag,dmag,x,y,major,minor,phi,det,chi/N,Pvr,Ptr,Pmv,Pkn,Pno,Pbn,Pcr,Pxt,Psc,Dup,WPflx,dflx --types=str,str,str,float,float,float,float,float,float,float,float,float,float,int,float,float,float,float,float,float,float,float,float,int,float,float,float,float,float,float,float,float,float,float,int,float,float --flattenheader --headerlength=37 --racol=RA --deccol=Dec --rownumcolumn=det_id --nprocesses=8 --nfileprocesses=4

"""
import sys
__doc__ = __doc__ % (sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0])
from docopt import docopt
import os, shutil, re
from gkutils.commonutils import Struct, cleanOptions, readGenericDataFile, dbConnect, which, splitList, parallelProcess
from datetime import datetime
from datetime import timedelta
import subprocess
import gzip
from collections import OrderedDict

# 2021-02-11 KWS Import the new htmNameBulk function! No need anymore to rely on an external binary!
#                No need to write temporary files anymore.
from gkhtm._gkhtm import htmNameBulk, htmIDBulk

def readZTFAvroPacket(filename, addhtm16 = None):
    from fastavro import reader
    print(filename)
    with open(filename, 'rb') as f:
        candlist = []
        nondetectionCandlist = []
        avro_reader = reader(f)
        for record in avro_reader:
            prv_candidates = []
            try:
                if record['prv_candidates'] is not None:
                    prv_candidates = record['prv_candidates']
            except KeyError as e:
                pass
            candidates = [record['candidate']] + prv_candidates
            for cand in candidates:
   
                # Remove the images.
                try:
                    del cand['cutoutDifference']
                except KeyError as e:
                    pass
                try:
                    del cand['cutoutTemplate']
                except KeyError as e:
                    pass
                try:
                    del cand['cutoutScience']
                except KeyError as e:
                    pass

                cand['objectId'] = record['objectId']

                if not 'candid' in cand or not cand['candid']:
                    nondetectionCandlist.append({'objectId': cand['objectId'],
                                                 'jd': cand['jd'],
                                                 'fid': cand['fid'],
                                                 'diffmaglim': cand['diffmaglim'],
                                                 'nid': cand['nid'],
                                                 'field': cand['field'],
                                                 'magzpsci': cand['magzpsci'],
                                                 'magzpsciunc': cand['magzpsciunc'],
                                                 'magzpscirms': cand['magzpscirms']})
                else:
                    candlist.append(cand)

    if addhtm16 is not None:
        coords = [[x['ra'], x['dec']] for x in candlist]
        htm16s = htmIDBulk(16, coords)
        for i in range(len(candlist)):
            candlist[i]['htm16'] = htm16s[i]

    data = {'candidates': candlist, 'noncandidates': nondetectionCandlist}

    return data


def nullValue(value, nullValue = '\\N'):
   returnValue = nullValue

   if value and value.strip():
      returnValue = value.strip()

   return returnValue

def nullValueNULL(value):
   returnValue = None

   if value and not isinstance(value, int) and value.strip() and value != 'NULL':
      returnValue = value.strip()

   return returnValue

def boolToInteger(value):
    returnValue = value
    if value == 'true':
        returnValue = 1
    if value == 'false':
        returnValue = 0
    return returnValue


# Use INSERT statements so we can use multiprocessing
# 2021-10-16 KWS Why do we need types?? This is because if we send the data as a CSV dict,
#                then Cassandra will not know what to do with the data. A float != string.
#                MySQL is a bit more generous inasmuch as it will auto cast. Not Cassandra.
#                We allow this option so that we can pass the data directly from CSV.
#                An alternative approach is to modify readGenericDataFile so that it will
#                cast during the load. Avro dictionaries are already typed.
def executeLoad(session, table, data, bundlesize = 1, types = None):

    rowsUpdated = 0

    if len(data) == 0:
        print('No data!')
        return rowsUpdated

    #if types is None:
    #    return rowsUpdated

    keys = list(data[0].keys())

    typesDict = OrderedDict()

    if types is not None:
        if len(keys) != len(types):
            print("Keys & Types mismatch")
            return rowsUpdated
        i = 0
        for k in keys:
            typesDict[k] = types[i]
            i += 1


    formatSpecifier = ','.join(['%s' for i in keys])

    chunks = int(1.0 * len(data) / bundlesize + 0.5)
    if chunks == 0:
        subList = [data]
    else:
        bins, subList = splitList(data, bins = chunks, preserveOrder = True)


    for dataChunk in subList:
        try:
            sql = "insert into %s " % table
            # Force all keys to be lowercase and devoid of hyphens
            sql += "(%s)" % ','.join(['%s' % k.lower().replace('-','').replace('/','') for k in keys])

            sql += " values "
            sql += ',\n'.join(['('+formatSpecifier+')' for x in range(len(dataChunk))])
            sql += ';'

            values = []

            for row in dataChunk:
                # If data comes from a CSV. We need to cast the results using the types. Otherwise assume
                # the types are already correct. (E.g. data read from an Avro file.)
                for key in keys:
                    if types is not None:
                        value = nullValueNULL(boolToInteger(row[key]))
                        if value is not None:
                            value = eval(typesDict[key])(value)
                        values.append(value)
                    # The data is already in the right python type. (Actually it doesn't matter! All the values are strings!)
                    else:
                        value = row[key]
                        values.append(value)


            #print(sql, tuple(values))
            session.execute(sql, tuple(values))


        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print(message)

    return


def workerInsert(num, db, objectListFragment, dateAndTime, firstPass, miscParameters):
    """thread worker function"""
    # Redefine the output to be a log file.
    from cassandra.cluster import Cluster
    options = miscParameters[0]

    pid = os.getpid()
    sys.stdout = open('%s%s_%s_%d_%d.log' % (options.loglocationInsert, options.logprefixInsert, dateAndTime, pid, num), "w")
    cluster = Cluster(db['hostname'])
    session = cluster.connect()
    session.set_keyspace(db['keyspace']) 

    combinedTypes = options.types
    if options.fktablecoltypes is not None and options.types is not None:
        combinedTypes = options.types + ',' + options.fktablecoltypes

    # Add 3 string columns if the HTMs are being requested. You will not be able to insert into a table
    # if its htm name components are not specified.
    if not options.skiphtm and combinedTypes is not None:
        combinedTypes = combinedTypes + ",str,str,str"

    types = None
    if combinedTypes is not None:
        types = combinedTypes.split(',')

    # This is in the worker function
    objectsForUpdate = executeLoad(session, options.table, objectListFragment, int(options.bundlesize), types=types)

    print("Process complete.")
    cluster.shutdown()
    print("Connection Closed - exiting")

    return 0

def ingestData(options, inputFiles, fkDict = None):

    import yaml
    with open(options.configFile) as yaml_file:
        config = yaml.safe_load(yaml_file)

    username = config['cassandra']['local']['username']
    password = config['cassandra']['local']['password']
    keyspace = config['cassandra']['local']['keyspace']
    hostname = config['cassandra']['local']['hostname']

    db = {'username': username,
          'password': password,
          'keyspace': keyspace,
          'hostname': hostname}

    currentDate = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    (year, month, day, hour, min, sec) = currentDate.split(':')
    dateAndTime = "%s%s%s_%s%s%s" % (year, month, day, hour, min, sec)

    delimiter=options.tableDelimiter
    if delimiter == '\\s':
        delimiter = ' '
    if delimiter == '\\t':
        delimiter = '\t'

    for inputFile in inputFiles:
        print("Ingesting %s" % inputFile)
        if '.gz' in inputFile:
            # It's probably gzipped
            f = gzip.open(inputFile, 'rb')
            print(type(f).__name__)
        else:
            f = inputFile
    
        if 'avro' in inputFile:
            # Data is in Avro packets, with schema. Let's hard-wire to the ZTF schema for the time being.
            avroData = readZTFAvroPacket(f, addhtm16 = True)
            if 'noncandidates' in options.table:
                data = avroData['noncandidates']
            elif 'candidates' in options.table:
                data = avroData['candidates']
            else:
                print("Error. Incorrect table definition for Avro packets. Must contain candidates or noncandidates.")
                exit(1)

        else:
            # Data is in plain text file. No schema present, so will need to provide
            # column types.
            if options.flattenheader:
                data = readGenericDataFile(f, delimiter=delimiter, useOrderedDict=True, skipLines=int(options.headerlength), appendheaderlines=True, headerdelimiter=options.headerdelimiter, headerprefix=options.headerprefix, rownumcolumn=options.rownumcolumn)
            else:
                data = readGenericDataFile(f, delimiter=delimiter, useOrderedDict=True, rownumcolumn=options.rownumcolumn)

        # 2021-07-29 KWS This is a bit inefficient, but trim the data down to specified columns if they are present.
        if options.columns:
            trimmedData = []
            for row in data:
                trimmedRow = {key: row[key] for key in options.columns.split(',')}
                trimmedData.append(trimmedRow)
            data = trimmedData


        foreignKey = options.fkfrominputdata
        if foreignKey == 'filename':
            foreignKey = os.path.basename(inputFile).split('.')[0]


        if fkDict:
            for i in range(len(data)):
                try:
                    if options.fktablecols:
                        # just pick out the specified keys
                        keys = options.fktablecols.split(',')
                        for k in keys:
                            data[i][k] = fkDict[foreignKey][k]
                    else:
                        # Use all the keys by default
                        for k,v in fkDict[foreignKey].items():
                            data[i][k] = v
                except KeyError as e:
                    pass

        #print(data[0])
        pid = os.getpid()
    
        if not options.skiphtm:
    
            coords = []
            for row in data:
                coords.append([float(row[options.racol]), float(row[options.deccol])])
    
            htm16Names = htmNameBulk(16, coords)

            # For Cassandra, we're going to split the HTM Name across several columns.
            # Furthermore, we only need to do this once for the deepest HTM level, because
            # This is always a subset of the higher levels.  Hence we only need to store
            # the tail end of the HTM name in the actual HTM 16 column.  So...  we store
            # the full HTM10 name as the first 12 characters of the HTM 16 one, then the
            # next 3 characters into the HTM 13 column, then the next 3 characters (i.e.
            # the last few characters) the HTM 16 column
            # e.g.:
            # ra, dec =      288.70392, 9.99498
            # HTM 10  = N02323033011
            # HTM 13  = N02323033011 211
            # HTM 16  = N02323033011 211 311

            # Incidentally, this hierarchy also works in binary and we should seriously
            # reconsider how we are currently using HTMs.

            # HTM10 ID =    13349829 = 11 00 10 11 10 11 00 11 11 00 01 01
            # HTM13 ID =   854389093 = 11 00 10 11 10 11 00 11 11 00 01 01  10 01 01
            # HTM16 ID = 54680902005 = 11 00 10 11 10 11 00 11 11 00 01 01  10 01 01  11 01 01


            for i in range(len(data)):
                # Add the HTM IDs to the data
                data[i]['htm10'] = htm16Names[i][0:12]
                data[i]['htm13'] = htm16Names[i][12:15]
                data[i]['htm16'] = htm16Names[i][15:18]
    
    
        nprocesses = int(options.nprocesses)
    
        if len(data) > 0:
            nProcessors, listChunks = splitList(data, bins = nprocesses, preserveOrder=True)
    
            print("%s Parallel Processing..." % (datetime.now().strftime("%Y:%m:%d:%H:%M:%S")))
            parallelProcess(db, dateAndTime, nProcessors, listChunks, workerInsert, miscParameters = [options], drainQueues = False)
            print("%s Done Parallel Processing" % (datetime.now().strftime("%Y:%m:%d:%H:%M:%S")))


    
def workerIngest(num, db, objectListFragment, dateAndTime, firstPass, miscParameters):
    """thread worker function"""
    # Redefine the output to be a log file.
    options = miscParameters[0]
    fkDict = miscParameters[1]
    pid = os.getpid()
    sys.stdout = open('%s%s_%s_%d_%d.log' % (options.loglocationIngest, options.logprefixIngest, dateAndTime, pid, num), "w")

    # This is in the worker function
    objectsForUpdate = ingestData(options, objectListFragment, fkDict = fkDict)

    print("Process complete.")

    return 0

def ingestDataMultiprocess(options, fkDict = None):

    currentDate = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    (year, month, day, hour, min, sec) = currentDate.split(':')
    dateAndTime = "%s%s%s_%s%s%s" % (year, month, day, hour, min, sec)

    # Read the contents of the input file(s) to get the filenames to process.
    files = options.inputFile

    if options.fileoffiles:
        files = []
        for f in options.inputFile:
            with open(f) as fp:
                content = fp.readlines()
                content = [filename.strip() for filename in content]
            files += content

    #print(files)
    nProcessors, fileSublist = splitList(files, bins = int(options.nfileprocesses), preserveOrder=True)
    
    print("%s Parallel Processing..." % (datetime.now().strftime("%Y:%m:%d:%H:%M:%S")))
    parallelProcess([], dateAndTime, nProcessors, fileSublist, workerIngest, miscParameters = [options, fkDict], drainQueues = False)
    print("%s Done Parallel Processing" % (datetime.now().strftime("%Y:%m:%d:%H:%M:%S")))


def main(argv = None):
    opts = docopt(__doc__, version='0.1')
    opts = cleanOptions(opts)

    # Use utils.Struct to convert the dict into an object for compatibility with old optparse code.
    options = Struct(**opts)

    fkDict = {}
    # If we have a foreign key table, read the data once only.  Pass this to the subprocesses.
    if options.fktable:
        fkeys = readGenericDataFile(options.fktable, delimiter='\t')
        for row in fkeys:
            fkDict[row[options.fkfield]] = row

    ingestDataMultiprocess(options, fkDict = fkDict)

    #files = options.inputFile
    #if options.fileoffiles:
    #    files = []
    #    for f in inputFile:
    #        with open(f) as fp:
    #            content = fp.readlines()
    #        files += content
    #ingestData(options, files, fkDict = fkDict)


if __name__=='__main__':
    main()


