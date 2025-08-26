from ili9488 import LCD_3inch5
import time

# ------------------------
# Display setup
# ------------------------
display = LCD_3inch5()
display.bl_ctrl(100)  # Set backlight to maximum
time.sleep(0.1)

RED = display.RED
BLACK = display.BLACK

# ------------------------
# Digit and colon patterns
# ------------------------
# 7x5 style "pixels" for each digit
digits = {
    '0': ["11111", "10001", "10001", "10001", "10001", "10001", "11111"],
    '1': ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    '2': ["11111", "00001", "00001", "11111", "10000", "10000", "11111"],
    '3': ["11111", "00001", "00001", "11111", "00001", "00001", "11111"],
    '4': ["10001", "10001", "10001", "11111", "00001", "00001", "00001"],
    '5': ["11111", "10000", "10000", "11111", "00001", "00001", "11111"],
    '6': ["11111", "10000", "10000", "11111", "10001", "10001", "11111"],
    '7': ["11111", "00001", "00001", "00001", "00001", "00001", "00001"],
    '8': ["11111", "10001", "10001", "11111", "10001", "10001", "11111"],
    '9': ["11111", "10001", "10001", "11111", "00001", "00001", "11111"]
}

# Colon pattern
colon = ["0", "1", "0", "0", "1", "0", "0"]

# ------------------------
# Layout configuration
# ------------------------
BLOCK = 20       # Size of one "pixel" block
SPACING = 10     # Spacing between digits
START_Y = 50     # Top Y position of digits

# Sequence of digits/colon for display
digit_sequence = ['M', ':', 'S1', 'S2']

# Compute widths for positioning
digit_widths = [BLOCK if d == ':' else 5*BLOCK for d in digit_sequence]
total_width = sum(digit_widths) + SPACING * (len(digit_sequence) - 1)
START_X = (display.width - total_width) // 2

# Compute horizontal positions of each element
positions = []
x = START_X
for d in digit_sequence:
    positions.append(x)
    x += (BLOCK if d == ':' else 5*BLOCK) + SPACING

# ------------------------
# Drawing functions
# ------------------------
def draw_digit(digit: str, x: int, y: int, color=RED):
    """
    Draw a single digit using the predefined 7x5 pattern.

    Args:
        digit: Character '0'-'9'
        x: Top-left x-coordinate
        y: Top-left y-coordinate
        color: Foreground color
    """
    pattern = digits[digit]
    for row, line in enumerate(pattern):
        for col, c in enumerate(line):
            fill_color = color if c == '1' else BLACK
            display.fill_rect(x + col*BLOCK, y + row*BLOCK, BLOCK, BLOCK, fill_color)


def draw_colon(x: int, y: int):
    """
    Draw a colon ":" pattern at the specified position.

    Args:
        x: Top-left x-coordinate
        y: Top-left y-coordinate
    """
    for row, c in enumerate(colon):
        fill_color = RED if c == '1' else BLACK
        display.fill_rect(x, y + row*BLOCK, BLOCK, BLOCK, fill_color)


# ------------------------
# Clear the screen once
# ------------------------
display.fill_rect(0, 0, display.width, display.height, BLACK)

# ------------------------
# Countdown loop (2:00 minutes)
# ------------------------
total_seconds = 2 * 60
last_tick = time.ticks_ms()  # record the starting time

while total_seconds >= 0:
    # Check how much time has passed
    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, last_tick)

    if elapsed >= 1000:  # 1000 ms = 1 second
        total_seconds -= 1
        last_tick = time.ticks_add(last_tick, 1000)  # move forward by one second

        mins = total_seconds // 60
        secs = total_seconds % 60

        # Prepare string representation
        str_digits = [str(mins), ':', str(secs // 10), str(secs % 10)]

        # Draw each element in sequence
        for i, d in enumerate(str_digits):
            if d == ':':
                draw_colon(positions[i], START_Y)
            else:
                draw_digit(d, positions[i], START_Y)

    # Small sleep to reduce CPU usage
    time.sleep(0.01)
