from setuptools import setup

setup(
    entry_points={
        'console_scripts': [
            'ansible=fallible._vendor.ansible.lib.ansible.cli.adhoc:main',
            'ansible-config=fallible._vendor.ansible.lib.ansible.cli.config:main',
            'ansible-console=fallible._vendor.ansible.lib.ansible.cli.console:main',
            'ansible-doc=fallible._vendor.ansible.lib.ansible.cli.doc:main',
            'ansible-galaxy=fallible._vendor.ansible.lib.ansible.cli.galaxy:main',
            'ansible-inventory=fallible._vendor.ansible.lib.ansible.cli.inventory:main',
            'ansible-playbook=fallible._vendor.ansible.lib.ansible.cli.playbook:main',
            'ansible-pull=fallible._vendor.ansible.lib.ansible.cli.pull:main',
            'ansible-vault=fallible._vendor.ansible.lib.ansible.cli.vault:main',
            'ansible-connection=fallible._vendor.ansible.lib.ansible.cli.scripts.ansible_connection_cli_stub:main',
            'ansible-test=fallible._vendor.ansible.test.lib.ansible_test._util.target.cli.ansible_test_cli_stub:main',
        ],
    },
)
