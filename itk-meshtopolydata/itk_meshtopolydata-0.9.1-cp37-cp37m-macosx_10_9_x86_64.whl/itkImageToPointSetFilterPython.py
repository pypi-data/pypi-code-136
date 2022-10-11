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
    from . import _itkImageToPointSetFilterPython
else:
    import _itkImageToPointSetFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkImageToPointSetFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkImageToPointSetFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToMeshFilterPython
import itk.itkPointSetPython
import itk.itkArrayPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkMeshBasePython
import itk.itkMapContainerPython
import itk.itkBoundingBoxPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkMeshSourcePython

def itkImageToPointSetFilterID2PSD2_New():
    return itkImageToPointSetFilterID2PSD2.New()

class itkImageToPointSetFilterID2PSD2(itk.itkImageToMeshFilterPython.itkImageToMeshFilterID2PSD2):
    r"""Proxy of C++ itkImageToPointSetFilterID2PSD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID2PSD2___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID2PSD2_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterID2PSD2
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID2PSD2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterID2PSD2

        Create a new object of the class itkImageToPointSetFilterID2PSD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterID2PSD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterID2PSD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterID2PSD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterID2PSD2 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterID2PSD2_swigregister(itkImageToPointSetFilterID2PSD2)
itkImageToPointSetFilterID2PSD2___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterID2PSD2___New_orig__
itkImageToPointSetFilterID2PSD2_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterID2PSD2_cast


def itkImageToPointSetFilterID3PSD3_New():
    return itkImageToPointSetFilterID3PSD3.New()

class itkImageToPointSetFilterID3PSD3(itk.itkImageToMeshFilterPython.itkImageToMeshFilterID3PSD3):
    r"""Proxy of C++ itkImageToPointSetFilterID3PSD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID3PSD3___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID3PSD3_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterID3PSD3
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID3PSD3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterID3PSD3

        Create a new object of the class itkImageToPointSetFilterID3PSD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterID3PSD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterID3PSD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterID3PSD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterID3PSD3 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterID3PSD3_swigregister(itkImageToPointSetFilterID3PSD3)
itkImageToPointSetFilterID3PSD3___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterID3PSD3___New_orig__
itkImageToPointSetFilterID3PSD3_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterID3PSD3_cast


def itkImageToPointSetFilterID4PSD4_New():
    return itkImageToPointSetFilterID4PSD4.New()

class itkImageToPointSetFilterID4PSD4(itk.itkImageToMeshFilterPython.itkImageToMeshFilterID4PSD4):
    r"""Proxy of C++ itkImageToPointSetFilterID4PSD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID4PSD4___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID4PSD4_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterID4PSD4
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterID4PSD4_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterID4PSD4

        Create a new object of the class itkImageToPointSetFilterID4PSD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterID4PSD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterID4PSD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterID4PSD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterID4PSD4 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterID4PSD4_swigregister(itkImageToPointSetFilterID4PSD4)
itkImageToPointSetFilterID4PSD4___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterID4PSD4___New_orig__
itkImageToPointSetFilterID4PSD4_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterID4PSD4_cast


def itkImageToPointSetFilterIF2PSF2_New():
    return itkImageToPointSetFilterIF2PSF2.New()

class itkImageToPointSetFilterIF2PSF2(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIF2PSF2):
    r"""Proxy of C++ itkImageToPointSetFilterIF2PSF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF2PSF2___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF2PSF2_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIF2PSF2
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF2PSF2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIF2PSF2

        Create a new object of the class itkImageToPointSetFilterIF2PSF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIF2PSF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIF2PSF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIF2PSF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIF2PSF2 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF2PSF2_swigregister(itkImageToPointSetFilterIF2PSF2)
itkImageToPointSetFilterIF2PSF2___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIF2PSF2___New_orig__
itkImageToPointSetFilterIF2PSF2_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIF2PSF2_cast


def itkImageToPointSetFilterIF3PSF3_New():
    return itkImageToPointSetFilterIF3PSF3.New()

class itkImageToPointSetFilterIF3PSF3(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIF3PSF3):
    r"""Proxy of C++ itkImageToPointSetFilterIF3PSF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF3PSF3___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF3PSF3_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIF3PSF3
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF3PSF3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIF3PSF3

        Create a new object of the class itkImageToPointSetFilterIF3PSF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIF3PSF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIF3PSF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIF3PSF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIF3PSF3 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF3PSF3_swigregister(itkImageToPointSetFilterIF3PSF3)
itkImageToPointSetFilterIF3PSF3___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIF3PSF3___New_orig__
itkImageToPointSetFilterIF3PSF3_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIF3PSF3_cast


def itkImageToPointSetFilterIF4PSF4_New():
    return itkImageToPointSetFilterIF4PSF4.New()

class itkImageToPointSetFilterIF4PSF4(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIF4PSF4):
    r"""Proxy of C++ itkImageToPointSetFilterIF4PSF4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF4PSF4___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF4PSF4_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIF4PSF4
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF4PSF4_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIF4PSF4

        Create a new object of the class itkImageToPointSetFilterIF4PSF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIF4PSF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIF4PSF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIF4PSF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIF4PSF4 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIF4PSF4_swigregister(itkImageToPointSetFilterIF4PSF4)
