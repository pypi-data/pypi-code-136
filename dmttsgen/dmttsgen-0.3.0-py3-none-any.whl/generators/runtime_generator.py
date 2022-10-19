#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Code generator for python runtime library
'''

import shutil
from pathlib import Path
from typing import Dict

from dmtgen.common.package import Package
from dmtgen import TemplateBasedGenerator, BaseGenerator

from . import PackageDescriptorGenerator, EntityGenerator, BasicTemplateGenerator

class RuntimeGenerator(BaseGenerator):
    """ Generates a Python runtime library to access the entities as plain objects """

    def __init__(self,root_dir,package_name,output_dir,root_package: Package) -> None:
        super().__init__(root_dir,package_name,output_dir,root_package)

    def get_template_generators(self) -> Dict[str,TemplateBasedGenerator]:
        """ Override in subclasses """
        return {
            "poto.ts.jinja": EntityGenerator(),
            "entity-minimal.ts.jinja": EntityGenerator(),
            "package_descriptor.ts.jinja": PackageDescriptorGenerator(),
            "package.json.jinja": BasicTemplateGenerator(),
            "index.ts.jinja": BasicTemplateGenerator()
        }

    def copy_templates(self, template_root: Path, output_dir: Path):
        """Copy template folder to output folder"""
        if self.source_only:
            src_dir = template_root / "src"
            dest_dir = output_dir
            shutil.copytree(str(src_dir), str(dest_dir))
        else:
            shutil.copytree(str(template_root), str(output_dir))
