from models.enemy import Enemy
from ursina import *
from direct.actor.Actor import Actor
import time as pytime

MODEL = "assets/models/cockroach.glb"
DISTANCE_SIGH = 3
SPEED = 1
DAMAGE = 1
MAX_HP = 1

class Cockroach(Entity, char):
    def __init__(self, player_ref, position_ref, model_ref=MODEL):
        super().__init__(
                         player_ref, 
                         position=position_ref,
                         model_ref=None
                         )

        self.actor = Actor(MODEL) 
        self.actor.reparentTo(self)
        self.player = player_ref
        self.distance_sigh = DISTANCE_SIGH
        self.speed = SPEED
        self.hp = MAX_HP 
        self.attack_damage = DAMAGE

        try:
           self.actor.loop('idle') 
        except Exception as e:
            print(f'Aviso de animacao: {e}')

    def update(self):
        if self.hp <= 0:
            return

        dist = distance_xz(self.position, self.player.position)

        if dist < self.distance_sigh and dist >= 1.0:
            self.look_at_2d(self.player.position, axis='y')
            self.position += self.forward * self.speed * time.dt
            
            if self.actor.getCurrentAnim() != 'walk':
                try:
                    self.actor.loop('walk')
                except:
                    pass
            elif dist > self.distance_sigh:
                if self.actor.getCurrentAnim() != 'idle':
                    try:
                        self.actor.loop('idle')
                    except:
                        pass

    def take_damage(self, amount):
        self.hp -= amount

        print(f"Enemy take damage! HP actual: {self.hp}")

        if self.hp <= 0:
            print("Enemy die")
            
            try:
                self.actor.play('death')
            except:
                pass

            self.collider = None
            destroy(self, delay=5.0)


