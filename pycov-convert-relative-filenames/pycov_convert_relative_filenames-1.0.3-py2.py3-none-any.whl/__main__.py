#!/usr/bin/env python3
import os
import sys
import xml.etree.ElementTree as ET


def walk(root, source_path, package):
    for child in root:
        if child.tag == "package":
            name = child.attrib["name"]
            if name == ".":
                name = package
            else:
                name = f"{package}.{name}"
            child.attrib["name"] = name

        if child.tag == "class":
            filename = child.attrib["filename"]
            filename = os.path.join(source_path, filename)
            child.attrib["filename"] = os.path.relpath(filename, os.getcwd())
        walk(child, source_path, package)


def convert(data):
    root = ET.fromstring(data)

    sources = root.findall("./sources/source")
    if len(sources) > 1:
        print(
            "error: more than one './sources/source' element found. This case is unhandled.",
            file=sys.stderr,
        )
        sys.exit(0)

    # Set the source path to current directory
    source_path = sources[0].text
    sources[0].text = os.getcwd()

    package = os.path.relpath(source_path, os.getcwd())
    walk(root, source_path, package)
    return ET.tostring(root, encoding="unicode")


def main():
    with open("/dev/stdin", "r", encoding="UTF-8") as fd:
        data = fd.read()
    document = convert(data)
    print(document)


if __name__ == "__main__":
    main()
