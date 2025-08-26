# ToothBrushTimer
Code for a timer used with a Pico Pi to make a 2 minute timer so I brush my teeth long enough

# Hardware
- [Raspberry Pi Pico](https://littlebirdelectronics.com.au/products/raspberry-pi-pico-raspberry-pi-pico-with-headers-microusb-cable)
- [Waveshare 3.5inch Touch Display Module for Raspberry Pi Pico](https://littlebirdelectronics.com.au/products/3-5inch-touch-display-module-for-raspberry-pi-pico-65k-colours-480-320-spi)

# Other tools used
- Development in Thonny for interfacing with Pico Pi
- Case design in AutoCAD (design files to be added)
- [Display datasheet](https://www.waveshare.com/w/upload/2/2d/ILI9488_Data_Sheet.pdf)

# Repo Structure

## testScripts
Includes all of the scripts used during initial testing
### test_ScreenScript.py
Fills a small rectangle in the bottom left of the screen
### test_TimerScript.py
Creates and displays a timer that counts down from 2 minutes

## Driver
### ILI9488
Driver from [PeterMatthias](https://github.com/PeterMatthias/Pico_ILI9488/)

## Design Files

# Todo
1. Create a stop/start button for the touchscreen
2. Test touch implementation from PeterMatthias' driver
3. Find a right angle micro usb connector for power
4. Implement stop/start functionality with new button
5. Find a way to power on/off the backlight
6. Design and print a case for the display and pi
7. Wrap all of the code up nicely and create a main.py
8. Enjoy your dental hygiene

### Potential features
- Ability to adjust timer length
- Blinking timer digits when it reaches zero
- Adding a small speaker to make a little chime when the time is up
