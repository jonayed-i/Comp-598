import pandas as pd
import langdetect
import re

def englishChecker(x):
    try:
        lang = langdetect.detect(x)
    except:
        #print(x)
        lang = "no"
    if (lang == "en"):
        return True
    else:
        return False

def isQuestion(content):
    if re.search("\?",content):
        return True
    else:
        return False

df = pd.read_csv(r"C:\Users\joisl\Documents\McGill\Comp 598\hw1\submission_template\data\IRAhandle_tweets_1.csv")
df = df.head(10000)
print(df.describe())

df.drop(df[df['language'] != 'English'].index, inplace=True)
print(df.describe())
df1 = df[['tweet_id','publish_date','content']]

#print(df1.head())

print(df1.describe())

#df1["isEng"] = df1['content'].apply(englishChecker)
#df1.drop(df1[df1['isEng'] == False].index, inplace=True)

print(df1.describe())

df1["isQuestion"] = df1['content'].apply(isQuestion)
df1.drop(df1[df1['isQuestion'] == True].index, inplace=True)

print(df1.describe())

print(df1.head())

df1.to_csv (r'C:\Users\joisl\Documents\McGill\Comp 598\hw1\submission_template\data\lang_dataframe.csv', index = False, header=True)
