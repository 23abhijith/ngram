import nltk
import random

def get_next_word(words, vocab, corpus, deterministic):
    occuranceCount = {}
    occurances = []
    ## build occrances counts and weights
    for occurance in vocab:
        matches = True
        for x in range(0, len(words)):
            if(words[x] != occurance[x]):
                matches = False
        if matches:
            occurances.append(occurance[len(words)])
            if occurance[len(words)] in occuranceCount:
                occuranceCount[occurance[len(words)]] += 1
            else:
                occuranceCount[occurance[len(words)]] = 1
    if deterministic:
        ## Choosing next word
        if occuranceCount == {}:
            ## Stupid backoff
            newVocab = []
            for idx in range(0, len(corpus)-len(words)):
                tokens = corpus[idx:idx+len(words)+1]
                newVocab.append(tokens)
            return get_next_word(words[-(len(words)-1):], newVocab, corpus, deterministic)
        else:
            return max(occuranceCount, key=occuranceCount.get)
    else:
        ## Random choice from all occurances by weight
        return random.choice(occurances)

def get_sentence_to_n(sentence, n, corpus, deterministic):
    if len(sentence) == 0:
        ## get most common word
        uniVocab = []
        occurancesCount = {}
        occurances = []
        for idx in range(0, len(corpus)-1-1):
            words = corpus[idx:idx+1]
            uniVocab.append(words)
        for word in uniVocab:
            if word[0] in occurancesCount:
                occurancesCount[word[0]] += 1
            else:
                occurancesCount[word[0]] = 1
            occurances.append(word[0])
        if deterministic:
            sentence.append(max(occurancesCount, key=occurancesCount.get))
        else:
            ## Random choice from all occurances by weight
            sentence.append(random.choice(occurances))
    ## work our way from bigram to n-gram to fill setence
    while(len(sentence) < n-1):
        vocab = []
        for idx in range(0, len(corpus)-len(sentence)):
            words = corpus[idx:idx+len(sentence)+1]
            vocab.append(words)
        sentence.append(get_next_word(sentence, vocab, corpus, deterministic))
    return sentence

def finish_sentence(sentence, n, corpus, deterministic=False):
    ## build vocab
    vocab = []
    for idx in range(0, len(corpus)-n-1):
        words = corpus[idx:idx+n]
        vocab.append(words)
    ## get setence to atleast length n-1
    if len(sentence) < n-1:
        sentence = get_sentence_to_n(sentence,n, corpus, deterministic)
    ## Complete sentence
    while len(sentence) < 15:
        phrase = sentence[-(n-1):]
        sentence.append(get_next_word(phrase,vocab, corpus, deterministic))
        if sentence[-1] in '?.,!':
            break
    return sentence

# corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
# corpus = nltk.word_tokenize(corpus.lower())
