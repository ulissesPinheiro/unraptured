from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from models.cockroach import Cockroach
from models.ursula import Ursula
from models.makarov_magazine import MakarovMagazine
from game_manager import GameManager
from ps1_render import PS1Renderer

app = Ursina()

window.borderless = True
window.fullscreen = True
window.vsync = True


window.color = color.gray
scene.fog_color = color.black
scene.fog_density = 0.12

AmbientLight(color=color.rgba(0.3,0.3,0.3,255))

ps1 = PS1Renderer(
        width = 320,
        height = 180
        )

sewer = Entity(
    model="assets/models/maps/sewer.glb",
    position=(0, 0, 0),
    scale=1,
    collider="mesh",
)

game = GameManager()

flashlight = SpotLight(
        parent=camera,
        position=(0,0,0),
        rotation=(0,0,0),
        color=color.rgb(255,235,200)
        )

flashlight.fov = 55
flashlight.range = 18
flashlight.enabled = True
render.setShaderAuto()

player_spawn = sewer.find("**/PlayerSpawn")

if player_spawn.isEmpty():
    raise RuntimeError("No spawn point")

player = Ursula(position_ref=player_spawn.getPos(render))

player.on_hurt = game.on_player_hurt
player.on_death = game.on_player_death

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

    if key == "e":
        player.interact()

    if key == "right mouse down":
        player.aim()

    if key == "left mouse down":
        player.shoot()
    if key == "f1":
        ps1.toggle()
    if key == "f2":
       PS1Renderer.debug_regions() 
    
app.run()
