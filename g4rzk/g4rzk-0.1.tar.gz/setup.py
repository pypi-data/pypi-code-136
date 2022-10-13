from distutils.core import setup, Extension

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = "g4rzk",
  packages = ["g4rzk"],
  version = "0.1",
  license ="MIT",
  description = "Yang Tau Tau Ajah Akwkwkw.",
  long_description = long_description,
  long_description_content_type = "text/markdown", 
  author = "Angga Kurniawan",
  author_email = "g4rzkurniawan@gmail.com",
  url = "https://github.com/g4rzk/g4rzk",
  download_url = "https://github.com/g4rzk/g4rzk/archive/g4rzk.tar.gz", 
  keywords = ["g4rzk", "garzk", "garz.id", "anggaxd"], 
  install_requires = [
          "bs4",
          "rich", 
          "inquirer", 
          "requests", 
          "futures", 
      ],
  classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
  ],
)