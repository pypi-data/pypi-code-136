"""Core game engine logic."""
import ctypes
import operator
from typing import Iterator
from typing import MutableMapping
from typing import Tuple
from PIL import Image, ImageDraw
import sdl2
import sdl2.ext
import sdl2.sdlttf
import sdl2.surface
from sdl2 import endian
from shikkoku.text_formatter import *

WHITE = sdl2.SDL_Color(255, 255, 255)


def sat_subtract(subtractor: int, subtractee: int) -> int:
    subtractee -= subtractor
    if subtractee < 0:
        subtractee = 0
    return subtractee


def get_mouse_position() -> Tuple[int, int]:
    x, y = ctypes.c_int(0), ctypes.c_int(0)
    sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
    return (x.value, y.value)

class Scene:
    """Scene assets, draw regions, and associated game state."""
    surfaces: MutableMapping[str, sdl2.SDL_Surface]
    region: "Region"
    sprite_factory: sdl2.ext.SpriteFactory
    ui_factory: sdl2.ext.UIFactory
    triggered_event: bool
    font: None
    animations: list
    animation_lock: list
    animation_locked: bool
    skipping_animations: bool

    def __init__(self, app, name: str):
        self.animations = []
        self.animation_lock = []
        self.skipping_animations = False
        self.animation_locked = False
        self.name = name
        self.app = app
        self.region = Region()
        self.animation_region = Region()
        self.sprite_factory = self.app.factory
        self.ui_factory = sdl2.ext.UIFactory(self.sprite_factory, free=True)
        self.surfaces = dict()
        self.window_closing = False
        self.window_up = False
        self.triggered_event = False

    def renderables(self) -> Iterator[sdl2.ext.Sprite]:
        return iter(self.region)

    def eventables(self) -> Iterator[sdl2.ext.Sprite]:
        return self.region.eventables()

    def add_animation(self, animation):
        self.animations.append(animation)
        if animation.lock:
            self.animation_locked = True
            self.animation_lock.append(animation)

    def remove_animation(self, animation):
        self.animations.remove(animation)

    def check_animation_lock(self, animation):
        self.animation_lock.remove(animation)
    
    def end_animations(self):
        end_funcs = list()
        for animation in self.animations:
            for func in animation.end_funcs:
                end_funcs.append(func)
        self.animations.clear()
        self.animation_lock.clear()
        self.animation_locked = False
        self.animation_region.clear()
        for func in end_funcs:
            func[0](*func[1])

    def progress_animations(self):
        self.animation_region.clear()
        for animation in self.animations:
            
            animation.progress_frame_timer()
            if animation.display:
                self.animation_region.add_sprite(animation.current_sprite, animation.display_x, animation.display_y)
    
    def check_animations(self):
        for animation in self.animations:
            if animation.has_ended:
                animation.end()
        
        if not self.animation_lock:
            self.animation_locked = False

    def make_button(self, surface):
        sprite = sdl2.ext.SoftwareSprite(surface, free=True)
        sdl2.ext.uisystem._compose_button(sprite)
        return sprite
    
    def make_sprite(self, image, width=0, height=0, flipped=False):
        surf = self.image_to_surf(image, width, height, flipped)
        sprite = sdl2.ext.SoftwareSprite(surf, free=True)
        return sprite
    
    def make_panel(self, color, size):
        return self.sprite_factory.from_color(color, size)

    def image_to_surf(self, img, width: int = 0, height: int = 0, flipped=False) -> sdl2.SDL_Surface:
        image = img
        if width != 0 or height != 0:
            image = image.resize((width, height))
        else:
            width, height = (image.size)
        mode = image.mode
        if flipped:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        rmask = gmask = bmask = amask = 0
        if mode in ("1", "L", "P"):
            # 1 = B/W, 1 bit per byte
            # "L" = greyscale, 8-bit
            # "P" = palette-based, 8-bit
            pitch = width
            depth = 8
        elif mode == "RGB":
            # 3x8-bit, 24bpp
            
            if endian.SDL_BYTEORDER == endian.SDL_LIL_ENDIAN:
                rmask = 0x0000FF
                gmask = 0x00FF00
                bmask = 0xFF0000
            else:
                rmask = 0xFF0000
                gmask = 0x00FF00
                bmask = 0x0000FF
            depth = 24
            pitch = width * 3
        elif mode in ("RGBA", "RGBX"):
            # RGBX: 4x8-bit, no alpha
            # RGBA: 4x8-bit, alpha
            
            if endian.SDL_BYTEORDER == endian.SDL_LIL_ENDIAN:
                rmask = 0x000000FF
                gmask = 0x0000FF00
                bmask = 0x00FF0000
                if mode == "RGBA":
                    amask = 0xFF000000
            else:
                rmask = 0xFF000000
                gmask = 0x00FF0000
                bmask = 0x0000FF00
                if mode == "RGBA":
                    amask = 0x000000FF
            depth = 32
            pitch = width * 4
        else:
            # We do not support CMYK or YCbCr for now
            raise TypeError("unsupported image format")
        pxbuf = image.tobytes()
        
        imgsurface = sdl2.surface.SDL_CreateRGBSurfaceFrom(pxbuf, width, height, depth, pitch, rmask, gmask, bmask, amask)
        imgsurface = imgsurface.contents
        imgsurface._pxbuf = pxbuf
        return imgsurface
    
    def render_text(self, font, text, color, target, x, y, flow = False, target_width = 0, fontsize = 0):
        if not flow:
            text_surface = sdl2.sdlttf.TTF_RenderText_Blended(font, str.encode(text), color)
            sdl2.surface.SDL_BlitSurface(text_surface, None, target.surface, sdl2.SDL_Rect(x, y))
            sdl2.SDL_FreeSurface(text_surface)
        else:
            lines = get_lines(text, target_width, fontsize)
            line_height = get_font_height(fontsize)
            for i, line in enumerate(lines):
                text_surface = sdl2.sdlttf.TTF_RenderText_Blended(font, str.encode(line), color)
                sdl2.surface.SDL_BlitSurface(text_surface, None, target.surface, sdl2.SDL_Rect(x, y + (i * line_height)))
                sdl2.SDL_FreeSurface(text_surface)
        return target
    
    def render_bordered_text(self, font, text, color, border_color, target, x, y, thickness, flow = False, target_width = 0, fontsize = 0):
        if not flow:
            text_surf = sdl2.sdlttf.TTF_RenderText_Blended(font, str.encode(text), border_color)
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x-thickness, y-thickness))
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x,           y-thickness))
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x+thickness, y-thickness))
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x-thickness, y))
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x+thickness, y))
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x-thickness, y+thickness))
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x,           y+thickness))
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x+thickness, y+thickness))
            sdl2.SDL_FreeSurface(text_surf)
            
            text_surf = sdl2.sdlttf.TTF_RenderText_Blended(font, str.encode(text), color)
            sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x, y))
            sdl2.SDL_FreeSurface(text_surf)
        else:
            lines = get_lines(text, target_width, fontsize)
            line_height = get_font_height(fontsize)
            for i, line in enumerate(lines):
                mod_y = y + (i * line_height)
                text_surf = sdl2.sdlttf.TTF_RenderText_Blended(font, str.encode(line), border_color)
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x-thickness, mod_y-thickness))
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x,           mod_y-thickness))
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x+thickness, mod_y-thickness))
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x-thickness, mod_y))
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x+thickness, mod_y))
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x-thickness, mod_y+thickness))
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x,           mod_y+thickness))
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x+thickness, mod_y+thickness))
                sdl2.SDL_FreeSurface(text_surf)
                
                text_surf = sdl2.sdlttf.TTF_RenderText_Blended(font, str.encode(line), color)
                sdl2.surface.SDL_BlitSurface(text_surf, None, target.surface, sdl2.SDL_Rect(x, mod_y))
                sdl2.SDL_FreeSurface(text_surf)
        
        return target

    def border_image(self, image, thickness):
        new = image.copy()
        w, h = image.size
        
        brush = ImageDraw.Draw(new)
        brush.rectangle([(0, 0), (w, thickness)], fill="black", outline = "black")
        brush.rectangle([(0, 0), (thickness, h)], fill="black", outline = "black")
        brush.rectangle([(w - 2, 0), (w, h)], fill="black", outline = "black")
        brush.rectangle([(0, h - 2), (w, h)], fill="black", outline = "black")
        
        return new

    def border_sprite(self, sprite, color, thickness):
        
        target_surface = sprite.surface
        height = target_surface.h
        width = target_surface.w
        horizontal_border = self.sprite_factory.from_color(color, (width, thickness))
        vertical_border = self.sprite_factory.from_color(color, (thickness, height))
        
        sdl2.surface.SDL_BlitSurface(horizontal_border.surface, None, sprite.surface, sdl2.SDL_Rect(0, 0))
        sdl2.surface.SDL_BlitSurface(horizontal_border.surface, None, sprite.surface, sdl2.SDL_Rect(0, height - thickness))
        sdl2.surface.SDL_BlitSurface(vertical_border.surface, None, sprite.surface, sdl2.SDL_Rect(0, 0))
        sdl2.surface.SDL_BlitSurface(vertical_border.surface, None, sprite.surface, sdl2.SDL_Rect(width - thickness, 0))
        
        return sprite
    
    def blit_surface(self, target, surface, dest):
        
        sdl2.surface.SDL_BlitSurface(surface, None, target.surface, sdl2.SDL_Rect(*dest))
        return target

    def add_horizontal_line(self, sprite, color, thickness, length, destination):
        
        line = self.sprite_factory.from_color(color, (length, thickness))
        sdl2.surface.SDL_BlitSurface(line.surface, None, sprite.surface, sdl2.SDL_Rect(*destination))
        
        return sprite
    
    def add_vertical_line(self, sprite, color, thickness, length, destination):
        
        line = self.sprite_factory.from_color(color, (thickness, length))
        sdl2.surface.SDL_BlitSurface(line.surface, None, sprite.surface, sdl2.SDL_Rect(*destination))
        
        return sprite

