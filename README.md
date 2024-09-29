# Utility Programs
Containes multiple utility programs created to speed up my day to day tasks

### Requirements:
- Python 3 is required to be installed in your system. (Visit [python.org](https://www.python.org/downloads/) to Download)

### 1. Merge Scripts
This utility is to merge multiple code scripts into single code script file.

#### Requirements:
- Required Libraries:
  - os
  - logging
  - datetime
- To install the required libraries, run command `pip install python-library`. Replace `python-library` with above mentioned libraries and install them one by one.

#### How to Use
1. Download and extract the folder **_merge-scripts_** from repository on your computer.
2. Open the folder and place the Control File (which contains order of execution of code scripts) and Scripts Folder (which contains all code scripts). **Example:** Here **Control File** is **controlFile.txt** and **Scripts Folder** is **code_files**.
3. Open **parameters.txt** and set the paths of Control File, Scripts Folder and Output Folder.
4. To merge the scripts, just double click the file **Execute_MergeScripts.bat**. This will start executiong the program in command prompt. Once completed you will find combined code script in mentioned output location.
