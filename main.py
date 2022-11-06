import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import Word
import  seaborn as sns

from nltk.corpus import stopwords
sw = stopwords.words("english")

df = pd.read_csv("Mental-Health-Twitter.csv")
desired_width = 200
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 11)

# print("Head*******************")
# print(df.head)
# print("Info*******************")
# df.info()
# print("Shape*******************")
# print(df.shape)


# print("Check NaN Values")
NAN = [(c, df[c].isna().mean()*100) for c in df]
NAN = pd.DataFrame(NAN, columns=["column_name", "percentage"])
NAN.sort_values("percentage", ascending=False)
# print(NAN)
# remove un used columns


# data manipulation
df.drop("Unnamed: 0", axis=1, inplace=True)
df.drop("post_id", axis=1, inplace=True)
df.drop("user_id", axis=1, inplace=True)
# print(df.head())



# datetime object
# print("datetime object******************")
df.post_created = df.post_created.apply(pd.to_datetime)
df["month"] = df.post_created.dt.month
df["year"] = df.post_created.dt.year
df.drop("post_created", axis=1, inplace=True)
# print(df.describe().T)



#Preproccessing

# print("first Convert to lowercase*****************************")
#1 Convert to lowercase
df["post_text"] = df["post_text"].apply(lambda x: " ".join(x.lower() for x in x.split()))
# print(df.head())


#2 numerical values
# print("second Removing numerical values*****************************")
df["post_text"] = df["post_text"].str.replace("\d", "")
# print(df.head())



#3 Removing punctations
# print("third Removing punctations*****************************")
df["post_text"] = df["post_text"].str.replace("[^\w\s]", "")



#4 STOPWORDS
# print("fourth STOPWORDS*****************************")
# nltk.download("stopwords")
df["post_text"] = df["post_text"].apply(lambda x: " ".join(x for x in x.split() if x not in sw))
# print(df.head())



#5 STOPWORDS
# nltk.download("wordnet")
df["post_text"] = df["post_text"].apply(lambda x: " ".join([Word(x).lemmatize()]))
# print(df.head())
# Frequency Analysis
# We need convert all reviews to single text
# Most Common Words

# Cleaned DataSet
# df.to_csv("Cleaned-Mental-Health-Twitter.csv")

