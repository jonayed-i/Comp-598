import pandas as pd
import re


df = pd.read_csv(r"C:\Users\joisl\Documents\McGill\Comp 598\hw1\submission_template\data\lang_dataframe.csv")

print(df.describe())



def containsTrump(content):

    if(re.search("[^a-zA-Z]Trump[^a-zA-Z]|^Trump[^a-zA-Z]]|[^a-zA-Z]Trump\Z",content)):
        return True
    else:
        return False


df["trump_mention"] = df['content'].apply(containsTrump)
df = df[['tweet_id','publish_date','content','trump_mention']]
print(df.describe())


trump_mentions = df.trump_mention[df.trump_mention==True].count()
notTrump_mentions = df.trump_mention[df.trump_mention==False].count()

fraction = (trump_mentions)/(trump_mentions+notTrump_mentions)
rounded = round(fraction,3)

results = pd.DataFrame(columns =['result', 'value'])
#new_row = 'frac-trump-mentions' + rounded
#results.append({'result':'frac-trump-mentions','value':rounded},ignore_index=True)
results.loc[len(results.index)] = ['frac-trump-mentions',rounded]
print(results.head())
print("hello")



df.to_csv (r'C:\Users\joisl\Documents\McGill\Comp 598\hw1\submission_template\data\dataset.tsv', index = False, header=True, sep = '\t')
results.to_csv (r'C:\Users\joisl\Documents\McGill\Comp 598\hw1\submission_template\data\results.tsv', index = False, header=True, sep = '\t')