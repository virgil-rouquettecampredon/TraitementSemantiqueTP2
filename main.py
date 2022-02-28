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

def getAllTypes(graph):
    req = """  
            SELECT DISTINCT ?type
            WHERE {
                ?s a ?type.
            }
          """
    result = graph.query(req)
    print("Nombre types : " + str(len(result)))
    for row in result:
        print(row)
    return result

def getAllGenres(graph):
    #Retourne tous les genres de tous les F22_Self-Contained_Expression du graph
    req = """  
    PREFIX mus: <http://data.doremus.org/ontology#>
    PREFIX ecrm:  <http://erlangen-crm.org/current/>
    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT DISTINCT ?genre ?z
    WHERE {
        ?x a efrbroo:F22_Self-Contained_Expression ;
        mus:U12_has_genre ?genre .
        OPTIONAL {
            SELECT ?genre ?z
            WHERE {
                ?genre a mus:M5_Genre ;
                ecrm:P1_is_identified_by ?z;
            }
        }
    }
    """

    #mus:U12_has_genre [ a mus:M5_Genre ;
    #                      ecrm:P1_is_identified_by  "musique contemporaine"@fr
    #                  ] ;

    result = graph.query(req)

    print("Nombre genres : " + str(len(result)))
    for row in result:
        print(row)
    return result


if __name__ == '__main__':
    g1 = Graph()
    g2 = Graph()
    g1.parse("./source.ttl")
    g2.parse("./target.ttl")
    print(len(g1))
    print(len(g2))
    s1 = getRelationTypes(g1)
    s2 = getRelationTypes(g2)

    q1 = """
    PREFIX mus: <http://data.doremus.org/ontology#>
    PREFIX ecrm: <http://erlangen-crm.org/current/>
    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?title
    WHERE {
        ?x a efrbroo:F22_Self-Contained_Expression ;
        ecrm:P102_has_title ?title .
    }
    """

    #Obtenir Toutes les propriétés d'un type efrbroo:F22_Self-Contained_Expression
    q2 = """
    PREFIX mus: <http://data.doremus.org/ontology#>
    PREFIX ecrm: <http://erlangen-crm.org/current/>
    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT DISTINCT ?property
    WHERE {
        ?x a efrbroo:F22_Self-Contained_Expression ;
        ?property ?title .
    }
    """

    q3 = """
    
    """

    #qres = g1.query(q1)

    #for row in qres:
    #    print(f"{row.title}")

    qres = g1.query(q2)

    for row in qres:
        print(f"{row.property}")

    # Intersection entre deux graphes
    #gInter = g1 & g2
    #print("Intersection : ")
    #getRelationTypes(gInter)

    #intersection = existSame(s1, s2)

    #getAllTypes(g1)
    #getAllTypes(g2)

    getAllGenres(g1)
    getAllGenres(g2)

    #for s, p, o in g1.triples((None, None, "F22_Self-Contained_Expression")):
        #print(o.hasTitle)

    #Save un RDF file
    #g.serialize(destination="tbl.ttl")
