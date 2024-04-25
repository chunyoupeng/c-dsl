# Generated from PubSub.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PubSubParser import PubSubParser
else:
    from PubSubParser import PubSubParser

# This class defines a complete listener for a parse tree produced by PubSubParser.
class PubSubListener(ParseTreeListener):

    # Enter a parse tree produced by PubSubParser#parse.
    def enterParse(self, ctx:PubSubParser.ParseContext):
        pass

    # Exit a parse tree produced by PubSubParser#parse.
    def exitParse(self, ctx:PubSubParser.ParseContext):
        pass


    # Enter a parse tree produced by PubSubParser#line.
    def enterLine(self, ctx:PubSubParser.LineContext):
        pass

    # Exit a parse tree produced by PubSubParser#line.
    def exitLine(self, ctx:PubSubParser.LineContext):
        pass


    # Enter a parse tree produced by PubSubParser#subCommand.
    def enterSubCommand(self, ctx:PubSubParser.SubCommandContext):
        pass

    # Exit a parse tree produced by PubSubParser#subCommand.
    def exitSubCommand(self, ctx:PubSubParser.SubCommandContext):
        pass


    # Enter a parse tree produced by PubSubParser#subscriber_msg_func.
    def enterSubscriber_msg_func(self, ctx:PubSubParser.Subscriber_msg_funcContext):
        pass

    # Exit a parse tree produced by PubSubParser#subscriber_msg_func.
    def exitSubscriber_msg_func(self, ctx:PubSubParser.Subscriber_msg_funcContext):
        pass


    # Enter a parse tree produced by PubSubParser#voidPtr.
    def enterVoidPtr(self, ctx:PubSubParser.VoidPtrContext):
        pass

    # Exit a parse tree produced by PubSubParser#voidPtr.
    def exitVoidPtr(self, ctx:PubSubParser.VoidPtrContext):
        pass


    # Enter a parse tree produced by PubSubParser#topic.
    def enterTopic(self, ctx:PubSubParser.TopicContext):
        pass

    # Exit a parse tree produced by PubSubParser#topic.
    def exitTopic(self, ctx:PubSubParser.TopicContext):
        pass


    # Enter a parse tree produced by PubSubParser#pubCommand.
    def enterPubCommand(self, ctx:PubSubParser.PubCommandContext):
        pass

    # Exit a parse tree produced by PubSubParser#pubCommand.
    def exitPubCommand(self, ctx:PubSubParser.PubCommandContext):
        pass


    # Enter a parse tree produced by PubSubParser#topicData.
    def enterTopicData(self, ctx:PubSubParser.TopicDataContext):
        pass

    # Exit a parse tree produced by PubSubParser#topicData.
    def exitTopicData(self, ctx:PubSubParser.TopicDataContext):
        pass



del PubSubParser