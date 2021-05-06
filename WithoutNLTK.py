import string
from collections import Counter
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
tokenized_Words=CleanText.split()
#stop words without NLTK
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words=[]
for word in tokenized_Words:
    if word not in stop_words:
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




