from MergeScripts import MergeScripts

merger=MergeScripts(control_file="controlFile.txt", files_folder="code_files", output_file="COMBINED_CODE_FILES.txt")
merger.merge_files()