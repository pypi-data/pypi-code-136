# ------------------------------------------------------------------
#   __  __             _      _____                       _   
#  |  \/  |           (_)    |  __ \                     | |  
#  | \  / | __ _  __ _ _  ___| |__) |___ _ __   ___  _ __| |_ 
#  | |\/| |/ _` |/ _` | |/ __|  _  // _ \ '_ \ / _ \| '__| __|
#  | |  | | (_| | (_| | | (__| | \ \  __/ |_) | (_) | |  | |_ 
#  |_|  |_|\__,_|\__, |_|\___|_|  \_\___| .__/ \___/|_|   \__|
#                 __/ |                 | |                   
#                |___/                  |_|        fidle.MagicReport
# ------------------------------------------------------------------
# A simple class to manage execution reports
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022

import os
import pathlib
import json
from string import Template

import fidle.config as config
import fidle.utils  as utils


class MagicReport :

    __version__  = config.VERSION
    

    def __init__(self, campain=None, notebooks=None, task_file=None):
        self.campain   = campain
        self.notebooks = notebooks
        self.task_file = task_file
        self.template  = campain.get('report_template','default')
        


    # --------------------------------------------------------------
    # -- Report stuffs
    # --------------------------------------------------------------
    #
    def build_report(self):

        # ---- Retrieve infos
        #
        campain   = self.campain
        notebooks = self.notebooks

        with open(self.task_file) as fp:
                task_list = json.load(fp)

        # ---- Metadata part
        #
        html_metadata=''
        for k in ['version', 'description', 'date', 'host', 'profile']:
            name   = k.title()
            value  = str( campain.get(k,'??') )
            html_metadata +=  f'<b>{name}</b> : {value} <br>\n'

        # ---- Retrieve reports
        #
        report_dir    = campain['campain_html_dir']
        feedback_dir  = campain['campain_feedback_dir']
        missing       = []

        # ---- Add table header
        html_report = '<table>'
        html_report += '<tr><th>Id</th><th>Status</th><th>Notebook</th><th>Start</th><th>Duration</th><th>Running</th><th>By</th></tr>\n'

        # ---- Add lines
        #
        total_duration = 0
        for task_id in notebooks.keys():
            feedback_file = f'{feedback_dir}/{task_id}.json'
            
            # ---- Get report, if exist
            #
            if os.path.isfile(feedback_file):
                # Read it 
                with open(feedback_file) as fp:
                    feedback = json.load(fp)
            else:
                # Empty report
                feedback={}
                missing.append(task_id)

            # ---- Get task if exist
            #
            task={}
            for t in task_list:
                if t['id']==task_id: task=t         

            # ---- Get infos
            #
            s_notebook = feedback.get('notebook', {})
            s_feedback = feedback.get('feedback', {})

            path        = s_notebook.get('notebook', '-')
            status      = s_feedback.get('status',   '-')
            start       = s_feedback.get('start',    '-')
            duration    = s_feedback.get('duration', '-')
            done_html   = s_feedback.get('output_html_file', '#')
            task_status = task.get('status','-')
            task_runner = task.get('runner','-')
                   
            if task_status not in ['running','done','ready'] : 
                task_status = '-'
                task_runner = '-'
            
            if isinstance(duration,float):
                total_duration+=duration
                duration=utils.hdelay(duration)

            cols = []
            cols.append( task_id  )
            cols.append( status   )
            cols.append( f'<a href="{done_html}" target="_blank">{path}</a>' )
            cols.append( start    )
            cols.append( duration )
            cols.append( task_status )
            cols.append( task_runner )

            html_report+='\n<tr>'
            for c in cols:
                html_report+=f'<td>{c}</td>'
            html_report+='</tr>\n'

        total_duration=utils.hdelay(total_duration)

        html_report+='</table>'
        html_report+=f'<div>Cumulative duration : {total_duration}</div>'

        # ---- Finalize report
        #
        body_html = self.__finalize_report(html_metadata, html_report)

        # ---- Save it
        #
        report_file = f'{report_dir}/index.html'

        with open(report_file, "wt") as fp:
            fp.write(body_html)
        # print(f'\nSaved HTML full report : {report_file}')
            

    

    def __finalize_report(self,html_metadata, html_report):

        # ---- Load template
        # 
        if self.template in ['default', 'fidle']:
            # Predefined template
            module_dir = pathlib.Path(__file__).parent
            template_path = f'{module_dir}/templates/MagicReport_{self.template}.html'
        else:
            # Given template
            template_path = self.template

        template = Template( open(template_path).read() )

        # ---- Template substitution
        #
        if self.template=='fidle':
            logo_header = open(f'{module_dir}/img/00-Fidle-header-01.svg'   ).read()
            logo_ender  = open(f'{module_dir}/img/00-Fidle-logo-01-80px.svg').read()
            html= template.substitute( logo_header   = logo_header, 
                                       logo_ender    = logo_ender,
                                       html_report   = html_report, 
                                       html_metadata = html_metadata,
                                       fidle_version = config.VERSION)
        else:
            html= template.substitute( html_report   = html_report, 
                                       html_metadata = html_metadata,
                                       fidle_version = config.VERSION)

        return html