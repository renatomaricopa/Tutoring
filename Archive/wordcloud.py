from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import regex as re
import re


# nltk.download('punkt')
# nltk.download("stopwords")
# nltk.download("wordnet")


def remove_non_alpha(self):
    with open("pp.txt", "r", encoding="utf-8") as f:
        for i in f:
            # Remove all the non-alphabetical characters
            s = re.sub(r"[^a-zA-Z]+", " ", i)


with open("pp.txt", "r", encoding="utf-8") as f:
    for i in f:
        # Remove all the non-alphabetical characters
        s = re.sub(r"[^a-zA-Z]+", " ", i)
        tb = TextBlob(s)
        print(tb)
        sw = stopwords.words("english")
        sw.append('wa')
        w2 = [w for w in tb.words.lemmatize() if w not in sw]


        str1 = " ".join(w2)
        wc = WordCloud(background_color="white")
        wc.generate(str1)
        plt.imshow(wc)

