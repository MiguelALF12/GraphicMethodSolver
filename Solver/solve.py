import re
def standardized_restrictions(restriction):

    #Regular Expression here
    for item in restriction:
        expr_flag = re.search("\d+",item)
        if expr_flag:
            item_index = restriction.index(item)
            restriction[item_index] = int(item)

    return restriction


def findPoints(restriction):
    cteResult = 0
    cteX1 = 0
    cteX2 = 0
    for item in restriction:
        expr_flag = re.search("\d+", str(item))
        # print("item", item, re.search("\d+", str(item)))
        if expr_flag:
            if cteX1 == 0:
                cteX1 = int(item)
            elif cteX2 == 0:
                cteX2 = int(item)
            elif cteResult == 0:
                cteResult = int(item)
    # For X1 = 0
    # cte1X2 <= cte2
    # X2 <= (cte2/cte1)
    # X2 <= cte3
    X1 = cteResult/cteX1

    # For X2 = 0
    # cte1X1 <= cte2
    # X1 <= (cte2/cte1)
    # X1 <= cte3
    X2 = cteResult/cteX2
    print("X1:", X1, "X2:", X2)
    return [(X1,0),(0,X2)]


def FindSolutionSet(excercises):
    restricciones_index = 0
    for item in excercises:
        if 'restricciones' in item:
            restricciones_index = excercises.index(item)
            break

    restricciones = excercises[restricciones_index][1:]
    solution_points = []
    for restriction in restricciones:
        restriction = standardized_restrictions(restriction)
        solution_points.append(findPoints(restriction))
    return solution_points
def solve(excercises):
    solution_points = FindSolutionSet(excercises)
    print(solution_points)
    pass