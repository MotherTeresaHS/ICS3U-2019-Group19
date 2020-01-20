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

volume = 0
score = 0
number_of_missiles = 10


def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

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

    global volume

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile:
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
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

    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    # get sound ready
    # follow this guide to convert your other sounds to something
    #   that will work https://learn.adafruit.com/microcontroller-
    #       compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    if volume % 2 == 0:
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
    # this function is the main menu scene
    global score
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
    # this function is the help scene

    global volume

    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    image_bank_3 = stage.Bank.from_bmp16("avoid_or_shoot.bmp")

    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

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
    text4.move(20, 70)
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

    box = []

    check_box = stage.Sprite(image_bank_3, 4, 130, 60)
    box.append(check_box)

    border = []

    box_border = stage.Sprite(image_bank_3, 13, 130, 60)
    border.append(box_border)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + border + box + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_O != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        if b_button == constants.button_state["button_just_pressed"]:
            if keys & ugame.K_O != 0:
                volume += 1
        if volume % 2 == 1:
            check_box.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        else:
            check_box.move(130, 60)

        if keys & ugame.K_START != 0:
            selection_scene()

        game.render_sprites(box)
        game.tick()


def selection_scene():
    # this function is the air plane selection scene

    global volume

    image_bank_3 = stage.Bank.from_bmp16("avoid_or_shoot.bmp")

    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = 1
            background.tile(x_location, y_location, tile_picked)

    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    text = []

    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("PLANE SELECTION")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(15, 100)
    text2.text("SELECT:GAME START")
    text.append(text2)

    sprites = []

    plane1 = stage.Sprite(image_bank_3, 6, int(constants.SCREEN_X / 4),
                          int(constants.SCREEN_Y / 4))
    sprites.append(plane1)

    plane2 = stage.Sprite(image_bank_3, 7, int(constants.SCREEN_X / 4),
                          int(constants.SCREEN_Y * 3 / 4 -
                              constants.SPRITE_SIZE))
    sprites.append(plane2)

    plane3 = stage.Sprite(image_bank_3, 8, int(constants.SCREEN_X * 3 / 4 -
                          constants.SPRITE_SIZE), int(constants.SCREEN_Y / 4))
    sprites.append(plane3)

    plane4 = stage.Sprite(image_bank_3, 9, int(constants.SCREEN_X * 3 / 4 -
                          constants.SPRITE_SIZE), int(constants.SCREEN_Y * 3 /
                          4 - constants.SPRITE_SIZE))
    sprites.append(plane4)

    select_box = []

    select_box1 = stage.Sprite(image_bank_3, 13, int(constants.SCREEN_X / 4),
                               int(constants.SCREEN_Y / 4))
    select_box.append(select_box1)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = select_box + sprites + text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:
            if select_box1.y != constants.SCREEN_Y / 4:
                select_box1.move(int(select_box1.x),
                                 int(constants.SCREEN_Y / 4))
            else:
                pass
            pass
        if keys & ugame.K_DOWN != 0:
            if select_box1.y != (constants.SCREEN_Y * 3 / 4 -
                                 constants.SPRITE_SIZE):
                select_box1.move(int(select_box1.x),
                                 int(constants.SCREEN_Y * 3 / 4 -
                                     constants.SPRITE_SIZE))
            else:
                pass
            pass
        if keys & ugame.K_LEFT != 0:
            if select_box1.x != constants.SCREEN_X / 4:
                select_box1.move(int(constants.SCREEN_X / 4),
                                 int(select_box1.y))
            else:
                pass
            pass
        if keys & ugame.K_RIGHT != 0:
            if select_box1.x != (constants.SCREEN_X * 3 / 4 -
                                 constants.SPRITE_SIZE):
                select_box1.move(int(constants.SCREEN_X * 3 / 4 -
                                     constants.SPRITE_SIZE),
                                 int(select_box1.y))
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
            if volume % 2 == 0:
                sound.play(coin_sound)
            game_scene(plane_info)

        game.render_sprites(select_box + sprites)
        game.tick()


