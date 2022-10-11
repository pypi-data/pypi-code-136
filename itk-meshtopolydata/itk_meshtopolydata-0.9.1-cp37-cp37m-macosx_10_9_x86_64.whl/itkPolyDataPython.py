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
    from . import _itkPolyDataPython
else:
    import _itkPolyDataPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPolyDataPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPolyDataPython.SWIG_PyStaticMethod_New

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
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkArrayPython

def itkPolyDataD_New():
    return itkPolyDataD.New()

class itkPolyDataD(itk.ITKCommonBasePython.itkDataObject):
    r"""Proxy of C++ itkPolyDataD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataPython.itkPolyDataD___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_Clone)
    GetNumberOfPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetNumberOfPoints)
    SetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_SetPoints)
    GetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetPoints)
    SetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_SetVertices)
    GetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetVertices)
    SetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_SetLines)
    GetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetLines)
    SetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_SetPolygons)
    GetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetPolygons)
    SetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_SetTriangleStrips)
    GetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetTriangleStrips)
    SetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_SetPoint)
    GetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetPoint)
    SetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_SetPointData)
    GetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetPointData)
    SetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_SetCellData)
    GetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataD_GetCellData)
    __swig_destroy__ = _itkPolyDataPython.delete_itkPolyDataD
    cast = _swig_new_static_method(_itkPolyDataPython.itkPolyDataD_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataD

        Create a new object of the class itkPolyDataD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataD in _itkPolyDataPython:
_itkPolyDataPython.itkPolyDataD_swigregister(itkPolyDataD)
itkPolyDataD___New_orig__ = _itkPolyDataPython.itkPolyDataD___New_orig__
itkPolyDataD_cast = _itkPolyDataPython.itkPolyDataD_cast


def itkPolyDataF_New():
    return itkPolyDataF.New()

class itkPolyDataF(itk.ITKCommonBasePython.itkDataObject):
    r"""Proxy of C++ itkPolyDataF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataPython.itkPolyDataF___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_Clone)
    GetNumberOfPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetNumberOfPoints)
    SetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_SetPoints)
    GetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetPoints)
    SetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_SetVertices)
    GetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetVertices)
    SetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_SetLines)
    GetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetLines)
    SetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_SetPolygons)
    GetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetPolygons)
    SetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_SetTriangleStrips)
    GetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetTriangleStrips)
    SetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_SetPoint)
    GetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetPoint)
    SetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_SetPointData)
    GetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetPointData)
    SetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_SetCellData)
    GetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataF_GetCellData)
    __swig_destroy__ = _itkPolyDataPython.delete_itkPolyDataF
    cast = _swig_new_static_method(_itkPolyDataPython.itkPolyDataF_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataF

        Create a new object of the class itkPolyDataF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataF in _itkPolyDataPython:
_itkPolyDataPython.itkPolyDataF_swigregister(itkPolyDataF)
itkPolyDataF___New_orig__ = _itkPolyDataPython.itkPolyDataF___New_orig__
itkPolyDataF_cast = _itkPolyDataPython.itkPolyDataF_cast


def itkPolyDataSS_New():
    return itkPolyDataSS.New()

class itkPolyDataSS(itk.ITKCommonBasePython.itkDataObject):
    r"""Proxy of C++ itkPolyDataSS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataPython.itkPolyDataSS___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_Clone)
    GetNumberOfPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetNumberOfPoints)
    SetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_SetPoints)
    GetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetPoints)
    SetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_SetVertices)
    GetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetVertices)
    SetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_SetLines)
    GetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetLines)
    SetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_SetPolygons)
    GetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetPolygons)
    SetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_SetTriangleStrips)
    GetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetTriangleStrips)
    SetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_SetPoint)
    GetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetPoint)
    SetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_SetPointData)
    GetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetPointData)
    SetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_SetCellData)
    GetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataSS_GetCellData)
    __swig_destroy__ = _itkPolyDataPython.delete_itkPolyDataSS
    cast = _swig_new_static_method(_itkPolyDataPython.itkPolyDataSS_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataSS

        Create a new object of the class itkPolyDataSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataSS in _itkPolyDataPython:
_itkPolyDataPython.itkPolyDataSS_swigregister(itkPolyDataSS)
itkPolyDataSS___New_orig__ = _itkPolyDataPython.itkPolyDataSS___New_orig__
itkPolyDataSS_cast = _itkPolyDataPython.itkPolyDataSS_cast


def itkPolyDataUC_New():
    return itkPolyDataUC.New()

class itkPolyDataUC(itk.ITKCommonBasePython.itkDataObject):
    r"""Proxy of C++ itkPolyDataUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataPython.itkPolyDataUC___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_Clone)
    GetNumberOfPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetNumberOfPoints)
    SetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_SetPoints)
    GetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetPoints)
    SetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_SetVertices)
    GetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetVertices)
    SetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_SetLines)
    GetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetLines)
    SetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_SetPolygons)
    GetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetPolygons)
    SetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_SetTriangleStrips)
    GetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetTriangleStrips)
    SetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_SetPoint)
    GetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetPoint)
    SetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_SetPointData)
    GetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetPointData)
    SetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_SetCellData)
    GetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUC_GetCellData)
    __swig_destroy__ = _itkPolyDataPython.delete_itkPolyDataUC
    cast = _swig_new_static_method(_itkPolyDataPython.itkPolyDataUC_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataUC

        Create a new object of the class itkPolyDataUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataUC in _itkPolyDataPython:
_itkPolyDataPython.itkPolyDataUC_swigregister(itkPolyDataUC)
itkPolyDataUC___New_orig__ = _itkPolyDataPython.itkPolyDataUC___New_orig__
itkPolyDataUC_cast = _itkPolyDataPython.itkPolyDataUC_cast


def itkPolyDataUS_New():
    return itkPolyDataUS.New()

class itkPolyDataUS(itk.ITKCommonBasePython.itkDataObject):
    r"""Proxy of C++ itkPolyDataUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPolyDataPython.itkPolyDataUS___New_orig__)
    Clone = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_Clone)
    GetNumberOfPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetNumberOfPoints)
    SetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_SetPoints)
    GetPoints = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetPoints)
    SetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_SetVertices)
    GetVertices = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetVertices)
    SetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_SetLines)
    GetLines = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetLines)
    SetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_SetPolygons)
    GetPolygons = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetPolygons)
    SetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_SetTriangleStrips)
    GetTriangleStrips = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetTriangleStrips)
    SetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_SetPoint)
    GetPoint = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetPoint)
    SetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_SetPointData)
    GetPointData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetPointData)
    SetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_SetCellData)
    GetCellData = _swig_new_instance_method(_itkPolyDataPython.itkPolyDataUS_GetCellData)
    __swig_destroy__ = _itkPolyDataPython.delete_itkPolyDataUS
    cast = _swig_new_static_method(_itkPolyDataPython.itkPolyDataUS_cast)

    def New(*args, **kargs):
        """New() -> itkPolyDataUS

        Create a new object of the class itkPolyDataUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyDataUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPolyDataUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPolyDataUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPolyDataUS in _itkPolyDataPython:
_itkPolyDataPython.itkPolyDataUS_swigregister(itkPolyDataUS)
itkPolyDataUS___New_orig__ = _itkPolyDataPython.itkPolyDataUS___New_orig__
itkPolyDataUS_cast = _itkPolyDataPython.itkPolyDataUS_cast



