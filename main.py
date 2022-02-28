from rdflib import *


class F22_Expression:
    def getAllTitles(self, expression):
        req = """
            PREFIX mus: <http://data.doremus.org/ontology#>
            PREFIX ecrm: <http://erlangen-crm.org/current/>
            PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

            SELECT ?expression ?title
            WHERE {
                ?expression ecrm:P102_has_title ?title .
            }
        """

        qres = self.graph.query(req, initBindings={'expression' : expression})
        result = []

        for row in qres:
            result.append(str(row.title))

        return result;

    def getAllGenres(self, expression):
        req = """
                    PREFIX mus: <http://data.doremus.org/ontology#>
                    PREFIX ecrm: <http://erlangen-crm.org/current/>
                    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

                    SELECT ?genre
                    WHERE {
                      ?expression mus:U12_has_genre ?genre .
                      FILTER (isIRI(?genre))
                    }
                    
                """

        qres = self.graph.query(req, initBindings={'expression': expression})
        result = []

        for row in qres:
            result.append(str(row.genre))

        return result;

    def getAllNotes(self, expression):
        req = """
                    PREFIX mus: <http://data.doremus.org/ontology#>
                    PREFIX ecrm: <http://erlangen-crm.org/current/>
                    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

                    SELECT ?expression ?note
                    WHERE {
                      ?expression ecrm:P3_has_note ?note .
                    }
                """

        qres = self.graph.query(req, initBindings={'expression' : expression})
        result = []

        for row in qres:
            result.append(str(row.note))

        return result;



    def getAllKey(self, expression):
        req = """
                    PREFIX mus: <http://data.doremus.org/ontology#>
                    PREFIX ecrm: <http://erlangen-crm.org/current/>
                    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

                    SELECT ?expression ?key
                    WHERE {
                      ?expression mus:U11_has_key ?key .
                      FILTER (isIRI(?key))
                    }
                """

        qres = self.graph.query(req, initBindings={'expression': expression})
        result = []

        for row in qres:
            result.append(str(row.key))

        return result;

    def getAllOpus(self, expression):
        req = """
                    PREFIX mus: <http://data.doremus.org/ontology#>
                    PREFIX ecrm: <http://erlangen-crm.org/current/>
                    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

                    SELECT ?expression ?opus
                    WHERE {
                      ?expression mus:U17_has_opus_statement / mus:U42_has_opus_number ?opus .
                      
                    }
                """

        qres = self.graph.query(req, initBindings={'expression': expression})
        result = []

        for row in qres:
            result.append(str(row.opus))

        return result;

    def getAllComposer(self, expression):
        req = """
                    PREFIX mus: <http://data.doremus.org/ontology#>
                    PREFIX ecrm: <http://erlangen-crm.org/current/>
                    PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

                    SELECT ?expression ?composer
                    WHERE {
                      ?expression a efrbroo:F22_Self-Contained_Expression .
                      ?expCreation efrbroo:R17_created ?expression ;
                        ecrm:P9_consists_of / ecrm:P14_carried_out_by ?composer ;

                    }
                """

        qres = self.graph.query(req, initBindings={'expression': expression})
        result = []

        for row in qres:
            result.append(str(row.composer))

        return result;

    def __init__(self, graph, expression):
        self.graph = graph

        self.expression = expression
        self.title = self.getAllTitles(expression)
        self.note = self.getAllNotes(expression)
        self.composer = self.getAllComposer(expression)
        self.key = self.getAllKey(expression)
        self.opus = self.getAllOpus(expression)
        self.genre = self.getAllGenres(expression)

    def __str__(self):
        return "Expression : " + str(self.expression) + "\n\tTitle : " + str(self.title) + "\n\tGenre : " + str(self.genre) \
               + "\n\tNotes : " + str(self.note) +"\n\tComposer : " + str(self.composer) \
               + "\n\tKey : " + str(self.key) + "\n\tOpus : " + str(self.opus)


def getAllExpressions(graph):
    print("Lecture d'un fichier ttl : ")
    req = """
            PREFIX mus: <http://data.doremus.org/ontology#>
            PREFIX ecrm: <http://erlangen-crm.org/current/>
            PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

            SELECT DISTINCT ?expression
            WHERE {
              ?expression a efrbroo:F22_Self-Contained_Expression .
            }
            """

    qres = graph.query(req)
    print(str(len(qres)))

    return qres


if __name__ == '__main__':
    g1 = Graph()
    g2 = Graph()
    g1.parse("./source.ttl")
    g2.parse("./target.ttl")

    result = getAllExpressions(g1)
    result2 = getAllExpressions(g2)

    for row in result:
        a = F22_Expression(g1, row[0])
        print(str(a))

    for row in result2:
        a = F22_Expression(g2, row[0])
        print(str(a))
