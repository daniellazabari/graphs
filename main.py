from charts import *

user_menu = """ Please choose from the following options:
- Enter 'c' to chart a Contour plot
- Enter 's' to chart a Scatter plot
- Enter 'b' to chart a Bar plot
- Enter 'f' to chart a simple function plot
- Enter 'q' to quit the program.
Your choice:\n"""

while True:
    user_selection = input(user_menu)
    if user_selection == 'q':
        break
    
    elif user_selection == 'c':
        contour()
    
    elif user_selection == 's':
        scatter()
    
    elif user_selection == 'b':
        bar()
    
    elif user_selection == 'f':
        simple()
    
    else:
        print("Invalid selection. Please try again.")