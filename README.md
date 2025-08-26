# ToothBrushTimer
Code for a timer used with a pico pi to make a 2 minute timer so I brush my teeth long enough

# Hardware
[Raspberry Pi Pico](https://littlebirdelectronics.com.au/products/raspberry-pi-pico-raspberry-pi-pico-with-headers-microusb-cable)
[Waveshare 3.5inch Touch Display Module for Raspberry Pi Pico](https://littlebirdelectronics.com.au/products/3-5inch-touch-display-module-for-raspberry-pi-pico-65k-colours-480-320-spi)

# Files

## testScripts
Includes all of the scripts used during initial testing
### test_ScreenScript.py
Fills a small rectangle in the bottom left of the screen
### test_TimerScript.py
Creates and displays a timer that counts down from 2 minutes

## driver
### ILI9488
Driver from [PeterMatthias](https://github.com/PeterMatthias/Pico_ILI9488/)



# Todo
1. Create a stop/start button for the touchscreen
2. Find a right angle micro usb connector for power
3. Implement stop/start functionality with new button
4. Find a way to power on/off the backlight
5. Design and print a case for the display and pi
6. Wrap all of the code up nicely and create a main.py
7. Enjoy your dental hygiene