itkImageToPointSetFilterIF4PSF4___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIF4PSF4___New_orig__
itkImageToPointSetFilterIF4PSF4_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIF4PSF4_cast


def itkImageToPointSetFilterISS2PSSS2_New():
    return itkImageToPointSetFilterISS2PSSS2.New()

class itkImageToPointSetFilterISS2PSSS2(itk.itkImageToMeshFilterPython.itkImageToMeshFilterISS2PSSS2):
    r"""Proxy of C++ itkImageToPointSetFilterISS2PSSS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS2PSSS2___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS2PSSS2_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterISS2PSSS2
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS2PSSS2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterISS2PSSS2

        Create a new object of the class itkImageToPointSetFilterISS2PSSS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterISS2PSSS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterISS2PSSS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterISS2PSSS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterISS2PSSS2 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS2PSSS2_swigregister(itkImageToPointSetFilterISS2PSSS2)
itkImageToPointSetFilterISS2PSSS2___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterISS2PSSS2___New_orig__
itkImageToPointSetFilterISS2PSSS2_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterISS2PSSS2_cast


def itkImageToPointSetFilterISS3PSSS3_New():
    return itkImageToPointSetFilterISS3PSSS3.New()

class itkImageToPointSetFilterISS3PSSS3(itk.itkImageToMeshFilterPython.itkImageToMeshFilterISS3PSSS3):
    r"""Proxy of C++ itkImageToPointSetFilterISS3PSSS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS3PSSS3___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS3PSSS3_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterISS3PSSS3
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS3PSSS3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterISS3PSSS3

        Create a new object of the class itkImageToPointSetFilterISS3PSSS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterISS3PSSS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterISS3PSSS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterISS3PSSS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterISS3PSSS3 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS3PSSS3_swigregister(itkImageToPointSetFilterISS3PSSS3)
itkImageToPointSetFilterISS3PSSS3___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterISS3PSSS3___New_orig__
itkImageToPointSetFilterISS3PSSS3_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterISS3PSSS3_cast


def itkImageToPointSetFilterISS4PSSS4_New():
    return itkImageToPointSetFilterISS4PSSS4.New()

class itkImageToPointSetFilterISS4PSSS4(itk.itkImageToMeshFilterPython.itkImageToMeshFilterISS4PSSS4):
    r"""Proxy of C++ itkImageToPointSetFilterISS4PSSS4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS4PSSS4___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS4PSSS4_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterISS4PSSS4
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS4PSSS4_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterISS4PSSS4

        Create a new object of the class itkImageToPointSetFilterISS4PSSS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterISS4PSSS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterISS4PSSS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterISS4PSSS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterISS4PSSS4 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterISS4PSSS4_swigregister(itkImageToPointSetFilterISS4PSSS4)
itkImageToPointSetFilterISS4PSSS4___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterISS4PSSS4___New_orig__
itkImageToPointSetFilterISS4PSSS4_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterISS4PSSS4_cast


def itkImageToPointSetFilterIUC2PSUC2_New():
    return itkImageToPointSetFilterIUC2PSUC2.New()

class itkImageToPointSetFilterIUC2PSUC2(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIUC2PSUC2):
    r"""Proxy of C++ itkImageToPointSetFilterIUC2PSUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC2PSUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC2PSUC2_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIUC2PSUC2
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC2PSUC2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIUC2PSUC2

        Create a new object of the class itkImageToPointSetFilterIUC2PSUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIUC2PSUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIUC2PSUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIUC2PSUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIUC2PSUC2 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC2PSUC2_swigregister(itkImageToPointSetFilterIUC2PSUC2)
itkImageToPointSetFilterIUC2PSUC2___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC2PSUC2___New_orig__
itkImageToPointSetFilterIUC2PSUC2_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC2PSUC2_cast


def itkImageToPointSetFilterIUC3PSUC3_New():
    return itkImageToPointSetFilterIUC3PSUC3.New()

