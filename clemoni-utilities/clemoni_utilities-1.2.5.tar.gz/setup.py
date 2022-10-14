from setuptools import setup

setup(
    name='clemoni_utilities',
    version='1.2.5',
    url='https://github.com/clemoni/clemoni_utilities',
    author='Clement Liscoet',
    author_email='clement.liscoet@gmail.com',
    license='MIT',
    description='A short utility library for Python',
    long_description="""Provide a function for folder manipulation mainly:
    - apply_fun_to_list
    - if_regex_return_value
    - exit_if_error
    - try_except_all
    - if_type_test_bool
    - if_test_is_value_test_return_test_none
    - compose* (currying function, up to 5 functions)
    - check_given_folder
    - get_file_from_dir
    - get_file_object_from_dir
    - get_file_from_dir_if_extension
    - get_file_object_from_dir_if_extension
    - get_the_latest_inserted (document)
    - delete_all_files_from_dir
    - delete_all_folders_from_dir
    - create_sub_directory
    - redirect_file
    - redirect_file_object
    - redirect_folder
    - get_folder_from_dir
    - get_folder_object_from_dir_if_name
    - get_folder_object_from_dir
    - is_subfolders
    - flatten_list
    - confirm_choice
    - yes_no_prompt
    - init_grab_key
    """,
    packages=['utilities'],
    install_requires=['SQLAlchemy',
                      'mysql-connector-python', 
                      'pymysql',
                      'pyyaml'                  
                      ],
    py_modules=['primary_tools', 'db_tools']
)