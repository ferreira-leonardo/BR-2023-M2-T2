import pygame
import os

# Global Constants
TITLE = "Goat Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_GRAY = (173, 211, 232)

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraRun1.png"))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

DINO_START = pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraRun1.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraShield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraRun2.png")),
]

RUNNING_FIRE = [
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraFire.png")),
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraFire2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraJumpShield.png"))
JUMPING_FIRE = pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraFire.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraJump.png")),
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraJump.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraJumpShield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraJumpShield.png")),
]

DUCKING_FIRE = [
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraFire.png")),
    pygame.image.load(os.path.join(IMG_DIR, "cabra/cabraFire2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/1b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/2b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/3b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/4b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/5b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/6b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/7b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/8b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/9b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/10b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/11b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/12b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/13b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/14b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/15b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/16b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/17b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/18b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/19b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/20b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/21b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/22b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/23b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/24b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/25b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/26b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/27b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/28b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/29b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/30b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/31b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/32b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/33b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/34b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/35b.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/36b.png"))
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
FIRE_BALL = pygame.image.load(os.path.join(IMG_DIR, 'Other/fire.png'))

FLOOR = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

LANDSCAPE1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/mountains.png'))

LANDSCAPE2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/crepusculo.png'))

PORTAL = pygame.image.load(os.path.join(IMG_DIR, 'Other/cubo.png'))

DEFAULT_TYPE = "default"

SHIELD_TYPE = "shield"

FIRE_TYPE = 'fire'

PORTAL_TYPE = 'portal'

FONT_STYLE = 'freesansbold.ttf'

#SOUNDS
pygame.mixer.init()
BACKGROUND_MUSIC = pygame.mixer.music.load(os.path.join(IMG_DIR, 'sounds/smb_over.mid'))

SOUND_POWER_UP = pygame.mixer.Sound(os.path.join(IMG_DIR, 'sounds/smw_coin.wav'))

SOUND_JUMP = pygame.mixer.Sound(os.path.join(IMG_DIR, 'sounds/smw_jump.wav'))

SOUND_SHIELD = pygame.mixer.Sound(os.path.join(IMG_DIR, 'sounds/smw_bowser_fire.wav'))

SOUND_FIRE = pygame.mixer.Sound(os.path.join(IMG_DIR, 'sounds/smw_stomp_no_damage.wav'))

SOUND_GAME_OVER = pygame.mixer.Sound(os.path.join(IMG_DIR, 'sounds/cabraDeathh.wav'))