import pandas as pd
import re


df = pd.read_csv(r"C:\Users\joisl\Documents\McGill\Comp 598\hw1\submission_template\data\lang_dataframe.csv")

print(df.describe())



def containsTrump(content):
    return True


df["isQuestion"] = df['content'].apply(isQuestion)