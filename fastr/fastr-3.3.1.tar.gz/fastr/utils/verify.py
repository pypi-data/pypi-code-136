import os
import gzip
import shutil
from tempfile import mkdtemp

import fastr
from ..abc.serializable import Serializable, ReadWriteHandler
from ..core.tool import Tool
from ..helpers import iohelpers, config
from .. import exceptions


def verify_resource_loading(filename: str, log=fastr.log):
    """
    Verify that a resource file can be loaded. Returns loaded object.

    :param filename: path of the object to load
    :param log: the logger to use to send messages to
    :return: loaded resource
    """
    name, ext = os.path.splitext(filename)

    # Check if file is gzipped
    if ext == '.gz':
        compressed = True
        name, ext = os.path.splitext(filename)
    else:
        compressed = False

    # Read file data
    log.info('Trying to read file with compression {}'.format('ON' if compressed else 'OFF'))
    if compressed:
        try:
            with gzip.open(filename, 'r') as file_handle:
                data = file_handle.read()
        except:
            log.error('Problem reading gzipped file: {}'.format(filename))
            return None
    else:
        try:
            with open(filename, 'r') as file_handle:
                data = file_handle.read()
        except:
            log.error('Problem reading normal file: {}'.format(filename))
            return None

    log.info('Read data from file successfully')

    # Try to read tool doc based on serializer matching the extension
    serializer = ext[1:]
    log.info('Trying to load file using serializer "{}"'.format(serializer))

    try:
        serializer = ReadWriteHandler.get_handler(serializer)
    except KeyError:
        log.error('No matching serializer found for "{}"'.format(serializer))
        return None

    load_func = serializer.loads

    try:
        doc = load_func(data)
    except Exception as exception:
        log.error('Could not load data using serializer "{}", encountered exception: {}'.format(serializer,
                                                                                                      exception))
        return None

    return doc


def verify_tool_schema(doc, log=fastr.log):
    """
    Verify the tool schema. Returns checked loaded object.

    :param doc: loaded object to check
    :param log: the logger to use to send messages to
    :return: object with checked schema
    """
    # Match the data to the schema for Tools
    log.info('Validating data against Tool schema')
    serializer = Tool.get_serializer()

    try:
        doc = serializer.instantiate(doc)
    except Exception as exception:
        log.error('Encountered a problem when verifying the Tool schema: {}'.format(exception))
        return None
    return doc


def verify_tool_instantiate(doc, filename, log=fastr.log):
    """
    Verify the tool schema. Returns checked loaded object.

    :param doc: loaded object
    :param filename: filename of the tool definition
    :param log: the logger to use to send messages to
    :return: Tool object
    """
    # Create the Tool object as the final test
    log.info(f'Instantiating Tool object')
    try:
        tool = Tool(doc)
        tool.filename = filename
    except Exception as exception:
        log.error('Encountered a problem when creating the Tool object: {}'.format(exception))
    return tool


def verify_tool(filename, log=fastr.log, perform_tests=True):
    """
    Verify that a tool correctly works. Returns Tool.

    :param filename: filename of the tool definition
    :param log: the logger to use to send messages to
    :param perform_test: Boolean to 
    :return: Tool object
    """
    # Load the file
    doc = verify_resource_loading(filename, log)

    if not doc:
        log.error('Could not load data successfully from  {}'.format(filename))
        return None

    # Match the data to the schema for Tools
    doc = verify_tool_schema(doc, log)

    # Create the Tool object as the final test
    tool = verify_tool_instantiate(doc, filename, log)

    if perform_tests:
        log.info('Testing tool...')
        try:
            tool.test()
        except fastr.exceptions.FastrValueError as e:
            log.error('Tool is not valid: {}'.format(e))

    return tool


