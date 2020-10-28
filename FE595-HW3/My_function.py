import numpy as np
import pandas as pd
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter


def Merge_Dataframe(file_name_txt, file_name_csv):
    '''

    :param file_name_txt: Input the txt file
    :param file_name_csv: Input the csv file
    :return: A merged data frame with company name and company purpose
    '''

    company_name_vec1 = np.array([])
    company_purpose_vec1 = np.array([])

    for i in file_name_txt:
        df = pd.read_csv(i, delimiter="\t", header=None)
        nrow = len(df)
        for j in range(nrow):
            str = df.iloc[j, 0]
            company_name = str.split(':', 2)
            company_purpose = company_name[2]
            company_name = company_name[1].split('---')[0]

            company_name_vec1 = np.append(company_name_vec1,
                                          company_name)
            company_purpose_vec1 = np.append(company_purpose_vec1,
                                             company_purpose)

    company_name_vec2 = np.array([])
    company_purpose_vec2 = np.array([])

    for i in file_name_csv:

        df = pd.read_csv(i, index_col=False)

        company_name_vec2 = np.append(company_name_vec2,
                                      df.iloc[:, -2].values)

        company_purpose_vec2 = np.append(company_purpose_vec2,
                                         df.iloc[:, -1].values)

    C_n = np.append(company_name_vec1, company_name_vec2)
    C_p = np.append(company_purpose_vec1, company_purpose_vec2)
    res = pd.DataFrame(data={'Company Name' : C_n,
                             'Company Purpose' : C_p})
    return res


def Text_anlyzer(df):

    '''

    :param df: The merged data frame with company name and company purpose
    :return: This function will return me the best company idea and the worst company idea

    '''

    analyzer = SentimentIntensityAnalyzer()
    nrow = len(df)
    Score = np.array([])

    for i in range(nrow):
        Score = np.append(Score, analyzer.polarity_scores(df['Company Purpose'][i])['compound'])

    df['Score'] = Score
    max_pos = np.argmax(Score,axis=0)
    max_neg = np.argmin(Score,axis=0)

    print("The best idea is ----" + df['Company Purpose'][max_pos])
    print("The worst idea is ----" + df['Company Purpose'][max_neg])

    return df


def Find_most_common_word(df, common_number):
    '''

    :param df: The merged data frame with company name and company purpose
    :param common_number: The number of the most common words you want to find
    :return: The n most common words
    '''

    big_str = ""
    for i in range(len(df)):
        big_str = big_str + df['Company Purpose'][i] + ". "

    my_word_list = TextBlob(big_str)
    word = Counter(my_word_list.words)
    most_common = word.most_common(common_number)

    return most_common
