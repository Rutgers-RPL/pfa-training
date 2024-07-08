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

- Explain.

#### Managing Multiple Environments

- Different package versions, different python versions
- All kept seperate
- Easy to switch between

#### Controling Dependencies and Conflicts

- Explain dependency graph
- Some dependencies clash (need minimum version/become deprecated eventually)
- conda has solver to find valid "transactions" that install/change/remove the target package

### 0.3: How do we use Python and Conda?

- Make automation tools
- Make graphs
- Do math
- etc

## Part 1: Installing Conda

### Windows

### MacOS

### Linux

### Verify Conda Installation

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
