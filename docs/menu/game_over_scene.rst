.. _game_over_scene:

Game Over Scene
===============

T

.. code-block:: python
        :linenos:
        
        def game_over_scene(final_score, cause):


You get the score of game and cause.

.. code-block:: python
        :linenos:
        
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


The score and cause put on the screen.
