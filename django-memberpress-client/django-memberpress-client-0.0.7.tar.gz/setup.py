# pylint: disable=open-builtin
import io
import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.md"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "memberpress_client", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


README = load_readme()
ABOUT = load_about()
VERSION = ABOUT["__version__"]


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split("#")[0].strip() for line in open(path).readlines() if is_requirement(line.strip())
        )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.
    Returns:
        bool: True if the line is not blank, a comment, a URL, or an included file
    """
    return not (
        line == ""
        or line.startswith("-c")
        or line.startswith("-r")
        or line.startswith("#")
        or line.startswith("-e")
        or line.startswith("git+")
    )


print("Found packages: {packages}".format(packages=find_packages()))

print("requirements found: {requirements}".format(requirements=load_requirements("requirements/common.in")))

setup(
    name="django-memberpress-client",
    version=VERSION,
    url="https://github.com/lpm0073/django-memberpress-client",
    project_urls={
        "Code": "https://github.com/lpm0073/django-memberpress-client",
        "Issue tracker": "https://github.com/lpm0073/django-memberpress-client/issues",
        "Community": "https://docs.memberpress.com/category/215-developer-resources",
    },
    author="Lawrence McDaniel",
    author_email="lpm0073@gmail.com",
    description="A Django plugin to add Memberpress REST API and Webhook integrations.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.html"]},  # include any Mako templates found in this repo.
    zip_safe=False,
    keywords="Python, Django, Wordpress, MemberPress, REST API",
    python_requires=">=3.8",
    install_requires=load_requirements("requirements/common.txt"),
    entry_points={
        # mcdaniel aug-2021
        #
        # IMPORTANT: ensure that this entry_points coincides with that of edx-platform
        #            and also that you are not introducing any name collisions.
        # https://github.com/openedx/edx-platform/blob/master/setup.py#L88
        "lms.djangoapp": [
            "memberpress_client = memberpress_client.apps:MemberPressPluginConfig",
        ],
        "cms.djangoapp": [],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    extras_require={
        "Django": ["Django>=2.2,<2.3"],
    },
)
