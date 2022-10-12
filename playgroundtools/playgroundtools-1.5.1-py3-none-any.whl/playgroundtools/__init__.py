from .metadata import get_metadata

_metadata = get_metadata()


APP_NAME = _metadata["Name"]
APP_TITLE = APP_NAME.title()
DESCRIPTION = _metadata["Summary"]
VERSION = _metadata["Version"]
AUTHOR = _metadata["Author"]
LICENSE = _metadata["License"]
HOMEPAGE = _metadata["Home-page"]

ABOUT_TEXT = f"""
{APP_NAME} v {VERSION}
{HOMEPAGE}

{APP_TITLE}:

Version: {VERSION}
Author: {AUTHOR}
Licensed under: {LICENSE}
Copyright: © 2022 {AUTHOR}"""
