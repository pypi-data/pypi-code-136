"""
Code generator for typescript object representing the entity instances
"""

import codecs
from pathlib import Path
from typing import Dict, Set

from dmtgen.common.package import Package
from dmtgen.common.blueprint import Blueprint
from dmtgen.common.blueprint_attribute import BlueprintAttribute
from dmtgen.package_generator import PackageGenerator
from dmtgen.template_generator import TemplateBasedGenerator
from jinja2.environment import Template


class EntityGenerator(TemplateBasedGenerator):
    """Generates entities"""

    types = {"number": "number", "double": "number", "string": "string", "char": "string",
            "integer": "number", "short": "number", "boolean": "boolean"}

    default_values = {"number": "0.0", "string": "\"\"", "int": "0", "boolean": "false"}

    def generate(
        self,
        package_generator: PackageGenerator,
        template: Template,
        outputfile: Path,
        config: Dict,
    ):
        """Generate typescript classes with properties"""
        if self.__skip(template,config):
            return
        outputdir = outputfile.parents[0]
        root_package = package_generator.root_package
        self.__generate_package(root_package,template, outputdir, config)

    def __skip(self, template: Template, config: Dict):
        is_poto = template.name == "poto.ts.jinja"
        if config.get("minimal", False):
            # This is the minimal stage
            return is_poto

        return not is_poto

    def __generate_package(self, package: Package, template, pkg_dir,config: Dict):
        for blueprint in package.blueprints:
            self.__generate_entity(blueprint,template,pkg_dir, config)

        for sub_package in package.packages:
            name = sub_package.name
            sub_dir = pkg_dir / name
            self.__generate_package(sub_package,template, sub_dir, config)

    def __generate_entity(self, blueprint: Blueprint,template: Template, outputdir: Path, config: Dict):
        outputdir.mkdir(exist_ok=True)
        model = self.__create_model(blueprint, config)
        filename = model["file_basename"].lower() + ".ts"
        outputfile = outputdir / filename
        with codecs.open(outputfile, "w", "utf-8") as file:
            file.write(template.render(model))

    def __create_model(self, blueprint: Blueprint, config: Dict):
        minimal = config.get("minimal", False)
        package=blueprint.get_parent()
        package_name = package.name
        imports = set()

        model = {}
        name = blueprint.name
        model["package"] = package_name
        model["package_class"] = (
            self.__first_to_upper(package_name) + "PackageDescription"
        )

        model["extends"] = self.__find_extensions(blueprint, imports)
        model["name"] = name
        model["file_basename"] = name.lower()
        model["description"] = self.__reshape_multiline_string(
            blueprint.description
        )
        model["type"] = self.__first_to_upper(name)
        fields = []
        # for attribute in blueprint.all_attributes.values():
        for attribute in blueprint.attributes:
            field = self.__create_field(attribute, minimal,package,imports)
            if field:
                fields.append(field)

        model["imports"] = imports
        model["fields"] = fields

        return model

    def __find_extensions(self, blueprint: Blueprint, imports: Set) -> str:
        extensions = []
        for ext in blueprint.extensions:
            if ext:
                if ext.name == "NamedEntity":
                    continue
                ext_name =self.__first_to_upper(ext.name)
                extensions.append(ext_name)
                fname = ext.name.lower()
                imports.add(f"import {{{ext_name}}} from './{fname}'")

        if len(extensions) == 0:
            return ""
        return "extends " +  ", ".join(extensions)

    def __reshape_multiline_string(self, value: str) -> str:
        if not value:
            return ""
        return value.replace("'", '"').encode("unicode_escape").decode("utf-8")

    def __first_to_upper(self, string):
        # Make sure the first letter is uppercase
        return string[:1].upper() + string[1:]

    def __create_field(self, attribute: BlueprintAttribute, minimal: bool, package: Package,imports: Set):
        field = {}
        field["name"] = attribute.name
        is_array = attribute.is_many
        field["isArray"] = is_array

        a_type: str = attribute.get("attributeType")
        if a_type not in self.types:
            blueprint = package.get_blueprint(a_type)
            if blueprint:
                ext_name =self.__first_to_upper(blueprint.name)
                fname = ext_name.lower()
                imports.add(f"import {{{ext_name}}} from './{fname}'")
                return self.__create_blueprint_field(field, blueprint.name, is_array)
            else:
                # Not found
                parts=a_type.split("/")
                bp_name = parts[-1]
                ext_name =self.__first_to_upper(bp_name)
                fname = "/".join(parts).lower()
                imports.add(f"import {{{ext_name}}} from '../{fname}'")
                return self.__create_blueprint_field(field, bp_name, is_array)


        ftype = self.__map(attribute.type, self.types)
        if is_array:
            if minimal:
                field["type"] = ftype + "[]"
                field["init"] = "[]"
            else:
                field["type"] = "BaseList<" + ftype + ">"
                field["init"] = "new BaseList()"
        else:
            field["type"] = ftype
            field["init"] = self.__find_default_value(attribute)

        field["createMethod"] = self.__first_to_upper(ftype)
        field["description"] = self.__reshape_multiline_string(attribute.get("description", ""))
        return field

    def __create_blueprint_field(self, field, name, is_array) -> Dict:
        if is_array:
            field["type"] = f"{name}[]"
        else:
            field["type"] = name
        return field

    def __map(self, key, values):
        converted = values[key]
        if not converted:
            raise Exception("Unkown type " + key)
        return converted

    def __map_type(self,ptype):
        return self.__map(ptype, self.types)

    def __find_default_value(self, attribute: BlueprintAttribute):
        """Returns the default value literal"""
        a_type: str = attribute.get("attributeType")
        etype = self.__map_type(a_type)
        default_value = attribute.get("default")
        if default_value is not None:
            return self.__convert_default(attribute,default_value)
        default_value = self.__map(etype, self.default_values)
        return default_value


    def __convert_default(self, attribute: BlueprintAttribute, default_value):
        # converts json value to Python value
        if isinstance(default_value,str):
            if default_value == '' or default_value == '""':
                return '""'
            elif attribute.type == 'integer':
                return int(default_value)
            elif attribute.type == 'number':
                return float(default_value)
            elif attribute.type == 'boolean':
                bval = bool(default_value)
                if bval:
                    return "true"
                return "false"
            else:
                return "'" + default_value + "'"
        return default_value
