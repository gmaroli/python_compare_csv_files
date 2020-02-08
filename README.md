## Python Script to compare 2 csv files

The script reads two csv files  
Places them in dataframes  
Ask the user to delete the columns from source and destination dataframes  
Finally creates 2 outputs:   
<p>
Records that exist in both files:  diff_both_YYYY-MM-DD.csv 

Records that exist only is destination file: diff_destonly_YYYY-MM-DD.csv

Records that exist only in source file: diff_sourceonly_YYYY-MM-DD.csv
 
</p>
 
 setup.py: This scripst is used to build an exe from the python script  
 Refer [here](https://github.com/gmaroli/pythonexe) for details
