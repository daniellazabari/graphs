import matplotlib.pyplot as plt
import numpy as np


def contour():
    pass

def scatter():
    x_vals = input("Enter ten x values: (different values should be seperated with ','):\n")
    y_vals = input("Enter ten x values: (different values should be seperated with ','):\n")

    x = [float(i) for i in x_vals.split(',')]
    y = [float(i) for i in y_vals.split(',')]

    if len(x) != 10 or len(y) != 10:
        print("Error! You must enter 10 values")
        return
    
    plt.scatter(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Scatter Plot")
    plt.show()
    

def bar():
    pass

def simple():
    pass
    

# def start_input():
#     graph_type = str(input("""Enter the type of graph you want to plot:
#     - 'simple' for a simple plot
#     - 'contour' for a contour plot
#     - 'both' for both a simple plot and a contour plot
#     """))
#     return graph_type

# def func_input():
#     return input("Enter the function you want to plot: ")

# while True:
#     graph_type = start_input()
#     func = func_input()
#     if graph_type == 'simple':
#         x = np.linspace(-5, 5, 50)
#         y = eval(func)
#         plt.plot(x, y)
#         plt.show()
         

