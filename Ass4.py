
# Mohammed Hamada 
# No : 120201362
# Quize 4


# dataset of coprpus is attached


from __future__ import division
from collections import defaultdict as ddict
import itertools
import math
import random
import nltk



# 3.8 Write a program to compute unsmoothed unigrams and bigrams.
class NGrams(object):
    def init__f(self, max_n, words=None):
        self._max_n = max_n
        self._n_range = range(1, max_n + 1)
        self._counts = ddict(lambda: 0)
        
        if words is not None:
            self.update(words)
    def update(self, words):
        
        self._counts[()] += len(words)
        
        for i, word in enumerate(words):
            for n in self._n_range:
                if i + n <= len(words):
                    ngram_range = range(i, i + n)
                    ngram = [words[j] for j in ngram_range]
                    self._counts[tuple(ngram)] += 1
                   
    def probability(self, words):
        if len(words) <= self._max_n:
            return self._probability(words)
        else:
            prob = 1
            for i in range(len(words) - self._max_n + 1):
                ngram = words[i:i + self._max_n]
                prob *= self._probability(ngram)
            return prob
    def _probability(self, ngram):
        
        ngram = tuple(ngram)
        ngram_count = self._counts[ngram]
        prefix_count = self._counts[ngram[:-1]]
        
        if ngram_count and prefix_count:
            print(ngram_count / prefix_count)
            return ngram_count / prefix_count
        else:
            return 0.0
    
    # 3.10 Add an option to your program to generate random sentences.
    def generate(self, n_words):
        # select unigrams
        ngrams = iter(self._counts)
        unigrams = [x for x in ngrams if len(x) == 1]

        # keep trying to generate sentences until successful
        while True:
            try:
                return self._generate(n_words, unigrams)
            except RuntimeError:
                pass 

    # Meta function for unigram
    def _generate(self, n_words, unigrams):
        # add the requested number of words to the list
        words = []
        for i in itertools.repeat(self._max_n):
            # the prefix of the next ngram
            if i == 1:
                prefix = ()
            else:
                prefix = tuple(words[-i + 1:])
            
            # select a probability cut point, and then try
            # adding each unigram to the prefix until enough
            # probability has been seen to pass the cut point
            threshold = random.random()
            total = 0.0
            for unigram in unigrams:
                total += self._probability(prefix + unigram)
                if total >= threshold:
                    words.extend(unigram)
                    break
            
            # return the sentence if enough words were found
            if len(words) == n_words:
                return words
            # exit if it was impossible to find a plausible
            # ngram given the current partial sentence
            if total == 0.0:
                raise RuntimeError("impossible sequence")
    
    # Add an option to your program to compute the perplexity of a test set.
    def perplexity(self, words):
         prob = self.probability(words)
         # print("preplexity")
         return math.pow(prob, -1 / len(words))

# 3.9 Run your n-gram program on two different small corpora of your choice (you
#     might use email text or newsgroups). Now compare the statistics of the two
#     corpora. What are the differences in the most common unigrams between the
#     two? How about interesting differences in bigrams?

# Initial new Object 
f = NGrams()

# Assign the maximum number 
f.init__f(20)

# open small dataset corpus and insert the sentances in the model
with open('sent.txt', 'r') as in_file :
    text = in_file.read()
    sents = nltk.sent_tokenize(text)
   # print(sents[1])

# Insert every single sentance in the model
for i in sents:
    f.update(i)
   # print(i)

# find the propabillities
f.probability("cyberspace")

f.generate(20)

f.perplexity("cy")










