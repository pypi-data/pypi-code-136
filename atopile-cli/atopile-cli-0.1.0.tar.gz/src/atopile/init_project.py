from pathlib import Path

import yaml
from . import options, utils

import logging

log = logging.getLogger()

def init_project(project_dir, merge):
    """
    Initalise a project with atopile things
    """

    project_dir = Path(project_dir)
    
    # create the project directory if it doesn't exist
    project_dir.mkdir(parents=True, exist_ok=True)

    # find all the KiCAD files in the project directory
    kicad_projects = list(project_dir.glob('**/*.kicad_pro'))

    atopile_config = {
        'name': project_dir.with_suffix('').name,
        'tasks': {
            'check': {},
            'build': {},
        }
    }

    for p in kicad_projects:
        if p.with_suffix('.kicad_pcb').exists() and p.with_suffix('.kicad_sch').exists():
            name = p.with_suffix('').name
            rel_path = str(p.relative_to(project_dir).with_suffix(''))

            atopile_config['tasks']['check'][f'drc-{name}'] = {
                'path': 'atopile.io/atopile/kibot.git/kibot-drc.stage.yaml',
                'board': rel_path,
            }

            atopile_config['tasks']['check'][f'erc-{name}'] = {
                'path': 'atopile.io/atopile/kibot.git/kibot-erc.stage.yaml',
                'board': rel_path,
            }

            atopile_config['tasks']['build'][f'build-{name}'] = {
                'path': 'atopile.io/atopile/kibot.git/kibot-build.stage.yaml',
                'project': rel_path,
            }

    if merge:
        with open(project_dir / options.atopile_file.raw_value, 'r') as f:
            # preference the existing config when mergeing
            atopile_config = utils.merge_dict(atopile_config, yaml.safe_load(f))
    else:
        if (project_dir / options.atopile_file.raw_value).exists():
            log.error(f'atopile.yaml already exists in {project_dir} and the merge option isn\'t set')
            exit(1)
            
    with open(project_dir / options.atopile_file.raw_value, 'w') as f:
        yaml.dump(atopile_config, f)
