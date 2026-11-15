from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from models.cockroach import Cockroach
from models.player import Player

app = Ursina()

window.title = "PS1 Horror FPS"
window.borderless = False
window.fullscreen = False
window.vsync = False

window.color = color.black
scene.fog_color = color.black
scene.fog_density = 0.15

AmbientLight(color=color.rgb(2, 2, 2))

DirectionalLight(color=color.rgb(15,15,20), rotation=(45,-45, 45))


bunker = Entity(
    model="assets/models/maps/bunker.glb",
    position=(0, 0, 0),
    scale=1,
    collider="mesh",
)

player_spawn = bunker.find("**/PlayerSpawn")

player = None

if not player_spawn.isEmpty():
    player_spawn_cord = player_spawn.getPos(render)
    player = Player(position_ref=player_spawn_cord)
    print(f"Plyer status position: {player.position}")


#cockroach = Cockroach(player_ref=player, position_ref=(0,0,-5)) 

def input(key):
    if key == 'p':
        print(f"Position player status: {player.position}")
    if key == "left mouse down":
        gun.position += (0, 0.05, -0.1)
        invoke(lambda: setattr(gun, 'position', (0.4, -0.3, 0.8)), delay=0.1)

        hit_info = raycast(camera.world_position, camera.forward, distance=20)

        if(hit_info.hit):
            print(f"Hit the: {hit_info.entity}")

            if hasattr(hit_info.entity, 'take_damage'):
                hit_info.entity.take_damage(1)

app.run()
