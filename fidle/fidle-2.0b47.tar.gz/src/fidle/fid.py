
# ------------------------------------------------------------------
#   ______ _     _ _                    _           _       
#  |  ____(_)   | | |          /\      | |         (_)      
#  | |__   _  __| | | ___     /  \   __| |_ __ ___  _ _ __  
#  |  __| | |/ _` | |/ _ \   / /\ \ / _` | '_ ` _ \| | '_ \ 
#  | |    | | (_| | |  __/  / ____ \ (_| | | | | | | | | | |
#  |_|    |_|\__,_|_|\___| /_/    \_\__,_|_| |_| |_|_|_| |_|
#                                                  Fidle admin (fid)
# ------------------------------------------------------------------
# A simple class to admin fidle bizness : fid command
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022


from ast import arg
from asyncio import format_helpers
from genericpath import isdir
import os
import sys
import traceback
import argparse
from typing_extensions import Required
import yaml
import importlib

from IPython.display import display
import pandas as pd


import fidle.config as config
import fidle.utils  as utils
from fidle.Chrono           import Chrono
from fidle.TocBuilder       import TocBuilder
from fidle.MagicCooker      import MagicCooker
from fidle.Installer        import Installer
from fidle.TimeSheetManager import TimeSheetManager


__version__        = config.VERSION
use_interactivity  = False                # by default

usage_end_user='''
    fid

      check                                   Check environment
            [--directory    <directory> ]        The place to check            (.)

      install                                 Install notebooks and datasets
            [--notebooks   <ress. name> ]        Notebooks ressource name      (default)
            [--datasets    <ress. name> ]        Datasets ressource name       (default)
            [--install_dir <directory>  ]        The place to install          (.)
            [--quiet                    ]        Quiet mode

      install_notebooks                       Install notebooks
            [--notebooks   <ress. name> ]        Notebooks ressource name      (default)
            [--install_dir  <directory> ]        The place to install          (.)
            [--quiet                    ]        Quiet mode

      install_datasets                        Install datasets
            [--datasets    <ress. name> ]        Datasets ressource name       (default)
            [--install_dir  <directory> ]        The place to install          (.)
            [--quiet                    ]        Quiet mode

      show_branch                             Show available notebooks and datasets branches

      help | --help                            Help             
    
    Examples :
    --------
    1/ To install Fidle notebooks and datasets in the current directory :
            # fid --install

    2/ To install a new version or reinstall notebooks in the current directory :
            # Rename or remove your existant notebooks directory, then
            # fid install_notebooks
    
    '''

