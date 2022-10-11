from setuptools import find_packages, setup

setup(
    name="lifeguard-notification-msteams",
    version="0.0.3",
    url="https://github.com/LifeguardSystem/lifeguard-notification-msteams",
    author="Diego Rubin",
    author_email="contact@diegorubin.dev",
    license="GPL2",
    scripts=[],
    include_package_data=True,
    description="Lifeguard integration with MS Teams",
    install_requires=["lifeguard", "pymsteams"],
    classifiers=["Development Status :: 3 - Alpha"],
    packages=find_packages(),
)
