# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 7, 0):
    raise RuntimeError("Python 3.7 or later required")

from . import _ITKCommonPython


from . import _MeshToPolyDataPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkPolyDataToMeshFilterPython
else:
    import _itkPolyDataToMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPolyDataToMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPolyDataToMeshFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.itkPolyDataPython
import itk.itkPointPython
import itk.itkVectorPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkVectorContainerPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkArrayPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkMeshBasePython
import itk.itkMapContainerPython
import itk.itkPointSetPython
import itk.itkBoundingBoxPython

def itkPolyDataToMeshFilterPDD_New():
    return itkPolyDataToMeshFilterPDD.New()

class itkPolyDataToMeshFilterPDD(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkPolyDataToMeshFilterPDD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD_Clone)
    SetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD_SetInput)
    GetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD_GetInput)
    GetOutput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD_GenerateOutputInformation)
    __swig_destroy__ = _itkPolyDataToMeshFilterPython.delete_itkPolyDataToMeshFilterPDD
    cast = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataToMeshFilterPDD

        Create a new object of the class itkPolyDataToMeshFilterPDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataToMeshFilterPDD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataToMeshFilterPDD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataToMeshFilterPDD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataToMeshFilterPDD in _itkPolyDataToMeshFilterPython:
_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD_swigregister(itkPolyDataToMeshFilterPDD)
itkPolyDataToMeshFilterPDD___New_orig__ = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD___New_orig__
itkPolyDataToMeshFilterPDD_cast = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDD_cast


def itkPolyDataToMeshFilterPDF_New():
    return itkPolyDataToMeshFilterPDF.New()

class itkPolyDataToMeshFilterPDF(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkPolyDataToMeshFilterPDF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF_Clone)
    SetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF_SetInput)
    GetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF_GetInput)
    GetOutput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF_GenerateOutputInformation)
    __swig_destroy__ = _itkPolyDataToMeshFilterPython.delete_itkPolyDataToMeshFilterPDF
    cast = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataToMeshFilterPDF

        Create a new object of the class itkPolyDataToMeshFilterPDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataToMeshFilterPDF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataToMeshFilterPDF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataToMeshFilterPDF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataToMeshFilterPDF in _itkPolyDataToMeshFilterPython:
_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF_swigregister(itkPolyDataToMeshFilterPDF)
itkPolyDataToMeshFilterPDF___New_orig__ = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF___New_orig__
itkPolyDataToMeshFilterPDF_cast = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDF_cast


def itkPolyDataToMeshFilterPDSS_New():
    return itkPolyDataToMeshFilterPDSS.New()

class itkPolyDataToMeshFilterPDSS(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkPolyDataToMeshFilterPDSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS_Clone)
    SetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS_SetInput)
    GetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS_GetInput)
    GetOutput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS_GenerateOutputInformation)
    __swig_destroy__ = _itkPolyDataToMeshFilterPython.delete_itkPolyDataToMeshFilterPDSS
    cast = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataToMeshFilterPDSS

        Create a new object of the class itkPolyDataToMeshFilterPDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataToMeshFilterPDSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataToMeshFilterPDSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataToMeshFilterPDSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataToMeshFilterPDSS in _itkPolyDataToMeshFilterPython:
_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS_swigregister(itkPolyDataToMeshFilterPDSS)
itkPolyDataToMeshFilterPDSS___New_orig__ = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS___New_orig__
itkPolyDataToMeshFilterPDSS_cast = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDSS_cast


def itkPolyDataToMeshFilterPDUC_New():
    return itkPolyDataToMeshFilterPDUC.New()

class itkPolyDataToMeshFilterPDUC(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkPolyDataToMeshFilterPDUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC_Clone)
    SetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC_SetInput)
    GetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC_GetInput)
    GetOutput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC_GenerateOutputInformation)
    __swig_destroy__ = _itkPolyDataToMeshFilterPython.delete_itkPolyDataToMeshFilterPDUC
    cast = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataToMeshFilterPDUC

        Create a new object of the class itkPolyDataToMeshFilterPDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataToMeshFilterPDUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataToMeshFilterPDUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataToMeshFilterPDUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataToMeshFilterPDUC in _itkPolyDataToMeshFilterPython:
_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC_swigregister(itkPolyDataToMeshFilterPDUC)
itkPolyDataToMeshFilterPDUC___New_orig__ = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC___New_orig__
itkPolyDataToMeshFilterPDUC_cast = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUC_cast


def itkPolyDataToMeshFilterPDUS_New():
    return itkPolyDataToMeshFilterPDUS.New()

class itkPolyDataToMeshFilterPDUS(itk.ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkPolyDataToMeshFilterPDUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS_Clone)
    SetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS_SetInput)
    GetInput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS_GetInput)
    GetOutput = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS_GetOutput)
    GenerateOutputInformation = _swig_new_instance_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS_GenerateOutputInformation)
    __swig_destroy__ = _itkPolyDataToMeshFilterPython.delete_itkPolyDataToMeshFilterPDUS
    cast = _swig_new_static_method(_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataToMeshFilterPDUS

        Create a new object of the class itkPolyDataToMeshFilterPDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataToMeshFilterPDUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataToMeshFilterPDUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataToMeshFilterPDUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataToMeshFilterPDUS in _itkPolyDataToMeshFilterPython:
_itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS_swigregister(itkPolyDataToMeshFilterPDUS)
itkPolyDataToMeshFilterPDUS___New_orig__ = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS___New_orig__
itkPolyDataToMeshFilterPDUS_cast = _itkPolyDataToMeshFilterPython.itkPolyDataToMeshFilterPDUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def poly_data_to_mesh_filter(*args, **kwargs):
    """Functional interface for PolyDataToMeshFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.PolyDataToMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def poly_data_to_mesh_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.MeshToPolyData.PolyDataToMeshFilter
    poly_data_to_mesh_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    poly_data_to_mesh_filter.__doc__ = filter_object.__doc__




