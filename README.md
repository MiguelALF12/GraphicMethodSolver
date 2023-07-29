<h1 align="center">GUIDE FOR THE GRAPHIC METHOD SOLVER</h1>

In this repository you will find the code for the solver of maximize and minimize problems. This solver use the graphic method.

## GRAPHIC METHOD
The graphical method consists of representing the graphs associated with the equations of the system to deduce their solution. The solution of the system is the point of intersection between the graphs. The reason for this is that the coordinates of this point satisfy both equations and, therefore, it is the solution of the system.

## HOW TO USE THE PROGRAM

The program consist of the following steps:

1. Choose an excercise and put it into the Excercise.csv
2. Read the CSV file with a standardized text with <code>input()</code>
3. Parse the information saved from the read before with <code>ParseExcercises(reuturnOfInput())</code>
4. Call <code>solver(returnOfParseExcercises())</code>
5. Run the program

### SOME ADVICES FOR CSV FILES AND NEW EXCERCISES

#### Code execution

* The program was made to analyze N number of restrictions in just ONE excercises, each of them with a similar look (only two variables of decission).
* It will only accept problems that achieve the terms of solutions given by the graphic method solver

#### CSV file terms

Every text must be like the following example: <br>

![image](https://user-images.githubusercontent.com/54087310/145414708-4c4929fe-4d8e-48f0-8366-f08ae507bbeb.png)

Despite <i>criterio;max</i> does not have any functionality within the code, its a need to be given, this just for keep the structure of work defined.

You will see another file called <i>Excercises.txt</i>. It contain other two differents examples. If you want to use them, choose one and copy/paste it in Excercises.csv .


# CONTACT AND OTHERS
Comments and improvements will be apprecciated. You can make the pull request, or if you dont, here I put some of my social profiles: <br>
* email: <a href="mailto:miguel.lopez@utp.edu.co" target="_blank">Miguel Angel Lopez Fernández</a>
