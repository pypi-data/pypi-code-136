import sys
import venv
import asyncio
from pathlib import Path
from shlex import quote

from django.core.management import call_command

from . import const, utils, parser
from .utils.git import Repo
from .utils.files import write_file
from .utils.process import run_cmd


async def exec():
    args = parser.parse_args()

    project_path = Path(args.dir).absolute()

    print('Checking project directory...')

    if not project_path.exists():
        print('Project directory not found, creating project directory')

        project_path.mkdir()
    else:
        print('Project directory found')

    repo = Repo(project_path)

    name = args.name

    print('Creating Django project...')

    call_command('startproject', name, str(project_path))

    print('Django project created')

    venv_path = project_path / 'venv'

    bin_path = venv_path / 'bin'

    pip_path = bin_path / 'pip'

    requirements_path = project_path / 'requirements.txt'

    args.packages.extend(const.REQUIRED_PACKAGES)

    print(f'Creating virtual environment at {venv_path}')
    if args.python:
        await run_cmd([
            args.python,
            '-m',
            'venv',
            str(venv_path)
        ])
    else:
        venv.create(str(venv_path), with_pip=True)

    print(f'Created virtual environment at {venv_path}')

    tasks = [
        write_file(
            str(project_path / '.gitignore'),
            const.GITIGNORE
        ),
        write_file(
            str(project_path / '.env'),
            utils.generate_env(args.debug, args.hosts)
        ),
        write_file(
            str(project_path / 'env.example'),
            const.ENV_EXAMPLE
        ),
        utils.write_settings(str(project_path / args.name / 'settings.py')),
        utils.install_packages(
            str(pip_path),
            args.packages,
            str(requirements_path),
            *(('--no-compile',) if args.no_compile else tuple())
        )
    ]

    if args.git:
        tasks.append(repo.init())

    print('Creating files...')

    await asyncio.gather(*tasks)

    print('Created files')

    tasks = []

    if args.git and args.commit:
        await repo.add(('.',), _v=True)

        task = repo.commit(args.commit_message, _v=True)

        tasks.append(task)

    if args.migrate:
        python_path = bin_path / 'python'

        manage_path = project_path / 'manage.py'

        task = run_cmd((
            str(python_path),
            quote(str(manage_path)),
            'migrate',
            '--no-input'
        ))

        tasks.append(task)

    await asyncio.gather(*tasks)


def main():
    asyncio.run(exec())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
