from conan.internal.api.new.cmake_lib import source_cpp, source_h, test_main

conanfile_exe = '''from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class {{package_name}}Recipe(ConanFile):
    name = "{{name}}"
    version = "{{version}}"
    package_type = "application"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of {{ name }} package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
'''

cmake_exe_v2 = """cmake_minimum_required(VERSION 3.15)
project({{name}} CXX)

add_executable({{name}} src/{{name}}.cpp src/main.cpp)

install(TARGETS {{name}} DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
"""

test_conanfile_exe_v2 = """import os
from conan import ConanFile
from conan.tools.build import cross_building


class {{package_name}}TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def test(self):
        if not cross_building(self):
            self.run("{{name}}", env="conanrun")
"""

cmake_exe_files = {"conanfile.py": conanfile_exe,
                   "src/{{name}}.cpp": source_cpp,
                   "src/{{name}}.h": source_h,
                   "src/main.cpp": test_main,
                   "CMakeLists.txt": cmake_exe_v2,
                   "test_package/conanfile.py": test_conanfile_exe_v2
                   }
