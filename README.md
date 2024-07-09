# Post-Flight Analysis Training

## Part 0: Getting Started

Post-flight analysis is a key part of the iterative engineering process. Looking back at the data collected during a test flight can provide insights into the forces experienced on the rocket, the general flight path, the specific timings of staging events, and more. The insights, in turn, allow other groups within our team to improve their designs to build a better rocket.

### 0.1: What is Python?

Python is one of the most widely-used programming languages in the computer engineering and computer science industry, and for good reason; it has very simple syntax that beginners can read and understand, is very easy to develop and test code with, and has built-in support for many powerful packages that assist the development process greatly. It’s especially useful for post-flight data analysis, in which case Python is able to provide powerful data visualization tools (like graphs and charts), as well as interactive interfaces and automation services to make interacting and analyzing our data even easier. By taking advantage of these features of Python, post-flight data analysis can be made far simpler and efficient.


#### Compiled vs. Interpreted Languages

Python is an interpreted programming language, just like Javascript and R. “Interpreted” means that when you run your code, your program is evaluated and executed line by line, every single time you run the program. This isn’t always the case; certain programming languages, like C, C++, and Rust, are called compiled languages. Compiled languages are translated (or compiled) into a more computer-friendly format the first time they’re run, and this new version is used every time the program is run.


A compiled language, over time, will be faster than an interpreted one; after all, it’s easier and faster for a computer to understand its own language than have everything translated line-by-line. Additionally, more errors will be caught at compile time as opposed to runtime, meaning some mistakes are caught earlier. However, if you make a lot of changes to the code, and the language needs to constantly re-translate (or re-compile) the entire program every time a change is made, this can become a huge time-waster for a programmer. With an interpreted language like Python, changes to the code will mean relatively little change in runtimes, making it an ideal option for our testing and development.


#### Packages and Modules

Using packages, you can incorporate python code written by others into your own program. These packages, oftentimes, are downloaded off the internet to your machine and stored locally so your code can pull from them. Packages are simply groups of “modules,” where each module is a python file with useful routines written into them that can be pulled into your main program. When you incorporate a module or a package into your program, they become “dependencies.” As the name implies, a Python program needs all of its dependencies at runtime in order to function correctly, or oftentimes, function at all. Sometimes modules include packages or modules within themselves; in this case, you still need to find and download these modules for your program to function. This means that dependencies can have dependencies as well!

#### Installing Packages (pip)



PIP is one of the most common tools for package management in python. With one-line terminal commands, packages can be downloaded to your machine, meaning the only thing you need to do is import the code into your file. However, some projects may require certain packages while others require different packages; in this case, installing all the packages for every project you’ll work on is messy and a waste of resources. A simple solution is venv, a “virtual environment” creator for python, which essentially allows you to create a separate space for different projects and sets of packages. This means multiple package and module installations won’t clutter up and pollute your build environment, whatever it may be for that project.


Pip, however, has no built-in support for packages and modules written outside of the standard python libraries, and also has no built-in isolated build environment support; it relies on outside tools like Venv to achieve this. This means that although using PIP will work for some time, it is good to pursue other package management tools that have more dynamic package and build environment support, such as Conda.


### 0.2: What is Conda?

Conda is an open-source package management and envionrnment management system. This tool is used to install, run, and update software packages and dependencies. Conda and pip both can be used to install packages and dependencies but conda is perfered becasue it allows the users to create virtual enviornments for different projects while being more efficient and easy to use.

#### Managing Multiple Environments

As stated above conda allows the user to create different virtual enviornments. A virtual enviornment is an isolated space where you can install and manage a specific set of packages and dependencies without affection other projects on your system. Each enviornment has its own directory, seperate from the system's global enviornment, containing all the necessary files and libraries required for a particula project. This isolation helps prevent conflicts between different projects, allowing you to use different version of packages and Python for each project. Enviornments are especially useful for managing dependencies and ensuring that your projects are reproducible and consisten across different systems. Conda allows you to switch between these different envrionemnts and install different version of python or packages in different envionrments efficnetly and easily. 

#### Controling Dependencies and Conflicts

It is important to have the ability to control the version of dependecies installed for your project because of how different packages when used together rely on others. A good visualation for this is called a dependency graph which can be seen bellow. A dependency graph is a visual representation of the relationships between software packages and their dependencies. In this graph, each node represents a packaged, and each edge represents a dependency relationship. For example, if Packae A depdends on Package B, there will be a directed edge from A to B. This graph helps in understanding how packages are interconnected and which packages rely on others. Sometimes, different packages require different versions of the same dependency. For instance, Package A might need version 1.2 of a library, while Package B requries version 2.0. This can lead to dependency clashes, where it becomes impossible to satisfy all requirements simultaneously. Additionaly, packages or their verisons can become deprecated over time, meaning they are no longer maintained or recommended for use. This is where conda excels. Conda addresses these issues with a dependency resolver that analyzes the dependency graph and finds valid "transactions" to install, change, or remove packages. The solver ensures that all dependencies are met and compatible versions are used. When you issue a command to install or update a package, Conda's solver determines the best set of actions to maintain a functional and conflict-free enviornment. This process helps in avoidning dependency clashes and ensures that your enviornment remains stable and consistent.

![Error Displaying Image!](./gfx/dependency_graph.png "Dependency Graph Example")


### 0.3: How do we use Python and Conda?

Python and Conda are used all the time for post flight analysis. We use python and conda to automation tools. For example, we have developed a binary parser that would take flight log data in bytes and converted it into a .csv format using python. This allowed us to retrieve data such as rocket position, acceleration, time, etc. This data then would be used in jupyter notebooks to make graphs. We would plot things such as acceleration vs time in order to notice possible errors in the hardware, or even the program. These are a few exmaples as to how we use python an Conda but we are continously looking for ways to develop our flight analysis to improve future rocket designs and builds. 

