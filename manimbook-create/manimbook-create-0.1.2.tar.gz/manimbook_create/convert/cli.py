import os
import re
import json
import string
import shutil
import tarfile
import argparse
import nbformat
from pathlib import Path
from traitlets.config import Config
from nbconvert.writers import FilesWriter
from nbconvert import SlidesExporter, MarkdownExporter
from nbconvert.preprocessors import ExecutePreprocessor


def get_path(s):
    return str(Path(s).expanduser().absolute().resolve())


def dir_to_list(dirname):
    data = []
    for name in sorted(os.listdir(dirname)):
        dct = {}
        dct['name'] = name
        dct['path'] = get_path(os.path.join(dirname, name))
        full_path = os.path.join(dirname, name)
        if os.path.isfile(full_path):
            data.append(dct)
    return data


def format_name(s, i):
    a = re.sub("ch\d", f"{i}.", s)
    b = string.capwords(a.replace("_", " "))
    return b


# get the command line arguments
parser = argparse.ArgumentParser(
    description='Convert Jupyter Notebooks to ManimBooks')
parser.add_argument('project_name', type=str, help='Name of the project')
parser.add_argument('notebook_dir', type=Path,
                    help='Directory of notebooks (chapters) to convert')
parser.add_argument('--slides', action='store_true', help='Convert to slides')
parser.add_argument('--md', action='store_true', help='Convert   to markdown')
parser.add_argument('--exec-timeout', type=int, default=600,
                    help='Timeout for execution of Manim scenes')
args = parser.parse_args()

script_dir = os.path.dirname(os.path.realpath(__file__))
user_dir = os.getcwd()

# custom configuration for nbconvert
c = Config()
c.TemplateExporter.extra_template_basedirs
my_templates = script_dir + '/templates'
c.TemplateExporter.extra_template_basedirs = [my_templates]
c.TemplateExporter.exclude_input = True
c.SlidesExporter.theme = 'dark'
c.SlidesExporter.reveal_theme = 'night'
c.SlidesExporter.reveal_scroll = True
c.FilesWriter.build_directory = f"{script_dir}/.cache/{args.project_name}"


def main():
    # initialize cache output folder
    if not os.path.exists(f"{script_dir}/.cache/"):
        os.mkdir(f"{script_dir}/.cache/")
    if not os.path.exists(c.FilesWriter.build_directory):
        os.mkdir(c.FilesWriter.build_directory)

    chapters = []

    i = 1
    for notebook in dir_to_list(get_path(args.notebook_dir)):
        dct = {}
        os.chdir(c.FilesWriter.build_directory)
        print("Converting ", notebook['name'])
        shutil.copy2(notebook['path'], c.FilesWriter.build_directory)
        filename = format_name(str(notebook['name']).replace(".ipynb", ""), i)
        dct['name'] = filename
        i += 1

        # execute (render) the contents of the notebook
        print("Executing contents of notebook...", end="    ")
        ep = ExecutePreprocessor(timeout=600)
        nb = nbformat.read(notebook['path'], nbformat.NO_CONVERT)
        ep.preprocess(nb)
        print("Done")

        # convert the notebook to slides
        if args.slides:
            print("Converting to slides...", end="    ")
            slides = SlidesExporter(config=c, template_name="reveal.js")
            (output, resources) = slides.from_notebook_node(nb)
            fw = FilesWriter(config=c)
            fw.write(output, resources, notebook_name=filename)
            dct['slides'] = filename + ".slides.html"
            print("Done")

        # convert the notebook to markdown, copy it to texme html template
        print("Converting to markdown...", end="    ")
        shutil.copy2(f"{script_dir}/templates/scroll.html",
                     f"{filename}.html")
        scroll = MarkdownExporter(config=c)
        (output, resources) = scroll.from_notebook_node(nb)
        fw = FilesWriter(config=c)
        fw.write(output, resources, notebook_name=filename)
        with open(f"{filename}.md", "r") as f, open(f"{filename}.html", "a+") as g:
            g.write(f.read())
            os.remove(f"{filename}.md")
        dct['md'] = filename + ".html"
        print("Done")
        chapters.append(dct)

    # create index.json file
    open("index.json", "w").write(json.dumps(chapters, indent=4))

    # create tarball
    os.chdir(get_path(f"{c.FilesWriter.build_directory}") + "/../..")

    def make_tarfile(output_filename, source_dir):
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
        tar.close()

    print("Creating tarball...", end="    ")
    make_tarfile(f"{args.project_name}.mbook", f"./.cache/{args.project_name}")
    shutil.move(f"{args.project_name}.mbook", user_dir)
    print("Done")

    print("Cleaning up...", end="    ")
    shutil.rmtree(f"./.cache/{args.project_name}")
    print("Done")


main()
