class DataTypes:
    data_types = {}

    def set_type(self, attr, value):
        self.data_types[attr] = type(value)

    def get_data_types(self):
        return self.data_types
