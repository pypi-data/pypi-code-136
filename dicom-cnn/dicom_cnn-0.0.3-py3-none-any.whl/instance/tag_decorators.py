from dicom_cnn.exceptions.dicom_exceptions import DicomEmptyTag, DicomTagNotFound


def type_1(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if (result == None):
                raise(DicomEmptyTag('Empty Type 1 Tag'))
            return result
        except:
            raise(DicomTagNotFound('Type 1 Tag Not Found'))
    return inner


def type_2(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            raise(DicomTagNotFound('Type 2 Tag Not Found'))
    return inner


def type_3(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return None
    return inner
