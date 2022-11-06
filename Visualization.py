from pandas import  read_csv
import matplotlib.pyplot as plt
import  pandas as pd
from wordcloud import WordCloud
import  seaborn as sns

# Data Visualization

df = read_csv('Cleaned-Mental-Health-Twitter.csv')


# data = {
#     "title": ["rt", "im" ,"one", "depression", "dont", "time",
#               "love","know","thank", "people"],
#     "count": [6630, 3328 ,2063, 950, 887, 785, 754, 729, 702, 593],
# }
#
# data = pd.DataFrame(data)
# data.head(10)
#
# print(data)
#
# text = " ".join(str(i) for i in df.post_text)
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


sns.lineplot(data=df, x="favourites", y="retweets").set(title="Density of Retweets/Likes");


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
# sns.boxplot(df)


# sns.distplot(a=df['retweets'])

# Creating the pie plot

# fig = plt.figure(figsize =(10, 7))
# myexplode = [0.1, 0, 0, 0,0,0,0,0,0,0]
# plt.pie(data["count"], labels = data["title"], autopct='%1.2f%%', explode=myexplode)
# plt.title("Most Common Words")
#
plt.show()