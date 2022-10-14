import ast
import builtins
import sys

import codefast.reader
import codefast.utils as utils
from codefast.base.format_print import FormatPrint as fp
from codefast.constants import constants
from codefast.ds import fpjson, fplist, nstr, pair_sample, fpdict
from codefast.functools.random import random_string
from codefast.io import FastJson
from codefast.io import FileIO as io
from codefast.io import dblite, mydb
from codefast.io._json import fpjson
from codefast.logger import Logger, critical, error, exception, info, warning
from codefast.math import math
from codefast.network import Network as http
from codefast.network import Network as net
from codefast.network import url_shortener, urljoin
from codefast.network.tools import bitly
from codefast.utils import (b64decode, b64encode, cipher, decipher, retry,
                            shell, syscall, uuid)

# Export methods and variables
csv = utils.CSVIO
dic = fpdict
eval = ast.literal_eval
j = fpjson
js = FastJson()
lis = fplist
l = fplist
os = utils._os()
r = io.read
read = io.read

builtins.lis = fplist
builtins.dic = fpdict

# Deprecated
sys.modules[__name__] = utils.wrap_mod(sys.modules[__name__],
                                       deprecated=['text', 'file'])
