import matplotlib.pyplot as plt
import numpy as np

palette = ['#558B6E', '#88A09E', '#704C5E', '#B88C9E', '#F1C8DB', '#558B6E', '#88A09E', '#704C5E', '#B88C9E', '#F1C8DB']

def contour():
    pass

def scatter():
    x_vals = input("Enter up to ten x values: (different values should be seperated with ','):\n")
    y_vals = input("Enter up to ten x values: (different values should be seperated with ','):\n")

    x = [float(i) for i in x_vals.split(',')]
    y = [float(i) for i in y_vals.split(',')]

    if len(x) > 10 or len(y) > 10:
        print("Error! You must enter up to 10 values")
        return
    
    if len(x) != len(y):
        print("Error! You must enter the same amount of x and y values")
        return
    
    plt.scatter(x, y, color = palette)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Scatter Plot")
    plt.show()
    
def bar():
    labels_input = input("Enter up to ten labels: (different values should be seperated with ','):\n")
    values_input = input("Enter up to ten bar hights: (different values should be seperated with ','):\n")

    labels = [i for i in labels_input.split(',')]
    values = [float(i) for i in values_input.split(',')]

    if len(labels) > 10 or len(values) > 10:
        print("Error! You must enter up to 10 values")
    
    if len(labels) != len(values):
        print("Error! You must enter the same amount of labels and values")
    
    plt.bar(labels, values, color = palette)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Bar Chart")
    plt.show()

# So far, this code can't handle functions with more than one variable and non-simple functions (like sin(x)).
def simple():
    x = np.linspace(-5, 5, 50)
    y = input("Enter a simple function to plot: (e.g. x**2 + 2*x + 1):\n")
    y = eval(y)
    plt.plot(x, y, color = palette[0])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Simple Function Plot")
    plt.show()

    

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
         

