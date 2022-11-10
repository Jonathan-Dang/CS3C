import pygame
import random
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#==============================================================#
#   Class Object Documentations
#==============================================================#
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
            #Line below essentially converts the png to mask the surface, allowing us to
            #use it as an asset
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        
    def update(self, pressed_keys : dict):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        #If block below is one of the versions of boundaries so that the player
        # can't fly off the screen.
        #I liked this approach better because I think it looks cleaner.
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
#==============================================================#



#==============================================================#
#   Screen Size Constants
#==============================================================#
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#==============================================================#



#==============================================================#
#   Music and Sounds
#==============================================================#
pygame.mixer.init()
# Load and play background music
# Sound source: http://ccmixter.org/files/airtone/64531
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("airtone_-_ennui.mp3")
pygame.mixer.music.play(loops=-1)
# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("pygame-a-primer_Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("pygame-a-primer_Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("pygame-a-primer_Collision.ogg")
#==============================================================#



#==============================================================#
#   Initialize the game
#==============================================================#
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
#==============================================================#



#==============================================================#
#   NEW USEREVENTS
#==============================================================#
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
#==============================================================#



#==============================================================#
#   Sprites and Entities
#==============================================================#
player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
#==============================================================#



#==============================================================#
#   Event Manager
#==============================================================#
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
    
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys= pressed_keys)
    
    enemies.update()
    clouds.update()
            
    screen.fill((135, 206, 250))
    
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        running = False
    
    pygame.display.flip()
    clock.tick(30)
#==============================================================#



#==============================================================#
#   QUITTING
#==============================================================#
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
#==============================================================#