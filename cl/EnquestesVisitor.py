# Generated from Enquestes.g by ANTLR 4.7.2
from antlr4 import *
import networkx as nx
import matplotlib.pyplot as plt
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitor(ParseTreeVisitor):

    def __init__(self):
        self.ast = nx.DiGraph()
        self.items = {}
        self.enquestes = {}

    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        self.visitChildren(ctx)
        return self.ast

    # Visit a parse tree produced by EnquestesParser#expr.
    def visitExpr(self, ctx:EnquestesParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        #   Crear nodo Px con su respectiva pregunta

        g = ctx.getChildren()   #   obtenir els fills [ID : PREGUNTA text*]
        fills = ctx.getChildCount()
        l = [next(g) for i in range(fills)]
        
        q = [x.getText() for x in l[3:]]
        self.ast.add_node(l[0].getText(), content = q)

    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        #   Crear nodo Rx con sus respuestas
        g = ctx.getChildren()   #   obtenir els fills [ID : RESPOSTA opcio*]
        fills = ctx.getChildCount()
        l = [next(g) for i in range(fills)]

        q = [self.visit(x) for x in l[3:]]
        self.ast.add_node(l[0].getText(), content = q)

    # Visit a parse tree produced by EnquestesParser#item.
    def visitItem(self, ctx:EnquestesParser.ItemContext):
        #   Crear arista entre Px y Rx con Ix como tag
        g = ctx.getChildren()   #   obtenir els fills [ID ':' 'ITEM' assig]
        fills = ctx.getChildCount()
        l = [next(g) for i in range(fills)]

        a1, a2 = self.visit(l[3])
        item = l[0].getText()

        self.items[item] = (a1,a2)   #   Ix = (Px,Rx)
        self.ast.add_edge(a1,a2, tag = item, color ='blue')

    # Visit a parse tree produced by EnquestesParser#alternativa.
    def visitAlternativa(self, ctx:EnquestesParser.AlternativaContext):
        #   Crear arista entre Px y cada Pi alternativa con tag dado
        g = ctx.getChildren()   #obtenir els fills [ID ':' 'ALTERNATIVA' ID '[' alt ']']
        l = [next(g) for i in range(ctx.getChildCount())]
        item = l[3].getText()

        node = self.items[item][0]
        alts = self.visit(l[5])
        for i in range(0,len(alts),2):
            tag, aux = self.visit(alts[i])
            aux = self.items[aux][0]
            self.ast.add_edge(node, aux, tag = tag, color = 'green')
        

    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx:EnquestesParser.EnquestaContext):
        g = ctx.getChildren() #obtenir els fills [ID ':' 'ENQUESTA' ID*]
        fills = ctx.getChildCount()
        l = [(next(g)).getText() for i in range(fills)]
        pre = l[0]
        suc = self.items[l[3]][0]
        self.ast.add_edge(pre, suc, color='black', tag="")
        pre = suc
        for i in range(4,fills):
            suc = self.items[l[i]][0]
            self.ast.add_edge(pre,suc, color='black', tag="")
            pre = suc

        self.ast.add_edge(pre, 'END', color='black', tag="")

    # Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx:EnquestesParser.OpcioContext):
        g = ctx.getChildren()   #obtenir els fills [NUMBER ':' TEXT* ';']
        l = [next(g) for i in range(ctx.getChildCount())]
        return [x.getText() for x in l[2:-1]]

    # Visit a parse tree produced by EnquestesParser#assig.
    def visitAssig(self, ctx:EnquestesParser.AssigContext):
        g = ctx.getChildren()   #obtenir els fills [ID '->' ID]
        l = [next(g) for i in range(ctx.getChildCount())]
        return l[0].getText(), l[2].getText()

    # Visit a parse tree produced by EnquestesParser#alt.
    def visitAlt(self, ctx:EnquestesParser.AltContext):
        g = ctx.getChildren() #obtenir els fills [new (',' new)*]
        fills = ctx.getChildCount()
        l = [next(g) for i in range(fills)]

        return l

    # Visit a parse tree produced by EnquestesParser#new.
    def visitNew(self, ctx:EnquestesParser.NewContext):
        g = ctx.getChildren()
        fills = ctx.getChildCount()
        l = [next(g).getText() for i in range(fills)]

        return l[1],l[3]
#del EnquestesParser
