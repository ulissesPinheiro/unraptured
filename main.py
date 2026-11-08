from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from models.enemy import Enemy
from models.player import Player

app = Ursina()

window.title = "PS1 Horror FPS"
window.borderless = False
window.fullscreen = False
window.vsync = True

window.color = color.black
scene.fog_color = color.black
scene.fog_density = 0.08

AmbientLight(color=color.rgb(10, 10, 10))

DirectionalLight(color=color.rgb(30,30,40), rotation=(45,-45, 45))


prison = Entity(
    model="assets/models/prison.glb",
    position=(0, 0, 0),
    scale=(1, 1, 1),
    collider="mesh",
)

gun = Entity(
        model="assets/models/makarov_PM.glb",
        parent=camera,
        position=(0.4,-0.3,0.8),
        scale=(1,1,1),
        )

player = Player()

orus = Enemy(position=(0,0,10), player_ref=player) 

flashlight = SpotLight(
    parent=player, color=color.rgb(255, 255, 220), position=(0, 1.5, 0)
)
flashlight.look_at(player.forward)
flashlight.fov = 70
flashlight.brightness = 1 

def input(key):
    if key == "left mouse down":
        gun.position += (0, 0.05, -0.1)
        invoke(lambda: setattr(gun, 'position', (0.4, -0.3, 0.8)), delay=0.1)

        hit_info = raycast(camera.world_position, camera.forward, distance=20)

        if(hit_info.hit):
            print(f"Hit the: {hit_info.entity}")

            if hasattr(hit_info.entity, 'take_damage'):
                hit_info.entity.take_damage(1)

app.run()