usage_admin_user='''
    fid

    END USER COMMANDS :

      check                                   Check environment
            [--directory    <directory> ]        The place to check            (.)

      install                                 Install notebooks and datasets
            [--notebooks   <ress. name> ]        Notebooks ressource name      (default)
            [--datasets    <ress. name> ]        Datasets ressource name       (default)
            [--install_dir <directory>  ]        The place to install          (.)
            [--quiet                    ]        Quiet mode

      install_notebooks                       Install notebooks
            [--notebooks   <ress. name> ]        Notebooks ressource name      (default)
            [--install_dir <directory>  ]        The place to install          (.)
            [--quiet                    ]        Quiet mode

      install_datasets                        Install datasets
            [--datasets    <ress. name> ]        Datasets ressource name       (default)
            [--install_dir <directory>  ]        The place to install          (.)
            [--quiet                    ]        Quiet mode

      show_branch                             Show available notebooks and datasets branches

    ADMIN COMMANDS :

      toc                                     (re)Build readme.md and readme.ipynb
            [--about_file  <about file> ]         About file                    (./fidle/about.yml)
            [--root_dir    <root dir>   ]         root dir of the notebooks     (.)

      run_ci                                  Run a continous integration campain
            [--root_dir    <root dir>   ]        Root directory                (.)
            [--campain     <ci profile> ]        Campain profile name          (./fidle/ci/run-01.yml)
            [--filter      <filter> x n ]        Filter to apply               (.*)
            [--campain_tag <tag>        ]        Campain tag                   (None)
            [--quiet                    ]        Quiet mode                

      reset_ci                                Reset a continous integration campain
            [--root_dir    <root dir>   ]         Root directory                (.)
            [--campain     <ci profile> ]         Campain profile name          (./fidle/ci/run-01.yml)
            [--filter      <filter> x n ]         Filter to apply               (.*)
            [--campain_tag <tag>        ]         Campain tag                   (None)
            [--quiet                    ]         Quiet mode
      
      tms_check                               Just Show time sheet emails
            [--profile     <tms profile> ]       Profile name                  (~/timeSheet.yml)
            [--sequence_id <sequence_id> ]       Sequence id                   (None)
            [--magickey    <magickey>    ]       MagicKey                      (None)
            [--at          <date>        ]       Start or end date, format : 21-09-2022 11:30:00 or None for now
            [--duration    <duration>    ]       Duration in minutes,          (10)

      tms_send                                Send confirmations time sheet emails
            [--profile     <tms profile> ]       Profile name                  (~/timeSheet.yml)
            [--sequence_id <sequence_id> ]       Sequence id                   (None)
            [--magickey    <magickey>    ]       MagicKey                      (None)
            [--at          <date>        ]       Start or end date, format : 21-09-2022 11:30:00 or None for now
            [--duration    <duration>    ]       Duration in minutes,          (10)
            [--no_copy                   ]       Don't save a copy of each confirmation email sent
            [--no_flag_answered          ]       Don't set the answered flag of the emails to which a confirmation is sent

      tms_unflag                              Unflag time sheet emails, ie: remove answered and seen flags
            [--profile     <tms profile> ]       Profile name                  (~/timeSheet.yml)
            [--sequence_id <sequence_id> ]       Sequence id                   (None)
            [--magickey    <magickey>    ]       MagicKey                      (None)
            [--at          <date>        ]       Start or end date, format : 21-09-2022 11:30:00 or None for now
            [--duration    <duration>    ]       Duration in minutes,          (10)

      help                                    Help
            [--admin]                            Admin usage
    
    Examples :
    --------
    1/ To install Fidle notebooks and datasets :
            # fid --install

    2/ To install a new version or reinstall notebooks :
            # Rename or remove your existant notebooks directory, then
            # fid install_notebooks
    
    '''



# ------------------------------------------------------------------
# -- Check
# ------------------------------------------------------------------
#
def do_check(args):
    '''
    Check Fidle environment.
    '''
    installer=Installer()
    installer.check(directory = args.directory)


# ------------------------------------------------------------------
# -- Toc
# ------------------------------------------------------------------
#
def do_toc(args):
        print('Update TOC in readme : \n')
        tb       = TocBuilder()
        tb.update( about_file = args.about_file, 
                   root_dir   = args.root_dir )

# ------------------------------------------------------------------
# -- reset_ci
# ------------------------------------------------------------------
#
def do_reset_ci(args):
        print('Reset continous intégration campain : \n')
        if not are_you_sure(args.quiet) : return
        mck = MagicCooker()
        mck.reset_campain( args.campain,
                           root_dir    =  args.root_dir,
                           filters     =  args.filter, 
                           campain_tag =  args.campain_tag)

# ------------------------------------------------------------------
# -- run_ci
# ------------------------------------------------------------------
#
def do_run_ci(args):
        print('Run continous intégration campain : \n')
        if not are_you_sure(args.quiet) : return
        mck = MagicCooker()
        mck.run_campain( args.campain,
                         root_dir    =  args.root_dir,
                         filters     =  args.filter, 
                         campain_tag =  args.campain_tag)


# ------------------------------------------------------------------
# -- install
# ------------------------------------------------------------------
#
def do_install(args):

        do_install_notebooks(args)
        do_install_datasets(args)


# ------------------------------------------------------------------
# -- install notebooks
# ------------------------------------------------------------------
#
def do_install_notebooks(args):
        print(f'Install Fidle notebooks in {args.install_dir} : \n')
        if not are_you_sure(args.quiet) : return
        installer=Installer()
        installer.install_ressource( catalog_name     = 'notebooks', 
                                     ressource_name   = args.notebooks, 
                                     installation_dir = args.install_dir )

# ------------------------------------------------------------------
# -- install datasets
# ------------------------------------------------------------------
#
def do_install_datasets(args):
        print(f'Install Fidle datasets in {args.install_dir} : \n')
        if not are_you_sure(args.quiet) : return
        installer=Installer()
        installer.install_ressource( catalog_name     = 'datasets', 
                                     ressource_name   = args.datasets, 
                                     installation_dir = args.install_dir )

