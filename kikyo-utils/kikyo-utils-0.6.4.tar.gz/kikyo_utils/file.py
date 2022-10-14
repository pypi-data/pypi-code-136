import base64
import gzip
import io
import mimetypes
import re
from typing import List, Optional

import fitz
import piexif
import requests
from PIL import Image
from fitz import Pixmap
from pydantic import BaseModel
from requests_toolbelt import MultipartEncoder

from kikyo_utils.constants import YURI_API_HOST, TIKA_HOST, PADDLEOCR_HOST, PDF_CONVERTER_HOST, FILE_CONTENT_LIMIT
from kikyo_utils.retry import retry_rest_api


def pdf_to_image(data: bytes, limit: Optional[int] = None, format: str = 'jpeg', **params):
    result = []
    pdf = fitz.Document(stream=io.BytesIO(data), filetype='pdf')
    zoom = 2  # zoom factor
    mat = fitz.Matrix(zoom, zoom)
    for i, page in enumerate(pdf):
        # 将每一页pdf读取为图片
        img: Pixmap = page.get_pixmap(matrix=mat)
        img_bytes = img.tobytes()
        if format == 'png':
            result.append(img_bytes)
        else:
            t = Image.open(io.BytesIO(img_bytes))
            o = io.BytesIO()
            t.save(o, format=format, **params)
            o.seek(0)
            result.append(o.read())
        if limit is not None and len(result) >= limit:
            break
    return result


def pdf_to_png(data: bytes, limit: Optional[int] = None) -> List[bytes]:
    return pdf_to_image(data, limit=limit, format='png')


