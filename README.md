# Sudoku-Solver-and-Generator
This is a sudoku solver and generator with GUI built using Python

(scroll below for screenshots)

**ALGORITHM:**

The solver uses the Recursive Backtracking Algorithm. Backtracking is a form of search that climbs recursively down a tree made of different choices. Whenever a backtracking algorithm is used, its goal is to reach the very end of its recursion tree where the solutions are, so in order to reach the end it will have to search its way down along a valid path.

Hence, however complex the sudoku is, the solving algorithm is always able to find a solution to it.

The generator also uses the Recursive Backtracking Algorithm to generate a Sudoku. First a complete Sudoku is generated. Then the program starts removing 1 number at a time and checks if the Sudoku hence formed is solvable by the backtracking approach. If it is solvable , the next number is removed and the process is repeated. Else the number is put back and another number is removed. When the required number of numbers are removed, the Sudoku generated is given to the user to solve. Once the user clicks the submit button , the code checks if the user has solved it correctly and accordingly awards points to the user.

**DATA HANDLING:**

While the backtracking algorithm is the core of the program, data handling helps keep track of each user’s information and progress.

Every time a new user joins, the user’s name and other stats are added to a csv file named “points.csv” and the stats are initialized to zero.

As the user progresses with solving, the points are updated in the csv to keep record.

If the user saves a sudoku, a csv file is created with the user’s name and it stores the saved sudoku. Another csv file is created to store the solution of the same sudoku.

The user may load the saved sudoku at any time.

Only one sudoku can be saved by a user at any given moment.

Alongside, each user’s points is collected from the ‘points.csv’ file and is sorted to find out the highest scoring players and this information is displayed on the leaderboard.

### Screenshots:
![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img1.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img2.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img3.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img4.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img5.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img6.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img7.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img8.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img9.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img10.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img11.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img12.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img13.png)

![alt text](https://github.com/nachiketsrao/Sudoku-Solver-and-Generator/blob/main/readme-images/img14.png)


### MODULES AND FUNCTIONS

#### Main modules:
1.	current_main

This is the main code which calls all other modules. This module is executed to run the project.

2.	final_4cross4

This is the program for solving a 4 cross 4 sudoku.

3.	final_9cross9

This is the program for solving a 9 cross 9 sudoku.

4.	generating_unique_new_generator

To generate a new unique sudoku of a given level.

5.	generator

Creates window and displays generated sudoku. It checks the sudoku and calculates points.

6.	LoadPrevious

This is the program to load the previously saved sudoku and check the progress made in it.

7.	new_user

Enables the creation of a new user object.

8.	old_user_modified

Manages the entry for already existing users.

9.	original_control_room

Manages the activity on the user’s window.

10.	Solver_for_generating_complete_sudoku

Backtracking code for checking if the degenerated sudoku has a unique solution.

11.	user

Manages all activities pertaining to the user object.

#### Imported Modules:

1.	tkinter

Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications.

2.	random

The random module is a built-in module to generate the pseudo-random variables. It can be used to perform some action randomly such as to get a random number.

3.	pickle

The pickle module implements binary protocols for serializing and de-serializing a Python object structure.

4.	csv

The csv module implements classes to read and write tabular data in CSV format.

5.	os

The OS module in Python provides functions for interacting with the operating system.

6.	time

The Python time module provides many ways of representing time in code, such as objects, numbers, and strings.

7.	copy

Copy Module is a set of functions that are related to copying different elements of a list, objects, arrays, etc. It can be used to create shallow copies as well as deep copies.

8.	PIL (for ImageTk)

Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different 
image file formats.

#### Class Used:

1.	Class user:

This class is used to create a user object. 
The user object has many attributes like name, password, number of sudokus solved, total points,etc.

#### List of all defined functions:

Current_main:
1.	cred()
2.	hosa_user()
3.	entry()

final_4cross4:
1.	fourfour()
2.	runtime()
3.	find_empty()
4.	used_row()
5.	used_col()
6.	used_box()
7.	location_safe()
8.	solve_sudoku()
9.	reset()
10.	all_null()
11.	all_full()
12.	only_num
13.	print_solved()
14.	show_all()
15.	entry()

final_9cross9:
1.	ninenine()
2.	runtime()
3.	elimination()
4.	d_creation()
5.	print_sudoku()
6.	find_empty
7.	used_row()
8.	used_col()
9.	used_box()
10.	location_safe()
11.	solve_sudoku()
12.	reset()
13.	only_num()
14.	all_null()
15.	all_full()
16.	print_solved()
17.	show_all()
18.	entry()

Generating_unique_new_generator:
1.	print_sudoku()
2.	internal_check_box()
3.	check_box()
4.	check_column()
5.	generate_empty_sudoku()
6.	generate_complete_sudoku()
7.	generate_main_sudoku()

generator:
1.	GenerateSudokuToSolve()
2.	click()
3.	disable_buttons()
4.	button_guess_to_real_func()
5.	button_guess_func()
6.	button_real_func()
7.	clear()
8.	instruction()
9.	hint()
10.	pause()
11.	play()
12.	return_time()
13.	time_control()
14.	timer()
15.	correct()
16.	modify_row_and_col()
17.	decorate_grid()
18.	process_data()
19.	get_data()
20.	check_all_inputs()
21.	calculate_points()
22.	yes_button()
23.	no_button()
24.	preparing_for_exit()
25.	destroy_window()
26.	discard_button()
27.	save_button()
28.	solution()
29.	output_data()

LoadPrevious:
1.	check_IsAnySaved()
2.	solve_previous()
3.	GenerateSudokuToSolve()
4.	click()
5.	disable_buttons()
6.	button_guess_func()
7.	button_real_func()
8.	button_guess_to_real_func()
9.	clear()
10.	hint()
11.	instruction()
12.	pause()
13.	play()
14.	return_time()
15.	time_control()
16.	correct()
17.	modify_row_and_col()
18.	decorate_grid()
19.	process_data()
20.	get_data()
21.	check_all_inputs()
22.	calculate_points()
23.	yes_button()
24.	no_button()
25.	preparing_for_exit()
26.	destroy_window()
27.	discard_button()
28.	save_button()
29.	solution()
30.	output_data()

new_user:
1.	check_valid()
2.	entry()

old_user_modified:
1.	cred()
2.	hosa_user()
3.	entry()

original_control_room:
1.	tab2()
2.	CheckAndLoad()
3.	LevelButtons()
4.	level()
5.	showchoice1()
6.	showchoice2()
7.	showchoice3()
8.	close_window3()
9.	leaderboard()

Solve_for_generating_complete_sudoku:
1.	solver()
2.	print_sudoku()
3.	find_empty()
4.	used_row()
5.	used_col()
6.	used_box()
7.	location_safe()
8.	solve_sudoku()

Class user:
1.	__init__()
2.	check_name()
3.	pass_check()
4.	first_input()
5.	edit_csv()
6.	get_csv()
7.	get_fullSolved()
8.	calculate_points()
