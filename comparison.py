#import nltk
import py_stringmatching as sm
#from nltk.corpus import wordnet



def identityEqualMeasure(s1, s2):
    return s1 == s2


def levenshtein(s1, s2):
    lev = sm.Levenshtein()
    # Similarité (1 ok)
    return lev.get_sim_score(s1, s2)


def jaro(s1, s2):
    jaro = sm.Jaro()
    # Similarité (1 ok)
    return jaro.get_sim_score(s1, s2)


def smoa(s1, s2):
    return 0


def ngram(s1, s2, size):
    # TODO A TESTER

    # http://anhaidgroup.github.io/py_stringmatching/v0.4.x/QgramTokenizer.html?highlight=ngram
    i = 0
    same = 0

    while ((i + size - 1) < len(s1)) or ((i + size - 1) < len(s2)):
        if s1[i:i + size] == s2[i:i + size]:
            same += 1
        i += 1

    # The closer to 1, the better
    return (same) / (min(len(s2), len(s1)) - size + 1)


def synonymity(s1, s2):
    # print(s1)
    # synonyms = []
    # for syn in wordnet.synsets(s1):
    #     for l in syn.lemmas():
    #         synonyms.append(l.name())
    #         print(l.name())
    #
    # if (s2 in synonyms):
    #     return 1
    # else:
    return 0
    # TODO USE SPACY NLTK fonctionne qu'en anglais et est pas fou (dog synonyms de hotdog)

    #TODO IMPORTANT https://crisco2.unicaen.fr/des/

    #TODO BABEL.NET FOR SYNONYM
    #Token.similarity

def jaccard(set1, set2):
    jaccard = sm.Jaccard()
    return jaccard.get_sim_score(set1, set2)


def monge_elkan(set1, set2):
    monge_elkan = sm.MongeElkan()
    # RAW SCORE 1 GOOD, 0 BAD
    # S1 et S2 BAG OF WORD
    return monge_elkan.get_raw_score(set1, set2)

def compare(s1, s2, threshold, identity=True, levenshteinBool=True, jaroBool=True, ngramBool=False, ngram_size=2, jaccardBool=True, monge_elkanBool=True):
    result = 0
    nbMesure = 0

    if monge_elkanBool or jaccardBool:
        #TODO : Not really a set, word duplication happens
        set1 = [token.text for token in s1.tokens]
        set2 = [token.text for token in s2.tokens]

    if identity:
        result += identityEqualMeasure(s1.text, s2.text)
        if result:
            return True
    if levenshteinBool:
        result += levenshtein(s1.text, s2.text)
        nbMesure += 1
    if jaroBool:
        result += jaro(s1.text, s2.text)
        nbMesure += 1
    if ngramBool:
        result += ngram(s1.text, s2.text, ngram_size)
        nbMesure += 1
    if jaccardBool:
        result += jaccard(set1, set2)
        nbMesure += 1
    if monge_elkanBool:
        result += monge_elkan(set1, set2)
        nbMesure += 1
    #print("Found : " + str(result/nbMesure))
    return result/nbMesure


if __name__ == '__main__':
    # alphabet_tok = sm.AlphabeticTokenizer()

    print(compare("Le chien dort", "Le chien mange", 0.5 , identity=True, levenshteinBool=True, jaroBool=True, ngramBool=True, ngram_size=2, jaccardBool=True, monge_elkanBool=True))
