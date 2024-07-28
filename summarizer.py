import nltk
nltk.download('punkt')
nltk.download('stopwords')
# Counter counts frequency of words
from collections import Counter
# imports list of stop words to be removed (a, an, the ...)
from nltk.corpus import stopwords
# sentence tokeniser splits texts into sentences
# word tokenizer splits sentence into words
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from heapq import nlargest
def summarize_vectorized(text, n):
  # Tokenize the text into sentences
  sentences = sent_tokenize(text)
  # use tokens to make tfidf matrix
  # tfidf matrix takes into accound the frequency of words in the sentences
  # and the frequency of words in the entire corpus (weighting rare words)
  vectorizer = TfidfVectorizer(stop_words='english')
  tfidf_matrix = vectorizer.fit_transform(sentences)

  #cosine similarity checks the similarity between the sentence and the document
  sentence_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]

  #find indices for n sentences with highest similarity scores
  summarized_sentences = nlargest(n, range(len(sentence_scores)), key=sentence_scores.__getitem__)

  # use indices to add sentences
  return ' '.join([sentences[i] for i in sorted(summarized_sentences)])