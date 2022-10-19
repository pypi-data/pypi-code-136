"""Basic generator, one template, one output file"""

import codecs
from pathlib import Path
from typing import Dict
from dmtgen import TemplateBasedGenerator
from dmtgen.package_generator import PackageGenerator
from dmtgen.common.package import Package

class BasicTemplateGenerator(TemplateBasedGenerator):
    """Basic generator, one template, one output file"""

    def generate(self, package_generator: PackageGenerator, template, outputfile: Path, config: Dict):
        """Basic generator, one template, one output file"""
        model = {}
        package_name = package_generator.package_name
        model["package_name"] = package_name
        model["package_class"] = self.first_to_upper(package_name) + "PackageDescription"
        model["lib_name"] = config.get("lib_name",f'{package_name}-ts')
        model["description"] = package_name + " - Generated types"
        model["version"] = config["version"]
        etypes = []

        pkg: Package = package_generator.root_package

        for blueprint in pkg.blueprints:
            etype = {}
            name = blueprint.name
            etype["name"] = self.first_to_upper(name)
            etype["file_basename"] = name.lower()
            etypes.append(etype)

        model["types"] = etypes

        with codecs.open(outputfile, "w", "utf-8") as file:
            file.write(template.render(model))

    @staticmethod
    def first_to_upper(string):
        """ Make sure the first letter is uppercase """
        return string[:1].upper() + string[1:]
