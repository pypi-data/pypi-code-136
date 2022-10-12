import os
from clean_gml.gml import Gml

filepath = 'examples/Vrijvervalleiding.gml'
# filepath = 'example.gml'

# datatype_changes = {'OPENBARE_RUIMTE': 'xsd:float'}
# datatype_changes = {'PROPERTY': 'xsd:float'}

gml = Gml(filepath)
# print(gml.schema.get_parameters_floats())
# gml.datatype_changes(changes=datatype_changes)
gml.replace_commas(ndigits=2)
gml.save()
