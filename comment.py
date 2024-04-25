from antlr4 import *
from PubSubLexer import PubSubLexer
from PubSubParser import PubSubParser
from PubSubListener import PubSubListener
import sys

class PubSubCodeGenerator(PubSubListener):
    def enterSubCommand(self, ctx):
        msg_func = ctx.subscriber_msg_func().msg_func.text
        msg_arg = ctx.voidPtr().msg_arg.text
        topic_name = ctx.topic().topicName.text
        print(f"Subscriber* sub = new_Subscriber({msg_func}, {msg_arg});")
        print("Subscriber_init(sub);")
        print(f"Subscriber_sub(sub, &{topic_name});")
        print("Subscriber_start(sub);")

    def enterPubCommand(self, ctx):
        topic_data_name = ctx.topicData().dataName.text
        print("Publisher* pub = new_Publisher();")
        print(f"Publisher_pub(pub, &{topic_data_name});")


def handle_input(input_string):
    input_stream = InputStream(input_string)
    lexer = PubSubLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PubSubParser(stream)
    tree = parser.parse()  # Assuming 'prog' is the entry point of your parser.

    walker = ParseTreeWalker()
    listener = PubSubCodeGenerator()
    walker.walk(listener, tree)

# Example usage
if __name__ == '__main__':
    input_string = sys.argv[1]
    handle_input(input_string)
