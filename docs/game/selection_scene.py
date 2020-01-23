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

