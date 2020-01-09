#!/usr/bin/env python3

# Created by: Jaeyoon(Jay) Lee
# Created on: Jan 2019
# This file is the Avoid or Shoot game
#   for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random

import constants

sound = 0


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
    image_bank_1 = stage.Bank.from_bmp16("avoid_shoot.bmp")

    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
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

    plane1 = stage.Sprite(image_bank_1, 6, int(constants.SCREEN_X / 4),
                        int(constants.SCREEN_Y / 4))
    sprites.append(plane1)

    plane2 = stage.Sprite(image_bank_1, 7, int(constants.SCREEN_X / 4),
                        int(constants.SCREEN_Y * 3 / 4))
    sprites.append(plane2)

    plane3 = stage.Sprite(image_bank_1, 8, int(constants.SCREEN_X * 3 / 4),
                        int(constants.SCREEN_Y / 4))
    sprites.append(plane3)

    plane4 = stage.Sprite(image_bank_1, 9, int(constants.SCREEN_X * 3 / 4),
                        int(constants.SCREEN_Y * 3 / 4))
    sprites.append(plane4)

    select_box = []

    select_box1 = stage.Sprite(image_bank_1, 13, int(constants.SCREEN_X / 4),
                        int(constants.SCREEN_Y / 4))
    sprites.append(select_box1)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = select_box + sprites + text + [background]
    game.render_block()

    time.sleep(1.0)
    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:
            if select_box1.y = constants.SCREEN_Y / 4:
                pass
            else:
                select_box1.move(select_box1.x, constants.SCREEN_Y / 4)
            pass
        if keys & ugame.K_DOWN != 0:
            if select_box1.y = constants.SCREEN_Y * 3 / 4:
                pass
            else:
                select_box1.move(select_box1.x, constants.SCREEN_Y * 3 / 4)
            pass
        if keys & ugame.K_LEFT != 0:
            if select_box1.x = constants.SCREEN_X * 3 / 4:
                pass
            else:
                select_box1.move(constants.SCREEN_X * 3 / 4, select_box1.y)
            pass
        if keys & ugame.K_RIGHT != 0:
            if select_box1.x = constants.SCREEN_X / 4:
                pass
            else:
                select_box1.move(constants.SCREEN_X / 4, select_box1.y)
            pass
        if keys & ugame.K_SELECT != 0:
            if select_box1.x = plane1.x and select_box1.y = plane1.y:
                plane_info = 1
            elif select_box1.x = plane2.x and select_box1.y = plane2.y:
                plane_info = 2
            elif select_box1.x = plane3.x and select_box1.y = plane3.y:
                plane_info = 3
            elif select_box1.x = plane4.x and select_box1.y = plane4.y:
                plane_info = 4
        if keys & ugame.K_START != 0:
            game_scene(plane_info)

        game.tick()


def game_scene(plane):
    # this function is the game scene
    # this function is the game scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


def game_over_scene(final_score):
    # this function is the game over scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


if __name__ == "__main__":
    blank_white_reset_scene()
