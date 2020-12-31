import string
import re 
# from autocorrect import spell
from contractions import contractions_dict
from autocorrect import Speller
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
from nltk.stem import SnowballStemmer
# snowball_stemmer = SnowballStemmer(‘english’)

class Clean:
    def __init__(self,data):
        self.data = data

    #remove punctuation 
    def remove_punctuation(self, word):
        if word in string.punctuation:
            return False
        return True

    #tokenize text to word
    def tokenize(self,text):
        if text:
            return re.split('\W+',text)
        return []

    #Stemming word
    def stemming_word(self, word):
        pass

    #clean url + emoji + html tags + numbers
    def cleaning_tags(self, text):
        stop_words = stopwords.words('english')  
        new_text=re.sub(emoji.get_emoji_regexp(), r"", text)
        re.sub('<[^<]+?>','', text)
        return new_text
    
    #Spell Check coorect word 
    def correct_word(self, word):
        spell = Speller(lang='en')
        return spell(word)
    
