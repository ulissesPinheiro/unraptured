from enum import Enum, auto

from ursina import *
from direct.actor.Actor import Actor
from models.base.gun_fire import GunFire
from panda3d.core import AmbientLight as PandaAmbientLight


DAMAGE = 5
RANGE = 20
MODEL = "assets/models/makarov.glb"
FALLBACK_DURATION = 0.3  


class GunState(Enum):
    IDLE = auto()
    AIM_IN = auto()
    AIMING = auto()
    AIM_OUT = auto()
    SHOOTING = auto()
    RACKING = auto()
    RELOADING = auto()
    INSPECTING = auto()


STATES = {
    GunState.IDLE:       dict(anim="idle",           loop=True,  next=None),
    GunState.AIM_IN:     dict(anim="aim",            loop=False, next=GunState.AIMING),
    GunState.AIMING:     dict(anim=None,             loop=False, next=None),
    GunState.AIM_OUT:    dict(anim="aim",            loop=False, next=GunState.IDLE, reverse=True),
    GunState.SHOOTING:   dict(anim="shoot",          loop=False, next=GunState.AIMING),
    GunState.RACKING:    dict(anim="rack",           loop=False, next=GunState.IDLE),
    GunState.RELOADING:  dict(anim="change_magazine",loop=False, next=GunState.IDLE),
    GunState.INSPECTING: dict(anim=None,             loop=False, next=GunState.IDLE),
}


ALLOWED = {
    "aim":     {GunState.IDLE},
    "unaim":   {GunState.AIMING},
    "shoot":   {GunState.AIMING},
    "rack":    {GunState.IDLE},
    "reload":  {GunState.IDLE},
    "inspect": {GunState.IDLE},
}

AIM_STATES = {GunState.AIM_IN, GunState.AIMING, GunState.SHOOTING}


class Makarov(GunFire):
    def __init__(self, magazine):
        super().__init__(magazine=magazine)
        self.name = "Makarov"
        self.damage = DAMAGE

        self.actor = Actor(MODEL)
        self.actor.reparentTo(camera)
        self.actor.setShaderOff(1)

        self.state = None
        self.state_timer = 0.0
        self.change_state(GunState.IDLE)
        
        gun_light = PandaAmbientLight("gun_light")
        gun_light.setColor((0.35, 0.33, 0.30, 1))
        gun_light_np = self.actor.attachNewNode(gun_light)
        self.actor.setLight(gun_light_np)


    def can(self, action):
        return self.state in ALLOWED[action]

    @property
    def aim_mode(self):
        return self.state in AIM_STATES

    def change_state(self, new_state, anim_override=None):
        self._exit_state(self.state)
        self.state = new_state
        self._enter_state(new_state, anim_override)

    def _enter_state(self, state, anim_override=None):
        cfg = STATES[state]
        anim = anim_override or cfg["anim"]

        if state == GunState.AIMING:
            frames = self.actor.getNumFrames("aim")
            if frames:
                self.actor.pose("aim", frames - 1)
            self.state_timer = 0.0
            return

        if anim is None:
            self.state_timer = FALLBACK_DURATION
            return

        if cfg["loop"]:
            self.actor.loop(anim)
            self.state_timer = 0.0
            return

        if cfg.get("reverse"):
            self.actor.setPlayRate(-1.0, anim)
        self.actor.play(anim)
        self.state_timer = self._duration(anim)

    def _exit_state(self, state):
        if state == GunState.AIM_OUT:
            self.actor.setPlayRate(1.0, "aim")

    def _duration(self, anim):
        d = self.actor.getDuration(anim)
        return d if d else FALLBACK_DURATION

    def update(self):
        nxt = STATES[self.state]["next"]
        if nxt is None:
            return

        self.state_timer -= time.dt
        if self.state_timer <= 0:
            self.change_state(nxt)

    def aim(self):
        if self.can("aim"):
            self.change_state(GunState.AIM_IN)
        elif self.can("unaim"):
            self.change_state(GunState.AIM_OUT)

    def shoot(self, ignore=()):
        if not self.can("shoot"):
            return None

        if not GunFire.shoot(self):
            print("*click* câmara vazia")
            return None

        self.change_state(GunState.SHOOTING)

        hit = raycast(camera.world_position, camera.forward,
                      distance=RANGE, ignore=ignore)
        if hit.hit and hasattr(hit.entity, "take_damage"):
            hit.entity.take_damage(self.damage)
        return hit

    def rack(self):
        if not self.can("rack"):
            return False
        GunFire.rack(self)
        self.change_state(GunState.RACKING)
        return True

    def changeMagazine(self, magazine):
        if not self.can("reload"):
            return False
        GunFire.addMagazine(self, magazine=magazine)
        self.change_state(GunState.RELOADING)
        return True

    def removeMagazine(self):
        return GunFire.removeMagazine(self)

    def checkChumber(self):
        if not self.can("inspect"):
            return False
        GunFire.printHasBulletChamber(self)
        self.change_state(GunState.INSPECTING, anim_override="chamber")
        return True

    def checkMagazine(self):
        if not self.can("inspect"):
            return False
        GunFire.printQuantityMagazine(self)
        self.change_state(GunState.INSPECTING, anim_override="check_magazine")
        return True

    def idle(self):
        self.change_state(GunState.IDLE)
