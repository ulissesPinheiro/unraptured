from panda3d.core import Texture as PandaTexture, CardMaker, NodePath, Camera, OrthographicLens
from ursina import *


SCREEN_SORT = 5

class PS1Renderer:

    def __init__(self, width=320, height=180, clear_color=color.gray):
        self.width = width
        self.height = height

        self.texture = PandaTexture() 
        self.texture.setName("ps1_texture")

        self.texture.setMinfilter(PandaTexture.FTNearest)
        self.texture.setMagfilter(PandaTexture.FTNearest)


        self.buffer = base.win.makeTextureBuffer(
            "ps1_buffer",
            width,
            height,
            self.texture
        )

        if self.buffer is None:
            raise RuntimeError("Não foi possível criar o framebuffer PS1.")

        self.buffer.setClearColor(clear_color)

        self.low_res_camera = base.makeCamera(
            self.buffer,
            scene=render
        )

        self.low_res_camera.node().setLens(
            base.cam.node().getLens()
        )

        self.low_res_camera.reparentTo(base.cam)
        self.low_res_camera.setPos(0, 0, 0)
        self.low_res_camera.setHpr(0, 0, 0)

        
        self.screen_root = NodePath("ps1_screen_root") 
        self.screen_root.setDepthTest(False)
        self.screen_root.setDepthWrite(False)

        lens = OrthographicLens()
        lens.setFilmSize(2, 2)

        lens.setNearFar(-10, 10)

        screen_cam_node = Camera("ps1_screen_cam")
        screen_cam_node.setLens(lens)
        self.screen_cam = self.screen_root.attachNewNode(screen_cam_node)


        self.display_region = base.win.makeDisplayRegion()
        self.display_region.setSort(SCREEN_SORT)
        self.display_region.setCamera(self.screen_cam)

        card = CardMaker("ps1_screen")
        card.setFrame(-1, 1, -1, 1)
        self.screen = self.screen_root.attachNewNode(card.generate())
        self.screen.setTexture(self.texture)


        self.enabled = False
        self.set_enabled(True)

    def set_enabled(self, on):
        self.enabled = on
        base.camNode.setActive(not on)
        self.low_res_camera.node().setActive(on)
        self.buffer.setActive(on)
        self.display_region.setActive(on)

    def toggle(self):
        self.set_enabled(not self.enabled)

    def debug_regions():
        regions = sorted(base.win.getDisplayRegions(), key=lambda r: r.getSort())

        for r in regions:
            cam = r.getCamera()
            name = cam.getName() if not cam.isEmpty() else "(Withou camera)"
            print(f"sort={r.getSort():>3} ativa={r.isActive()} camera={name}")
