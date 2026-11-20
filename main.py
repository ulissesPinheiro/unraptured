from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from models.cockroach import Cockroach
from models.ursula import Ursula
from models.makarov_magazine import MakarovMagazine

app = Ursina()

window.title = "PS1 Horror FPS - Unrapture"
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
        player.changeMagazine(magazine=MakarovMagazine())

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
