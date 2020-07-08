import sys
from antlr4 import *
import networkx as nx
import matplotlib.pyplot as plt
import pickle

from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from EnquestesVisitor import EnquestesVisitor


if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
else:
    input_stream = InputStream(input('? '))

lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = EnquestesParser(token_stream)

tree = parser.root()

visitor = EnquestesVisitor()
graph = visitor.visit(tree)


pos = nx.circular_layout(graph)
nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'), 
                       node_color = 'lightblue', node_size = 500)

nx.draw_networkx_labels(graph, pos)

edge_labels = nx.get_edge_attributes(graph,'tag')

nx.draw_networkx_edge_labels(graph, pos, edge_labels, font_color = 'black', font_size = 7)
nx.draw_networkx_edges(graph, pos, edge_color = [graph[i][j]['color'] for (i,j) in graph.edges()])

#nx.draw_networkx_edges(graph, pos, edgelist=red_edges, edge_color='r', arrows=True)
enquestes =  {}
pickle_out = open('enq.pickle','wb')
pickle.dump(enquestes,pickle_out)
pickle_out.close()

#nx.draw_networkx_edges(graph, pos, edgelist=black_edges, arrows=False)
#plt.show()
nx.write_gpickle(graph, "graph.gpickle")
