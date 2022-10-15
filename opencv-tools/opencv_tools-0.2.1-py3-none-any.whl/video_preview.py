from time import perf_counter, sleep

import cv2
import numpy as np
from opencvtools.img import Img


class StopVideo(Exception):
    """Exception to stop video."""
    pass


class VideoPreview:
    """
    Video display with OpenCV with some common functionality.

    Usage
    -------------------------
    with VideoPreview() as vid:
        for frame in Capture():
            vid.show(frame)

    Alternative usage (throws StopVideo exception on quit):
    -------------------------------------------------------
    vid = VideoPreview()
    for frame in Capture():
        vid.show(frame)
    """

    def __init__(self, window_name="Video preview", binds=None, window_size=None, force_framerate=None):
        self.keys = None
        self.window_name = window_name

        self.fullscreen = False
        self.binds = {27: self.quit, ord("f"): self.toggle_fullscreen} if binds is None else binds

        self.delay = 1 / force_framerate if force_framerate is not None else 0
        self.last_frame_time = 0

        cv2.namedWindow(self.window_name, cv2.WINDOW_FREERATIO)

        self.window_size = (1080, 1920) if window_size is None else window_size
        cv2.resizeWindow(self.window_name, *self.window_size[::-1])

    def toggle_fullscreen(self):
        cv2.setWindowProperty(self.window_name, cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN if not self.fullscreen else cv2.WINDOW_NORMAL)
        self.fullscreen = not self.fullscreen

    def show(self, frame):
        cv2.imshow(self.window_name, frame)

        self.keys = cv2.waitKey(1) & 0xFF
        if self.keys in self.binds:
            self.binds[self.keys]()

        sleep(max(self.last_frame_time + self.delay - perf_counter(), 0))
        self.last_frame_time = perf_counter()

    def show_many(self, *frames):
        frame = np.zeros(shape=(*self.window_size, 3), dtype=np.uint8)
        for f, pos in zip(frames, self.layout):
            x, y, w, h = pos
            f = Img.resize(f, width=w, height=h, keep_aspect_ratio=self.keep_aspect_ratio)
            x, y = x + int((w - f.width) / 2), y + int((h - f.height) / 2)
            w, h = f.width, f.height
            frame[y:y + h, x:x + w] = f

        self.show(frame)

    def set_multiframe_layout(self, n_frames, keep_aspect_ratio=False, orientation="cols"):
        self.keep_aspect_ratio = keep_aspect_ratio
        n = int(np.ceil(np.sqrt(n_frames)))
        layout = [n] * (n - 1) + [n_frames - n * (n - 1)]


        # grid
        if orientation == "cols":
            layout = [[j, i, 1, 1] for j, row in enumerate(layout) for i in range(row)]
        else:
            layout = [[i, j, 1, 1] for j, col in enumerate(layout) for i in range(col)]

        # scale
        max_i, max_j = max(i for i, _, _, _ in layout), max(j for _, j, _, _ in layout)


        # scale each subframe
        scale = self.window_size[1] / self.window_size[0]
        layout = [[x * scale, y, w * scale, h] for (x, y, w, h) in layout]

        # scale whole
        w = max([pos[0] + pos[2] for pos in layout])
        h = max([pos[1] + pos[3] for pos in layout])
        scale = min(self.window_size[0] / h, self.window_size[1] / w)
        layout = [[scale * p for p in pts] for pts in layout]

        # center
        x_offset = (self.window_size[1] - max([pos[0] + pos[2] for pos in layout])) / 2
        y_offset = (self.window_size[0] - max([pos[1] + pos[3] for pos in layout])) / 2
        layout = [[x + x_offset, y + y_offset, w, h] for (x, y, w, h) in layout]

        layout = [[int(p) for p in pts] for pts in layout]

        self.layout = layout

    def quit(self):
        raise StopVideo

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        cv2.destroyAllWindows()
        if type == StopVideo:
            return True
        return False
