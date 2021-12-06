import re
from Solver.plots import *
def standardized_restrictions(restriction):

    #Regular Expression here
    for item in restriction:
        expr_flag = re.search("\d+",item)
        if expr_flag:
            item_index = restriction.index(item)
            restriction[item_index] = int(item)

    return restriction

def standardized_objFuncs(excercises):
    objFunc_index = 0
    for item in excercises:
        if 'objetivo' in item:
            objFunc_index = excercises.index(item)
            break
    objFunc = excercises[objFunc_index][1]
    stand_objFunction = standardized_restrictions(objFunc)
    return stand_objFunction

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
    # print("X1:", X1, "X2:", X2)
    return [(X1,0),(0,X2)]

def verifyDivisionByZero(cte):
    if cte == 0:
        raise TypeError("División por cero. Revise sus Restricciones!")
        exit()

def compareTwoEquations(restrictionOne,restrictionTwo):
    def changeSign(sign):
        return '+' if sign == '-' else '-'

    # print("here ", restrictionOne,restrictionTwo)
    left = [0,0,0,0]
    right = [0,0,0,0]

    #Fill left side of igualation procces expression
    for _ in range(len(restrictionTwo)):

        #-------this could be reformmated in a way that we can fill both at the same time!!!!
        if left[0] == 0:
            left[0] = restrictionTwo[0]*restrictionOne[6]
        elif left[1] == 0:
            new_sign = changeSign(restrictionOne[2])
            left[1] = new_sign
        elif left[2] == 0:
            left[2] = restrictionTwo[0]*restrictionOne[3]
        elif left[3] == 0:
            left[3] = restrictionOne[4]

        if right[0] == 0:
            right[0] = restrictionOne[0]*restrictionTwo[6]
        elif right[1] == 0:
            new_sign = changeSign(restrictionTwo[2])
            right[1] = new_sign
        elif right[2] == 0:
            right[2] = restrictionOne[0]*restrictionTwo[3]
        elif right[3] == 0:
            right[3] = restrictionTwo[4]

    #solving all the expression made above in left list
    # print("First left and right", left, right)
    #Using eval, and assumming the expression wont have negative values as cteResult
    left[0] = eval(f"{left[0]}-{right[0]}")
    var_rightSide_sign = changeSign(right[1])
    left[2] = eval(f"{left[1]}{left[2]}{var_rightSide_sign}{right[2]}")
    var_final_sign = changeSign(left[1])

    #Avoiding duplicated signs (numbers as itselfs and strings)
    for item in left:
        if type(item) == int:
            if item < 0:
                left[left.index(item)] = item*-1

    # Verify  if the expr. has cteX2 as zero
    verifyDivisionByZero(left[2])

    #Calculating the value for X2
    cteX2 =  eval(f"({left[0]}/({var_final_sign}{left[2]}))")

    # print("Second left and right", left, right)
    #solving for cteX1 using cteX2
    X1_sign = changeSign(restrictionOne[2])
    cteX1 = eval(f"({restrictionOne[6]}{X1_sign}({restrictionOne[3]}*{cteX2}))/{restrictionOne[0]}")

    #final point
    # print("X1: ", cteX1,"X2: ", cteX2, )
    return (cteX1,cteX2)

def findOptimalSolution(excercises):
    #['restricciones', [1, 'p', '+', 2, 'm', '<=', 80], [3, 'p', '+', 2, 'm', '<=', 120]]
    #There is a 4 limit of total restrictions
    rest_index = 0
    # restrictions_copy = restrictions
    restricciones_index = 0
    optimal_solutions = []
    for item in excercises:
        if 'restricciones' in item:
            restricciones_index = excercises.index(item)
            break
    restrictions = excercises[restricciones_index]
    for restrictionOne in range(1,len(restrictions)):
        for restrictionTwo in range(restrictionOne + 1,len(restrictions)):
            if restrictionOne != len(restrictions) - 1:
                optimal_solutions.append(compareTwoEquations(restrictions[restrictionOne],restrictions[restrictionTwo]))

    return optimal_solutions

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

def unifiy(solution_points,optimal_solution):
    points_to_eval = []
    #this is just for be aware (remember when we pass arguments in main, those are local but still can be changed)
    for item in solution_points:
        points_to_eval.append(item[0])
        points_to_eval.append(item[1])
    for item in optimal_solution:
        points_to_eval.append(item)

    return points_to_eval

def eval_points(points_to_eval,excercises):
    obj_func =  standardized_objFuncs(excercises)
    for item in points_to_eval:
        evaluating = eval(f"{obj_func[0]}*{item[0]}{obj_func[2]}{obj_func[3]}*{item[1]}")
        print(f"\t Con {item} el resultado evaluando en la función objetivo es: {evaluating} \n")

def solve(excercises):
    solution_points = FindSolutionSet(excercises)
    optimal_solution = findOptimalSolution(excercises)
    points_to_eval = unifiy(solution_points, optimal_solution)
    print("\n")
    print("1. Conjunto de soluciónes factibles \n\t")
    print(solution_points)
    print("\n")
    print("2. Intersección entre restricciones para solución optima \n\t")
    print(optimal_solution)
    print("\n")
    print("3. Evaluando el conjunto de soluciones y la posible solución optima en la función objetivo \n\t")
    eval_points(points_to_eval,excercises)
    print("4. Visualización del conjunto de soluciones factibles y la solución optima \n\t")
    make_plot(solution_points, optimal_solution)