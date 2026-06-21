#handles all switching between scenes (menus,pause,gameplat etc.)
from scenes.gameplayScene import GameplayScene 
class Engine:
    def __init__(self):

        self.scenes = {
            "GAMEPLAY": GameplayScene()
        }

        self.active_scene = self.scenes["GAMEPLAY"]
        self.active_scene.on_enter()

    def handle_event(self,events):
        self.active_scene.handle_event(events)

    def update(self, dt):
        self.active_scene.update(dt)

    def draw(self,screen):
        self.active_scene.draw(screen)

    def switch_scene(self, next_scene_key):

        if next_scene_key in self.scenes:

            if hasattr(self.active_scene, 'on_exit'):
                self.active_scene.on_exit()
    
            self.active_scene = self.scenes[next_scene_key]
            
            self.active_scene.on_enter()
        else:
            print(f"Error: Scene key '{next_scene_key}' was not found in Engine registry.")
