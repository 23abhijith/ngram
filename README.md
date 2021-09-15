# ngram
The algorithm in mtg.py is an example of Markov Generated Langanguage using N-grams.

In the case of this algorithm each word is treated as a "gram".

The agruments provided to finish sentence are as follows:

1. a sentence [list of tokens] that we’re trying to build on,
2. n [int], the length of n-grams to use for prediction, and
3. a source corpus [list of tokens]
4. a flag indicating whether the process should be deterministic [bool]

The determinisitc algorithm uses markov chains to identify the word that best fits the situation.
If no case of that occuring in the text for a given n-gram then it will attempt to find something in 
n-1 gram all the way to unigram.

## To Run
Make sure nltk is installed (only required for test dataset)
Then run Python mtg.py
