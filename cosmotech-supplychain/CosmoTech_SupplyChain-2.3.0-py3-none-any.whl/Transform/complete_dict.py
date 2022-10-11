from datetime import date

from Supplychain.Generic.folder_io import FolderWriter, FolderReader
from Supplychain.Generic.timer import Timer
from Supplychain.Schema.adt_column_description import ADTColumnDescription
from Supplychain.Schema.default_values import parameters_default_values, variables_default_values
from Supplychain.Schema.validation_schemas import ValidationSchemas

dataset_description = ADTColumnDescription.format


class DictCompleter(Timer):

    def __init__(self,
                 reader: FolderReader,
                 writer: FolderWriter):
        Timer.__init__(self, prefix="[Complete]")
        self.reader = reader
        self.writer = writer
        self.schema = ValidationSchemas()

    def __initialize_configuration(self):
        self.reader.files.setdefault('Configuration', [])
        if not self.reader.files['Configuration']:
            self.reader.files['Configuration'].append({})

    def __complete_data_generic(self):
        for file_name, values in parameters_default_values.items():
            for datum in self.reader.files.get(file_name, []):
                if datum.get('Label') is None and 'id' in datum:
                    datum['Label'] = datum['id']
                for key, value in values.items():
                    if datum.get(key) is None:
                        datum[key] = value

    def __cast_integers(self):
        for file_name in self.schema.schemas:
            keys = [
                key
                for key, description in self.schema.schemas[file_name]['properties'].items()
                if description['type'] == 'integer'
            ]
            for datum in self.reader.files.get(file_name, []):
                for key in keys:
                    value = datum.get(key)
                    if value is not None:
                        datum[key] = int(value)

    def __standardize_time_steps(self):
        for file_name, file_description in dataset_description.items():
            time_elements = list(file_description['change'])
            for events in file_description['event'].values():
                time_elements.extend(events)

            for datum in self.reader.files.get(file_name, []):
                for time_element in time_elements:
                    datum[time_element] = {
                        str(int(float(time_step))): value
                        for time_step, value in datum[time_element].items()
                    }

    def __complete_data_specific(self):
        for configuration in self.reader.files.get('Configuration', []):
            if configuration.get('StartingDate') is None:
                configuration['StartingDate'] = date.today().isoformat()

        may_be_infinite = (
            set(s['id'] for s in self.reader.files.get('Stock', []))
            - set(o['target'] for o in self.reader.files.get('output', []))
            - set(t['target'] for t in self.reader.files.get('Transport', []))
            - set(t['source'] for t in self.reader.files.get('Transport', []))
        )
        for stock in self.reader.files.get('Stock', []):
            is_infinite = stock.get('IsInfinite')
            initial_stock = stock.get('InitialStock')
            initial_value = stock.get('InitialValue')
            if is_infinite or (is_infinite is None and initial_stock is None and stock['id'] in may_be_infinite):
                stock['IsInfinite'] = True
                stock['InitialStock'] = 0
                stock['InitialValue'] = 0
            else:
                stock['IsInfinite'] = False
                stock['InitialStock'] = initial_stock or 0
                stock['InitialValue'] = initial_value or 0
            demands = stock['Demands']
            demands_weight = stock['DemandWeights']
            demands_uncertainties = stock['DemandUncertainties']
            for time_step in demands:
                if demands_weight.get(time_step) is None:
                    demands_weight[time_step] = variables_default_values['Stock']['DemandWeights']
                if demands_uncertainties.get(time_step) is None:
                    demands_uncertainties[time_step] = variables_default_values['Stock']['DemandUncertainties']

        for resource in self.reader.files.get('ProductionResource', []):
            if resource.get('OpeningTimes') is None:
                resource['OpeningTimes'] = {'0': self.reader.files['Configuration'][0]['TimeStepDuration']}

    def __write_updated_files(self):
        for file_name, dict_list in self.reader.files.items():
            self.writer.write_from_list(dict_list, file_name)

    def complete(self):
        self.display_message("Starting completion")
        self.__initialize_configuration()
        self.__complete_data_generic()
        self.__cast_integers()
        self.__standardize_time_steps()
        self.display_message("Generic completion done")
        self.__complete_data_specific()
        self.display_message("Specific completion done")
        self.__write_updated_files()
