from panda3d.core import Texture as PandaTexture, CardMaker
from ursina import *

class PS1Renderer:

    def __init__(self, width=320, height=180):
        self.width = width
        self.height = height

        self.texture = PandaTexture() 
        self.texture.setName("ps1_texture")

        self.buffer = base.win.makeTextureBuffer(
            "ps1_buffer",
            width,
            height,
            self.texture
        )

        if self.buffer is None:
            raise RuntimeError("Não foi possível criar o framebuffer PS1.")

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

        self.texture.setMinfilter(PandaTexture.FTNearest)
        self.texture.setMagfilter(PandaTexture.FTNearest)

        card = CardMaker("ps1_screen")
        card.setFrame(-1, 1, -1, 1)

        self.screen = render2d.attachNewNode(card.generate())
        self.screen.setTexture(self.texture)
        self.screen.setDepthTest(False)
        self.screen.setDepthWrite(False)
        self.screen.setBin("fixed", 100)
