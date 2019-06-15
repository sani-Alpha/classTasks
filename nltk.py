import time
#wordnet for synonyms, antonyms, definition, examples
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import sent_toekenize,word_toeknize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

data='''
Whose woods these are I think I know.
His house is in the village, though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.

He gives his harness bells a shake
To ask if there is some mistake.
The only other sound’s the sweep
Of easy wind and downy flake.

The woods are lovely, dark, and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
'''

#sentence tokenizer
print(data)
time.sleep(2)
print(sent_tokenize(data))
#word tokenizer
print(word_tokenize(data))
#removing stop words
removedata=[i for i in word_tokenize(data) if i.lower() not in stopwords.words('english')]
print(removedata)
