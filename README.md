## Python Script to compare 2 csv files

The script reads two csv files  
Places them in dataframes  
Ask the user to delete the columns from source and destination dataframes (optional , if no columns to delete, then hit <enter> to skip>
Finally creates 3 outputs:   
<p>
Records that exist in both files:  diff_both_YYYY-MM-DD.csv 
Records that exist only is destination file: diff_destonly_YYYY-MM-DD.csv
Records that exist only in source file: diff_sourceonly_YYYY-MM-DD.csv
</p>
 
 setup.py: This script is used to build an exe from the python script  
 Refer [here](https://github.com/gmaroli/pythonexe) for details
 
sample output of the script:
```
2020-02-11 14:04:03,083 - Compare two csv files - INFO - Log files will be written to: <Path of the log File>
Enter the source file path:<Path of Source file>
2020-02-11 14:04:18,948 - Compare two csv files - INFO - Source File Path: <sourceFileName>
Enter the destination file path: <Destination fil Path>
2020-02-11 14:04:25,357 - Compare two csv files - INFO - Destination File Path: <destinationFileName>
Columns to be dropped in the source file (comma separted values if more than one column). Press <Enter> to skip: <Enter column names to be dropped or <enter> to skip>
Columns to be dropped in the destination file (comma separted values if more than one column). Press <Enter> to skip: <Enter column names to be dropped or <enter> to skip>
2020-02-11 14:04:45,969 - Compare two csv files - INFO - Dropping single / multiple column: <dropped column name in source file>
2020-02-11 14:04:45,971 - Compare two csv files - INFO - Dropping single / multiple column: <dropped column name in destination file>
2020-02-11 14:04:46,018 - Compare two csv files - INFO - Result file is stored in the following location: <filePath>\diff_sourceonly_2020-02-11.csv
2020-02-11 14:04:46,042 - Compare two csv files - INFO - Result file is stored in the following location: <filePath>\diff_destonly_2020-02-11.csv
2020-02-11 14:04:46,064 - Compare two csv files - INFO - Result file is stored in the following location: <filePath>\diff_both_2020-02-11.csv
2020-02-11 14:04:46,064 - Compare two csv files - INFO - **************************************************END**************************************************
Press enter to exit
```
