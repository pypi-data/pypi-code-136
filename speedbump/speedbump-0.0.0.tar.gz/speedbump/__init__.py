import sys
import os
from github import Github
from yaml import load, dump


github = Github(os.getenv("GITHUB_TOKEN"))


def conf_item(package_ecosystem: str, directory: str):
    return {
        'package-ecosystem': package_ecosystem,
        'directory': directory,
        'schedule': {'interval': 'daily'},
    }


def make_conf(file_path):
    if ('.github/workflows' in file_path):
        return conf_item('github-actions', '/')

    if file_path.endswith(('requirements.txt', 'setup.py')):
        path, _, _ = file_path.rpartition('/')
        return conf_item('pip', '/' + path)

    if (file_path.endswith('package.json')):
        path, _, _ = file_path.rpartition('/')
        return conf_item('npm', '/' + path)

    if (file_path.endswith('Dockerfile')):
        path, _, _ = file_path.rpartition('/')
        return conf_item('docker', '/' + path)

    if (file_path.endswith('pom.xml')):
        path, _, _ = file_path.rpartition('/')
        return conf_item('maven', '/' + path)

    return False


def run2(repo_name: str):
    repo = github.get_repo(repo_name)
    main_branch = repo.get_branch(repo.default_branch)
    head = main_branch.commit.sha
    tree = repo.get_git_tree(head, recursive=True).tree
    files = {t.path for t in tree}

    config = dict(version=2, updates=[])
    configured_ecosystems = set()
    
    for f in files:
        update_conf = make_conf(f)
        if update_conf:
            eco_dir = (update_conf['package-ecosystem'], update_conf['directory'])
            if eco_dir not in configured_ecosystems:
                config['updates'].append(update_conf)
                configured_ecosystems.add(eco_dir)

    print(dump(config, sort_keys=False))

def run():
    files = set(sys.stdin)

    config = dict(version=2, updates=[])
    configured_ecosystems = set()
    
    for f in files:
        update_conf = make_conf(f.strip())
        if update_conf:
            #print(update_conf)
            eco_dir = (update_conf['package-ecosystem'], update_conf['directory'])
            if eco_dir not in configured_ecosystems:
                config['updates'].append(update_conf)
                configured_ecosystems.add(eco_dir)

    print(dump(config, sort_keys=False))
