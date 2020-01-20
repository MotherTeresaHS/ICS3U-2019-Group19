.. _selection:

Plane Selection
==========

sprites can be placed in front of the background. xxx

.. code-block:: python
        :linenos:

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


As soon as you save the file onto the PyBadge, the screen should flash and you should see something like:

.. figure:: ./images/select_plane.GIF
   :width: 480 px
   :alt: Plane Selection
   :align: center

   Plane Selection

This code will not work. The code above has a lot to do. Here is a better version that shows the background. You can see that you called the :py:func:`main()` function. This is common in python code but usually not visible in CircuitPython. I am including it because by breaking the code into different functions to match different scenes, eventually will be really helpful.


Now, you can move a plane in front of your background on your PyBadge.
    

