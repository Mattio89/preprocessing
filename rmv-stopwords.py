import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WhitespaceTokenizer

with open(r"Orlando_Data.txt",'r', encoding="utf8") as inFile, open(r"Orlando_Data_Filtered.txt",'w') as outFile:
	stop_words = set(stopwords.words('english'))
	for line in inFile.readlines():
		words = WhitespaceTokenizer().tokenize(line)
		filtered_words = " ".join(w for w in words if w not in stop_words)
		outFile.write(filtered_words + '\n')