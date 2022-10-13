from setuptools import Extension, setup

module1 = Extension(
    # The "name" defines where the compiled shared object will be placed
    name="pymzxml.rampy.ramp",
    # Support for large files
    define_macros=[("FILE_OFFSET_BITS", "64")],
    # We need to link against the zlib library
    extra_link_args=["-lz"],
    sources=[
        "pymzxml/ramp/src/ramp.cpp",
        "pymzxml/ramp/src/ramp_base64.cpp",
        "pymzxml/ramp/src/fd_ramp.cpp",
    ],
)

setup(ext_modules=[module1])
