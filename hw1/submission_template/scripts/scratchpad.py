import re
import pandas as pd


df = pd.read_csv(r"C:\Users\joisl\Documents\McGill\Comp 598\hw1\submission_template\data\lang_dataframe.csv")
def containsTrump(content):

    if(re.search("Trump",content)):
        return True
    else:
        return False
df["trump_mention"] = df['content'].apply(containsTrump)
trump_mentions = df.trump_mention[df.trump_mention==True].count()
notTrump_mentions = df.trump_mention[df.trump_mention==False].count()

fraction = (trump_mentions)/(trump_mentions+notTrump_mentions)
rounded = round(fraction,3)

print(rounded)