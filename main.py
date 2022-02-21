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
    rdf2dot(g, stream, opts = {display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue
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
        #(f"{s} is a {o}")
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
    source2_button.grid(column=0, row=1, padx=10, pady=10)

    root.mainloop()

    #Save un RDF file
    #g.serialize(destination="tbl.ttl")
