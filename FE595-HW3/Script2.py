import numpy as np
import pandas as pd
import os
import My_function as mf



def main():

    # choose the directory
    current_adress = os.getcwd()
    new_adress = current_adress + '/Merged data frame'
    os.chdir(new_adress)

    # read the merged data frame that we saved in script1
    df = pd.read_csv('All Company.csv')

    # Find out the best company idea and the worst company idea
    mf.Text_anlyzer(df)



if __name__ == "__main__" :
    main()