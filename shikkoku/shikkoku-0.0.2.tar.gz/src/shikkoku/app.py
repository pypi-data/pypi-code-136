import sdl2
import sdl2.ext
import sdl2.sdlttf
import os
from shikkoku.engine import Scene
import importlib.resources
from PIL import Image
import asyncio
import contextvars
import logging

class App():
    
    def __init__(self, app_name: str, window_size: tuple):
        
        sdl2.ext.init()
        sdl2.sdlttf.TTF_Init()
        
        self.window = sdl2.ext.Window(app_name, window_size)
        self.current_scene = None
        self.scenes = dict()
        self.images = dict()
        self.uiprocessor = sdl2.ext.UIProcessor()
        self.factory = sdl2.ext.SpriteFactory(sprite_type=sdl2.ext.SOFTWARE, free=False)
        self.spriterenderer = self.factory.create_sprite_render_system(self.window)
        self.target_fps = contextvars.ContextVar('target_fps', default=60)
        self.frame_count = 0
        self.timer = 0
        self.current_fps = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        sdl2.ext.quit()
        return 0
    
    @property
    def input_locked(self):
        return self.current_scene.animation_locked
    
    def add_scene(self, scene: Scene):
        self.scenes[scene.name] = scene
    
    def assign_image_path(self, resource_module):
        self.resource_module = resource_module
    
    def get_image_from_path(self, file_name: str) -> Image:
        with importlib.resources.path(self.resource_module, file_name) as path:
            return Image.open(path)
        
    def init_font(self, size: int, font_file_name: str):
        with importlib.resources.path(self.resource_module, font_file_name) as path:
            return sdl2.sdlttf.TTF_OpenFont(str.encode(os.fspath(path)), size)
        
    def assign_font(self, font):
        self.font = font
    
    def load(self, image_name: str, width: int = 0, height: int = 0) -> Image:
        try:
            return self.images[image_name]
        except KeyError:
            self.images[image_name] = self.get_image_from_path(image_name)
            return self.images[image_name]

    def reset_event_trigger(self):
        self.current_scene.triggered_event = False
        
    def start_game_loop(self, initial_scene: Scene):
        self.change_scene(initial_scene)
        self.window.show()
        game_loop_task = self.game_loop()
        asyncio.run(game_loop_task)
        
        sdl2.ext.quit()
    
    def update_mouse_position(self, x: int, y: int):
        self.mouse_x = x
        self.mouse_y = y
    
    async def game_loop(self):
        running = True
        logging.debug("Starting game loop!")
        while running:
            start = sdl2.SDL_GetPerformanceCounter()
            self.reset_event_trigger()
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running=False
                    logging.debug("sdl2.SDL_QUIT event!")
                    break
                if not self.input_locked:
                    if event.type == sdl2.SDL_MOUSEMOTION:
                        self.update_mouse_position(event.motion.x, event.motion.y)
                    else:
                        self.current_scene.handle_event(event)
                    for sprite in self.current_scene.eventables():
                        self.uiprocessor.dispatch(sprite, event)
                        if self.current_scene.triggered_event:
                            break
            self.current_scene.update_scene_state()
            
            if self.current_scene.animations:
                self.current_scene.progress_animations()
            self.spriterenderer.render(self.current_scene.renderables())
            self.current_scene.triggered_event = False
            self.window.refresh()
            
            if self.current_scene.animations:
                self.current_scene.check_animations()
            
            done = sdl2.SDL_GetPerformanceCounter()
            elapsed = (done - start) / float(sdl2.SDL_GetPerformanceFrequency())
            self.count_frames()
            sleep_duration = max( ( 1.0 / self.target_fps.get() ) - elapsed, 0 )
            self.fps = 1.0 / elapsed
            await asyncio.sleep(sleep_duration)
        logging.debug("Exited game loop!")
    
    def count_frames(self):
        self.frame_count += 1
        if self.frame_count > 60:
            self.tick_timer()
            self.frame_count = 0
    
    def tick_timer(self):
        if self.timer > 0:
            self.timer -= 1
            if self.timer == 0:
                self.stop_timer()
                
    def stop_timer(self):
        pass
    
    def change_scene(self, scene):
        '''Change the currently active scene to the scene passed as an argument. Can accept
        either a Scene object or the name of a Scene object already in the App's collection of known Scenes.'''
        if isinstance(scene, Scene):
            self.current_scene = scene
        elif isinstance(scene, str):
            self.current_scene = self.scenes[scene]
        
        self.current_scene.full_render()
