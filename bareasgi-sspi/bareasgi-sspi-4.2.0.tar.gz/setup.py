# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareasgi_sspi']

package_data = \
{'': ['*']}

install_requires = \
['bareasgi>=4.2,<5.0', 'pyspnego>=0.6,<0.7']

setup_kwargs = {
    'name': 'bareasgi-sspi',
    'version': '4.2.0',
    'description': 'bareASGI middleware for SSPI',
    'long_description': '# bareASGI-sspi\n\n[ASGI](https://asgi.readthedocs.io/en/latest/index.html) middleware\nfor the [bareASGI](https://github.com/rob-blackbourn/bareASGI) framework\nproviding [SSPI](https://en.wikipedia.org/wiki/Security_Support_Provider_Interface) authentication\non Windows.\n\nThe implementation uses the [pyspnego](https://github.com/jborean93/pyspnego) package.\n\nThere is also a generic ASGI server middleware implementation in the package\n[jetblack-asgi-sspi](https://github.com/rob-blackbourn/jetblack-asgi-sspi).\n\n## Installation\n\nInstall from the pie store.\n\n```\npip install bareasgi-sspi\n```\n\n## Usage\n\nThe following program uses the\n[Hypercorn](https://pgjones.gitlab.io/hypercorn/)\nASGI server.\n\n```python\nimport asyncio\nimport logging\nfrom typing import Optional\n\nfrom bareasgi import Application, HttpRequest, HttpResponse\nfrom bareutils import text_writer\nfrom hypercorn import Config\nfrom hypercorn.asyncio import serve\n\nfrom bareasgi_sspi import add_sspi_middleware, sspi_details\n\n# A callback to display the results of the SSPI middleware.\nasync def http_request_callback(request: HttpRequest) -> HttpResponse:\n    # Get the details from the request context request[\'sspi\']. Note if\n    # authentication failed this might be absent or empty.\n    sspi = sspi_details(request)\n    client_principal = (\n        sspi[\'client_principal\']\n        if sspi is not None\n        else \'unknown\'\n    )\n    return HttpResponse(\n        200,\n        [(b\'content-type\', b\'text/plain\')],\n        text_writer(f"Authenticated as \'{client_principal}\'")\n    )\n\n\nasync def main_async():\n    # Make the ASGI application using the middleware.\n    app = Application()\n    app.http_router.add({\'GET\'}, \'/\', http_request_callback)\n\n    # Add the middleware. Change the protocol from Negotiate to NTLM,\n    # and allow unauthenticated requests to pass through.\n    add_sspi_middleware(\n        app,\n        protocol=b\'NTLM\',\n        forbid_unauthenticated=False\n    )\n\n    # Start the ASGI server.\n    config = Config()\n    config.bind = [\'localhost:9023\']\n    await serve(app, config)\n\nif __name__ == \'__main__\':\n    logging.basicConfig(level=logging.DEBUG)\n    asyncio.run(main_async())\n```\n\n### Arguments\n\nOptional arguments include:\n\n* `protocol` (`bytes`): Either `b"Negotiate"` or `b"NTLM"` (for systems not part of a domain).\n* `service` (`str`): The SPN service. Defaults to `"HTTP"`.\n* `hostname` (`str`, optional): The hostname. Defaults to he result of `socket.gethostname()`.\n* `session_duration` (`timedelta`, optional): The duration of a session. Defaults to 1 hour.\n* `forbid_unauthenticated` (`bool`): If true, and authentication fails, send 403 (Forbidden). Otherwise handle the request unauthenticated.\n* `context_key` (`str`, optional): The key used in the request context. Defaults to `sspi`.\n* `whitelist` (`Sequence[str]`, optional): Paths not to authenticate. Defaults to `()`.\n\n### Results\n\nIf the authentication is successful the SSPI details are added to the\n`context` dictionary of the HttpRequest object with the key `"sspi"`\n(if not overridden). There is a helper method `sspi_details` for this.\n\nThe following properties are set:\n\n* `"client_principal"` (`str`): The username of the client.\n* `"negotiated_protocol"` (`str`): The negotiated protocol.\n* `"protocol"` (`str`): The requested protocol.\n* `"spn"` (`str`): The SPN of the server.\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareASGI-SSPI',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