class itkImageToPointSetFilterIUC3PSUC3(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIUC3PSUC3):
    r"""Proxy of C++ itkImageToPointSetFilterIUC3PSUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC3PSUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC3PSUC3_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIUC3PSUC3
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC3PSUC3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIUC3PSUC3

        Create a new object of the class itkImageToPointSetFilterIUC3PSUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIUC3PSUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIUC3PSUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIUC3PSUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIUC3PSUC3 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC3PSUC3_swigregister(itkImageToPointSetFilterIUC3PSUC3)
itkImageToPointSetFilterIUC3PSUC3___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC3PSUC3___New_orig__
itkImageToPointSetFilterIUC3PSUC3_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC3PSUC3_cast


def itkImageToPointSetFilterIUC4PSUC4_New():
    return itkImageToPointSetFilterIUC4PSUC4.New()

class itkImageToPointSetFilterIUC4PSUC4(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIUC4PSUC4):
    r"""Proxy of C++ itkImageToPointSetFilterIUC4PSUC4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC4PSUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC4PSUC4_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIUC4PSUC4
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC4PSUC4_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIUC4PSUC4

        Create a new object of the class itkImageToPointSetFilterIUC4PSUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIUC4PSUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIUC4PSUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIUC4PSUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIUC4PSUC4 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC4PSUC4_swigregister(itkImageToPointSetFilterIUC4PSUC4)
itkImageToPointSetFilterIUC4PSUC4___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC4PSUC4___New_orig__
itkImageToPointSetFilterIUC4PSUC4_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUC4PSUC4_cast


def itkImageToPointSetFilterIUS2PSUS2_New():
    return itkImageToPointSetFilterIUS2PSUS2.New()

class itkImageToPointSetFilterIUS2PSUS2(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIUS2PSUS2):
    r"""Proxy of C++ itkImageToPointSetFilterIUS2PSUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS2PSUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS2PSUS2_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIUS2PSUS2
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS2PSUS2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIUS2PSUS2

        Create a new object of the class itkImageToPointSetFilterIUS2PSUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIUS2PSUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIUS2PSUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIUS2PSUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIUS2PSUS2 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS2PSUS2_swigregister(itkImageToPointSetFilterIUS2PSUS2)
itkImageToPointSetFilterIUS2PSUS2___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS2PSUS2___New_orig__
itkImageToPointSetFilterIUS2PSUS2_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS2PSUS2_cast


def itkImageToPointSetFilterIUS3PSUS3_New():
    return itkImageToPointSetFilterIUS3PSUS3.New()

class itkImageToPointSetFilterIUS3PSUS3(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIUS3PSUS3):
    r"""Proxy of C++ itkImageToPointSetFilterIUS3PSUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS3PSUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS3PSUS3_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIUS3PSUS3
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS3PSUS3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIUS3PSUS3

        Create a new object of the class itkImageToPointSetFilterIUS3PSUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIUS3PSUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIUS3PSUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIUS3PSUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIUS3PSUS3 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS3PSUS3_swigregister(itkImageToPointSetFilterIUS3PSUS3)
itkImageToPointSetFilterIUS3PSUS3___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS3PSUS3___New_orig__
itkImageToPointSetFilterIUS3PSUS3_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS3PSUS3_cast


def itkImageToPointSetFilterIUS4PSUS4_New():
    return itkImageToPointSetFilterIUS4PSUS4.New()

class itkImageToPointSetFilterIUS4PSUS4(itk.itkImageToMeshFilterPython.itkImageToMeshFilterIUS4PSUS4):
    r"""Proxy of C++ itkImageToPointSetFilterIUS4PSUS4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS4PSUS4___New_orig__)
    Clone = _swig_new_instance_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS4PSUS4_Clone)
    __swig_destroy__ = _itkImageToPointSetFilterPython.delete_itkImageToPointSetFilterIUS4PSUS4
    cast = _swig_new_static_method(_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS4PSUS4_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPointSetFilterIUS4PSUS4

        Create a new object of the class itkImageToPointSetFilterIUS4PSUS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPointSetFilterIUS4PSUS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkImageToPointSetFilterIUS4PSUS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkImageToPointSetFilterIUS4PSUS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPointSetFilterIUS4PSUS4 in _itkImageToPointSetFilterPython:
_itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS4PSUS4_swigregister(itkImageToPointSetFilterIUS4PSUS4)
itkImageToPointSetFilterIUS4PSUS4___New_orig__ = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS4PSUS4___New_orig__
itkImageToPointSetFilterIUS4PSUS4_cast = _itkImageToPointSetFilterPython.itkImageToPointSetFilterIUS4PSUS4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def image_to_point_set_filter(*args: itkt.ImageLike,  output: itkt.PointSet=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for ImageToPointSetFilter"""
    import itk

    kwarg_typehints = { 'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ImageToPointSetFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def image_to_point_set_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.MeshToPolyData.ImageToPointSetFilter
    image_to_point_set_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    image_to_point_set_filter.__doc__ = filter_object.__doc__




