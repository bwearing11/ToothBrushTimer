from ili9488 import LCD_3inch5
import time

# Initialize display
display = LCD_3inch5()

# Turn on backlight full
display.bl_ctrl(100)

# Optional delay to make sure display initialized
time.sleep(0.1)

# Draw a small red rectangle (50x50) in top-left corner
display.fill_rect(0, 0, 50, 50, display.RED)

print("Test rectangle drawn!")