class Region:
    """Spatial region on the screen with relative coordinate offsets & spinning rims."""
    x: int
    y: int
    width: int
    height: int
    _regions: list["Region"]
    _sprites: list[sdl2.ext.Sprite]

    def __init__(self, x: int = 0, y: int = 0, width: int = 0, height: int = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self._regions = []
        self._sprites = []

    def __iter__(self) -> Iterator[sdl2.ext.Sprite]:
        yield from self._sprites
        for subregion in self._regions:
            yield from subregion

    def subregion(self, x: int, y: int, width: int, height: int) -> "Region":
        subreg = Region(self.x + x, self.y + y, width, height)
        self._regions.append(subreg)
        return subreg

    def add_sprite(self, sprite: sdl2.ext.Sprite, x: int, y: int, depth: int = 0):
        sprite.x = self.x + x
        sprite.y = self.y + y
        sprite.depth = depth
        self._sprites.append(sprite)
        self._sprites.sort(key=operator.attrgetter('depth'))

    def add_sprite_vertical_center(self, sprite: sdl2.ext.Sprite, x: int, depth: int = 0):
        sprite.x = self.x + x
        sprite.depth = depth

        region_center = self.height // 2
        sprite_center = sprite.size[1] // 2

        sprite.y = self.y + region_center - sprite_center

        self._sprites.append(sprite)
        self._sprites.sort(key=operator.attrgetter('depth'))

    def size(self) -> Tuple[int, int]:
        return (self.width, self.height)

    def clear(self):
        """Removes all sprites from this region and all sub-regions"""
        self._sprites.clear()
        
        for subregion in self._regions:
            subregion.clear()

    def from_bottom(self, y: int) -> int:
        return self.height - y

    def from_right(self, x: int) -> int:
        return self.width - x

    def eventables(self) -> Iterator[sdl2.ext.Sprite]:
        for subregion in reversed(self._regions):
            yield from subregion.eventables()
        yield from filter(is_eventable, reversed(self._sprites))


def is_eventable(sprite: sdl2.ext.Sprite) -> bool:
    """"Determines whether a sprite is configured to be an event handler or not."""
    return (isinstance(sprite, sdl2.ext.Sprite) and hasattr(sprite, "events")
            and hasattr(sprite, "uitype"))


def clone_surface(surface: sdl2.SDL_Surface) -> sdl2.SDL_Surface:
    return sdl2.SDL_DuplicateSurface(surface).contents
