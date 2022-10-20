# -*- coding =utf-8 -*-
import logging
from enum import Enum

logger = logging.getLogger(__name__)


class HTTPStatus(Enum):
    """HTTP status codes and reason phrases
    Status codes from the following RFCs are all observed =
        * RFC 7231 = Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616
        * RFC 6585 = Additional HTTP Status Codes
        * RFC 3229 = Delta encoding in HTTP
        * RFC 4918 = HTTP Extensions for WebDAV, obsoletes 2518
        * RFC 5842 = Binding Extensions to WebDAV
        * RFC 7238 = Permanent Redirect
        * RFC 2295 = Transparent Content Negotiation in HTTP
        * RFC 2774 = An HTTP Extension Framework
    """
    def __new__(cls, value, phrase, description=''):
        obj = object.__new__(cls)
        obj._value_ = obj
        obj.code = value
        obj.phrase = phrase
        obj.description = description
        return obj

    @property
    def value(self):
        return self.code

    # informational
    SUCCESS = (0, 'success', 'Success')

    ### 通用 40xxxxx

    # 400001 请求路径错误
    REQUEST_PATH_ERR = (400001, '请求路径错误', '请求路径错误')

    # 400002 请求方法错误
    REQUEST_METHOD_ERR = (400002, "请求方法错误", "请求方法错误，请使用 POST 请求")
    REQUEST_METHOD_GET_ERR = (400002, "请求方法错误", "请求方法错误，请使用 GET 请求")

    # 400003 请求体内容为空
    BODY_EMPTY_ERR = (400003, "请求体内容为空", "请求体请求数据为空，没有包含内容")

    # 400004 请求体内容为空
    BODY_JSON_ERR = (400004, "请求体非 json 格式", "请求体内容需要符合 json 要求")

    # 400005 请求体类型错误
    BODY_TYPE_ERR = (400005, "请求体类型错误", "请求体需为字典，不能为其他类型")

    # 400006 必传的参数未传
    MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Action、ImageData）未传")
    ACTION_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Action）未传")
    IMAGE_AB_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Action、ImageDataA、ImageDataB）未传")
    TEXT_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Action、TextData）未传")
    AUDIO_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Action、AudioData）未传")
    VIDEO_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Action、VideoData）未传")
    MAKEUP_TYPE_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（MakeupType）未传")
    APPKEY_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（AppKey）未传")
    TOKEN_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Token）未传")
    VERSION_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Version）未传")
    IMAGE_DATA_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（ImageData）未传")
    INPUTS_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（inputs）未传")
    INPUT_URLS_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（input_urls）未传")
    INPUTS_OR_URLS_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（inputs 或 input_urls）未传")
    WEBSOCKET_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Action、Signal）未传")
    DBNAME_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（DbName）未传")
    ENTITY_ID_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（EntityId）未传")
    LABEL_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Label）未传")
    OFFSET_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Offset）未传")
    EXTRA_DATA_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（ExtraData）未传")
    LIMIT_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（Limit）未传")
    FACE_ID_MUST_PRAM_ERR = (400006, "必传的参数未传", "必须的参数（FaceId）未传")

    # 400007 传递非法参数
    ILLEGAL_PRAM_ERR = (400007, "传递非法参数", "请求体字典内有除（Action、ImageData）外的参数")

    # 400008 请求体的字段类型错误
    PRAM_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Action、ImageData 字段应该是 string 类型")
    IMAGE_AB_PRAM_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Action、ImageDataA、ImageDataB 字段应该是 string 类型")
    TEXT_PRAM_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Action、TextData 字段应该是 string 类型")
    AUDIO_PRAM_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Action、AudioData 字段应该是 string 类型")
    VIDEO_PRAM_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Action、VideoData 字段应该是 string 类型")
    IMAGE_URL_LIST_TYPE_ERR = (400008, "请求体的参数字段类型错误", "ImageURL 字段应该是 list 类型")
    IMAGE_URL_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "ImageURL 字段应该是 string 类型")
    TEXT_URL_LIST_TYPE_ERR = (400008, "请求体的参数字段类型错误", "TextURL 字段应该是 list 类型")
    TEXT_URL_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "TextURL 字段应该是 string 类型")
    AUDIO_URL_LIST_TYPE_ERR = (400008, "请求体的参数字段类型错误", "AudioURL 字段应该是 list 类型")
    AUDIO_URL_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "AudioURL 字段应该是 string 类型")
    VIDEO_URL_LIST_TYPE_ERR = (400008, "请求体的参数字段类型错误", "VideoURL 字段应该是 list 类型")
    VIDEO_URL_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "VideoURL 字段应该是 string 类型")
    INPUT_URLS_LIST_TYPE_ERR = (400008, "请求体的参数字段类型错误", "input_urls 字段应该是 list 类型")
    INPUT_URLS_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "input_url 字段应该是 string 类型")
    VOICE_TYPE_INT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "VoiceType 字段应该是 int 类型")  # 语音合成
    PITCH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Pitch 字段应该是 float 类型")  # 语音合成
    SPEED_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Speed 字段应该是 float 类型")  # 语音合成
    PERSON_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "PersonThresh 字段应该是 float 类型")  # 行人检测
    FACE_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "FaceThresh 字段应该是 float 类型")  # 人脸检测
    FIRE_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "FireThresh 字段应该是 float 类型")  # 烟雾明火检测
    SMOKE_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "SmokeThresh 字段应该是 float 类型")  # 烟雾明火检测
    CAR_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "CarThresh 字段应该是 float 类型")  # 车辆检测
    HELMET_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "HelmetThresh 字段应该是 float 类型")  # 安全帽检测
    SMOKE_LEVEL_INT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Level 字段应该是 int 类型")  # 吸烟检测
    SUIT_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "SuitThresh 字段应该是 float 类型")  # 防护服检测
    IMG_CENSOR_SUBTASK_LIST_TYPE_ERR = (400008, "请求体的参数字段类型错误", "SubTask 字段应该是 list 类型")  # 内容审核
    OCR_CAR_NEED_CAR_BOX_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedCarBox 字段应该是 bool 类型")  # 车牌识别
    OCR_CAR_NEED_CAR_ORIEN_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedCarOrien 字段应该是 bool 类型")  # 车牌识别
    EBIKE_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "EbikeThresh 字段应该是 float 类型")  # 电动车检测
    SCORE_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "ScoreThresh 字段应该是 float 类型")  # 通用分数阈值
    LANGUAGE_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Language 字段应该是 string 类型")  # 语种分类
    IS_MONOLINGUAL_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "IsMonolingual 字段应该是 bool 类型")  # 语种分类
    AREA_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "AreaThresh 字段应该是 float 类型")  # 遮挡检测
    HAND_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "HandThresh 字段应该是 float 类型")  # 手势关键点检测
    MAKEUP_TYPE_INT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "MakeupType 字段应该是 int 类型")  # 人脸美妆
    STRENGTH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Strength 字段应该是 float 类型")  # 人脸美妆
    OCR_CAR_NEED_CAR_TYPE_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedCarType 字段应该是 bool 类型")  # 车辆属性
    OCR_CAR_NEED_CAR_COLOR_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedCarColor 字段应该是 bool 类型")  # 车辆属性
    OCR_CAR_NEED_CAR_BRAND_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedCarBrand 字段应该是 bool 类型")  # 车辆属性
    DETECT_FACE_NEED_FACE_FEATURE_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedFaceFeature 字段应该是 bool 类型")  # 人脸检测
    DETECT_FACE_NEED_FACE_QUALITY_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedFaceQuality 字段应该是 bool 类型")  # 人脸检测
    DETECT_FACE_NEED_FACE_ANGLE_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedFaceAngle 字段应该是 bool 类型")  # 人脸检测
    MASK_THRESH_FLOAT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "MaskThresh 字段应该是 float 类型")  # 口罩检测
    DETECT_PERSON_NEED_BODY_FEATURE_BOOL_TYPE_ERR = (400008, "请求体的参数字段类型错误", "NeedBodyFeature 字段应该是 bool 类型")  # 行人检测
    APPKEY_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "AppKey 字段应该是 string 类型")
    TOKEN_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Token 字段应该是 string 类型")
    VERSION_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Version 字段应该是 string 类型")
    ACTION_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Action 字段应该是 string 类型")
    IMAGE_DATA_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "ImageData 字段应该是 string 类型")
    INPUTS_LIST_TYPE_ERR = (400008, "请求体的参数字段类型错误", "inputs 字段应该是 list 类型")
    WEBSOCKET_PRAM_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Action、Signal 字段应该是 string 类型")
    DBNAME_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "DbName 字段应该是 string 类型")
    ENTITY_ID_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "EntityId 字段应该是 string 类型")
    LABEL_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Label 字段应该是 string 类型")
    OFFSET_INT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Offset 字段应该是 int 类型")
    EXTRA_DATA_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "ExtraData 字段应该是 string 类型")
    LIMIT_INT_TYPE_ERR = (400008, "请求体的参数字段类型错误", "Limit 字段应该是 int 类型")
    FACE_ID_STRING_TYPE_ERR = (400008, "请求体的参数字段类型错误", "FaceId 字段应该是 string 类型")

    # 400009 请求体的参数字段值为空
    IMAGE_DATA_EMPTY_ERR = (400009, "请求体的参数字段值为空", "ImageData 字段值为空字符")
    IMAGE_AB_DATA_EMPTY_ERR = (400009, "请求体的参数字段值为空", "ImageDataA、ImageDataB 字段值为空字符")
    TEXT_DATA_EMPTY_ERR = (400009, "请求体的参数字段值为空", "TextData 字段值为空字符")
    AUDIO_DATA_EMPTY_ERR = (400009, "请求体的参数字段值为空", "AudioData 字段值为空字符")
    VIDEO_DATA_EMPTY_ERR = (400009, "请求体的参数字段值为空", "VideoData 字段值为空字符")
    IMAGE_URL_EMPTY_ERR = (400009, "请求体的参数字段值为空", "ImageURL 字段值为空字符")
    TEXT_URL_EMPTY_ERR = (400009, "请求体的参数字段值为空", "TextURL 字段值为空字符")
    AUDIO_URL_EMPTY_ERR = (400009, "请求体的参数字段值为空", "AudioURL 字段值为空字符")
    VIDEO_URL_EMPTY_ERR = (400009, "请求体的参数字段值为空", "VideoURL 字段值为空字符")
    INPUT_URLS_EMPTY_ERR = (400009, "请求体的参数字段值为空", "input_urls 列表为空")
    INPUTS_EMPTY_ERR = (400009, "请求体的参数字段值为空", "inputs 列表为空")
    WEBSOCKET_DATA_EMPTY_ERR = (400009, "请求体的参数字段值为空", "Signal 字段值为空字符")
    ACTION_EMPTY_ERR = (400009, "请求体的参数字段值为空", "Action 字段值为空字符")
    IMAGE_DATA_AND_ACTION_EMPTY_ERR = (400009, "请求体的参数字段值为空", "Action、ImageData 字段值为空字符")
    IMG_CENSOR_SUBTASK_EMPTY_ERR = (400009, "请求体的参数字段值为空", "SubTask 列表为空")
    
    # 400010 请求体的参数字段值设置错误
    ACTION_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Action 值设置错误")  # ACTION
    IMAGE_URL_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "ImageURL 字段不符合规范，请参考接口文档说明")
    TEXT_URL_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "TextURL 字段不符合规范，请参考接口文档说明")
    AUDIO_URL_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "AudioURL 字段不符合规范，请参考接口文档说明")
    VIDEO_URL_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "VideoURL 字段不符合规范，请参考接口文档说明")
    INPUT_URLS_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "input_urls 字段不符合规范，请参考接口文档说明")
    VOICE_TYPE_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "VoiceType 字段不符合规范，请参考接口文档说明")  # 语音合成
    PITCH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Pitch 字段不符合规范，请参考接口文档说明")  # 语音合成
    SPEED_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Speed 字段不符合规范，请参考接口文档说明")  # 语音合成
    PERSON_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "PersonThresh 字段不符合规范，请参考接口文档说明")  # 行人检测
    FACE_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "FaceThresh 字段不符合规范，请参考接口文档说明")  # 人脸检测
    FIRE_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "FireThresh 字段不符合规范，请参考接口文档说明")  # 烟雾明火检测
    SMOKE_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "SmokeThresh 字段不符合规范，请参考接口文档说明")  # 烟雾明火检测
    CAR_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "CarThresh 字段不符合规范，请参考接口文档说明")  # 车辆检测
    HELMET_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "HelmetThresh 字段不符合规范，请参考接口文档说明")  # 安全帽检测
    SMOKE_LEVEL_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Level 字段不符合规范，请参考接口文档说明")  # 吸烟检测
    SUIT_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "SuitThresh 字段不符合规范，请参考接口文档说明")  # 防护服检测
    IMG_CENSOR_SUBTASK_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "SubTask 字段不符合规范，请参考接口文档说明")  # 内容审核
    EBIKE_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "EbikeThresh 字段不符合规范，请参考接口文档说明")  # 电动车检测
    SCORE_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "ScoreThresh 字段不符合规范，请参考接口文档说明")  # 通用分数阈值
    LANGUAGE_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Language 字段不符合规范，请参考接口文档说明")  # 语种分类
    IS_MONOLINGUAL_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "IsMonolingual 字段不符合规范，请参考接口文档说明")  # 语种分类
    AREA_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "AreaThresh 字段不符合规范，请参考接口文档说明")  # 遮挡检测
    HAND_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "HandThresh 字段不符合规范，请参考接口文档说明")  # 手势关键点检测
    MAKEUP_TYPE_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "MakeupType 字段不符合规范，请参考接口文档说明")  # 人脸美妆
    STRENGTH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Strength 字段不符合规范，请参考接口文档说明")  # 人脸美妆
    MASK_THRESH_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "MaskThresh 字段不符合规范，请参考接口文档说明")  # 口罩检测
    APPKEY_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "AppKey 字段不符合规范，请参考接口文档说明")
    TOKEN_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Token 字段不符合规范，请参考接口文档说明")
    VERSION_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Version 字段不符合规范，请参考接口文档说明")
    INPUTS_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "inputs 字段不符合规范，请参考接口文档说明")
    SIGNAL_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Signal 值设置错误")
    DBNAME_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "DbName 字段不符合规范，请参考接口文档说明")
    ENTITY_ID_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "EntityId 字段不符合规范，请参考接口文档说明")
    LABEL_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Label 字段不符合规范，请参考接口文档说明")
    OFFSET_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Offset 字段不符合规范，请参考接口文档说明")
    EXTRA_DATA_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "ExtraData 字段不符合规范，请参考接口文档说明")
    LIMIT_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "Limit 字段不符合规范，请参考接口文档说明")
    FACE_ID_VALUE_ERR = (400010, "请求体的参数字段值设置错误", "FaceId 字段不符合规范，请参考接口文档说明")

    # 400011 base64 数据处理异常
    IMAGE_DATA_BASE64_ERR = (400011, "base64 数据处理异常", "ImageData 字段的 base64 字符串转换字节码异常")
    IMAGE_AB_DATA_BASE64_ERR = (400011, "base64 数据处理异常", "ImageDataA 或 ImageDataB 字段的 base64 字符串转换字节码异常")
    AUDIO_DATA_BASE64_ERR = (400011, "base64 数据处理异常", "AudioData 字段的 base64 字符串转换字节码异常")
    VIDEO_DATA_BASE64_ERR = (400011, "base64 数据处理异常", "VideoData 字段的 base64 字符串转换字节码异常")
    INPUTS_BASE64_ERR = (400011, "base64 数据处理异常", "inputs 字段的 base64 字符串转换字节码异常")

    # 400012 文件格式不合法
    IMAGE_TYPE_ERR = (400012, "文件格式不合法", "仅支持 jpeg/png/jpg/bmp 格式")
    IMAGE_TYPE_WEBP_ERR = (400012, "文件格式不合法", "仅支持 jpeg/png/jpg/bmp/webp 格式")
    IMAGE_TYPE_GIF_ERR = (400012, "文件格式不合法", "仅支持 jpeg/png/jpg/bmp/gif 格式")
    IMAGE_TYPE_TIFF_ERR = (400012, "文件格式不合法", "仅支持 jpeg/png/jpg/bmp/tiff 格式")
    IMAGE_TYPE_WEBP_GIF_TIFF_ERR = (400012, "文件格式不合法", "仅支持 jpeg/png/jpg/bmp/webp/tiff/gif 格式")
    IMAGE_TYPE_DOC_ERR = (400012, "文件格式不合法", "支持的图片格式请参考接口文档说明")
    AUDIO_TYPE_ERR = (400012, "文件格式不合法", "仅支持 pcm/wav 格式")
    AUDIO_TYPE_FLAC_ERR = (400012, "文件格式不合法", "仅支持 pcm/wav/flac 格式")
    AUDIO_TYPE_FLAC_MP3_ERR = (400012, "文件格式不合法", "仅支持 pcm/wav/flac/mp3 格式")
    AUDIO_TYPE_DOC_ERR = (400012, "文件格式不合法", "支持的音频格式请参考接口文档说明")

    # 400013 文件大小不符合要求
    IMAGE_SIZE_ERR = (400013, "文件大小不符合要求", "该文件大小不符合要求，图片要求小于 7M")
    AUDIO_SIZE_ERR = (400013, "文件大小不符合要求", "该文件大小不符合要求，音频要求小于 7M")
    VIDEO_SIZE_ERR = (400013, "文件大小不符合要求", "该文件大小不符合要求，视频要求小于 7M")

    # 4000014 请求时间范围不合法
    TIME_RANGE_ERR = (400014, "请求时间范围不合法", "请求时间范围不合法")

    # 4000015 文件下载错误
    IMAGE_URL_DOWNLOAD_ERR = (4000015, "文件下载错误", "无法解析图片链接，下载失败")
    TEXT_URL_DOWNLOAD_ERR = (4000015, "文件下载错误", "无法解析文本链接，下载失败")
    AUDIO_URL_DOWNLOAD_ERR = (4000015, "文件下载错误", "无法解析音频链接，下载失败")
    VIDEO_URL_DOWNLOAD_ERR = (4000015, "文件下载错误", "无法解析视频链接，下载失败")
    VINPUT_URLS_DOWNLOAD_ERR = (4000015, "文件下载错误", "无法解析链接，下载失败")

    # 4000016 必传的参数重复
    INPUTS_AND_URLS_DUPLI_PRAM_ERR = (
        4000016, "必传的参数重复", "必须的参数（inputs 或 input_urls）只能二选一")

    # 4000017 时间戳格式不对
    TIME_STAMP_FORMAT_ERR = (4000017, "时间戳格式不对", "必时间戳位数不是 10 位或者不是正整数")

    # 4000018 超过个数限制
    OVER_LIMIT_5_ERR = (4000018, "超过个数限制", "超过个数限制，最多传 5 张图片")

    # 图片 41xxxxx

    # 410001 图片解码错误
    IMAGE_DECODE_ERR = (410001, "图片解码错误", "字节码解码为图片错误")

    # 410002 图片尺寸不符合要求
    IMAGE_SHAPE_ERR = (410002, "图片尺寸不符合要求", "分辨率长宽尺寸应不高于 5000 不低于 32")
    IMAGE_SHAPE_6000_ERR = (410002, "图片尺寸不符合要求", "分辨率长宽尺寸应不高于 6000 不低于 32")

    # 文本 42xxxxx

    # 420001 文本长度超过限制
    TEXT_TOO_LONG_ERR = (420001, "文本长度超过限制", "文本输入过长，请参考接口文档说明")

    # 420002 文本长度低于阈值
    TEXT_TOO_SHORT_ERR = (420002, "文本长度低于阈值", "文本输入过短，请参考接口文档说明")

    # 420003 中文占比过低
    TEXT_CHINESE_TOO_LOW_ERR = (
        420003, "中文占比过低", "文本中的中文（仅包含汉字，不包含任何数字、符号）占比不低于50%")

    # 420004 文本不是 UTF8 格式
    TEXT_NOT_UTF8_ERR = (420004, "文本不是 UTF8 格式", "文本不是 UTF8 格式")

    # 420005 文本含有非法字符
    TEXT_ILLEGAL_ERR = (420005, "文本含有非法字符", "文本含有非法字符")

    # 音频 43xxxxx

    # 430001 音频解码错误
    AUDIO_DECODE_ERR = (430001, "音频解码错误", "字节码解码为音频解错误")

    # 430002 音频采样率不符合要求
    AUDIO_SAMPLE_RATE_ERR = (430002, "音频采样率不符合要求", "音频采样率应该为 16k")

    # 430003 音频采样精度不符合要求
    AUDIO_SAMPLE_ACCURACY_ERR = (430003, "音频采样精度不符合要求", "音频采样精度应该为 16bit")

    # 430004 音频声道数不符合要求
    AUDIO_CHANNEL_ERR = (430004, "音频声道数不符合要求", "音频应该为单声道")

    # 430005 音频长度不符合要求
    AUDIO_LENGTH_60s_ERR = (430005, "音频长度不符合要求", "音频长度过长，音频应该限制在 60s 内")
    AUDIO_LENGTH_120s_ERR = (430005, "音频长度不符合要求", "音频长度过长，音频应该限制在 120s 内")
    AUDIO_LENGTH_ERR = (430005, "音频长度不符合要求", "音频长度过长，请参考接口文档说明")

    # 数据库 45xxxxx
    # 450001 数据库操作失败
    DB_OPERATE_ERR = (450001, "数据库操作失败", "数据库操作失败")

    # 450002 请求的数据库不存在
    DB_NOT_EXIST_ERR = (450002, "请求的数据库不存在", "请求的数据库不存在")

    # 450003 请求的数据库已存在
    DB_EXIST_ERR = (450003, "请求的数据库已存在", "请求的数据库已存在")

    # 450004 请求的数据库实体不存在
    DB_NOT_ENTITY_EXIST_ERR = (450004, "请求的数据库实体不存在", "请求的数据库实体不存在")

    # 450005 请求的数据库实体已存在
    DB_ENTITY_EXIST_ERR = (450005, "请求的数据库实体已存在", "请求的数据库实体已存在")

    # server 服务 5xxxxxx
    SERVER_ERR = (500001, "服务接口异常，请联系管理员", "需要联系管理员处理")
    SERVER_DB_ERR = (500002, "数据库接口异常，请联系管理员", "需要联系管理员处理")
    SERVER_INFER_ERR = (500003, "模型推理错误，请联系管理员", "需要联系管理员处理")

    # 业务字段 6xxxxx

    # 人体相关业务字段 600xxx

    # 600001 人体特征提取错误
    BODY_FEATURE_ERR = (600001, "人体特征提取错误", "人体特征提取错误")

    # 600002 未检测到人体
    BODY_NO_DETECT_ERR = (600002, "未检测到人体", "未检测到人体")

    # 人脸相关业务字段 601xxx
    # 601001 人脸特征提取错误
    FACE_FEATURE_ERR = (601001, "人脸特征提取错误", "人脸特征提取错误")

    # 601002 未检测到人脸
    FACE_NO_DETECT_ERR = (601002, "未检测到人脸", "未检测到人脸")