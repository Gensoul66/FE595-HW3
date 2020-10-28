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

    # The ten most common words
    x = mf.Find_most_common_word(df=df, common_number=10)

    print('The 10 most common words: ')
    print(x)

if __name__ == "__main__" :
    main()