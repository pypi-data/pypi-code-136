
# ------------------------------------------------------------------
#         _______          ____        _ _     _           
#        |__   __|        |  _ \      (_) |   | |          
#            | | ___   ___| |_) |_   _ _| | __| | ___ _ __ 
#            | |/ _ \ / __|  _ <| | | | | |/ _` |/ _ \ '__|
#            | | (_) | (__| |_) | |_| | | | (_| |  __/ |   
#            |_|\___/ \___|____/ \__,_|_|_|\__,_|\___|_|   
#
#                                                   fidle.TocBuilder
# ------------------------------------------------------------------
# A simple class to build a notebook catalog and generate the README.
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022


from posixpath import dirname
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pandas as pd
from IPython.display import display, Markdown, HTML

import re
import sys, os, glob, yaml
import pathlib
import json
from datetime import datetime
from collections import OrderedDict
from IPython.display import display

import fidle.config as config
from fidle.Chrono import Chrono


class TocBuilder:

    __version__  = config.VERSION



    def __get_files(self, directory, root_dir='.', types=['*.ipynb', '*.py', '*.sh']):
        '''
        Return a list of files to index, from a given directory
        args:
            directory  : dictory to index
            root_dir   : root directory (ie: where directory is)
            types       : Files type to index
        return:
            files : filenames list
        '''
        root_dir  = os.path.expanduser(root_dir)
        all_files = []

        for t in types:
            files = glob.glob(f'{root_dir}/{directory}/{t}')
            files.sort()
            all_files.extend(files)
            
        all_files = [ x.replace(f'{root_dir}/','') for x in all_files]
        return all_files



    def __get_infos(self, filename, root_dir='.'):
        '''
        Extract informations from filename.
        Informations are dirname, basename, id, title, description
        These informations are extracted from comments tags in markdown.
        args:
            filename : file path
            root_dir : root directory 
        return:
            dict : with infos.
        '''
        if filename.endswith('.ipynb'):
            return self.__get_notebook_infos(filename, root_dir)
        else:
            return self.__get_textfile_infos(filename, root_dir)



    def __get_notebook_infos(self, filename, root_dir='.'):
        '''
        Extract informations from a fidle notebook.
        Informations are dirname, basename, id, title, description and are extracted from comments tags in markdown.
        args:
            filename : notebook path from root_dir
            root_dir : root directory 
        return:
            dict : with infos.
        '''
        
        root_dir  = os.path.expanduser(root_dir)

        about={}
        about['id']          = '??'
        about['dirname']     = os.path.dirname(filename)
        about['basename']    = os.path.basename(filename)
        about['title']       = '??'
        about['description'] = '??'
        about['overrides']   = '??'
        
        # ---- Read notebook
        #
        notebook = nbformat.read(f'{root_dir}/{filename}', nbformat.NO_CONVERT)
        
        # ---- Get id, title, desc
        #
        overrides={}
        for cell in notebook.cells:
        
            # ---- Find informations
            #
            if cell['cell_type'] == 'markdown':

                # <!-- TITLE --> tag
                find = re.findall(r'<\!-- TITLE -->\s*\[(.*)\]\s*-\s*(.*)\n',cell.source)
                if find:
                    about['id']    = find[0][0]
                    about['title'] = find[0][1]

                # <!-- DESC --> tag
                find = re.findall(r'<\!-- DESC -->\s*(.*)\n',cell.source)
                if find:
                    about['description']  = find[0]

            # ---- Get override
            #
            if cell['cell_type'] == 'code':
                
                # Try to find : override(...) call
                for m in re.finditer('override\((.+?)\)', cell.source):
                    for override_name in re.findall(r'\w+', m.group(1)):
                        overrides[override_name]='default'

                about['overrides']=overrides

        return about


        
    def __get_textfile_infos(self, filename, root_dir='.'):
        '''
        Extract fidle  informations from a text file (script...).
        Informations are dirname, basename, id, title, description and are extracted from comments tags in document
        args:
            filename : file to analyze
        return:
            dict : with infos.
        '''

        root_dir  = os.path.expanduser(root_dir)

        about={}
        about['id']          = '??'
        about['dirname']     = os.path.dirname(filename)
        about['basename']    = os.path.basename(filename)
        about['title']       = '??'
        about['description'] = '??'
        about['overrides']   = []
        
        # ---- Read file
        #
        with open(f'{root_dir}/{filename}') as fp:
            text = fp.read()

        find = re.findall(r'<\!-- TITLE -->\s*\[(.*)\]\s*-\s*(.*)\n',text)
        if find:
            about['id']    = find[0][0]
            about['title'] = find[0][1]

        find = re.findall(r'<\!-- DESC -->\s*(.*)\n',text)
        if find:
            about['description']  = find[0]

        return about


 

    def __get_content(self, directories={}, root_dir='.'):

        root_dir = os.path.expanduser(root_dir)
        now      = Chrono.now()

        md       = [ f'<!-- Automatically generated on : {now} -->']

        campain= { 'campain' : {  
                        "version"          : '1.0',
                        "description"      : f'Automatically generated ci profile ({now})',
                        "directory"        : './campains/default',
                        "existing_notebook":   "remove    # remove|skip", 
                        "report_template"  :   "fidle     # fidle|default",
                        "timeout"          :   6000
                        }
                 }
        ci = [ yaml.dump(campain, sort_keys=False, default_flow_style=False) ]

        # ------ Notebooks -------------------------------------------------

        # ---- For each directory
        #
        for dir_name,dir_title in directories.items():
            
            # ---- Add title
            md.append(f'\n### {dir_title}')
            ci.append(f'\n#\n# ------------ {dir_name}\n#\n')

            # ---- For each file
            #
            ci_dir = OrderedDict()
            for filename in self.__get_files(dir_name, root_dir):
                
                # Get infos for toc
                #
                infos = self.__get_infos(filename, root_dir)
                file_id          = infos['id']
                file_dirname     = infos['dirname']
                file_basename    = infos['basename']
                file_title       = infos['title']
                file_description = infos['description']
                file_overrides   = infos['overrides']
                file_link        = f'{dir_name}/{file_basename}'.replace(' ','%20')

                md.append(  f'- **[{file_id}]({file_link})** - [{file_title}]({file_link})  '  )
                md.append(  f'{file_description}'  )
            
                # Get infos for ci (if ipynb)
                #
                if not file_basename.endswith('.ipynb'): continue

                ci_file = {}
                ci_file['notebook']  = f'{file_dirname}/{file_basename}'
                if len(file_overrides)>0: ci_file['overrides'] = file_overrides
                
                ci_dir[file_id] = ci_file
            
            # ---- ci / add directory ci
            ci.append( yaml.dump(dict(ci_dir), sort_keys=False, default_flow_style=False) )

        toc_md   = '\n'.join(md)
        toc_ci   = ''.join(ci)
        return toc_md, toc_ci



    def __build_ipynb_readme(self, readme_md='README.md', readme_ipynb='README.ipynb', root_dir='.'):
        '''
        Creation d'un notebook Readme from scratch et sauvegarde de celui-ci
        '''
        # ---- Create Notebook from scratch
        #
        notebook = nbformat.v4.new_notebook()

        # ---- Add a code cell
        #
        code = "from IPython.display import display,Markdown\n"
        code+= "display(Markdown(open('README.md', 'r').read()))\n"
        code+= "#\n"
        code+= "# This README is visible under Jupiter Lab ;-)"
        code+= f"# Automatically generated on : {Chrono.now()}"

        new_cell = nbformat.v4.new_code_cell(source=code)
        new_cell['metadata']= { "jupyter": { "source_hidden": True} }
        notebook.cells.append(new_cell)

        # --- To avoid a modification when opening the notebook
        # # Not annoying in itself, but it requires to save the document again when closing...
        notebook['metadata']["kernelspec"] = {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3" }

        # ---- Run it
        #
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(notebook,  {'metadata': {'path': root_dir}})

        # ---- Save it
        #
        readme_path = f'{root_dir}/{readme_ipynb}'
        with open(readme_path, mode="w", encoding='utf-8') as fp:
            nbformat.write(notebook, fp)



    def __tag(self,tag, text, document):
        '''
        Put a text inside a tag
        args:
            tag : tag prefix name
            txt : text to insert
            document : document 
        return:
            updated document
        '''
        debut  = f'<!-- {tag}_BEGIN -->'
        fin    = f'<!-- {tag}_END -->'

        output = re.sub(f'{debut}.*{fin}',f'{debut}{text}{fin}',document, flags=re.DOTALL)
        return output




    def update(self, about_file='./fidle/about.yml', root_dir='.'):
        '''
        Update readme with about_file informations
        args:
            about_file : yaml file with fidle informations (./fidle/about.yml)
            root_dir   : root directory (.)
        return:
            Nothing, updated readme is just saved.
        '''

        print(f'\n=== Fidle/TocBuilder - Update tables of content')
        print(f'=== Version : {self.__version__}\n')

        # ---- Preparation
        #
        if about_file is None : 
            print('About_file is None.. exit.')
            return

        root_dir    = os.path.expanduser(root_dir)
        about_file  = os.path.expanduser(about_file)

        # ---- Load about.yml file
        #
        with open(about_file,'r') as fp:
            about=yaml.load(fp, Loader=yaml.FullLoader)

        readme_md    = about['readme_md']
        readme_ipynb = about['readme_ipynb']
        ci_file      = about['default_ci']
        version      = about['version']
        directories  = about['toc']

        print('Update parameters :')
        print('    Root directory   : ', root_dir)
        print('    About file       : ', about_file)

        # ---- Get toc
        #
        print('\nStart update :')
        print(f'    Build toc, for readme and ci...')
        toc_md,toc_ci = self.__get_content(directories, root_dir)

        # ---- Readme markdown -------------------------------------
        #
        # ---- Load readme
        #
        readme_path = f'{root_dir}/{readme_md}'
        print(f'    Load markdown readme...')
        with open(readme_path, 'r') as f:
            readme = f.read()

        # ---- tag version
        #
        print(f'    Update : Version -> {version}')
        readme=self.__tag('VERSION', version, readme)
        
        print(f'    Update : toc')
        readme=self.__tag('TOC', f'\n{toc_md}\n', readme)

        # ---- Save it
        print(f'    Save new markdown readme        : {readme_md}')
        with open(readme_path, 'w') as f:
            f.write(readme)

        # ---- Readme ipynb ----------------------------------------
        #
        print('    Build ipynb readme...')
        self.__build_ipynb_readme(readme_md, readme_ipynb, root_dir)
        print(f'    Save new ipynb readme           : {readme_ipynb}')

        # ---- Save default ci profile -----------------------------
        #
        ci_path = f'{root_dir}/{ci_file}'
        with open(ci_path,'wt') as f:
            f.write(toc_ci)
            print(f'    Save new default ci profile     : {ci_file}')
        print('    done.\n')

