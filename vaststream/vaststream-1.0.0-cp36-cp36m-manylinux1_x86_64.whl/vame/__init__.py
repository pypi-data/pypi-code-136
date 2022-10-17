# coding: utf-8

from _vaststream_pybind11 import vame

# 返回值校验
def err_checker(func):
    def wrapper(*args,**kwargs):
        ret = func(*args,**kwargs)
        if ret != vame.vameER_SUCCESS:
            raise Exception(f"{func.__name__} return error.")
    return wrapper

# enum
class CODEC_TYPE():
    """
    vame codec type.\n
    ----------\n
    @enum CODEC_DEC_JPEG: decode for jpeg.\n
    @enum CODEC_DEC_H264: decode for h264.\n
    @enum CODEC_DEC_HEVC: decode for hevc.\n
    @enum CODEC_ENC_JPEG: encode for jpeg.\n
    @enum CODEC_ENC_H264: encode for jpeg.\n
    @enum CODEC_ENC_HEVC: encode for jpeg.\n
    """
    CODEC_DEC_JPEG: int = vame.codeType.VAME_CODEC_DEC_JPEG
    CODEC_DEC_H264: int = vame.codeType.VAME_CODEC_DEC_H264
    CODEC_DEC_HEVC: int = vame.codeType.VAME_CODEC_DEC_HEVC
    CODEC_ENC_JPEG: int = vame.codeType.VAME_CODEC_ENC_JPEG
    CODEC_ENC_H264: int = vame.codeType.VAME_CODEC_ENC_H264
    CODEC_ENC_HEVC: int = vame.codeType.VAME_CODEC_ENC_HEVC

class SOURCE_MODE():
    """
    vame source mode.\n
    ----------\n
    @enum VAME_SRC_FRAME: src frame.\n
    """
    SRC_FRAME: int = vame.sourceMode.VAME_SRC_FRAME

class DECODE_MODE():
    """
    vame decode mode.\n
    ----------\n
    @enum NORMAL: normal mode for decode.\n
    @enum INTRA_ONLY: intral_only mode for decode.\n
    """
    NORMAL: int = vame.decodeMode.VAME_DEC_NORMAL
    INTRA_ONLY: int = vame.decodeMode.VAME_DEC_INTRA_ONLY

class PIXEL_FORMAT():
    """
    vame pixel format
    ----------\n
    ...
    """
    PIX_FMT_NONE: int = vame.pixelFormat.VAME_PIX_FMT_NONE
    VAME_PIX_FMT_YUV420P: int = vame.pixelFormat.VAME_PIX_FMT_YUV420P
    VAME_PIX_FMT_YUV444P: int = vame.pixelFormat.VAME_PIX_FMT_YUV444P
    VAME_PIX_FMT_YUV422P: int = vame.pixelFormat.VAME_PIX_FMT_YUV422P
    VAME_PIX_FMT_YUV420P9: int = vame.pixelFormat.VAME_PIX_FMT_YUV420P9
    VAME_PIX_FMT_YUV422P9: int = vame.pixelFormat.VAME_PIX_FMT_YUV422P9
    VAME_PIX_FMT_YUV444P9: int = vame.pixelFormat.VAME_PIX_FMT_YUV444P9
    VAME_PIX_FMT_YUV420P10: int = vame.pixelFormat.VAME_PIX_FMT_YUV420P10
    VAME_PIX_FMT_YUV422P10: int = vame.pixelFormat.VAME_PIX_FMT_YUV422P10
    VAME_PIX_FMT_YUV444P10: int = vame.pixelFormat.VAME_PIX_FMT_YUV444P10
    VAME_PIX_FMT_YUV420P12: int = vame.pixelFormat.VAME_PIX_FMT_YUV420P12
    VAME_PIX_FMT_YUV422P12: int = vame.pixelFormat.VAME_PIX_FMT_YUV422P12
    VAME_PIX_FMT_YUV444P12: int = vame.pixelFormat.VAME_PIX_FMT_YUV444P12
    VAME_PIX_FMT_NV12: int = vame.pixelFormat.VAME_PIX_FMT_NV12
    VAME_PIX_FMT_NV21: int = vame.pixelFormat.VAME_PIX_FMT_NV21
    VAME_PIX_FMT_GRAY8: int = vame.pixelFormat.VAME_PIX_FMT_GRAY8
    VAME_PIX_FMT_GRAY9: int = vame.pixelFormat.VAME_PIX_FMT_GRAY9
    VAME_PIX_FMT_GRAY10: int = vame.pixelFormat.VAME_PIX_FMT_GRAY10
    VAME_PIX_FMT_GRAY12: int = vame.pixelFormat.VAME_PIX_FMT_GRAY12
    VAME_PIX_FMT_RGB24: int = vame.pixelFormat.VAME_PIX_FMT_RGB24
    VAME_PIX_FMT_BGR24: int = vame.pixelFormat.VAME_PIX_FMT_BGR24
    VAME_PIX_FMT_ARGB: int = vame.pixelFormat.VAME_PIX_FMT_ARGB
    VAME_PIX_FMT_RGBA: int = vame.pixelFormat.VAME_PIX_FMT_RGBA
    VAME_PIX_FMT_ABGR: int = vame.pixelFormat.VAME_PIX_FMT_ABGR
    VAME_PIX_FMT_BGRA: int = vame.pixelFormat.VAME_PIX_FMT_BGRA

