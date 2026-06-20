#handles all switching between scenes (menus,pause,gameplat etc.)
from scenes.gameplayScene import GameplayScene 
class Engine:
    def __init__(self):

        self.scenes = {
            "GAMEPLAY": GameplayScene()
        }

        self.active_scene = self.scenes["GAMEPLAY"]
        self.active_scene.on_enter()

    def update(self, dt):
        self.active_scene.update(dt)
    def draw(self,screen):
        self.active_scene.draw(screen)
    def switch_scene(self, next_scene_key):
        """Safely shuts down the old scene and boots up the new one."""
        if next_scene_key in self.scenes:
            # Run cleanup on the old scene if it has one
            if hasattr(self.active_scene, 'on_exit'):
                self.active_scene.on_exit()
                
            # Swap the pointer to the new scene
            self.active_scene = self.scenes[next_scene_key]
            
            # Run setup or variables reset on the incoming scene
            self.active_scene.on_enter()
        else:
            print(f"Error: Scene key '{next_scene_key}' was not found in Engine registry.")
