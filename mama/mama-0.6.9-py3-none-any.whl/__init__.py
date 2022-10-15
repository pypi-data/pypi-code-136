import pkg_resources
pkg_resources.declare_namespace(__name__)

# these imports are executed when mamafile.py does `import mama`
from .build_config import BuildConfig
from .build_target import BuildTarget
