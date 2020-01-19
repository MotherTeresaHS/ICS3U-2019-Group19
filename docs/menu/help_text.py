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
