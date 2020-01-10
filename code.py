#!/usr/bin/env python3

# Created by: Jaeyoon(Jay) Lee
# Created on: Jan 2019
# This file is the Avoid or Shoot game
#   for CircuitPython

import ugame
import stage
import board
import time
import random

import constants

sound = 0
score = 0


def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # set up the NeoPixels
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    pixels.deinit()

    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        time.sleep(0.5)
        mt_splash_scene()


def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        time.sleep(1.0)
        main_menu_scene()


def main_menu_scene():
    image_bank_2 = stage.Bank.from_bmp16("avoid_title.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile:
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 0)

    background.tile(2, 3, 0)
    background.tile(3, 3, 4)
    background.tile(4, 3, 5)
    background.tile(5, 3, 6)
    background.tile(6, 3, 0)

    background.tile(2, 4, 0)
    background.tile(3, 4, 7)
    background.tile(4, 4, 8)
    background.tile(5, 4, 9)
    background.tile(6, 4, 0)

    # a list of sprites
    sprites = []

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(35, 100)
    text1.text("START:START")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("HELP:SELECT")
    text.append(text2)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            selection_scene()
        elif keys & ugame.K_SELECT != 0:
            help_scene()

        game.tick()


def help_scene():
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []
    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(35, 10)
    text1.text("HOW TO PLAY")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(20, 30)
    text2.text("Use D-Pad to fly")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text3.move(40, 40)
    text3.text("SHOOT [A]")
    text.append(text3)

    text4 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text4.move(40, 70)
    text4.text("SOUND [B]")
    text.append(text4)

    text5 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text5.move(35, 80)
    text5.text("START:START")
    text.append(text5)

    text6 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text6.move(25, 100)
    text6.text("CREATED BY JAY")
    text.append(text6)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            selection_scene()

        game.tick()


def selection_scene():
    # this function is the air plane selection scene
    image_bank_3 = stage.Bank.from_bmp16("avoid_or_shoot.bmp")

    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 1)
            background.tile(x_location, y_location, tile_picked)

    text = []

    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("PLANE SELECTION")
    text.append(text1)

    sprites = []

    plane1 = stage.Sprite(image_bank_3, 6, int(constants.SCREEN_X / 4),
                        int(constants.SCREEN_Y / 4))
    sprites.append(plane1)

    plane2 = stage.Sprite(image_bank_3, 7, int(constants.SCREEN_X / 4),
                        int(constants.SCREEN_Y * 3 / 4))
    sprites.append(plane2)

    plane3 = stage.Sprite(image_bank_3, 8, int(constants.SCREEN_X * 3 / 4),
                        int(constants.SCREEN_Y / 4))
    sprites.append(plane3)

    plane4 = stage.Sprite(image_bank_3, 9, int(constants.SCREEN_X * 3 / 4),
                        int(constants.SCREEN_Y * 3 / 4))
    sprites.append(plane4)

    select_box = []

    select_box1 = stage.Sprite(image_bank_3, 13, int(constants.SCREEN_X / 4),
                        int(constants.SCREEN_Y / 4))
    select_box.append(select_box1)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = select_box + sprites + text + [background]
    game.render_block()

    time.sleep(1.0)
    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:
            if select_box1.y != constants.SCREEN_Y / 4:
                select_box1.move(int(select_box1.x), int(constants.SCREEN_Y / 4))
            else:
                pass
            pass
        if keys & ugame.K_DOWN != 0:
            if select_box1.y != constants.SCREEN_Y * 3 / 4:
                select_box1.move(int(select_box1.x), int(constants.SCREEN_Y * 3 / 4))
            else:
                pass
            pass
        if keys & ugame.K_LEFT != 0:
            if select_box1.x != constants.SCREEN_X / 4:
                select_box1.move(int(constants.SCREEN_X / 4), int(select_box1.y))
            else:
                pass
            pass
        if keys & ugame.K_RIGHT != 0:
            if select_box1.x != constants.SCREEN_X * 3 / 4:
                select_box1.move(int(constants.SCREEN_X * 3 / 4), int(select_box1.y))
            else:
                pass
            pass
        if keys & ugame.K_SELECT != 0:
            if select_box1.x == plane1.x and select_box1.y == plane1.y:
                plane_info = 6
            elif select_box1.x == plane2.x and select_box1.y == plane2.y:
                plane_info = 7
            elif select_box1.x == plane3.x and select_box1.y == plane3.y:
                plane_info = 8
            else:
                plane_info = 9
            game_scene(plane_info)

        game.render_sprites(select_box + sprites)
        game.tick()


def game_scene(plane):
    # this function is the game scene
    
    global score
    
    image_bank_3 = stage.Bank.from_bmp16("avoid_or_shoot.bmp")

    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    for y_location in range(constants.SCREEN_GRID_Y):
        for x_location in range(constants.SCREEN_GRID_X):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    text = []

    score_text = stage.Text(width=29, height=14, font=None,
                            palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))
    text.append(score_text)
    
    missile_text = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    missile_text.clear()
    missile_text.cursor(0, 0)
    missile_text.move(0, 10)
    missile_text.text("Missile {0}".format(constants.TOTAL_NUMBER_OF_MISSILES))
    text.append(missile_text)
    
    sprites = []
    
    plane = stage.Sprite(image_bank_3, int(plane), int(constants.SCREEN_X / 2),
                        int(constants.SCREEN_Y -
                        constants.SPRITE_SIZE))
    sprites.append(plane)
    
    missiles = []
    
    for missile_number in range(constants.TOTAL_NUMBER_OF_MISSILES):
        missile = stage.Sprite(image_bank_3, 13, constants.OFF_SCREEN_X,
                               constants.OFF_SCREEN_Y)
        missiles.append(missile)

    birds = []

    bird = stage.Sprite(image_bank_3, 5, constants.OFF_SCREEN_X,
                        constants.OFF_SCREEN_Y)
    birds.append(bird)
    
    enemies = []

    enemy = stage.Sprite(image_bank_3, 10, constants.OFF_SCREEN_X,
                        constants.OFF_SCREEN_Y)
    enemies.append(enemy)
    
    game = stage.Stage(ugame.display, constants.FPS)
    # set the background layer
    game.layers = sprites + text + enemies + birds + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()


    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # print(keys)
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_UP != 0:
            if plane.y < 0:
                plane.move(plane.x, 0)
            else:
                plane.move(plane.x, plane.y - 1)
            pass
        if keys & ugame.K_DOWN != 0:
            if plane.y > constants.SCREEN_Y - constants.SCREEN_GRID_Y:
                plane.move(plane.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
            else:
                plane.move(plane.x, plane.y + 1)
            pass

        # update game logic
        if a_button == constants.button_state["button_just_pressed"]:
            for missile_number in range(len(missiles)):
                if missiles[missile_number].x < 0:
                    missiles[missile_number].move(plane.x, plane.y)
                    break

        # redraw sprite list
        game.render_sprites(sprites + missiles + birds)
        game.tick()


def game_over_scene(final_score):
    # this function is the game over scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


if __name__ == "__main__":
    game_scene(10)
