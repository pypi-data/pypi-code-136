from distutils.core import setup

setup(
    name="job_helper",
    version="1.1",
    description="A (async) simple job system using RabbitMQ for DAMS",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    author="Inuits",
    author_email="developers@inuits.eu",
    license="GPLv2",
    packages=["job_helper"],
    install_requires=[
        "cloudevents>=1.4.0",
        "Flask>=1.1.2",
        "rabbitmq-pika-flask>=1.2.15",
    ],
    provides=["job_helper"],
)
