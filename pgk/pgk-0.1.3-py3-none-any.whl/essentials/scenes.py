class Scenes:
    def __init__(self):
        self.current_scene = None
        self.scenes = {}

    def process(self):
        self.current_scene.process()

    def render(self):
        self.current_scene.render()

    def set_current_scene(self, scene, scene_name=None):
        self.current_scene = scene
        if scene_name is None:
            scene_name = scene.__class__.__name__
        self.scenes[scene_name] = scene.__class__
