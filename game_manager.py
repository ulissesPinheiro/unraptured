import os
import sys

from ursina import *

class GameManager(Entity):
    def __init__(self):
        super().__init__()

        self.is_game_over = False

        self.hurt_flash = Entity(parent=camera.ui, model="quad",
                             scale=(window.aspect_ratio, 1),
                             color=color.red,
                             z=-1)

        self.hurt_flash.alpha = 0

        self.dark = Entity(parent=camera.ui, model="quad",
                       scale=(window.aspect_ratio, 1),
                       color=color.black,
                       z=-2, 
                       enabled=False)

        self.dark.alpha = 0

        self.title = Text(parent=camera.ui, text="You die", origin=(0,0),
                      y=0.05, scale=3, color=color.red, z=-3, enabled=False)

        self.hint = Text(parent=camera.ui, text="Press ENTER to start", origin=(0,0),
                     y=0.08, scale=1.2, z=-3, enabled=False)

    def on_player_hurt(self, player):
        self.hurt_flash.alpha = 0.45
        self.hurt_flash.fade_out(duration=0.4)

    def on_player_death(self, player):
        self.is_game_over = True
        self.dark.enabled = True
        self.dark.fade_in(value=0.85, duration=1.5)
        invoke(self.__show_text, delay=1.0)

    def _show_text(self):
        self.title.enabled = True
        self.hint.enabbled = True

    def input(self, key):
        if self.is_game_over and key == "enter":
            self.restart()


    def restart(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

