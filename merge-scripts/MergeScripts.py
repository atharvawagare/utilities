"""
A Utility Python Program to Merge Files with The Help of A Control File.
Created with The Purpose to Reduce My Manual Efforts of Combining the Code Files.

Author: Atharva Wagare
Date Created: 29 May 2024
Date Modified: 29 September 2024

Connect with Me: https://linkedin.com/in/atharvawagare
"""

# Necessary Imports
import os
import logging
from datetime import datetime as dt

class SetupLogging:
    def __init__(self, logger_name, log_dir="logs"):
        # Check if logs folder exists or not
        if not os.path.exists(os.path.join(os.getcwd(), log_dir)):
            os.mkdir(os.path.join(os.getcwd(), log_dir))

        log_filename=os.path.join(os.getcwd(), log_dir, "{}_{}.txt".format(logger_name, dt.now().strftime("%Y%m%d_%H%M%S")))
        logging.basicConfig(
            filename=log_filename,
            filemode="a",
            format="%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(lineno)d - %(message)s",
            level=logging.INFO
        )
        self.logger=logging.getLogger(logger_name)
        print("For Detailed Information Refer Log File\nLog Filename: {}".format(os.path.join(log_dir, log_filename.split("\\")[-1])))

    def return_logger(self):
        return self.logger

# Class to Merge Files
class MergeScripts:
    def __init__(self, control_file, files_folder, output_file, logger):
        self.control_file=os.path.join(os.getcwd(), control_file)
        self.files_folder=os.path.join(os.getcwd(), files_folder)
        self.output_file=os.path.join(os.getcwd(), output_file)
        self.logger=logger

    def merge_files(self):
        # Very First Step of doing All Checks

        # 1. Check whether controlfile exists or not
        if os.path.exists(self.control_file):
            self.logger.info(msg="Selected Control File: {}".format(self.control_file.split("\\")[-1]))
        else:
            self.logger.info(msg="Control File {} Doesn't Exists".format(self.control_file.split("\\")[-1]))
            self.logger.info(msg="Terminating the Process")
            exit(0)

        # 2. Check for the files folder
        if os.path.exists(self.files_folder):
            self.logger.info(msg="Found Files Folder: {}".format(self.files_folder.split("\\")[-1]))
        else:
            self.logger.info(msg="Could not Find the Files Folder: {}".format(self.files_folder.split("\\")[-1]))
            self.logger.info(msg="Terminating the Process")
            exit(0)

        # Check for existing output file and delete it
        if os.path.exists(self.output_file):
            self.logger.info(msg="Found Existing {} File. Deleting that.".format(self.output_file.split("\\")[-1]))
            os.remove(self.output_file)
        
        self.logger.info(msg="Creating File: {}".format(self.output_file.split("\\")[-1]))

        filenames=[]
        with open(self.control_file, "r") as file:
            for line in file.readlines():
                filenames.extend([name.strip() for name in line.strip().split(",")])
        
        filenames=list(filter(lambda x: len(x)!=0, filenames))

        self.logger.info(msg="Total File Names Found: {}".format(len(filenames)))
        self.logger.info(msg="Filenames are: {}".format(filenames))

        self.logger.info(msg="Starting the Combining Process")
        with open(self.output_file, "a") as combined_file:
            for filename in filenames:
                # 3. Check for the availability of script file
                if os.path.exists(os.path.join(self.files_folder, filename)):
                    self.logger.info(msg="Selected Script File: {}".format(filename))
                else:
                    self.logger.info(msg="Script File {} Doesn't Exists".format(filename))
                    self.logger.info(msg="Terminating the Process")
                    exit(0)

                combined_file.write("-- Begin: {}\n\n".format(filename))
                with open(os.path.join(self.files_folder, filename), "r") as scriptfile:
                    for line in scriptfile.readlines():
                        combined_file.write(line)
                combined_file.write("\n\n-- End: {}\n\n".format(filename))

        self.logger.info(msg="Process Completed")

# Setup the Logging
logger=SetupLogging(logger_name="MergeScripts").return_logger()

# Read the Parameters File
parameter_file=os.path.join(os.getcwd(), "parameters.txt")
parameters={}

if os.path.exists(parameter_file):
    logger.info(msg="Parameters File Found\n{}".format(parameter_file))
    with open(parameter_file, "r") as file:
        for line in file.readlines():
            key, value=list(map(lambda x: x.strip(), line.strip().split("=")))
            parameters[key]=value
else:
    logger.info(msg="Parameters File Does Not Exists\n{}".format(parameter_file))
    exit(0)

# Start the Main Program
merger=MergeScripts(control_file=parameters["CONTROL_FILE"], files_folder=parameters["SQL_FILES_FOLDER"], output_file=parameters["OUTPUT_FILE_PATH"], logger=logger)
merger.merge_files()