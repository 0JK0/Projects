# Currently Ongoing Project
It still lacks the deleting and auto updating history

### How to use?

  - Download the 4 files necessary for the program to work.
  - Execute the main.py file after downloading the required files.
  - The main classes are divided into separate modules for simplicity and organization.
  - The program is controlled through the "GUI" that appears in the terminal.
  - Be cautious as there are still many bugs that might appear if the inputs are not as expected.
  - The program attempts to create a new file locally for the database.
  - If the program cannot create a new file, it will break.
  - To prevent this, ensure you either execute it with Admin permissions or open all 4 files in VSCode and execute it from there.


Description(repeated from the main README.md)

A Workout Tracking "app" run from the terminal, it should allow to view, update, and register the date of a routine.
How?

I'm planing to make it using SQLite and Python i don't want a GUI since apart from the fact i don't feel like learning how to make one, i just feel like is kinda cooler if it is used without a GUI
Using experience:

The way the user(me) is going to interact with the "app" should go something along the lines of:

    Ask for options (1.Show all available Routines 2.Show Workout History)

if option 1 is chosen:

    Display routines table

    Chose the routine to use

    display the table for that specific routine then ask (1.View 2.Use 3.Update)

        View mode: shows the table again

        Use mode: display 1 by 1 each workout (row), it will display a counter to count sets, after it reaches the amount of sets it will give a resting timer and move to the next workout(row). When it finishes it should display the amount of time taken and save: the routine done, the date and the time it took, in another table; Finally show the History table and ask if they want to (1.Quit 2.Go back to menu)

        Update mode: Allow to change amount of sets,reps or workouts in said routine then just go to view mode.

if option 2 is chosen:

    Show the History table and ask for (1.Quit 2. Go back to menu)

