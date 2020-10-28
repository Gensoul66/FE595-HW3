import My_function as mf
import os


def main():

        # reset the working directory
        current_adress = os.getcwd()
        new_adress = current_adress + '/File Name'
        os.chdir(new_adress)

        # process the data
        file_name_txt = ['Haohang Li.txt']
        file_name_csv = ['Baihao Huang.csv',
                         'Haonan Wang.csv',
                         'Mengyuan He.csv',
                         'Zichen Gao.csv']

        My_df = mf.Merge_Dataframe(file_name_txt, file_name_csv)

        # output the file
        new_adress2 = current_adress + '/Merged data frame'
        os.chdir(new_adress2)
        My_df.to_csv('All Company.csv',index=False)

        print("File output finish")

if __name__ == "__main__":
    main()