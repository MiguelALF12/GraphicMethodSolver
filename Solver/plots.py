import matplotlib.pyplot as plt
import numpy as np

def make_plot(solution_points,optimal_solution):

    # plt.scatter([1.0, 1.3846153846153846, 3.0], [4.0, 2.4615384615384617, 2.0], c="black")
    # plt.plot([2.0,0.0],[0.0,8.0])
    # plt.plot([5.0, 0.0], [0.0, 5.0])
    # plt.plot([10.0, 0.0], [0.0, 2.857142857142857 ])

    #Plotting restrictions

    for item in solution_points:
        xsp = []  # x's solution_points
        ysp = []  # y's solution_points
        for scalar in item:
            xsp.append(scalar[0])
            ysp.append(scalar[1])
        plt.plot(xsp,ysp)

    # Plotting optimal solutions

    for item in optimal_solution:
        xop = []  # x's optimal_solution
        yop = []  # y's optimal_solution
        xop.append(item[0])
        yop.append(item[1])
        plt.scatter(xop,yop,c="black")

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    # plot title
    plt.title('RESTRICTIONS AND OPTIMAL SOLUTIONS')
    # function to show the plot
    plt.show()
