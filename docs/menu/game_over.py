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

