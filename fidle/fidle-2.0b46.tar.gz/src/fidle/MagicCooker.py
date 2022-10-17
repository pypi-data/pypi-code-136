
# ------------------------------------------------------------------
#   __  __             _       _____            _             
#  |  \/  |           (_)     / ____|          | |            
#  | \  / | __ _  __ _ _  ___| |     ___   ___ | | _____ _ __ 
#  | |\/| |/ _` |/ _` | |/ __| |    / _ \ / _ \| |/ / _ \ '__|
#  | |  | | (_| | (_| | | (__| |___| (_) | (_) |   <  __/ |   
#  |_|  |_|\__,_|\__, |_|\___|\_____\___/ \___/|_|\_\___|_|   
#                 __/ |                                       
#                |___/                             fidle.MagicCooker
# ------------------------------------------------------------------
# A simple class to run a set of notebooks with parameters overriding
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022

import sys,os,platform
import re
import yaml
import base64

import nbformat
from nbconvert               import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

import fidle.config       as     config
from fidle.Chrono         import Chrono
from fidle.MagicFeedback  import MagicFeedback
from fidle.MagicReport    import MagicReport
from fidle.TaskManager    import TaskManager


class MagicCooker:

    __version__  = config.VERSION


    def __init__(self):
        pass





    # --------------------------------------------------------------
    # Get profile
    # --------------------------------------------------------------
    #
    def __get_profile( self, 
                        profile_name = None, 
                        root_dir     = None,
                        filters      = ['.*'], 
                        campain_tag  = None):

        '''Load yaml profile'''

        # ---- Read profile
        #
        with open(profile_name,'r') as fp:
            profile=yaml.load(fp, Loader=yaml.FullLoader)

        # ---- Retreive campain, notebooks
        #
        campain   = profile['campain']
        notebooks = profile
        del notebooks['campain'] 

        # ---- Campain_dir
        #
        campain_dir = campain['directory']

        # Add tag if needed
        if campain_tag is not None: campain_dir += campain_tag

        # Absolute path from root_dir
        campain_dir = os.path.abspath( f'{root_dir}/{campain_dir}' )

        # ---- Complete campain
        #
        campain['host']         = platform.uname()[1]
        campain['location']     = os.getcwd()
        campain['profile']      = profile_name
        campain['date']         = Chrono.now(format='%A %-d %B %Y %H:%M:%S')
        campain['filters']      = filters
        campain['campain_dir']  = campain_dir

        # ---- Sub directories
        #
        campain['campain_html_dir']     = f'{campain_dir}/html'
        campain['campain_ipynb_dir']    = f'{campain_dir}/ipynb'
        campain['campain_feedback_dir'] = f'{campain_dir}/feedback'
        campain['campain_trace_dir']    = f'{campain_dir}/trace'

        # ---- Task and lock files
        #
        campain['campain_task_file']    = f'{campain_dir}/trace/task_list.json'
        campain['campain_lock_file']    = f'{campain_dir}/trace/task_list.lock'

        # What to do if a notebook already exists (default is skip)
        #
        if 'existing_notebook' not in campain : campain['existing_notebook']='skip'

        return campain, notebooks







    def reset_campain(self, 
                      profile_name = None, 
                      root_dir     = None,
                      filters      = ['.*'],
                      campain_tag  = None):
        '''
        Reset a campain - ie: remove posibles trace and task files
        args:
            profile_name : A profile in yml
            root_dir     : The root directory to be for this profile
            campain_tag  : tag to add to this campain
        return:
            None
        '''

        # ---- Expand dir
        #
        profile_name = os.path.expanduser(profile_name)
        root_dir     = os.path.expanduser(root_dir)
 
        # ---- Welcome
        #
        print(f'\n=== Fidle/MagicCooker - Reset campain')
        print(f'=== Version : {self.__version__}')

        # ---- Get profile
        #
        try:
            campain, notebooks = self.__get_profile(profile_name, root_dir, filters, campain_tag)
        except:
            print('\n*** OUPS : The profile cannot be found or retrieved... \n')
            return


        print('\nProfile           : ', campain['profile'])
        print('Campain directory : ', campain['campain_dir'],'\n')

        # ---- Remove task and lock files
        #
        try:
            os.remove(campain['campain_task_file'])
            print('Task file is removed.')
        except OSError:
            print('Task file not found.')
        try:
            os.remove(campain['campain_lock_file'])
            print('Lock file is removed.')
        except OSError:
            print('Lock file not found.')
        print('Done.\n')






    # --------------------------------------------------------------
    # Run campain
    # --------------------------------------------------------------
    #    
    def run_campain( self, 
                     profile_name = None, 
                     root_dir     = None,
                     filters      = ['.*'], 
                     campain_tag  = None):
        '''
        
        '''

        profile_name = os.path.expanduser(profile_name)
        root_dir     = os.path.expanduser(root_dir)
 
        print(f'\n=== Fidle/MagicCooker - Run campain')
        print(f'=== Version : {self.__version__}')

        # ---- Here and now ----------------------------------------
        #
        chrono = Chrono()
        chrono.start()

        # ---- About filters ---------------------------------------
        #       
        # Filters is a string
        if isinstance(filters, str) : filters = [s.strip() for s in filters.split(',')]
        # Not a list...
        if not isinstance(filters, list) :
            self.show(f"*** Oups, filters is invalid...")
            sys.exit(1)

        # ---- Retrieve profile ------------------------------------
        #
        try:
            campain, notebooks = self.__get_profile(profile_name, root_dir, filters, campain_tag)
        except:
            print('\n*** OUPS : The profile cannot be found or retrieved... \n')
            return


        # # ---- About this campain ----------------------------------
        # #
        print('\nCampain loaded :')
        print('    Date                : ', campain['date'])
        print('    Host                : ', campain['host'])
        print('    Current location    : ', campain['location'])
        print('    Profile             : ', campain['profile'])
        print('    Description         : ', campain['description'])
        print('    Version             : ', campain['version'])
        print('    Filters             : ', campain['filters'])
        print('    Campain directory   : ', campain['campain_dir'])
        print('    Existing notebook   : ', campain['existing_notebook'])
        print('    Notebook timeout    : ', campain['timeout'])

        # ---- Create campain directories
        #
        os.makedirs( campain['campain_html_dir'    ], mode=0o750, exist_ok=True)
        os.makedirs( campain['campain_ipynb_dir'   ], mode=0o750, exist_ok=True)
        os.makedirs( campain['campain_trace_dir'   ], mode=0o750, exist_ok=True)
        os.makedirs( campain['campain_feedback_dir'], mode=0o750, exist_ok=True)

        # ---- Environment vars ------------------------------------
        #
        environment_vars = campain.get('environment_vars',{})

        # ---- Create a nice task list -----------------------------
        # ----------------------------------------------------------
        #
        task_list=[]
        for task_id,notebook in notebooks.items():

            task = dict( id     = task_id,
                         after  = notebook.get('after',None),
                         status = 'desactivated' )

            if self.__match_filters(task_id, filters): task['status']='ready'
            task_list.append(task)

        # ---- Create a nice TaskManager ---------------------------
        # ----------------------------------------------------------
        #
        task_file = campain['campain_task_file' ]
        lock_file = campain['campain_lock_file' ]
       
        # ---- Create a TaskManager
        #
        tm = TaskManager( task_list, 
                          taskfile = task_file,
                          lockfile = lock_file,
                          verbose  = 0)

        # ---- Update dependencies
        #
        updated = tm.update_dependencies()
        if len(updated)>0:
            print('\nNote : For reasons of dependencies, the following tasks have been added : ')
            for task_id in updated:
                notebook = notebooks[task_id]
                path     = notebook['notebook']
                print(f'    {task_id:18s} : {path}')

        # ---- Prepare report
        #
        reporter = MagicReport(campain, notebooks, task_file)

        # ---- Run all tasks -----------------------------------------------
        # ------------------------------------------------------------------
        #
        for task_id in tm.runnable():

            notebook = notebooks[task_id]

            # ---- Get notebook infos ------------------------------
            #
            notebook_path = notebook['notebook']
            notebook_path = os.path.abspath( f'{root_dir}/{notebook_path}' )  # abs path of notebook from root_dir
            done_tag      = f'=={task_id}.done=='
            overrides     = notebook.get('overrides',{})
                
            # ---- Run notebook ------------------------------------
            # 
            feedback = self.run_notebook(  task_id            = task_id,
                                           notebook_path      = notebook_path,
                                           environment_vars   = environment_vars,
                                           overrides          = overrides,
                                           output_ipynb_dir   = campain['campain_ipynb_dir' ],
                                           output_html_dir    = campain['campain_html_dir'  ],
                                           output_tag         = done_tag,
                                           existing_notebook  = campain['existing_notebook'],
                                           timeout            = campain['timeout']
            )
            # ---- Save feedback -----------------------------------
            #
            if not feedback['status'] == 'skip': 
                # ---- Report filename
                feedback_dir  = campain['campain_feedback_dir']
                feedback_file = f'{feedback_dir}/{task_id}.json'
                # ---- Save feedback, with many infos
                mgfeed = MagicFeedback()
                mgfeed.add( task_id  = task_id,
                            campain  = campain, 
                            notebook = notebook,
                            feedback = feedback)
                mgfeed.save(feedback_file)
                print(f'    - Save feedback : {task_id}.json')

            # ---- Report ------------------------------------------
            #
            reporter.build_report()
            print(f'    - Report updated.')

        # ---- Update report
        #      Needed because task_file is saved out of step
        #
        reporter.build_report()
        
        # ---- End
        #
        print('\nDone.\n')
        tm.about_this_runner()





    # --------------------------------------------------------------
    # Run notebook
    # --------------------------------------------------------------
    #
    def run_notebook( self,
                      task_id            = None,
                      notebook_path      = None,
                      environment_vars   = {},
                      overrides          = {},
                      output_ipynb_dir   = './',
                      output_html_dir    = './',
                      output_tag         = '==done==',
                      existing_notebook  = 'remove',
                      timeout            = 6000 ):

        # ---- reporting -------------------------------------------
        #
        feedback = dict( task_id        = task_id, 
                         notebook_path = notebook_path)

        print('\nRun :', task_id)

        # ---- Notebook exist ? ------------------------------------
        #
        if task_id is None:
            print('    *** Abort : task_id cannot be None')
            feedback['status'] = 'error'
            feedback['error']  = 'Invalid task_id'
            return feedback

        if not os.path.isfile(notebook_path):
            print('    *** Abort : Notebook cannot be found : ', notebook_path )
            feedback['status'] = 'error'
            feedback['error']  = 'Notebook not found'
            return feedback

        # ---- Outputs ---------------------------------------------
        #
        notebook_dir  = os.path.dirname(  notebook_path )
        notebook_name = os.path.basename( notebook_path )
        notebook_noex = os.path.splitext( notebook_name)[0]

        output_ipynb_dir    = os.path.abspath(output_ipynb_dir)
        output_html_dir     = os.path.abspath(output_html_dir)

        output_ipynb_file   = f'{output_ipynb_dir}/{notebook_noex}{output_tag}.ipynb'
        output_html_file    = f'{output_html_dir}/{notebook_noex}{output_tag}.html'

        if (os.path.isfile(output_ipynb_file) or os.path.isfile(output_html_file) ) :
            # Output exist...
            if existing_notebook=='skip':
                # Skip : abort run
                print('    - Notebook output exist : Skip')
                feedback['status'] = 'skip'
                return feedback
            else:
                # Remove it
                print('    - Output exist : Remove it')
                if os.path.isfile(output_ipynb_file) : os.remove(output_ipynb_file)
                if os.path.isfile(output_html_file)  : os.remove(output_html_file)

        # ---- Set environment vars --------------------------------
        #
        to_unset=[]
        if isinstance(environment_vars, dict):
            print('    - Environment vars:')
            for name,value in environment_vars.items():
                # Set env
                os.environ[name] = str(value)
                # For cleaning
                to_unset.append(name)
                # About
                print(f'        {name:30s} = {value}')

        # ---- Set Overrides ---------------------------------------
        #
        print('    - Overrides :')
        if not isinstance(overrides, dict): overrides = {}

        # Probably add an override for task_id
        if not 'run_id' in overrides: overrides['run_id'] = task_id

        for name,value in overrides.items():
            # Default : no nothing
            if value=='default' : continue
            #  Set env
            env_name  = f'FIDLE_OVERRIDE_{name}'
            env_value = str(value)
            os.environ[env_name] = env_value
            # For cleaning
            to_unset.append(env_name)
            # About
            print(f'        {env_name:30s} = {env_value}')
                
        # ---- Reporting -------------------------------------------
        #
        feedback['environment_vars']  = environment_vars
        feedback['overrides']         = overrides

        # ---- Ok, Ready ? -----------------------------------------
        #
        chrono = Chrono()
        chrono.start()

        # ---- Run it ! --------------------------------------------
        #
        print('    - Notebook start...')
                
        try:
            notebook = nbformat.read( notebook_path, nbformat.NO_CONVERT)
            ep = ExecutePreprocessor(timeout=timeout, kernel_name="python3")
            ep.preprocess(notebook,  {'metadata': {'path': notebook_dir}})
            feedback['status'] = 'ok'
        except CellExecutionError as e:
            output_tag = f'=={task_id}.ERROR=='
            print('*'*60)
            print('** Oups, an error occured : ',type(e).__name__)
            print('*'*60)
            feedback['status'] = 'error'
            feedback['error']  = 'Notebook error'

        except Exception as e:
            notebook  = None
            print('*'*60)
            print('** AAARG.. A fatal error occured : ',type(e).__name__)
            print('*'*60)
            feedback['status'] = 'error'
            feedback['error']  = 'Fatal error'

        print('    - Notebook done.')
        
        # ---- Top chrono - Stop
        #
        chrono.stop()
        print(f'    - Duration    : {chrono.get_delay()}' )
        feedback['duration']  = chrono.get_delay(format='seconds')
        feedback['start']     = chrono.get_start()
        feedback['end']       = chrono.get_end()


        # ---- Clean env and overrides -----------------------------
        #
        for env_name in to_unset:
            del os.environ[env_name]

        # ---- Do nothing more if notebook died -------------------------
        #
        if notebook is None: 
            return feedback

        # ---- Check for images to embed ---------------------------
        #      We just try to embed <img src="..."> tag in some markdown cells
        #      Very fast and suffisant for header/ender.
        #
        for cell in notebook.cells:
            if cell['cell_type'] == 'markdown':
                cell.source = self.__images_embedder(cell.source, notebook_dir)

        # ---- Save notebook as ipynb -----------------------------------------
        #
        if output_ipynb_dir is not None:
            # Notebook filename (rebuilt because tag can be changed)
            output_ipynb_file = f'{output_ipynb_dir}/{notebook_noex}{output_tag}.ipynb'
            os.makedirs(output_ipynb_dir, mode=0o750, exist_ok=True)
            # Save
            with open(output_ipynb_file, mode="w", encoding='utf-8') as fp:
                print(f'    - Save ipynb  : {notebook_noex}{output_tag}.ipynb')
                nbformat.write(notebook, fp)

        # ---- Save notebook as html ------------------------------------------
        #
        if output_html_dir is not None:

            # ---- Convert notebook to html
            exporter = HTMLExporter()
            exporter.template_name = 'classic'
            (body_html, resources_html) = exporter.from_notebook_node(notebook)
            
            # ---- Embed images
            # Note : Pas du tout efficace.. et a priori inutile car le notebook a dejà été traité
            # body_html = self.__images_embedder(body_html)
            # print('    - html : images embedded.')

            # ---- Save
            # HTML filename (rebuilt because tag can be changed)
            output_html_file = f'{output_html_dir}/{notebook_noex}{output_tag}.html'
            os.makedirs(output_html_dir, mode=0o750, exist_ok=True)
            # Save
            with open(output_html_file, mode='wb') as fp:
                print(f'    - Save html   : {notebook_noex}{output_tag}.html')
                fp.write(body_html.encode("utf-8"))

        # ---- Reporting
        #
        feedback['output_ipynb_file'] = f'{notebook_noex}{output_tag}.ipynb'
        feedback['output_html_file']  = f'{notebook_noex}{output_tag}.html'

        # ---- Back to the old world..
        #
        return feedback


    # --------------------------------------------------------------
    # -- Match Filter
    # --------------------------------------------------------------
    #
    def __match_filters(self, task_id, filters):
        # We will look for a good reason to accept

        # Filters is None : Ok
        if filters is None : return True

        # For each filter
        for filter in filters:
            if re.match(filter, task_id): return True

        # Arrived here, we found no reason to accept
        return False
    
    

    def __get_base64_image(self, filename):
        '''
        Read an image file and return as a base64 encoded version
        params:
            filename : image filemane
        return:
            base 64 encoded image
        '''
        with open(filename, "rb") as image_file:
            img64 = base64.b64encode(image_file.read())
        src="data:image/svg+xml;base64,"+img64.decode("utf-8") 
        return src



        
    def __images_embedder(self, html, notebook_dir):
        '''
        Images embedder. Search images src="..." link and replace them
        by base64 embedded images.
        params:
            html: input html
        return:
            output html
        '''
        for img_tag in re.findall('.*(<img .*>).*', html):
            for src_tag in re.findall('.*src=[\'\"](.*)[\'\"].*', img_tag):
                # ---- Is is a data: tag ?
                if src_tag.startswith('data:'): continue
                # ---- Change file image to data:
                src_path = f'{notebook_dir}/{src_tag}'
                src_b64 = self.__get_base64_image(src_path)
                # ---- Replace it
                img_b64 = img_tag.replace(src_tag, src_b64)
                html = html.replace(img_tag,img_b64)
        return html


