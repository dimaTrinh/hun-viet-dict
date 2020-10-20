import codecs
import nltk
import re
from math import log
from nltk.tokenize import sent_tokenize
from nltk.util import ngrams
from nltk.probability import FreqDist


# remove punctuations, escape characters, and lower case the sentence
def preprocess(sent):
    # sent = re.sub("[\r\n\t\f]", " ", sent)
    # sent = re.sub(r"\\u[a-z0-9]{4}", " ", sent)
    # sent = re.sub(r"\\x[a-z0-9]{2}", " ", sent)
    sent = re.sub("[^\w ]", "", sent)
    sent = re.sub(" +", " ", sent)
    return sent.strip().lower()


# find unigram in a sentence
def find_unigram(sent):
    unigrams = ngrams(sent.split(), 1)
    unigrams = [elem[0] for elem in unigrams]
    return unigrams


# find bigrams in a sentence
def find_bigram(sent):
    bigrams = ngrams(sent.split(), 2)
    bigrams = [" ".join(elem) for elem in bigrams]
    return bigrams


def main():
    inputFile = codecs.open('./vietCorpus', encoding='utf8')
    sentences = inputFile.readlines()
    proc_sent = [preprocess(sent) for sent in sentences]

    unigrams = []
    for sent in proc_sent:
        unigrams.extend(find_unigram(sent))

    uni_fd = FreqDist(unigrams)
    uni_count = uni_fd.N()

    bigrams = []
    for sent in proc_sent:
        bigrams.extend(find_bigram(sent))

    bi_fd = FreqDist(bigrams)

    colloc = {}

    for (key, value) in bi_fd.items():
        if (value < 10):
            continue
        firstWord, secondWord = key.split()
        probFirst = uni_fd[firstWord]/uni_count
        probSecond = uni_fd[secondWord]/uni_count
        probBigram = bi_fd[key]/uni_fd[firstWord]
        pmi = log(float(probBigram)/float(probFirst*probSecond), 2)
        if pmi > 1.1:
            colloc[(key, value)] = float(pmi)

    sorted_colloc = {k: v for k, v in sorted(
        colloc.items(), key=lambda item: item[1], reverse=True)}

    outputFile = open("./colloc", "w")
    for key, value in sorted_colloc.items():
        word, count = key
        pmi = value
        outputFile.write("{}\t{}\t{}\n".format(word, count, pmi))
    outputFile.close()


if __name__ == "__main__":
    main()
