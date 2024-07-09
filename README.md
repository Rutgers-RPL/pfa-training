# Post-Flight Analysis Training

## Part 0: Getting Started

Post-flight analysis is a key part of the iterative engineering process. Looking back at the data collected during a test flight can provide insights into the forces experienced on the rocket, the general flight path, the specific timings of staging events, and more. The insights, in turn, allow other groups within our team to improve their designs to build a better rocket.

### 0.1: What is Python?

- Easy to use programming language, simple sintax, many powerful packages
- Tools for interactive development, visualization, and automation
- Extremely common in industry  

#### Compiled vs. Interpreted Languages

- List some examples of each (C, C++, Fortran, Rust) vs. (Python, JS, R)
- Execution process (machine translation all at once vs. line by line); speed difference, ease of development
- Error detection (compile-time vs runtime)

#### Packages and Modules

- Incorporate other people's code to accomplish tasks
- Packages are made up of modules
- Need to get packages from somewhere and put them somewhere
- What is a dependency? Dependencies can also have dependencies

#### Installing Packages (pip)

- Pip provides basic functionality for installing things
- Venvs, discuss limitations
- cannot easily have different versions of packages or different python versions

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

4. Here are some useful conda commands.
    ```Shell
    conda create --name Name_Of_Enviornment python = 3.10 # Create a new conda enviornment with python 3.10 (python version does not neet to be specified)
    conda env list # List all the enviornments on your system
    conda list # List all packages and versions installed in active enviornment
    conda install PACKAGENAME # Intall a package in current enviornment
    conda activate env_name # Activate an enviornment
    conda deactivate # Switch to base enviornment
    conda env remove --name env_name # Deleate an enviornment and everything in it
    conda remove PACKAGENAME # Uninstall package in enviornment
    ```
## Part 2: Simple Python Exercise

```Shell
python --version
```

```Shell
python -c "print('hello world!')"
```

```Shell
cd .\Projects\RRPL\
```

```Shell
mkdir py-exercises
```

```Shell
cd .\py-exercises\
```

```Shell
New-Item -ItemType File -Name "ex1.py"
```

```Shell
notepad.exe .\ex1.py
```

```Shell
code .\ex1.py
```

```Python
```

## Part 3: Simple Jupyter Exercise

```Shell
jupyter notebook
```
