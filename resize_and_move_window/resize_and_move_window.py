import pygetwindow as gw


def resize_and_move_window(title, width, height, x_position, y_position):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        window.resizeTo(width, height)
        window.moveTo(x_position, y_position)
        print(f"Window '{title}' resized and moved successfully.")
    except IndexError:
        print(f"Window '{title}' not found.")

# Replace 'Command Prompt' with the actual title of your Command Prompt window
window_title = 'Notepads'
# Set the desired width, height, x_position, and y_position
desired_width = 800
desired_height = 600
desired_x_position = 1
desired_y_position = 1

# Call the function to resize and move the window
resize_and_move_window(window_title, desired_width, desired_height, desired_x_position, desired_y_position)
