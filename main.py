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


# Data Visualization

data = {
    "title": ["rt", "im" ,"one", "depression", "dont", "time",
              "love","know","thank", "people"],
    "count": [6630, 3328 ,2063, 950, 887, 785, 754, 729, 702, 593],
}

data = pd.DataFrame(data)
data.head(10)

# text = " ".join(i for i in df.post_text)
# wordcloud = WordCloud(
#     background_color="#6B5B95",
#     colormap="Set2",
#     collocations=False).generate(text)
#
# plt.figure(figsize=[11,11])
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.title("The Tweet's About Depression")
# plt.show()


# sns.lineplot(df["retweets"])


# sns.lineplot(data=df, x="favourites", y="retweets").set(title="Density of Retweets/Likes");


# sns.scatterplot(data=df, x="friends", y="statuses",).set(title="Density of Retweets/Likes");


# sns.set_style("whitegrid")
# sns.despine(left=True, bottom=True)
# sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})
# sns.set(rc = {'figure.figsize':(11,5)})

# sns.barplot(data=df, x="month", y="friends").set(title="Frequency of tweets per month")

# sns.boxenplot(df)
# sns.kdeplot(x=df.followers, shade=True,).set(title="Density of followers") # dağılım grafiği

# fig = plt.figure(figsize =(10, 7))
# myexplode = [0.1, 0, 0, 0,0,0,0,0,0,0]
# plt.pie(data["count"], labels = data["title"], autopct='%1.2f%%', explode=myexplode)
# plt.title("Most Common Words")

# plt.show()




# sns.distplot(a=df['retweets'])
#
# plt.show()

# Creating the pie plot

# fig = plt.figure(figsize =(10, 7))
# myexplode = [0.1, 0, 0, 0,0,0,0,0,0,0]
# plt.pie(data["count"], labels = data["title"], autopct='%1.2f%%', explode=myexplode)
# plt.title("Most Common Words")
#
# plt.show()