# ------------------------------------------------------------------
# -- show_branch
# ------------------------------------------------------------------
#
def do_show_branch(args):
        installer=Installer()
        installer.show_branch('notebooks')
        installer.show_branch('datasets')



# ------------------------------------------------------------------
# -- tms show
# ------------------------------------------------------------------
#
# tms_show                                Just Show time sheet emails
#     [--profile     <tms profile> ]       Profile name                  (~/timeSheet.yml)
#     [--sequence_id <sequence_id> ]       Sequence id                   (None)
#     [--magickey    <magickey>    ]       MagicKey                      (None)
#     [--at          <date>        ]       Start or end date,   format : 21-09-2022 11:30:00
#     [--duration    <duration>    ]       Duration in minutes,          (10)

def do_tms_check(args):
    print(f'Check presences')
    tms  = TimeSheetManager(args.profile, debug=0)

    presences = tms.get_presences( sequence_id = args.sequence_id, 
                                    magickey    = args.magickey,
                                    at          = args.at, 
                                    duration    = int(args.duration) ) 

    print('Complete list of presence mails : \n')

    df = pd.DataFrame.from_dict(presences)
    df = df[ ['from','send_dt','transit','attestation_ok','sequence_id'] ]
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 2000):
        display(df)
    print()

    tms.save_presences(presences, save_as=args.save, default='Check')

        

# ------------------------------------------------------------------
# -- tms send
# ------------------------------------------------------------------
#
#   tms_send                                Send confirmations time sheet emails
#         [--profile     <tms profile> ]       Profile name                  (~/timeSheet.yml)
#         [--sequence_id <sequence_id> ]       Sequence id                   (None)
#         [--magickey    <magickey>    ]       MagicKey                      (None)
#         [--at          <date>        ]       Start or end date,   format : 21-09-2022 11:30:00
#         [--duration    <duration>    ]       Duration in minutes,          (10)
#         [--no_copy                   ]       Don't save a copy of each confirmation email sent
#         [--no_flag_answered          ]       Don't set the answered flag of the emails to which a confirmation is sent

def do_tms_send(args):
    print(f'Send confirmation presence emails')
    tms  = TimeSheetManager(args.profile, debug=0)

    presences = tms.get_presences(    sequence_id   = args.sequence_id, 
                                        magickey      = args.magickey,
                                        at            = args.at, 
                                        duration      = int(args.duration) ) 

    tms.send_confirmations(     presences, 
                                save_copy     = args.save_copy, 
                                flag_answered = args.flag_answered )

    tms.save_presences(presences, save_as=args.save, default='Send')

        
# ------------------------------------------------------------------
# -- tms unflag
# ------------------------------------------------------------------
#
#   tms_unflag                              Unflag time sheet emails, ie: remove answered and read flags
#         [--profile     <tms profile> ]       Profile name                  (~/timeSheet.yml)
#         [--sequence_id <sequence_id> ]       Sequence id                   (None)
#         [--magickey    <magickey>    ]       MagicKey                      (None)
#         [--at          <date>        ]       Start or end date, format : 21-09-2022 11:30:00 or None for now
#         [--duration    <duration>    ]       Duration in minutes,          (10)

def do_tms_unflag(args):
    print(f'Remove presence emails flags (answered)')

    tms  = TimeSheetManager(args.profile, debug=0)

    presences = tms.get_presences(    sequence_id   = args.sequence_id, 
                                        magickey      = args.magickey,
                                        at            = args.at, 
                                        duration      = int(args.duration) ) 

    tms.unflag( presences )

    tms.save_presences(presences, save_as=args.save, default='Unflag')



# ------------------------------------------------------------------
# -- Are you sure ?
# ------------------------------------------------------------------
#
def are_you_sure(quiet):
        if quiet :                return True
        if not use_interactivity: return True
        print('\nAre you sure ? (Y/N) ', end='')
        rep=input()
        print('')
        return (rep=='Y')


