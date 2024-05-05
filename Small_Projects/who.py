import curses

def draw_ui(stdscr):
    # Clear the screen
    stdscr.clear()

    # Game title
    stdscr.addstr(0, 0, "Terminal Wordle")

    # Word to Guess
    stdscr.addstr(2, 0, "Word to Guess: ______")

    # Input Field
    stdscr.addstr(4, 0, "Enter your guess:")
    stdscr.addstr(5, 0, "> ")

    # Feedback Area
    stdscr.addstr(7, 0, "Feedback:")
    stdscr.addstr(8, 0, "Correct: ___")
    stdscr.addstr(9, 0, "Misplaced: ___")
    stdscr.addstr(10, 0, "Incorrect: ___")

    # Game Status
    stdscr.addstr(12, 0, "Attempts Left: 5")

    # Quit/Restart Option
    stdscr.addstr(14, 0, "Press 'q' to quit")

    # Refresh the screen
    stdscr.refresh()

def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Draw the UI
    draw_ui(stdscr)

    # Wait for user input
    stdscr.getch()

# Run the application
curses.wrapper(main)