class JPEG_CODING_MODE():
    """
    vame jpeg coding mode
    ----------\n
    @enum JPEG_NONE: none.\n
    @enum JPEG_BASELINE: baseline.\n
    @enum JPEG_PROGRESSIVE: progressive.\n
    @enum JPEG_NONINTERLEAVED: noninterleaved.\n
    """
    JPEG_NONE: int = vame.jpegCodingMode.VAME_JPEG_NONE
    JPEG_BASELINE: int = vame.jpegCodingMode.VAME_JPEG_BASELINE
    JPEG_PROGRESSIVE: int = vame.jpegCodingMode.VAME_JPEG_PROGRESSIVE
    JPEG_NONINTERLEAVED: int = vame.jpegCodingMode.VAME_JPEG_NONINTERLEAVED

class CHROMA_FORMAT():
    """
    vame chroma format
    ----------\n
    @enum CHROMA_FMT_NONE: none.\n
    @enum CHROMA_FMT_400: 400.\n
    @enum CHROMA_FMT_411: 411.\n
    @enum CHROMA_FMT_420: 420.\n
    @enum CHROMA_FMT_422: 422.\n
    @enum CHROMA_FMT_440: 440.\n
    @enum CHROMA_FMT_444: 444.\n
    """
    CHROMA_FMT_NONE: int = vame.chromaFormat.VAME_CHROMA_FMT_NONE
    CHROMA_FMT_400: int = vame.chromaFormat.VAME_CHROMA_FMT_400
    CHROMA_FMT_411: int = vame.chromaFormat.VAME_CHROMA_FMT_411
    CHROMA_FMT_420: int = vame.chromaFormat.VAME_CHROMA_FMT_420
    CHROMA_FMT_422: int = vame.chromaFormat.VAME_CHROMA_FMT_422
    CHROMA_FMT_440: int = vame.chromaFormat.VAME_CHROMA_FMT_440
    CHROMA_FMT_444: int = vame.chromaFormat.VAME_CHROMA_FMT_444

class MEMORY_TYPE():
    """
    vame memory type.\n
    ----------\n
    @enum MEM_DEVICE: memory on devide.\n
    @enum MEM_HOST: memory on host.\n
    @enum MEM_FLUSH: memory on flush.\n
    """
    MEM_DEVICE: int = vame.memoryType.VAME_MEM_DEVICE
    MEM_HOST: int = vame.memoryType.VAME_MEM_HOST
    MEM_FLUSH: int = vame.memoryType.VAME_MEM_FLUSH

class VIDEO_FIELD():
    """
    vame video field.\n
    ----------\n
    @enum FLD_FRAME: fld.\n
    """
    FLD_FRAME: int = vame.videoField.VAME_FLD_FRAME

class FRAME_TYPE():
    """
    vame frame type.\n
    ----------\n
    @enum FRM_I: I.\n
    @enum FRM_P: P.\n
    @enum FRM_B: B.\n
    """
    FRM_I: int = vame.frameType.VAME_FRM_I
    FRM_P: int = vame.frameType.VAME_FRM_P
    FRM_B: int = vame.frameType.VAME_FRM_B


