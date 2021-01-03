import string
import re 
# from autocorrect import spell
from contractions import contractions_dict
from autocorrect import Speller
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
from nltk.stem import SnowballStemmer 
from textblob import TextBlob
import pandas as pd
from pprint import pprint
import  emoji

# snowball_stemmer = SnowballStemmer(‘english’)

class Clean:
    def __init__(self,data):
        self.data = data
        self.stem = SnowballStemmer('english')

    #remove punctuation 
    def remove_punctuation(self, word):
        list_word = []
        for c in word:
            if not c in string.punctuation:
                list_word.append(c)
        return ''.join(list_word)

    #tokenize => split text to word 
    def tokenize(self,text):
        # if text:
        #     return re.split('\W+',text)
        # return []
        return word_tokenize(text)

    #Stemming word
    def stemming_word(self, word):
        return self.stem(word)

    #clean url + emoji + html tags + numbers
    def cleaning_tags(self, text):
        # stop_words = stopwords.words('english')  
        new_text = re.sub(emoji.get_emoji_regexp(), "", text)
        # re.sub('<[^<]+?>','', text)
        return new_text
    
    #Spell Check coorect word 
    def correct_word(self, word):
        spell = Speller(lang='en')
        return spell(word)

    def translate(self, text):
        text_new = TextBlob(text)
        if (text_new.detect_language() != 'en'):
            return text_new.translate(to='en')
        return text_new.correct()
    
def main():
    # df  = pd.read_csv('./fb.csv')
    # tweets = df["tweet"]
    tweets = [ "اشعارات عن الافلام و المسلسلات الجديدة فور اضافتها على ايجي بست", "🔔🔔🔔   Numéro 🤙🏽Mohamed 1 au Maroc  🔔🔔🔔S 📸✈️lafac✈️CN-RNM"]
    data = Clean(tweets)
    # print(tweets.head())
    # pprint(data.cleaning_tags(tweets[0]))
    print(data.translate(tweets[0]))

if __name__ == '__main__':
    main()