@retry_rest_api
def download_file_from_bus(file_id: str, timeout: int = 20) -> bytes:
    resp = requests.get(
        f'{YURI_API_HOST}/filebus/download',
        params={
            'file_id': file_id,
        },
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp.content


@retry_rest_api
def download_file_from_link(link: str, timeout: int = 20) -> requests.Response:
    resp = requests.get(
        link,
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp


@retry_rest_api
def extract_content(source: bytes, timeout: int = 20) -> Optional[str]:
    resp = requests.put(
        f'{TIKA_HOST}/tika',
        data=source,
        timeout=timeout,
        headers={'Accept': 'text/plain'}
    )
    resp.raise_for_status()
    return resp.content.decode('utf-8')


def extract_content_by_ocr(source: bytes, timeout: int = 20) -> Optional[str]:
    img: Image.Image = Image.open(io.BytesIO(source))
    angle = _get_image_angle(img)
    res = ocr(source, timeout=timeout)
    _rotate_regions(res, img.width, img.height, angle)
    res.sort(key=lambda x: (x['text_region'][0][1], x['text_region'][0][0]))

    t = []
    for r in res:
        t.append(r['text'])
    return ''.join(t)


def _get_image_angle(img) -> str:
    orientation = 1
    if 'exif' in img.info:
        try:
            exif_dict = piexif.load(img.info['exif'])
            orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
        except Exception:
            pass
    if orientation == 3:
        angle = '180'
    elif orientation == 6:
        angle = '90'
    elif orientation == 8:
        angle = '270'
    else:
        angle = '0'
    return angle


def _rotate_regions(result, width, height, angle):
    count = 0
    for r in result:
        region = r['text_region']
        if region[1][0] - region[0][0] > region[3][1] - region[0][1]:
            count += 1
        else:
            count -= 1
    if count > 0:
        if angle == '180':
            for r in result:
                region = r['text_region']
                r['text_region'] = [
                    [width - region[2][0], height - region[2][1]],
                    [width - region[3][0], height - region[3][1]],
                    [width - region[0][0], height - region[0][1]],
                    [width - region[1][0], height - region[1][1]],
                ]
    else:
        if angle == '270':
            for r in result:
                region = r['text_region']
                r['text_region'] = [
                    [region[1][1], width - region[1][0]],
                    [region[2][1], width - region[2][0]],
                    [region[3][1], width - region[3][0]],
                    [region[0][1], width - region[0][0]],
                ]
        elif angle == '90':
            for r in result:
                region = r['text_region']
                r['text_region'] = [
                    [height - region[3][1], region[3][0]],
                    [height - region[0][1], region[0][0]],
                    [height - region[1][1], region[1][0]],
                    [height - region[2][1], region[2][0]],
                ]
        return height, width
    return width, height


@retry_rest_api
def ocr(source: bytes, timeout: int = 20) -> Optional[List[dict]]:
    image = base64.b64encode(source).decode('utf8')
    data = {"images": [image]}
    resp = requests.post(
        url=f'{PADDLEOCR_HOST}/predict/ocr_system',
        json=data,
        timeout=timeout,
    )
    resp.raise_for_status()
    res = resp.json()['results'][0]
    return res


content_file_ext = {
    'doc': 'application/msword',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'pdf': 'application/pdf',
    'ppt': 'application/vnd.ms-powerpoint',
    'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'xls': 'application/vnd.ms-excel',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
}


@retry_rest_api
def doc_to_pdf(source: bytes, filename: str = None, timeout: int = 20) -> Optional[bytes]:
    data = None
    if filename:
        ext = filename.rsplit('.', maxsplit=1)[-1]
        if ext in content_file_ext:
            data = (f'data.{ext}', io.BytesIO(source), content_file_ext[ext])
    if data is None:
        _meta = inspect_file(source, timeout=timeout)
        if _meta.content_type:
            data = ('data', io.BytesIO(source), _meta.content_type)
    if data is None:
        return

    payload = MultipartEncoder({'data': data})
    resp = requests.post(
        f'{PDF_CONVERTER_HOST}/lool/convert-to/pdf',
        data=payload,
        headers={'Content-Type': payload.content_type},
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp.content


@retry_rest_api
def extract_file_meta(source: bytes, timeout: int = 20) -> dict:
    resp = requests.put(
        f'{TIKA_HOST}/meta',
        data=source,
        headers={'Accept': 'application/json'},
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp.json()


class FileInspection(BaseModel):
    file_bytes: bytes = None
    file_ext: str = None
    content_type: str = None
    content_encoding: str = None


def inspect_file(file_bytes: bytes, timeout: int = 20) -> FileInspection:
    meta = extract_file_meta(file_bytes)

    content_type = meta.get('Content-Type')
    if content_type:
        content_type = content_type.split(';')[0]

    if content_type == 'application/gzip':
        file_bytes = gzip.decompress(file_bytes)
        meta = extract_file_meta(file_bytes, timeout=timeout)
        content_type = meta.get('Content-Type')
        if content_type:
            content_type = content_type.split(';')[0]

    content_encoding = meta.get('Content-Encoding')
    if content_type is not None:
        file_ext: Optional[str] = mimetypes.guess_extension(content_type)
        if file_ext:
            file_ext = file_ext[1:]
    else:
        file_ext = None

    return FileInspection(
        file_bytes=file_bytes,
        file_ext=file_ext,
        content_type=content_type,
        content_encoding=content_encoding,
    )


blank_reg = re.compile(r'[\r\f\t\v\u00a0\u1680\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]+')
line_break_reg = re.compile(r'[\n]{2,}')
word_blank_reg = re.compile(r'([\u4E00-\u9FA5\n])[ ]+([\u4E00-\u9FA5\n])')


def normalize_file_content(content: str, limit: int = None) -> str:
    content = blank_reg.sub(' ', content)

    content = word_blank_reg.sub(r'\1\2', content)
    content = word_blank_reg.sub(r'\1\2', content)

    content = line_break_reg.sub('\n\n', content)

    if limit is None:
        limit = FILE_CONTENT_LIMIT
    if limit > 0:
        if len(content) > limit:
            content = content[:limit]
    return content
