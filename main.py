from rdflib import *

def getRelationTypes(g):
    result_set = []

    # find all subjects of any type
    for s, p, o in g.triples((None, RDF.type, None)):
        #(f"{s} is a {o}")
        result_set.append(o)

    result_set = list(dict.fromkeys(result_set))

    return result_set

def existSame(s1, s2):
    intersection = set(s1).intersection(s2)
    return list(intersection)



if __name__ == '__main__':
    g1 = Graph()
    g2 = Graph()
    g1.parse("./source.ttl")
    g2.parse("./target.ttl")
    print(len(g1))
    print(len(g2))
    s1 = getRelationTypes(g1)
    s2 = getRelationTypes(g2)

    # Intersection entre deux graphes
    gInter = g1 & g2
    #print("Intersection : ")
    #getRelationTypes(gInter)

    intersection = existSame(s1, s2)
    for s, p, o in g1.triples((None, None, "F22_Self-Contained_Expression")):
        print(o.hasTitle)

    #Save un RDF file
    #g.serialize(destination="tbl.ttl")