def create_tool_test(filename, log=fastr.log):
    """
    Create test for fastr verify tool.

    By running `fastr verify -c tool FILENAME` the input data in the folders 
    under 'tests' in the tool definition is processed by the tool. The 
    output data is written to a folder in each test folder. In each test folder
    a gzipped pickle is created which is used to verify the working of the tool
    at a later time.

    :param filename: filename of the tool definition
    :param log: the logger to use to send messages to
    """
    # Load the file
    doc = verify_resource_loading(filename, log)

    if not doc:
        log.error('Could not load data successfully from  {}'.format(filename))
        return None

    doc = verify_tool_schema(doc, log)

    tool = verify_tool_instantiate(doc, filename, log)

    log.info('Loaded tool {} successfully'.format(tool))
    tool_dir = os.path.dirname(tool.filename)
    for test in tool.tests:
        reference_data_dir = os.path.abspath(os.path.join(tool_dir, test))
        try:
            if not isinstance(reference_data_dir, str):
                raise exceptions.FastrTypeError('reference_data_dir should be a string!')

            if reference_data_dir.startswith('vfs://'):
                reference_data_dir = vfs_plugin.url_to_path(reference_data_dir)

            if not os.path.isdir(reference_data_dir):
                raise exceptions.FastrTypeError('The reference_data_dir should be pointing to an existing directory!'
                                                ' {} does not exist'.format(reference_data_dir))

            test_data = iohelpers.load_json(
                os.path.join(reference_data_dir, tool.TOOL_REFERENCE_FILE_NAME)
            )

            input_data = {}

            for key, value in test_data['input_data'].items():
                if not isinstance(value, (tuple, list)):
                    value = value,

                # Set the $REFDIR correctly (the avoid problems with moving the reference dir)
                value = tuple(x.replace('$REFDIR', reference_data_dir) if isinstance(x, str) else x for x in value)
                input_data[key] = value

            temp_results_dir = None
            try:
                # Create temporary output directory
                temp_results_dir = os.path.normpath(mkdtemp(
                    prefix='fastr_tool_test_{}_'.format(tool.id), dir=config.mounts['tmp']
                ))

                # Create a new reference for comparison
                log.info('Creating new reference data for comparison...')
                try:
                    if not os.path.exists(os.path.join(reference_data_dir, 
                                                       tool.TOOL_RESULT_FILE_NAME)):
                        # Copy original __fastr_tool_ref__.json, 
                        # so it doesn't get overwritten. Afterwards move it back.
                        shutil.copy(os.path.join(reference_data_dir, 
                                                 tool.TOOL_REFERENCE_FILE_NAME), 
                                    os.path.join(reference_data_dir, 
                                                 ''.join([tool.TOOL_REFERENCE_FILE_NAME, 
                                                          'bak'])))
                        tool.create_reference(input_data,
                                              reference_data_dir,
                                              mount_name='__ref_tmp__',
                                              copy_input=False,
                                              input_datatypes=test_data['input_datatypes'])
                        log.info(
                            'Reference result for testing the {}/{} created in {}.'.format( 
                                 tool.ns_id, 
                                 tool.command_version,
                                 reference_data_dir
                        ))
                        shutil.copy(os.path.join(reference_data_dir, 
                                                 tool.TOOL_REFERENCE_FILE_NAME), 
                                    os.path.join(reference_data_dir, 
                                                 ''.join(['__output', 
                                                          tool.TOOL_REFERENCE_FILE_NAME])))
                        shutil.move(os.path.join(reference_data_dir, 
                                                 ''.join([tool.TOOL_REFERENCE_FILE_NAME, 
                                                          'bak'])),
                                    os.path.join(reference_data_dir, 
                                                 tool.TOOL_REFERENCE_FILE_NAME))
                    else:
                        log.warning(
                            'Reference result for testing the {}/{} tool already exists in {}!'.format( 
                                 tool.ns_id, 
                                 tool.command_version,
                                 reference_data_dir
                        ))
                except Exception as exception:
                    log.warning('Encountered exception when trying to run the {}/{} tool!'.format(
                        tool.ns_id, tool.command_version)
                    )
                    log.warning('Exception: [{}] {}'.format(type(exception).__name__, exception))
            finally:
                # Clean up
                log.info('Removing temp result directory {}'.format(temp_results_dir))
                if temp_results_dir is not None and os.path.isdir(temp_results_dir):
                    shutil.rmtree(temp_results_dir, ignore_errors=True)
        except exceptions.FastrTypeError:
            message = 'Reference data in {} is not valid!'.format(reference_data_dir)
            log.warning(message)
    return