# ------------------------------------------------------------------
# Run / Module method
# ------------------------------------------------------------------
#
# Run a command, directly from python : fidle.admin.run( )
# Or via an entry point / command line
#
def run(*arguments):
    print('\n==========================================================')
    print(f'fid - Your favorite Fidle admin command :-)    (v{config.VERSION})')
    print('==========================================================\n')

    # ---- Parser
    #
    parser = argparse.ArgumentParser( description="Fidle admin command (fid)",
                                      usage=usage_end_user)

    parser.add_argument('cmd',               help=argparse.SUPPRESS,    default='help')
                 
    parser.add_argument('--directory',             dest='directory',          help=argparse.SUPPRESS,    default='.')
    parser.add_argument('--notebooks',             dest='notebooks',          help=argparse.SUPPRESS,    default='default')
    parser.add_argument('--datasets',              dest='datasets',           help=argparse.SUPPRESS,    default='default')
    parser.add_argument('--install_dir',           dest='install_dir',        help=argparse.SUPPRESS,    default='.')
    parser.add_argument('--root_dir',              dest='root_dir',           help=argparse.SUPPRESS,    default='.')
    parser.add_argument('--about_file',            dest='about_file',         help=argparse.SUPPRESS,    default='./fidle/about.yml')
    parser.add_argument('--campain',               dest='campain',            help=argparse.SUPPRESS,    default='./fidle/ci/run-01.yml')
    parser.add_argument('--filter',                dest='filter',             help=argparse.SUPPRESS,    default=['.*'], nargs='+')
    parser.add_argument('--campain_tag',           dest='campain_tag',        help=argparse.SUPPRESS,    default=None)
    parser.add_argument('--profile',               dest='profile',            help=argparse.SUPPRESS,    default='~/timeSheet.yml')
    parser.add_argument('--sequence_id',           dest='sequence_id',        help=argparse.SUPPRESS,    default=None)
    parser.add_argument('--magickey',              dest='magickey',           help=argparse.SUPPRESS,    default=None)
    parser.add_argument('--at',                    dest='at',                 help=argparse.SUPPRESS,    default=None)
    parser.add_argument('--duration',              dest='duration',           help=argparse.SUPPRESS,    default=10, type=int)
    parser.add_argument('--no_copy',               dest='save_copy',          help=argparse.SUPPRESS,    action='store_false')
    parser.add_argument('--no_flag_answered',      dest='flag_answered',      help=argparse.SUPPRESS,    action='store_false')
    parser.add_argument('--save',                  dest='save',               help=argparse.SUPPRESS,    default=None, const='default', nargs='?' )
    parser.add_argument('--quiet',                 dest='quiet',              help=argparse.SUPPRESS,    action='store_true')
    parser.add_argument('--admin',                 dest='admin',              help=argparse.SUPPRESS,    action='store_true')
    
    try:
        args  = parser.parse_args(arguments)
    except:
        print('\n')
        return

    # ---- Command
    #
    try:
        if   args.cmd=='check'                :  do_check(args)
        elif args.cmd=='install'              :  do_install(args)
        elif args.cmd=='install_notebooks'    :  do_install_notebooks(args)
        elif args.cmd=='install_datasets'     :  do_install_datasets(args)
        elif args.cmd=='show_branch'          :  do_show_branch(args)
        elif args.cmd=='toc'                  :  do_toc(args)
        elif args.cmd=='reset_ci'             :  do_reset_ci(args)
        elif args.cmd=='run_ci'               :  do_run_ci(args)
        elif args.cmd=='tms_check'            :  do_tms_check(args)
        elif args.cmd=='tms_send'             :  do_tms_send(args)
        elif args.cmd=='tms_unflag'           :  do_tms_unflag(args)
        else: 
            # Usage
            if args.admin : print(usage_admin_user)    
            else:           print(usage_end_user)    
    except KeyboardInterrupt:
        print('\nAbort !\n')
        return
    except Exception as e:
        print('\nOups...  something went wrong !')
        print(e)
        print('\nMore details :\n')
        traceback.print_exc()

        return


# ------------------------------------------------------------------
# Run / Pypi entry point
# ------------------------------------------------------------------
# fidle.admin --help
#
def main():
    global use_interactivity
    
    # ---- We are in command line mode
    use_interactivity = sys.__stdin__.isatty()

    run(*sys.argv[1:])    


# ------------------------------------------------------------------
# Run / Command line
# ------------------------------------------------------------------
# python -m fidle.admin --help
#
if __name__ == '__main__':

    # ---- We are in command line mode
    use_interactivity = sys.__stdin__.isatty()

    run(*sys.argv[1:])    
