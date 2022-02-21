if __name__ == '__main__':
    g1 = Graph()
    g2 = Graph()
    g1.parse("./source.ttl")
    g2.parse("./target.ttl")
    print(len(g))

    #Save un RDF file
    #g.serialize(destination="tbl.ttl")
