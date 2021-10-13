# import libraries
#import numpy as np
##np.set_printoptions(edgeitems=10, linewidth=180)
import pandas as pd
#pd.set_option('display.max_rows', 5000)
#pd.set_option('display.max_columns', 5000)
#pd.set_option('display.width', 10000)
import os
import glob


# Changing the current working directory
os.chdir(r"/Users/dermotsheridan/Downloads/UCD/Project /data uci/a01/p1")
# Getting the FileNames of all .csv files in the current dir.
filenames = [i for i in glob.glob(f"*.txt")]
#Loading all the csv files to create a list of data frames
df = [pd.read_csv(file, sep = ",", header=None, engine = 'python' )
      for file in filenames]
print(df)

#df_Trans = df[0].T
#print(df_Trans)