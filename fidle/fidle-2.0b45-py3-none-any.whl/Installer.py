
# ------------------------------------------------------------------
#   ______ _     _ _        _____           _        _ _           
#  |  ____(_)   | | |      |_   _|         | |      | | |          
#  | |__   _  __| | | ___    | |  _ __  ___| |_ __ _| | | ___ _ __ 
#  |  __| | |/ _` | |/ _ \   | | | '_ \/ __| __/ _` | | |/ _ \ '__|
#  | |    | | (_| | |  __/  _| |_| | | \__ \ || (_| | | |  __/ |   
#  |_|    |_|\__,_|_|\___| |_____|_| |_|___/\__\__,_|_|_|\___|_|   
#
#                                                    Fidle installer
# ------------------------------------------------------------------
# A simple class to install fidle notebooks and datasets
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022


import os, sys
import importlib
import yaml
import requests, json
import tarfile
from random import randint

from IPython.display import display

import fidle.config       as     config
import fidle.utils        as     utils


class Installer:

    __version__  = config.VERSION


    def __init__(self):
        
        try:
            self.catalog = self.__load_catalog()
        except:
            print('\n*** OUPS ! The list of available installations cannot be retrieved...')
            print("*** Maybe it's a network problem or a Fidle problem.\n")



    def __load_catalog(self):
        '''
        Load the catalog od ressources
        args:
            None
        return:
            The catalog as a dict
        '''
        url = requests.get(config.CATALOG_URL)
        data = json.loads(url.text)
        return data


    def __check_catalog_name(self, catalog_name):
        '''
        Check catalog name
        args:
            catalog_name : Catalalog name
        return:
            True if catalog exist else False
        '''
        if not f'{catalog_name}.list' in self.catalog:
            print(f'\n*** Oups, The requested catalog "{catalog_name}" cannot be found...')
            return False
        return True


    def __check_directory(self, directory='.'):
        '''
        Check if directory exist and is writable
        args:
            directory :  directory to check
        return:
            True if installation directory exist else False
        '''
        if not os.path.isdir(directory):
            print('\n*** Oups, the installation directory cannot be found...\n')
            return False
        if not os.access(directory, os.W_OK):
            print('\n*** Oups, the installation directory is not writeable...\n')
            return False
        return True


    def __download_ressource(self, url, installation_dir='.', verbose=1):
        '''
        Download a ressource under a random prefixed name.
        args:
            url : Ressource URL
            installation_dir : The place to download the resource (.)
        return:
            Path to the downloaded ressource
        '''
        # ---- Check intallation_dir
        #
        installation_dir = os.path.expanduser(installation_dir)
        if not self.__check_directory(installation_dir): return False

        # ---- Retrieve all infos
        #
        ressource_name   = os.path.basename(url)
        prefix           = str(randint(1000000, 9999999))
        ressource_path   = f'{installation_dir}/_{prefix}_{ressource_name}'

        # ---- Download ressource
        #
        with open(ressource_path, "wb") as fp:
            response     = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                fp.write(response.content)
            else:
                total_length = int(total_length)
                total_hsize  = utils.hsize(total_length)
                dl   = 0
                i    = 0
                imax = int(total_length/4096)
                for data in response.iter_content(chunk_size=4096):
                    fp.write(data)
                    if verbose>0: utils.update_progress('Download : ',i,imax, redraw=False, verbosity=1, total_max=total_hsize)
                    i+=1
        return ressource_path


    def __extract_ressource(self, ressource_path, installation_dir='.', verbose=1):
        '''
        Extract a downloded ressource to an installation_dir
        args:
            ressource path : Path to the ressource tar archive
            installation_dir : The place to extract 
        return:
            installation dir
        '''
        # ---- Check intallation_dir
        #
        installation_dir = os.path.expanduser(installation_dir)
        if not self.__check_directory(installation_dir): return False

        # ---- Tar extraction
        #
        with tarfile.open(name=ressource_path) as tar:

            imax = len(tar.getmembers())
            i    = 0
            total_files = f'{imax} files'
            for member in tar.getmembers():
                i+=1
                tar.extract(member=member, path=installation_dir)
                if verbose>0: utils.update_progress('Extract  :',i,imax, redraw=False, verbosity=1, total_max=total_files)
        
        return installation_dir




    def show_branch(self,catalog_name=None):
        '''
        Print a description of available resources.
        args:
            catalog_name : Catalog name,  'notebooks'|'datasets'
        return:
            A textual description on the catalog or False
        '''
        # ---- Get catalog
        #
        if not self.__check_catalog_name(catalog_name): return False

        catalog_list    = self.catalog[ f'{catalog_name}.list']
        catalog_default = self.catalog[ f'{catalog_name}.default']

        # ---- Build description
        #
        about = f'Installable resources in catalog [{catalog_name}]\n\n'
        for entry in catalog_list:
            name = entry['name']
            desc = entry['description']
            if name == catalog_default : name = name+'*'
            about += f'   - {name:20s} :  {desc}\n'

        # ---- Print or display
        #
        print(about)



    def install_ressource(self, catalog_name=None, ressource_name=None, installation_dir='.', verbose=1):
        '''
        Install a ressource
        args:
            catalog_name     : Catalog name, 'notebooks'|'datasets'
            ressource_name   : Resource name in the catalog
            installation_dir : The location where to install the requested resource
        return:
            True if the install is ok, else False
        '''

        # ---- Welcome
        #
        if verbose>1:
            print(f'\n=== Fidle/Installer - Install ')
            print(f'=== Version : {self.__version__}')

        # ---- Check catalog_name
        #
        if verbose>1: print('Check requested ressource...')
        if not self.__check_catalog_name(catalog_name): return False

        # ---- Default ressource ?
        #
        if ressource_name=='default':
            ressource_name = self.catalog[ f'{catalog_name}.default' ]
        
        # ---- Check intallation_dir
        #
        if verbose>1: print('Check installation directory...')
        installation_dir = os.path.expanduser(installation_dir)
        if not self.__check_directory(installation_dir): return False

        if os.path.isdir( f'{installation_dir}/{ressource_name}' ):
            print(f'\n*** Oups, the installation directory already contains a directory "{ressource_name}"...\n')
            return

        # ---- Try to find the ressource url/name
        #
        found=False
        for entry in self.catalog[ f'{catalog_name}.list']:
            if entry['name'] == ressource_name:
                found=True
                break
        
        if not found:
            print('\n*** Oups, the requested resource is not in the catalog...\n')
            return

        ressource_url  = entry['url']

        # ---- Download and install ressource
        #
        if verbose>0: 
            print(f'Install ressource : {ressource_name}')
            print(f'In directory      : {installation_dir}')
        ressource_path   = self.__download_ressource(ressource_url, installation_dir, verbose=verbose)
        installation_dir = self.__extract_ressource(ressource_path, installation_dir, verbose=verbose)

        os.remove(ressource_path)
        print('Done.\n')
        # 


    def check(self, directory='.'):
        
        # ---- Clean/expand directory
        #
        directory = os.path.expanduser(directory)
        directory = os.path.abspath(directory)

        # ---- Search notebooks and datasets
        # le dossier exploré
        print('Notebooks and datasets can only be found if they are in/near the explored folder.')
        print(f'Explored directory is : {directory}')

        # datasets_dir by env var
        datasets_dir = os.getenv('FIDLE_DATASETS_DIR', 'undefined')
        # Searching
        notebooks, datasets = utils.looking_about(path=directory)

        # ---- Check datasets
        # 
        print('\nDatasets dir found : \n')

        for d in datasets:
            print(f"    {d['path']:50s}   ({d['name']} / {d['version']})")

        print(f'    The environment variable FIDLE_DATASETS_DIR is :     {datasets_dir}')

        if len(datasets)==0 and datasets_dir=='undefined':
            print('\n    ** No datasets directory found...')
            print('    ** Have you installed the notebooks ?')
            print('    ** Are you in / do you check the right directory ?')

        # ---- Check notebooks
        #
        print('\nNotebooks dir found : \n')


        for d in notebooks:
            print(f"    {d['path']:50s}   ({d['name']} / {d['version']})")

        if len(notebooks)==0:
            print('    ** No notebooks directory found...')
            print('    ** Have you installed the notebooks?')
            print('    ** Are you in /do ou check the right directory ?')

        # ---- Check environment
        #
        print('\nCheck environment : \n')
        print(f'    Fidle module         : Ok         ({config.VERSION})')

        for mod in config.USED_MODULES:
            try:
                importlib.import_module(mod)
                print(f'    {mod:21s}: Ok         ({sys.modules[mod].__version__})')
            except:
                print(f'    {mod:21s}: Not found')
        print('')
