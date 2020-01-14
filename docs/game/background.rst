.. _background:

Background
==========

Avoid or Shoot needs a background. This code is puts the first image in the background. The first image is 16 x 16 px image at the top. in this case the first image is white colour image. Of course when you save the file, save it as :file:`code.py` file:

.. code-block:: python
	:linenos:

	image_bank_1 = stage.Bank.from_bmp16("avoid_or_shoot.bmp")

   	background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                           	constants.SCREEN_GRID_Y)


As soon as you save the file onto the PyBadge, the screen should flash and you should see something like:

.. figure:: ./docs/game/images/white_background.png
   :width: 480 px
   :alt: White background
   :align: center

   Background on PyBadge

Although this code does work just as is, it is always nice to ensure we are following proper coding conventions, including style and comments. Here is a better version of Hello, World! You will notice that I have a call to a :py:func:`main()` function. This is common in Python code but not normally seen in CircuitPython. I am including it because by breaking the code into different functions to match different scenes, eventually will be really helpful.


.. literalinclude:: ./example.py
   :language: py
   :lines: 10-20

.. code-block:: python
	:linenos:

	#!/usr/bin/env python3

	# Created by : Jay Lee
	# Created on : January 2020
	# This program prints out Hello, World! onto the PyBadge

	  
	def main():
	    # this function prints out Hello, World! onto the PyBadge
	    print("Hello, World!")


	if __name__ == "__main__":
	    main()
    

Congratulations, we are ready to start.
