from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from models.cockroach import Cockroach
from models.ursula import Ursula
from models.makarov_magazine import MakarovMagazine
from ps1_render import PS1Renderer

app = Ursina()

window.borderless = True
window.fullscreen = True
window.vsync = True


# window.color = color.black
# scene.fog_color = color.black
# scene.fog_density = 0.12

#AmbientLight(color=color.rgba(0,0,0,255))

ps1 = PS1Renderer(
        width = 320,
        height = 180
        )

bunker = Entity(
    model="assets/models/maps/bunker.glb",
    position=(0, 0, 0),
    scale=1,
    collider="mesh",
)

# flashlight = SpotLight(
#         parent=camera,
#         position=(0,0,0),
#         rotation=(0,0,0),
#         color=color.rgb(255,235,200)
#         )
#
# flashlight.fov = 55
# flashlight.range = 18
# flashlight.enabled = True

player_spawn = bunker.find("**/PlayerSpawn")

player = None

if not player_spawn.isEmpty():
    player_spawn_cord = player_spawn.getPos(render)
    player = Ursula(position_ref=player_spawn_cord)
    print(f"Plyer status position: {player.position}")


#cockroach = Cockroach(player_ref=player, position_ref=(0,0,-5)) 

def input(key):
    if key == 'r':
        player.manualRack()

    if key == 'p':
        print(f"Position player status: {player.position}")

    if key == 'q':
        print("Mag change")
        player.changeMagazine()

    if key == 'c':
        print("Check chamber")
        player.checkChumber()

    if key == 'right mouse down':
        player.aim()

    if key == 'x':
        player.checkMagazine()

    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=20)
        player.shoot()

        if(hit_info.hit):
            print(f"Hit the: {hit_info.entity}")

            if hasattr(hit_info.entity, 'take_damage'):
                hit_info.entity.take_damage(1)

app.run()
