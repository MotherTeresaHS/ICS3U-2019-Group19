#!/usr/bin/env python3

# Created by: Jaeyoon Lee
# Created on: Jan 2019
# This constants file is CircuitPython Stage game

# CircuitPython screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60
TOTAL_NUMBER_OF_MISSILES = 30
TOTAL_NUMBER_OF_ENEMIES = 4
TOTAL_NUMBER_OF_BIRDS = 3
OFF_SCREEN_X = -20
OFF_SCREEN_Y = -20
MISSLE_SPEED = 2
BIRD_LEVEL_1 = 2
BIRD_LEVEL_2 = 3
BIRD_LEVEL_3 = 5
ENEMY_LEVEL_1 = 1
ENEMY_LEVEL_2 = 2
ENEMY_LEVEL_3 = 4

MT_GAME_STUDIO_PALETTE = (b'\xf8\x1f\x00\x00\xcey\x00\xff\xf8\x1f\xff\x19\xfc\xe0\xfd\xe0'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

SCORE_PALETTE = (b'\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
