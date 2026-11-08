from ursina import *
import time as pytime

DISTANCE_SIGH = 5

class Enemy(Entity):
    def __init__(self, player_ref, position=(0,0,5)):
        super().__init__(
                model="assets/models/enemy.glb",
                scale=1,
                position=position,
                collider="box"
                )
        self.speed = 0.5 
        self.hp = 3
        self.player = player_ref

        self.attack_cooldown = 1.5
        self.last_attack_time = 0

    def update(self):

        dist = distance_xz(self.position, self.player.position)

        if dist < DISTANCE_SIGH :
            self.look_at_2d(self.player.position, axis='y')
            self.position += self.forward * self.speed * time.dt

            if dist <1.0:
                current_time = pytime.time()
                if current_time - self.last_attack_time >= self.attack_cooldown:
                    self.player.take_damage(1)
                    print("Enemy atack the player")

    def take_damage(self, ammount):
        self.hp -= ammount
        print(f"Enemy take damage! HP actual: {self.hp}")

        if self.hp <= 0:
            print("Enemy die")
            destroy(self)



