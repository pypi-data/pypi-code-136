import codecs
from pathlib import Path
from typing import Dict

from dmtgen.common.package import Package
from dmtgen.package_generator import PackageGenerator
from dmtgen import TemplateBasedGenerator


class PackageDescriptorGenerator(TemplateBasedGenerator):
    """ Generate the Package description file"""

    def generate(self, package_generator: PackageGenerator, template, outputfile: Path, config: Dict):
        if config.get("minimal", False):
            # We ignore the package
            return
        outputdir = outputfile.parents[0]
        root_package: Package = package_generator.root_package
        self.__generate_package(root_package,template, outputdir, config)

    def __generate_package(self, package: Package, template, pkg_dir, config):
        """Renames the default output file"""
        pkg_dir.mkdir(exist_ok=True)
        filename = self.first_to_upper(package.name) + "PackageDescription.ts"
        renamed_output = pkg_dir / filename
        self.__generate_descriptor(package, template, renamed_output, config)
        for sub_package in package.packages:
            name = sub_package.name
            sub_dir = pkg_dir / name
            self.__generate_package(sub_package, template, sub_dir, config)


    def __generate_descriptor(self, pkg: Package, template, outputfile: Path, config: Dict):
        """Basic generator, one template, one output file"""
        model = {}
        package_name = pkg.name
        model["package_name"] = package_name
        model["package_class"] = self.first_to_upper(package_name) + "PackageDescription"
        model["lib_name"] = config.get("lib_name",f'{package_name}-ts')
        model["description"] = package_name + " - Generated types"
        model["version"] = config["version"]
        etypes = []

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