def game_scene(plane_number):
    # this function is the game scene

    global score
    global volume
    global number_of_missiles

    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    image_bank_3 = stage.Bank.from_bmp16("avoid_or_shoot.bmp")

    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    for y_location in range(constants.SCREEN_GRID_Y):
        for x_location in range(constants.SCREEN_GRID_X):
            if y_location == 1:
                tile_picked = random.randint(1, 3)
            else:
                tile_picked = random.randint(1, 1)
            background.tile(x_location, y_location, tile_picked)

    birds_sound = open("bird.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    bomb_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    shot_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    def show_flying():
        enemy_picked = random.randint(0, 1)
        if enemy_picked == 0:
            if bird.y < 0:
                bird.move(200, random.randint(0 + constants.SPRITE_SIZE,
                                              constants.SCREEN_Y -
                                              constants.SPRITE_SIZE))
        else:
            if enemy.y < 0:
                enemy.move(200, random.randint(0 + constants.SPRITE_SIZE,
                                               constants.SCREEN_Y -
                                               constants.SPRITE_SIZE))

    def show_missile():
        if loaded_missile. y < 0:
            loaded_missile.move(random.randint(200, 500),
                                random.randint(0 + constants.SPRITE_SIZE,
                                constants.SCREEN_Y - constants.SPRITE_SIZE))

    text = []

    score_text = stage.Text(width=29, height=14, font=None,
                            palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score:{0}".format(score))
    text.append(score_text)

    missile_text = stage.Text(width=29, height=14, font=None,
                              palette=constants.SCORE_PALETTE, buffer=None)
    missile_text.clear()
    missile_text.cursor(0, 0)
    missile_text.move(1, 10)
    missile_text.text("Missile:{0}".format(number_of_missiles))
    text.append(missile_text)

    sprites = []

    plane = stage.Sprite(image_bank_3, int(plane_number), 2,
                         int(constants.SCREEN_Y / 2))
    sprites.append(plane)

    missiles = []

    for missile_number in range(constants.TOTAL_NUMBER_OF_MISSILES):
        missile = stage.Sprite(image_bank_3, 12, constants.OFF_SCREEN_X,
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

    loaded_missiles = []
    loaded_missile = stage.Sprite(image_bank_3, 11, constants.OFF_SCREEN_X,
                                  constants.OFF_SCREEN_Y)
    loaded_missiles.append(loaded_missile)

    show_flying()
    show_missile()

    game = stage.Stage(ugame.display, constants.FPS)
    # set the background layer
    game.layers = (text + sprites + enemies + birds + missiles +
                   loaded_missiles + [background])
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

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

        # shot the missile
        if a_button == constants.button_state["button_just_pressed"]:
            if number_of_missiles > 0:
                for missile_number in range(len(missiles)):
                    if missiles[missile_number].y < 0:
                        missiles[missile_number].move(plane.x, plane.y)
                        number_of_missiles = number_of_missiles - 1
                        missile_text.clear()
                        missile_text.cursor(0, 0)
                        missile_text.move(1, 10)
                        missile_text.text("Missile:{0}"
                                          .format(number_of_missiles))
                        game.render_block()
                        if volume % 2 == 0:
                            sound.stop()
                            sound.play(shot_sound)
                        break

        # missiles move to right
        for missile_number in range(len(missiles)):
            if missiles[missile_number].y > 0:
                missiles[missile_number].move(missiles[missile_number].x +
                                              constants.MISSLE_SPEED,
                                              missiles[missile_number].y)
                if missiles[missile_number].x > constants.SCREEN_X:
                    missiles[missile_number].move(constants.OFF_SCREEN_X,
                                                  constants.OFF_SCREEN_Y)

        # move user's plane with d-pad
        if keys & ugame.K_UP != 0:
            if plane.y < 0:
                plane.move(plane.x, 0)
            else:
                plane.move(plane.x, plane.y - 2)
            pass
        if keys & ugame.K_DOWN != 0:
            if plane.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
                plane.move(plane.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
            else:
                plane.move(plane.x, plane.y + 2)
            pass

        # flying move left
        if bird.y > 0:
            # level
            if score <= 10:
                bird.move(bird.x - constants.BIRD_LEVEL_1, bird.y)
            elif score > 10 and score <= 30:
                bird.move(bird.x - constants.BIRD_LEVEL_2, bird.y)
            else:
                bird.move(bird.x - constants.BIRD_LEVEL_3, bird.y)

            if bird.x < constants.OFF_SCREEN_X:
                bird.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                show_flying()
                score += 1
                score_text.clear()
                score_text.cursor(0, 0)
                score_text.move(1, 1)
                score_text.text("Score:{0}".format(score))
                game.render_block()
        elif enemy.y > 0:
            # level
            if score <= 10:
                enemy.move(enemy.x - constants.ENEMY_LEVEL_1, enemy.y)
            elif score > 10 and score <= 30:
                enemy.move(enemy.x - constants.ENEMY_LEVEL_2, enemy.y)
            else:
                enemy.move(enemy.x - constants.ENEMY_LEVEL_3, enemy.y)

            if enemy.x < constants.OFF_SCREEN_X:
                enemy.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                show_flying()
                if score > 1:
                    score -= 2
                elif score == 1:
                    score -= 1
                score_text.clear()
                score_text.cursor(0, 0)
                score_text.move(1, 1)
                score_text.text("Score:{0}".format(score))
                game.render_block()

        # loaded missile move left
        if loaded_missile.y > 0:
            loaded_missile.move(loaded_missile.x - 1, loaded_missile.y)
            if loaded_missile.x < constants.OFF_SCREEN_X:
                loaded_missile.move(constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
                show_missile()

        # if the missile hit the flying thing
        for missile_number in range(len(missiles)):
            if missiles[missile_number].x > 0:
                if bird.x > 0:
                    if stage.collide(missiles[missile_number].x,
                                     missiles[missile_number].y,
                                     missiles[missile_number].x + 16,
                                     missiles[missile_number].y + 16,
                                     bird.x, bird.y, bird.x + 16, bird.y + 16):
                        # you hit an bird
                        bird.move(constants.OFF_SCREEN_X,
                                  constants.OFF_SCREEN_Y)
                        missiles[missile_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                        show_flying()
                        if score > 2:
                            score -= 3
                        elif score == 2:
                            score -= 2
                        elif score == 1:
                            score -= 1
                        score_text.clear()
                        score_text.cursor(0, 0)
                        score_text.move(1, 1)
                        score_text.text("Score:{0}".format(score))
                        game.render_block()
                        if volume % 2 == 0:
                            sound.stop()
                            sound.play(birds_sound)
                elif enemy.x > 0:
                    if stage.collide(missiles[missile_number].x + 7,
                                     missiles[missile_number].y + 7,
                                     missiles[missile_number].x + 8,
                                     missiles[missile_number].y + 8,
                                     enemy.x, enemy.y, enemy.x + 16,
                                     enemy.y + 16):
                        # missile hit an plane
                        enemy.move(constants.OFF_SCREEN_X,
                                   constants.OFF_SCREEN_Y)
                        missiles[missile_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                        show_flying()
                        score += 2
                        score_text.clear()
                        score_text.cursor(0, 0)
                        score_text.move(1, 1)
                        score_text.text("Score:{0}".format(score))
                        game.render_block()
                        if volume % 2 == 0:
                            sound.stop()
                            sound.play(bomb_sound)

        # user hit the flying thing
        if bird.x > 0:
            if stage.collide(bird.x, bird.y, bird.x + 10, bird.y + 10,
                             plane.x, plane.y, plane.x + 10, plane.y + 10):
                if volume % 2 == 0:
                    sound.stop()
                    sound.play(bomb_sound)
                    time.sleep(2.0)
                else:
                    time.sleep(1.0)
                cause = 0
                game_over_scene(score, cause)
        elif enemy.x > 0:
            if stage.collide(enemy.x, enemy.y, enemy.x + 12, enemy.y + 12,
                             plane.x, plane.y, plane.x + 12, plane.y + 12):
                if volume % 2 == 0:
                    sound.stop()
                    sound.play(bomb_sound)
                    time.sleep(4.0)
                else:
                    time.sleep(1.0)
                cause = 1
                game_over_scene(score, cause)

        # loaded missile hit the plane
        if loaded_missile.x > 0:
            if stage.collide(loaded_missile.x + 1, loaded_missile.y,
                             loaded_missile.x + 15, loaded_missile.y + 15,
                             plane.x, plane.y, plane.x + 15, plane.y + 15):
                number_of_missiles += 3
                missile_text.clear()
                missile_text.cursor(0, 0)
                missile_text.move(1, 10)
                missile_text.text("Missile:{0}".format(number_of_missiles))
                game.render_block()
                if volume % 2 == 0:
                    sound.stop()
                    sound.play(coin_sound)
                loaded_missile.move(constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
                show_missile()

        # redraw sprite list
        game.render_sprites(sprites + birds + enemies + missiles +
                            loaded_missiles)
        game.tick()


def game_over_scene(final_score, cause):
    # this function is the game over scene

    global score
    global number_of_missiles

    image_bank_3 = stage.Bank.from_bmp16("avoid_or_shoot.bmp")

    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    text = []

    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(45, 30)
    text1.text("GAME OVER")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(50, 50)
    text2.text("Score:{0}".format(final_score))
    text.append(text2)

    if cause == 0:
        text3 = stage.Text(width=29, height=14, font=None,
                           palette=constants.MT_GAME_STUDIO_PALETTE,
                           buffer=None)
        text3.move(12, 80)
        text3.text("YOU HIT THE BIRD!")
        text.append(text3)
    else:
        text3 = stage.Text(width=29, height=14, font=None,
                           palette=constants.MT_GAME_STUDIO_PALETTE,
                           buffer=None)
        text3.move(10, 80)
        text3.text("YOU HIT THE PLANE!")
        text.append(text3)

    text4 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text4.move(40, 100)
    text4.text("MENU:[A]")
    text.append(text4)

    game = stage.Stage(ugame.display, constants.FPS)
    # set the background layer
    game.layers = text + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X != 0:
            score = 0
            number_of_missiles = 10
            main_menu_scene()

        game.tick()


if __name__ == "__main__":
    blank_white_reset_scene()
