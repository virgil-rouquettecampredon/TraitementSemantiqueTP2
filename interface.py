# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from rdflib import *
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt
from rdflib.namespace import RDF
import io
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot


def visualize(g):
    stream = io.StringIO()
    rdf2dot(g, stream, opts={display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue)
    dg.write_png("output.png")


def display_graph(graph):
    G = rdflib_to_networkx_multidigraph(graph)

    # Plot Networkx instance of RDF Graph
    pos = nx.spring_layout(G, scale=2)
    edge_labels = nx.get_edge_attributes(G, 'r')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, with_labels=True)

    # if not in interactive mode for
    plt.show()
    print("OUI")


def open_rdf_file():
    filetypes = (
        ('Turtle', '*.ttl'),
        ('XML/RDF', '*.rdf*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='.',
        filetypes=filetypes)

    print(filename)

    g = Graph()
    g.parse(filename)
    print(len(g))

    visualize(g)
    print("Oui")

    test_set = []

    # find all subjects of any type
    for s, p, o in g.triples((None, RDF.type, None)):
        # (f"{s} is a {o}")
        test_set.append(o)
    test_set = list(dict.fromkeys(test_set))

    for el in test_set:
        print(el)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    root.title = "RDF Diff"

    source1_button = ttk.Button(
        root,
        text="Sélectionner source n°1",
        command=open_rdf_file
    )

    source2_button = ttk.Button(
        root,
        text="Sélectionner source n°2",
        command=open_rdf_file
    )


    source1_button.grid(column=0, row=0, padx=10, pady=10)
    source2_button.grid(column=2, row=0, padx=10, pady=10)

    def selectTitle(checked):
        print(not checked)

    def applied():
        print("Appliquer")

    title = BooleanVar()
    cb1 = Checkbutton(root, text="Title", onvalue = 1, offvalue = 0, variable=title, bg='#c2af7b', command= lambda : selectTitle(title)).grid(column=0, row=2, padx=90)
    composer = IntVar()
    Checkbutton(root, text="Composer", variable=composer, bg='#c2af7b').grid(column=1, row=2)
    notes = IntVar()
    Checkbutton(root, text="Notes", variable=notes, bg='#c2af7b').grid(column=2, row=2)
    genre = IntVar()
    Checkbutton(root, text="Genre", variable=genre, bg='#c2af7b').grid(column=0, row=3, padx=90)
    key = IntVar()
    Checkbutton(root, text="Key", variable=key, bg='#c2af7b').grid(column=1, row=3)
    opus = IntVar()
    Checkbutton(root, text="Opus", variable=opus, bg='#c2af7b').grid(column=2, row=3)

    Label(root, text="Threshold", bg='#c2af7b').grid(row=4, padx=110)
    e1 = Entry(root)
    e1.grid(row=4, column=1, padx=45)

    jaro = IntVar()
    Checkbutton(root, text="Jaro", variable=jaro, bg='#c2af7b').grid(column=0, row=5, sticky=W)
    Label(root, text="Weighting", bg='#c2af7b').grid(row=5, column=1)
    jaroInput = Entry(root)
    jaroInput.grid(row=5, column=2)

    identity = IntVar()
    Checkbutton(root, text="Identity", variable=identity, bg='#c2af7b').grid(column=0, row=6, sticky=W)
    Label(root, text="Weighting", bg='#c2af7b').grid(row=6, column=1)
    identityInput = Entry(root)
    identityInput.grid(row=6, column=2)

    levenshtein = IntVar()
    Checkbutton(root, text="Levenshtein", variable=levenshtein, bg='#c2af7b').grid(column=0, row=7, sticky=W)
    Label(root, text="Weighting", bg='#c2af7b').grid(row=7, column=1)
    levenshteinInput = Entry(root)
    levenshteinInput.grid(row=7, column=2)

    ngram = IntVar()
    Checkbutton(root, text="Ngram", variable=ngram, bg='#c2af7b').grid(column=0, row=8, sticky=W)
    Label(root, text="Weighting", bg='#c2af7b').grid(row=8, column=1)
    ngramInput = Entry(root)
    ngramInput.grid(row=8, column=2)
    Label(root, text="Size", bg='#c2af7b').grid(row=8, column=3)
    sizeInput = Entry(root)
    sizeInput.grid(row=8, column=4)

    jaccard = IntVar()
    Checkbutton(root, text="Jaccard", variable=jaccard, bg='#c2af7b').grid(column=0, row=9, sticky=W)
    Label(root, text="Weighting", bg='#c2af7b').grid(row=9, column=1)
    jaccardInput = Entry(root)
    jaccardInput.grid(row=9, column=2)

    monge_elkan = IntVar()
    Checkbutton(root, text="Monge Elkan", variable=monge_elkan, bg='#c2af7b').grid(column=0, row=10, sticky=W)
    Label(root, text="Weighting", bg='#c2af7b').grid(row=10, column=1)
    monge_elkanInput = Entry(root)
    monge_elkanInput.grid(row=10, column=2)

    Button(root, text="Applied", bg='#c27ba0', command=applied).grid(row=11, column=2)

    root.mainloop()

    # Save un RDF file
    # g.serialize(destination="tbl.ttl")
