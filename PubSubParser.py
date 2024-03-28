# Generated from PubSub.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,3,1,26,8,1,
        1,1,1,1,3,1,30,8,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,57,0,17,1,0,0,0,2,
        31,1,0,0,0,4,33,1,0,0,0,6,42,1,0,0,0,8,45,1,0,0,0,10,48,1,0,0,0,
        12,51,1,0,0,0,14,58,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,
        0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,
        1,1,0,0,0,23,25,3,4,2,0,24,26,5,1,0,0,25,24,1,0,0,0,25,26,1,0,0,
        0,26,32,1,0,0,0,27,29,3,12,6,0,28,30,5,1,0,0,29,28,1,0,0,0,29,30,
        1,0,0,0,30,32,1,0,0,0,31,23,1,0,0,0,31,27,1,0,0,0,32,3,1,0,0,0,33,
        34,5,2,0,0,34,35,5,3,0,0,35,36,3,6,3,0,36,37,5,4,0,0,37,38,3,8,4,
        0,38,39,5,4,0,0,39,40,3,10,5,0,40,41,5,5,0,0,41,5,1,0,0,0,42,43,
        5,6,0,0,43,44,5,11,0,0,44,7,1,0,0,0,45,46,5,7,0,0,46,47,5,11,0,0,
        47,9,1,0,0,0,48,49,5,8,0,0,49,50,5,11,0,0,50,11,1,0,0,0,51,52,5,
        9,0,0,52,53,5,3,0,0,53,54,3,10,5,0,54,55,5,4,0,0,55,56,3,14,7,0,
        56,57,5,5,0,0,57,13,1,0,0,0,58,59,5,10,0,0,59,60,5,11,0,0,60,15,
        1,0,0,0,4,19,25,29,31
    ]

class PubSubParser ( Parser ):

    grammarFileName = "PubSub.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\n'", "'//@SUB'", "'('", "','", "')'", 
                     "'subscriber_msg_func'", "'void*'", "'const Topic*'", 
                     "'//@PUB'", "'const TopicData*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_parse = 0
    RULE_line = 1
    RULE_subCommand = 2
    RULE_subscriber_msg_func = 3
    RULE_voidPtr = 4
    RULE_topic = 5
    RULE_pubCommand = 6
    RULE_topicData = 7

    ruleNames =  [ "parse", "line", "subCommand", "subscriber_msg_func", 
                   "voidPtr", "topic", "pubCommand", "topicData" ]

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
    ID=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PubSubParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PubSubParser.LineContext)
            else:
                return self.getTypedRuleContext(PubSubParser.LineContext,i)


        def getRuleIndex(self):
            return PubSubParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = PubSubParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.line()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==9):
                    break

            self.state = 21
            self.match(PubSubParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subCommand(self):
            return self.getTypedRuleContext(PubSubParser.SubCommandContext,0)


        def pubCommand(self):
            return self.getTypedRuleContext(PubSubParser.PubCommandContext,0)


        def getRuleIndex(self):
            return PubSubParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = PubSubParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.subCommand()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 24
                    self.match(PubSubParser.T__0)


                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.pubCommand()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 28
                    self.match(PubSubParser.T__0)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subscriber_msg_func(self):
            return self.getTypedRuleContext(PubSubParser.Subscriber_msg_funcContext,0)


        def voidPtr(self):
            return self.getTypedRuleContext(PubSubParser.VoidPtrContext,0)


        def topic(self):
            return self.getTypedRuleContext(PubSubParser.TopicContext,0)


        def getRuleIndex(self):
            return PubSubParser.RULE_subCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubCommand" ):
                listener.enterSubCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubCommand" ):
                listener.exitSubCommand(self)




    def subCommand(self):

        localctx = PubSubParser.SubCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(PubSubParser.T__1)
            self.state = 34
            self.match(PubSubParser.T__2)
            self.state = 35
            self.subscriber_msg_func()
            self.state = 36
            self.match(PubSubParser.T__3)
            self.state = 37
            self.voidPtr()
            self.state = 38
            self.match(PubSubParser.T__3)
            self.state = 39
            self.topic()
            self.state = 40
            self.match(PubSubParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subscriber_msg_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.msg_func = None # Token

        def ID(self):
            return self.getToken(PubSubParser.ID, 0)

        def getRuleIndex(self):
            return PubSubParser.RULE_subscriber_msg_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscriber_msg_func" ):
                listener.enterSubscriber_msg_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscriber_msg_func" ):
                listener.exitSubscriber_msg_func(self)




    def subscriber_msg_func(self):

        localctx = PubSubParser.Subscriber_msg_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subscriber_msg_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(PubSubParser.T__5)
            self.state = 43
            localctx.msg_func = self.match(PubSubParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidPtrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.msg_arg = None # Token

        def ID(self):
            return self.getToken(PubSubParser.ID, 0)

        def getRuleIndex(self):
            return PubSubParser.RULE_voidPtr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidPtr" ):
                listener.enterVoidPtr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidPtr" ):
                listener.exitVoidPtr(self)




    def voidPtr(self):

        localctx = PubSubParser.VoidPtrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_voidPtr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(PubSubParser.T__6)
            self.state = 46
            localctx.msg_arg = self.match(PubSubParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.topicName = None # Token

        def ID(self):
            return self.getToken(PubSubParser.ID, 0)

        def getRuleIndex(self):
            return PubSubParser.RULE_topic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopic" ):
                listener.enterTopic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopic" ):
                listener.exitTopic(self)




    def topic(self):

        localctx = PubSubParser.TopicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_topic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(PubSubParser.T__7)
            self.state = 49
            localctx.topicName = self.match(PubSubParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PubCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topic(self):
            return self.getTypedRuleContext(PubSubParser.TopicContext,0)


        def topicData(self):
            return self.getTypedRuleContext(PubSubParser.TopicDataContext,0)


        def getRuleIndex(self):
            return PubSubParser.RULE_pubCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPubCommand" ):
                listener.enterPubCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPubCommand" ):
                listener.exitPubCommand(self)




    def pubCommand(self):

        localctx = PubSubParser.PubCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pubCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(PubSubParser.T__8)
            self.state = 52
            self.match(PubSubParser.T__2)
            self.state = 53
            self.topic()
            self.state = 54
            self.match(PubSubParser.T__3)
            self.state = 55
            self.topicData()
            self.state = 56
            self.match(PubSubParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopicDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dataName = None # Token

        def ID(self):
            return self.getToken(PubSubParser.ID, 0)

        def getRuleIndex(self):
            return PubSubParser.RULE_topicData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopicData" ):
                listener.enterTopicData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopicData" ):
                listener.exitTopicData(self)




    def topicData(self):

        localctx = PubSubParser.TopicDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_topicData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(PubSubParser.T__9)
            self.state = 59
            localctx.dataName = self.match(PubSubParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





