# Generated from Enquestes.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("l\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32\n\2")
        buf.write("\f\2\16\2\35\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3&\n\3")
        buf.write("\3\4\3\4\3\4\3\4\7\4,\n\4\f\4\16\4/\13\4\3\5\3\5\3\5\3")
        buf.write("\5\7\5\65\n\5\f\5\16\58\13\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7\bK\n\b\f")
        buf.write("\b\16\bN\13\b\3\t\3\t\3\t\7\tS\n\t\f\t\16\tV\13\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13a\n\13\f\13\16")
        buf.write("\13d\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\2\2\2j\2\33\3\2\2\2\4%\3\2\2\2\6\'\3")
        buf.write("\2\2\2\b\60\3\2\2\2\n9\3\2\2\2\f>\3\2\2\2\16F\3\2\2\2")
        buf.write("\20O\3\2\2\2\22Y\3\2\2\2\24]\3\2\2\2\26e\3\2\2\2\30\32")
        buf.write("\5\4\3\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\36\3\2\2\2\35\33\3\2\2\2\36\37\7\3\2\2")
        buf.write("\37\3\3\2\2\2 &\5\6\4\2!&\5\b\5\2\"&\5\n\6\2#&\5\f\7\2")
        buf.write("$&\5\16\b\2% \3\2\2\2%!\3\2\2\2%\"\3\2\2\2%#\3\2\2\2%")
        buf.write("$\3\2\2\2&\5\3\2\2\2\'(\7\21\2\2()\7\4\2\2)-\7\5\2\2*")
        buf.write(",\7\23\2\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\7")
        buf.write("\3\2\2\2/-\3\2\2\2\60\61\7\21\2\2\61\62\7\4\2\2\62\66")
        buf.write("\7\6\2\2\63\65\5\20\t\2\64\63\3\2\2\2\658\3\2\2\2\66\64")
        buf.write("\3\2\2\2\66\67\3\2\2\2\67\t\3\2\2\28\66\3\2\2\29:\7\21")
        buf.write("\2\2:;\7\4\2\2;<\7\7\2\2<=\5\22\n\2=\13\3\2\2\2>?\7\21")
        buf.write("\2\2?@\7\4\2\2@A\7\b\2\2AB\7\21\2\2BC\7\t\2\2CD\5\24\13")
        buf.write("\2DE\7\n\2\2E\r\3\2\2\2FG\7\21\2\2GH\7\4\2\2HL\7\13\2")
        buf.write("\2IK\7\21\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2")
        buf.write("M\17\3\2\2\2NL\3\2\2\2OP\7\22\2\2PT\7\4\2\2QS\7\23\2\2")
        buf.write("RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3")
        buf.write("\2\2\2WX\7\f\2\2X\21\3\2\2\2YZ\7\21\2\2Z[\7\r\2\2[\\\7")
        buf.write("\21\2\2\\\23\3\2\2\2]b\5\26\f\2^_\7\16\2\2_a\5\26\f\2")
        buf.write("`^\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\25\3\2\2\2d")
        buf.write("b\3\2\2\2ef\7\17\2\2fg\7\22\2\2gh\7\16\2\2hi\7\21\2\2")
        buf.write("ij\7\20\2\2j\27\3\2\2\2\t\33%-\66LTb")
        return buf.getvalue()