## Part 1: Installing Conda
1. Install [Miniconda](https://docs.anaconda.com/miniconda/#quick-command-line-install). Miniconda is a lightweight version of Anaconda that includes Conda, Python, and a few essential packages. It's advantageous to install Miniconda instead of the full Anaconda because the installtion file is smaller. You can still add any of the packages provided by Anaconda to you enviornments using Conda as needed. Once conda is installed it will not be recognized by your systems terminal till it has been told to do so.
### Windows
2. Open a powershell terminal as administrator and run the following line bellow.
    ```Shell
    ```
### MacOS

### Linux

### Verify Conda Installation
3. Once you have succesfully installed Conda, run the following terminal commands to verify your installation.
    ```Shell
    conda --version
    ```
    The output should look something like the following.
    ![Error Displaying Image!](.gfx/Conda_Install_Verification.png "Installation Verification")

    If the output states that conda is not recognized, run the test scripts located in this Git repository and execute the one corresponding to your system. If the output states that conda is not installed, double-check your conda installation. If it says that conda is installed but not initialized, refer to the instructions above to ensure you have initialized conda in your system terminal.

## Part 2: Simple Python Exercise


Need to add conda install for numpy
-Tyler and Mahir


First, we're going to get started with setting up your first Python project.
Open your terminal and proceed with the steps below:


Check your python version to make sure it's installed and up to date.
```Shell
python --version
```
Run your first line of python code: Hello world!
```Shell
python -c "print('hello world!')" #"-c" lets you pass a string (the text that comes next) as a python line to your terminal and run it.
```


Enter your RRPL directory within your Projects directory.
```Shell
cd .\Projects\RRPL\  #"." is a symbol for the parent folder you're currently in.
```


Make a new folder called py_exercises.
```Shell
mkdir py-exercises # mkdir = make directory
```


Enter the new folder you just made.
```Shell
cd .\py-exercises\     #cd  = change directory
```




Create a new file called "ex1.py".
```Shell
New-Item -ItemType File -Name "ex1.py" #A file that ends with .py is a python executable.
```


If you don't have VSCode installed, go ahead and open the file in your notepad.


```Shell
notepad.exe .\ex1.py
```


If you do have vscode installed, open it with vscode.
```Shell
code .\ex1.py
```
Let's get started with writing your first lines of Python code!


First, go ahead and import the numpy package, with the alias np.
```Python
import numpy as np #from now on, you can refer to numpy as np in your program.
```


We're going to go ahead and define two new matrices now, l1 and l2:


```Python
l1 = [[0.31, 0.43, 0.66],
      [0.81, 0.49, 0.52],
      [0.04, 0.39, 0.35]]


l2 = [[0.39, 0.23, 0.93],
      [0.40, 0.83, 0.76],
      [0.57, 0.46, 0.18]]
     
#Both l1 and l2 store 3x3 matrices of numbers between 0 and 1.
```


We are going to do some math with these matrices and store it in a third.
In order to do this, we need to create a third matrix to store our results beforehand.


```Python
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


#Declare a matrix of 0s to store our results, and store the matrix in "result".
```


The idea here is to use a nested loop to go through every row and every column to
multiply these two matrices together. In order to do this efficiently, we need to know
the length and width of each array we are multiplying. We can do this using the built
in "len" command:


```Python
# Matrix Dimensions
rows_l1 = len(l1) #defaults to the number of rows, since specific row wasn't identified
cols_l1 = len(l1[0]) #gets the number of columns, since we indexed to specify a row.
cols_l2 = len(l2[0]) #does the same for the columns in l2.
```


Now we can write a triple-nested for-loop in order to manually multiply these two matrices together
and store it inside the "result" matrix we defined earlier.


```Python
# Iterate through rows of l1
for i in range(rows_l1):
    # Iterate through columns of l2
    for j in range(cols_l2):
        # Iterate through rows of l2
        for k in range(cols_l1):
            result[i][j] += l1[i][k] * l2[k][j]
```


Now we can go ahead and print out the resulting matrix.


```Python
print(f'Method 1 (Loops): ') # Print method information
# Print the result matrix
for row in result:
    print(row)
```


This works, and is easy to read, but it's not the most efficiently-typed
 way to do this, especially with the tools Python provides for us.
 Let's try this in a more efficient way using List Comprehensions.


First, lets re-establish our matrix dimensions.


```Python
# Matrix dimensions
rows_l1 = len(l1)
cols_l1 = len(l1[0])
cols_l2 = len(l2[0])
```


Let's calculate the result using our new method:


```Python
result = [[sum(l1[i][k] * l2[k][j] for k in range(cols_l1)) for j in range(cols_l2)] for i in range(rows_l1)]
```


And print out the result, which should be the same:


```Python
print(f'Method 2 (List Comprehension):') # Print method information
# Print the result matrix
for row in result:
    print(row)


```


The last, and most effiecient (and easiest to type) method is using our
NumPy package from earlier.


First, store both arrays as numpy array variables.


```Python
arr1 = np.array(l1)
arr2 = np.array(l2)
#we can use np instead of numpy, because we imported numpy as np at the top.
```
numpy arrays can be multiplied by simply using the @ operator, instead
of manually writing out a multiplication algorithm. Copy the code below
to do the multiplication and print out the result:


```Python
print(f'Method  (NumPy):') # Print method information
print(arr1@arr2)
```


And that's the basics of python, using for loops and numpy.




I still need to do part with speed comp
-Tyler

## Part 3: Simple Jupyter Exercise

```Shell
jupyter notebook
```