# define
DEC_MAX_PIX_FMT_NUM = vame.VAME_DEC_MAX_PIX_FMT_NUM
DEC_MAX_CODING_MODE_NUM = vame.VAME_DEC_MAX_CODING_MODE_NUM
DEC_VIDEO_MAX_WIDTH = vame.VAME_DEC_VIDEO_MAX_WIDTH    
DEC_VIDEO_MAX_HEIGHT = vame.VAME_DEC_VIDEO_MAX_HEIGHT
DEC_VIDEO_MIN_WIDTH = vame.VAME_DEC_VIDEO_MIN_WIDTH
DEC_VIDEO_MIN_HEIGHT = vame.VAME_DEC_VIDEO_MIN_HEIGHT
DEC_JPEG_MAX_WIDTH = vame.VAME_DEC_JPEG_MAX_WIDTH
DEC_JPEG_MAX_HEIGHT = vame.VAME_DEC_JPEG_MAX_HEIGHT
DEC_JPEG_MIN_WIDTH = vame.VAME_DEC_JPEG_MIN_WIDTH
DEC_JPEG_MIN_HEIGHT = vame.VAME_DEC_JPEG_MIN_HEIGHT
MAX_STREAM_SIZE_4_JPEG = vame.MAX_STREAM_SIZE_4_JPEG

# struct
class DecChannelParamters():
    """
    Decode Channel Paramters.
    """
    codecType: CODEC_TYPE
    sourceMode: SOURCE_MODE
    decodeMode: DECODE_MODE
    pixelFormat: PIXEL_FORMAT
    maxWidth: int
    maxHeight: int
    streamBufferSize: int
    extraBufferNumber: int

class DecJpegInfo():
    """
    Decode Jpeg Information
    """
    width: int
    height: int
    x_density: int
    y_density: int
    outputFormat: CHROMA_FORMAT
    codingMode: JPEG_CODING_MODE

# class CropInfo():
#     flag: int
#     width: int
#     height: int
#     xOffset: int
#     yOffset: int

# class Frame():
#     data: np.ndarray
#     busAddress: List[int]
#     stride: List[int]
#     dataSize: int
#     width: int
#     height: int
#     pts: int
#     memoryType: MEMORY_TYPE
#     field: VIDEO_FIELD
#     pixelFormat: PIXEL_FORMAT
#     frameType: FRAME_TYPE
#     cropInfo: CropInfo

# api
@err_checker
def systemInitialize() -> int:
    """
    Initialize the vame system.\n
    """
    return vame.systemInitialize()

@err_checker
def systemUninitialize() -> int:
    """
    Uninitialize the vame system.\n
    """
    return vame.systemUninitialize()

@err_checker
def createDecoderChannel(params: DecChannelParamters, channelId: int) -> int:
    """
    Create an decoder channel.\n
    ----------\n
    param [in]: The init parameter for create decoder channel.\n
    channelId [in]: Decoder channel index.\n
    """
    paramsPybind = vame.decChannelParamters()
    paramsPybind.codecType = params.codecType
    paramsPybind.sourceMode = params.sourceMode
    paramsPybind.decodeMode = params.decodeMode
    paramsPybind.pixelFormat = params.pixelFormat
    paramsPybind.maxWidth = params.maxWidth
    paramsPybind.maxHeight = params.maxHeight
    paramsPybind.streamBufferSize = params.streamBufferSize
    paramsPybind.extraBufferNumber = params.extraBufferNumber

    return vame.createDecoderChannel(paramsPybind, channelId)

@err_checker
def startDecoder(channelId: int) -> int:
    """
    Start the decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    return vame.startDecoder(channelId)

@err_checker
def stopDecoder(channelId: int) -> int:
    """
    Stop the decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    return vame.stopDecoder(channelId)

@err_checker
def resetDecoder(channelId: int) -> int:
    """
    Restart the decoder.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    return vame.resetDecoder(channelId)

@err_checker
def destoryDecoder(channelId: int) -> int:
    """
    Destory the system.\n
    ----------\n
    channelId [in]: Decoder channel index.\n
    """
    return vame.destoryDecoderChannel(channelId)

def getJpegInfo(imagePath: str) -> DecJpegInfo:
    """
    Get input jpeg information.\n
    ----------\n
    imagePath [in]: The image path.\n
    """
    jpegInfoPybind = vame.decJpegInfo()
    if (vame.getJpegInfo(imagePath, jpegInfoPybind) != 0):
        raise Exception("Interal Error")
    jpegInfo = DecJpegInfo()
    jpegInfo.width = jpegInfoPybind.width
    jpegInfo.height = jpegInfoPybind.height
    jpegInfo.x_density = jpegInfoPybind.x_density
    jpegInfo.y_density = jpegInfoPybind.y_density
    jpegInfo.outputFormat = jpegInfoPybind.outputFormat
    jpegInfo.codingMode = jpegInfoPybind.codingMode
    return jpegInfo

# def jegSyncDecoder(channelId: int, imagePath: str) -> Frame:
#     framePybind = vame.frame
#     if (vame.jegSyncDecoder(channelId, imagePath, framePybind) != 0):
#         raise Exception("Interal Error")
#     frame = Frame()

#     return frame
