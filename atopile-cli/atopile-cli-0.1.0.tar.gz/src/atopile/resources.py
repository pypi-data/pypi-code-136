from functools import partial
from pathlib import Path
from typing import Dict, List
import git
import logging
import asyncio
from attr import frozen

from . import options

log = logging.getLogger(__name__)

class AbstractResource:
    @property
    def path(self) -> Path:
        # if _path is inside the project dir, return a relative path
        if self._path.is_relative_to(options.project_dir.value):
            return self._path.relative_to(options.project_dir.value)
        else:
            return self._path.absolute()

    async def install(self):
        raise NotImplementedError

    @property
    def reference(self) -> str:
        raise NotImplementedError

@frozen
class GitResource(AbstractResource):
    _url: str
    _path: Path
    _branch: str
    _name: str

    @classmethod
    def resolve_path(cls, url, name, system=False):
        name = cls.resolve_name(url, name)
        if system:
            path = options.system_atopile_dir.value / name
        else:
            path = options.project_atopile_dir.value / name
        return path

    @staticmethod
    def resolve_name(url, name = None):
        if name is None:
            name = url.split('.git')[0].split('/')[-1]
        return name

    @classmethod
    def from_url(cls, url: str, branch: str = None, name: str = None, system: bool = False):
        name = cls.resolve_name(url, name)
        path = cls.resolve_path(url, name, system)
        return cls(url, path, branch, name)

    @classmethod
    def from_dict(cls, d: Dict):
        url = d['url']
        name = d.get('name') or cls.resolve_name(url)
        path = cls.resolve_path(url, name)
        branch = d.get('branch')
        return cls(url, path, branch, name)

    async def install(self):
        loop = asyncio.get_event_loop()
        if self._path.exists():
            repo = git.Repo(self._path)
            if repo.remotes.origin.url != self._url:
                log.error(f'Git repository at {self._path} is not the same as the requested resource')
                raise FileExistsError
            # TODO: don't pull if we're on a specific commit
            await loop.run_in_executor(None, repo.remotes.origin.pull, self._branch)
        else:
            clone = partial(git.Repo.clone_from, self._url, self._path, branch=self._branch, multi_options=['--depth=1'])
            repo = await loop.run_in_executor(
                None,
                clone
            )
    
    def to_dict(self) -> Dict:
        d = {'type': 'git', 'url': self._url, 'name': self._name}
        if self._branch:
            d['branch'] = self._branch
        return d

    @property
    def reference(self) -> str:
        return self._url


@frozen
class LocalResource(AbstractResource):
    _path: Path

    async def install(self):
        if not self._path.exists():
            log.error(f'Local resource at {self._path} does not exist')
            raise FileNotFoundError

    def to_dict(self) -> Dict:
        return {'type': 'local', 'path': self.path}

    @property
    def reference(self) -> str:
        return str(self.path)

def parse_resource(r: Dict[str, str]):
    t = r.get('type')
    if t == 'git':
        return GitResource.from_dict(r)
    elif t == 'local':
        return LocalResource(r['path'])
    else:
        log.error(f'Unknown resource type {t}')
        raise TypeError

def parse_resources(resource_list: List[Dict[str, str]]):
    resources = []
    for r in resource_list:
        resources.append(parse_resource(r))
    return resources

async def get_resources(resource_list: List[Dict[str, str]]):
    resources = parse_resources(resource_list)
    
    # try get all the resources and exit on error
    returns = await asyncio.gather(*[r.get() for r in resources], return_exceptions=True)
    for r in returns:
        if isinstance(r, Exception):
            exit(1)

    return resources

def dump_resources(resources: List[AbstractResource]) -> List[Dict]:
    return [r.to_dict() for r in resources]

async def add_resource(config_data: dict, url: str, branch: str, name: str):
    resource = GitResource.from_url(url, branch, name)
    all_resources = parse_resources(config_data['resources'])
    if resource not in all_resources:
        await resource.install()
        all_resources.append(resource)
    config_data['resources'] = dump_resources(all_resources)
    return resource

def split_path(path: str) -> List[str]:
    idx = path.rfind(':')
    if idx == -1:
        return path, None
    else:
        return path[:idx], path[idx+1:]
