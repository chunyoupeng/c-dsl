import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        // 使用 CharStreams 从标准输入中读取数据
        CharStream input = CharStreams.fromStream(System.in);

        CLexer lexer = new CLexer(input);

	CommonTokenStream tokens = new CommonTokenStream(lexer);
        CParser parser = new CParser(tokens);

        ParseTree tree = parser.compilationUnit(); // 或其他适当的起始规则
        ParseTreeWalker walker = new ParseTreeWalker();

        SpecialCommentListener listener = new SpecialCommentListener(tokens, args[0]);
        walker.walk(listener, tree);

        // 输出处理后的代码
        System.out.println(listener.getResult());


    }
}
