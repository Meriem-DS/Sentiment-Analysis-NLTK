#Tokenization : replace split with an other fonctionnalities of nltk & more faster , performant
#STOPWORDS: REMOVE ALLL THE STOP WORDS AND import stopwords of nltk in any language we need
#Valuer ajoutée => SEntiment Analysis : Positive , neg, neutre /pour plus de précision
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

         #Step1:Cleaning Data
#faire appel au texte csv
text=open('scraped_data.csv',encoding='UTF-8').read()
#convertir au miniscule
lowercase=text.lower()
#Supprimer ponctuation ( to visualise pounctuation in python we use (string.punctuation)
CleanText= lowercase.translate(str.maketrans('','',string.punctuation))
###info:
         # translate: convertir texte à un texte sans ponctauration à l'ainde str.maketrans
         #str1: specifier une liste des caractéres qu'on doit remplacer
         #str2 :specifier une liste des caractéres avec lequel on va remplacer
         #str3 : specifeir une liste des caracteres qu'on doit supprimer (dans notre cas ponctuation)

             #STEP 2: Tokenization & stop words:
tokenized_Words=word_tokenize(CleanText,"english") # nous retourne une liste des mots!!!
#stop words with NLTK
final_words=[]
for word in tokenized_Words:
    if word not in stopwords.words('english'):
        final_words.append(word)


            #STEP3 / WHERE WE WILL ANALYSING Emotions (word in final_words ===> emotion)
#verfier si les mots dans final_words existe dans emotions.txt
    #open file emotions
Emotions_list=[]
with open('emotions.txt','r') as file:
    for line in file:
         # clear each line in emotions.txt (punctiation ,spacein the beguning, space between lines...)
         clear_line=line.replace('/n',"").replace("'","").replace(",","").strip() #replace exxtra space with nothing , ' with nothing , , ... && supprimer espace de début
         word,emotion=clear_line.split(":") #va diviser lignes en deux word and emotions
         if word in final_words:
             Emotions_list.append(emotion)

#Compter les emotions
w=Counter(Emotions_list)

                    #STEP+:+ or - Sentiment
#create function wich have the whole text as input/param
def SentimentAnalysis(FullText):
    score = SentimentIntensityAnalyzer().polarity_scores(FullText)#Dictionnaire(keys:neg,pos ,neu..., values:scores)
    neg = score['neg']
    pos = score['pos']
    if pos < neg:
        print("Negative Sentiment :(")
    elif pos > neg:
        print("Positive Sentiment :)")
    else:
        print("Neutral Sentiment ")
#afficher
SentimentAnalysis(CleanText)  # CleanText is the full text


                    #STEP 4 :GRAPH MATPLOTLIB
#create bar graph
   #METHODE 1 :plt.bar(w.keys(),w.values())
   #METHODE 2 : NOUS PERMET LES MIS à jour AUTOMATIQUEMENT
# using the variable ax for single a Axes
fig, ax1 = plt.subplots()
# space between bar
ax1.bar(w.keys(), w.values())# les declarer
fig.autofmt_xdate() #updates
#save the graph's photo
plt.savefig("graph.png")
#SHOW GRAPH
plt.show()





