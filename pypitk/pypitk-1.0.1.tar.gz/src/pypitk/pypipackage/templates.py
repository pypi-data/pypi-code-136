pyproject_toml = """
[tool.poetry]
name = "*package_name*"
version = "*package_version*"
description = "*package_description*"
authors = ["*pypi_username* <*pypi_email*>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "^*python_version*"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""
