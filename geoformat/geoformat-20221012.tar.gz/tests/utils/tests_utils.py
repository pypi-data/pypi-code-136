import copy
import pathlib
import types
import warnings


def test_dependencies():

    try:
        from osgeo import ogr
        import_ogr_success = True
    except ImportError:
        import_ogr_success = False

    try:
        from osgeo import osr
        import_osr_sucess = True
    except ImportError:
        import_osr_sucess = False

    try:
        import psycopg2
        import psycopg2.extras
        import_psycopg2_success = True
    except ImportError:
        import_psycopg2_success = False

    return {'ogr': import_ogr_success, 'osr': import_osr_sucess, 'psycopg2': import_psycopg2_success}


def print_errors(in_error):
    if in_error:
        sentence = ''
        for error in in_error:
            (id_parameters, error_message, returned_values) = error
            sentence += "\tThe parameters #{} returned errors: \n".format(id_parameters)
            sentence += "\t\t" + error_message + '\n'
            sentence += "\t\t" + returned_values + '\n'
        return sentence
    else:
        return False


def test_function(function, test_parameters):
    in_error = []
    test_parameters_copy = copy.deepcopy(test_parameters)
    for id_parameters, parameters in test_parameters_copy.items():
        return_value = parameters['return_value']
        del parameters['return_value']

        try:
            result_value = function(**parameters)
        except Exception as e:
            result_value = e.__str__()

        # if return is a generator we transform it to tuple
        if isinstance(result_value, types.GeneratorType):
            result_value = tuple(result_value)

        elif isinstance(result_value, zip):
            result_value = list(result_value)

        # if return value is a path we just verify if file exists
        elif isinstance(return_value, pathlib.Path):
            if (return_value.is_file()):
                result_value = return_value

        if test_dependencies()['ogr']:
            from osgeo import ogr
            if isinstance(result_value, ogr.Geometry):
                if result_value.Equals(return_value):
                    result_value = True
                    return_value = True

        if result_value != return_value:
            in_error.append(
                (id_parameters,
                 'ERROR: return value must be {return_value}'.format(return_value=return_value),
                 'ERROR: function return this {result_value}'.format(result_value=result_value)))

    error_value = print_errors(in_error)
    if error_value:
        sentence = '{function_name} KO\n'.format(function_name=function.__name__)
        sentence += error_value
        warnings.warn(sentence)
    else:
        sentence = '{function_name} OK'.format(function_name=function.__name__)

    return sentence
