from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.title = "PS1 Horror FPS"
window.borderless = False
window.fullscreen = False
window.vsync = True

window.color = color.black
scene.fog_color = color.black
scene.fog_density = 0.08

AmbientLight(color=color.rgba(20, 20, 20, 255))

hall = Entity(
    model="assets/models/hall.glb",
    position=(0, 0, 0),
    scale=(1, 1, 1),
    collider="mesh",
)

player = FirstPersonController(
    model="cube", color=color.red, scale=(1, 1, 1), speed=2, jump_height=0
)

player.cursor.visible = False
player.position = (0, 0, -2)
player.rotation = (0, 0, 0)

flashlight = SpotLight(
    parent=player, color=color.rgb(255, 255, 220), position=(0, 1.5, 0)
)
flashlight.look_at(player.forward)
flashlight.fov = 60
flashlight.brightness = 2

app.run()
