import py_stringmatching as sm

def identityEqualMeasure(s1, s2):
    return s1.equal(s2)

def levenshtein(s1, s2):
    lev = sm.Levenshtein()
    #Similarité (1 ok)
    return lev.get_sim_score(s1, s2)

def jaro(s1, s2):
    jaro = sm.Jaro()
    # Similarité (1 ok)
    return jaro.get_sim_score(s1, s2)

def smoa(s1, s2):
    return 0

def ngram(s1, s2):
    #http://anhaidgroup.github.io/py_stringmatching/v0.4.x/QgramTokenizer.html?highlight=ngram
    return 0

def synonymity(s1, s2):
    #Voir avec NLTK
    return 0

def jaccard(s1, s2):
    jaccard = sm.Jaccard()
    return jaccard.get_sim_score(s1, s2)

def monge_elkan(s1, s2):
    monge_elkan = sm.MongeElkan()
    monge_elkan.set_sim_func()
    #RAW SCORE 0 GOOD, 1 BAD
    #S1 et S2 BAG OF WORD
    return monge_elkan.get_raw_score(s1, s2)

if __name__ == '__main__':
    alphabet_tok = sm.AlphabeticTokenizer()
