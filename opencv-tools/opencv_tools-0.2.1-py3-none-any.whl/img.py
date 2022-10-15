import cupy as cp
import cv2
import numpy as np
from opencvtools.colors import Color as Clr


class Img(np.ndarray):
    def __new__(cls, input_array):
        if not isinstance(input_array, np.ndarray):
            raise TypeError(f'Input must be a numpy array. Got {type(input_array)}')

        if not 2 <= input_array.ndim <= 3:
            raise ValueError('Input must be 2 or 3 dimensional.')

        if input_array.dtype != np.uint8:
            max, min = np.min(input_array), np.max(input_array)
            if input_array.dtype in (np.float32, np.float64):
                if 0 <= min and max <= 1:
                    input_array = (input_array * 255).astype(np.uint8)
                else:
                    raise ValueError('Input array must be between 0 and 1 to be converted from float to uint8.')
            if input_array.dtype in (np.int32, np.int64):
                if 0 <= min and max <= 255:
                    input_array = input_array.astype(np.uint8)
                else:
                    raise ValueError('Input array must be between 0 and 255 to be converted from int to uint8.')

            if input_array.dtype in (bool, np.bool):
                input_array = input_array.astype(np.uint8) * 255

        obj = np.asarray(input_array).view(cls)

        return obj

    @property
    def height(self):
        return self.shape[0]

    @property
    def width(self):
        return self.shape[1]

    def resize(self, width=None, height=None, keep_aspect_ratio=True):
        if width is None and height is None:
            raise ValueError('Must provide either width or height.')
        if width is not None and height is not None and keep_aspect_ratio:
            scale = min(width / self.width, height / self.height)
            width, height = int(self.width * scale), int(self.height * scale)
        elif width is None:
            width = int(self.width * height / self.height)
        elif height is None:
            height = int(self.height * width / self.width)

        return Img(cv2.resize(self, (width, height)))

    def draw_line(self, *pts, thickness=2, color=Clr.RED, closed=False):
        pts = np.array(pts, np.int32)
        cv2.polylines(self, [pts], isClosed=closed, color=color, thickness=thickness)
        return self

    def draw_circle(self, center, radius, thickness=2, color=Clr.RED):
        center = np.array(center, np.int32)
        cv2.circle(self, center, int(radius), color=color, thickness=thickness)
        return self

    def draw_text(self, text, pos, font_scale=0.8, color=Clr.BLACK, thickness=2, bg_color=None):
        pos = np.array(pos, np.int32)
        if bg_color is not None:
            (w, h), b = cv2.getTextSize(text, 0, font_scale, thickness)
            cv2.rectangle(self, pos + [0, b], pos + [w + 2 * thickness, -h - b // 2], bg_color, -1)
        cv2.putText(self, text, pos + [thickness, 0], cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
        return self

    def draw_rect(self, tl, br, thickness=2, color=Clr.RED):
        tl = np.array(tl, np.int32)
        br = np.array(br, np.int32)
        cv2.rectangle(self, tl, br, color=color, thickness=thickness)
        return self

    def box_label(self, tlbr, label, color=Clr.RED):
        t, l, b, r = tlbr
        text_color = Clr.BLACK if np.array(color).mean() > 127 else Clr.WHITE
        self.draw_rect([t, l], [b, r], color=color)
        self.draw_text(label, (t, l), color=text_color, bg_color=color)
        return self

    def blend(self, other, alpha=None):
        if alpha is None:
            return other.copy()
        if alpha.ndim == 2:
            alpha = np.expand_dims(alpha, 2)
        alpha_gpu = cp.asarray(alpha)
        other_gpu = cp.asarray(other)
        self_gpu = cp.asarray(self)
        result = (self_gpu * (1 - alpha_gpu) + other_gpu * alpha_gpu).astype(cp.uint8)
        cp.asnumpy(result, out=self)
        return self

    def fill_color(self, color, alpha=None):
        return self.blend(np.full(self.shape, color, np.uint8), alpha)