class EnquestesParser ( Parser ):

    grammarFileName = "Enquestes.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'END'", "':'", "'PREGUNTA'", "'RESPOSTA'", 
                     "'ITEM'", "'ALTERNATIVA'", "'['", "']'", "'ENQUESTA'", 
                     "';'", "'->'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "TEXT", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_pregunta = 2
    RULE_resposta = 3
    RULE_item = 4
    RULE_alternativa = 5
    RULE_enquesta = 6
    RULE_opcio = 7
    RULE_assig = 8
    RULE_alt = 9
    RULE_new = 10

    ruleNames =  [ "root", "expr", "pregunta", "resposta", "item", "alternativa", 
                   "enquesta", "opcio", "assig", "alt", "new" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ID=15
    NUMBER=16
    TEXT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.ExprContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.ExprContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = EnquestesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.ID:
                self.state = 22
                self.expr()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(EnquestesParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pregunta(self):
            return self.getTypedRuleContext(EnquestesParser.PreguntaContext,0)


        def resposta(self):
            return self.getTypedRuleContext(EnquestesParser.RespostaContext,0)


        def item(self):
            return self.getTypedRuleContext(EnquestesParser.ItemContext,0)


        def alternativa(self):
            return self.getTypedRuleContext(EnquestesParser.AlternativaContext,0)


        def enquesta(self):
            return self.getTypedRuleContext(EnquestesParser.EnquestaContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = EnquestesParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 30
                self.pregunta()
                pass

            elif la_ == 2:
                self.state = 31
                self.resposta()
                pass

            elif la_ == 3:
                self.state = 32
                self.item()
                pass

            elif la_ == 4:
                self.state = 33
                self.alternativa()
                pass

            elif la_ == 5:
                self.state = 34
                self.enquesta()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PreguntaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.TEXT)
            else:
                return self.getToken(EnquestesParser.TEXT, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_pregunta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPregunta" ):
                return visitor.visitPregunta(self)
            else:
                return visitor.visitChildren(self)




    def pregunta(self):

        localctx = EnquestesParser.PreguntaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pregunta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(EnquestesParser.ID)
            self.state = 38
            self.match(EnquestesParser.T__1)
            self.state = 39
            self.match(EnquestesParser.T__2)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.TEXT:
                self.state = 40
                self.match(EnquestesParser.TEXT)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RespostaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def opcio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.OpcioContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.OpcioContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_resposta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResposta" ):
                return visitor.visitResposta(self)
            else:
                return visitor.visitChildren(self)




    def resposta(self):

        localctx = EnquestesParser.RespostaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resposta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(EnquestesParser.ID)
            self.state = 47
            self.match(EnquestesParser.T__1)
            self.state = 48
            self.match(EnquestesParser.T__3)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.NUMBER:
                self.state = 49
                self.opcio()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def assig(self):
            return self.getTypedRuleContext(EnquestesParser.AssigContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EnquestesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(EnquestesParser.ID)
            self.state = 56
            self.match(EnquestesParser.T__1)
            self.state = 57
            self.match(EnquestesParser.T__4)
            self.state = 58
            self.assig()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlternativaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def alt(self):
            return self.getTypedRuleContext(EnquestesParser.AltContext,0)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alternativa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternativa" ):
                return visitor.visitAlternativa(self)
            else:
                return visitor.visitChildren(self)




    def alternativa(self):

        localctx = EnquestesParser.AlternativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_alternativa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(EnquestesParser.ID)
            self.state = 61
            self.match(EnquestesParser.T__1)
            self.state = 62
            self.match(EnquestesParser.T__5)
            self.state = 63
            self.match(EnquestesParser.ID)
            self.state = 64
            self.match(EnquestesParser.T__6)
            self.state = 65
            self.alt()
            self.state = 66
            self.match(EnquestesParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnquestaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_enquesta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnquesta" ):
                return visitor.visitEnquesta(self)
            else:
                return visitor.visitChildren(self)




    def enquesta(self):

        localctx = EnquestesParser.EnquestaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_enquesta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(EnquestesParser.ID)
            self.state = 69
            self.match(EnquestesParser.T__1)
            self.state = 70
            self.match(EnquestesParser.T__8)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 71
                    self.match(EnquestesParser.ID) 
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OpcioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(EnquestesParser.NUMBER, 0)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.TEXT)
            else:
                return self.getToken(EnquestesParser.TEXT, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_opcio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcio" ):
                return visitor.visitOpcio(self)
            else:
                return visitor.visitChildren(self)




    def opcio(self):

        localctx = EnquestesParser.OpcioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opcio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(EnquestesParser.NUMBER)
            self.state = 78
            self.match(EnquestesParser.T__1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.TEXT:
                self.state = 79
                self.match(EnquestesParser.TEXT)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(EnquestesParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(EnquestesParser.ID)
            else:
                return self.getToken(EnquestesParser.ID, i)

        def getRuleIndex(self):
            return EnquestesParser.RULE_assig

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)




    def assig(self):

        localctx = EnquestesParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(EnquestesParser.ID)
            self.state = 88
            self.match(EnquestesParser.T__10)
            self.state = 89
            self.match(EnquestesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AltContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def new(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnquestesParser.NewContext)
            else:
                return self.getTypedRuleContext(EnquestesParser.NewContext,i)


        def getRuleIndex(self):
            return EnquestesParser.RULE_alt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlt" ):
                return visitor.visitAlt(self)
            else:
                return visitor.visitChildren(self)




    def alt(self):

        localctx = EnquestesParser.AltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_alt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.new()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==EnquestesParser.T__11:
                self.state = 92
                self.match(EnquestesParser.T__11)
                self.state = 93
                self.new()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NewContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(EnquestesParser.NUMBER, 0)

        def ID(self):
            return self.getToken(EnquestesParser.ID, 0)

        def getRuleIndex(self):
            return EnquestesParser.RULE_new

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew" ):
                return visitor.visitNew(self)
            else:
                return visitor.visitChildren(self)




    def new(self):

        localctx = EnquestesParser.NewContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_new)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(EnquestesParser.T__12)
            self.state = 100
            self.match(EnquestesParser.NUMBER)
            self.state = 101
            self.match(EnquestesParser.T__11)
            self.state = 102
            self.match(EnquestesParser.ID)
            self.state = 103
            self.match(EnquestesParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





