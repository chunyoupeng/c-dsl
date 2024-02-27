import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.util.Scanner;
import java.io.IOException;
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;
import java.io.InputStreamReader;
public class Main {

    public static String rec(String text) throws IOException{
	if (!text.contains("//@")) return text;
	    InputStream stream = new ByteArrayInputStream(text.getBytes(StandardCharsets.UTF_8));
        CharStream input = CharStreams.fromStream(stream);

        CLexer lexer = new CLexer(input);

	CommonTokenStream tokens = new CommonTokenStream(lexer);
        CParser parser = new CParser(tokens);

        ParseTree tree = parser.compilationUnit(); // 或其他适当的起始规则
        ParseTreeWalker walker = new ParseTreeWalker();

        SpecialCommentListener listener = new SpecialCommentListener(tokens);
        walker.walk(listener, tree);
	var rt = listener.getResult();
	return rec(rt);
    }


    public static void main(String[] args) throws IOException {
	InputStreamReader reader = new InputStreamReader(System.in);


        StringBuilder inputStringBuilder = new StringBuilder();
        int charCode;
        while ((charCode = reader.read()) != -1) {
            char currentChar = (char) charCode;
            inputStringBuilder.append(currentChar);
        }

        // Convert StringBuilder to String
        String inputString = inputStringBuilder.toString();
	// System.out.println("Input string is " + inputString);
	String rt = "";
	try {
	    rt = rec(inputString);
	} catch (IOException e){
	    e.printStackTrace();
	    System.out.println("Some Error happen");
	}
	System.out.println(rt);
        // 使用 CharStreams 从标准输入中读取数据
        // CharStream input = CharStreams.fromStream(System.in);

        // CLexer lexer = new CLexer(input);

	// CommonTokenStream tokens = new CommonTokenStream(lexer);
        // CParser parser = new CParser(tokens);

        // ParseTree tree = parser.compilationUnit(); // 或其他适当的起始规则
        // ParseTreeWalker walker = new ParseTreeWalker();

        // SpecialCommentListener listener = new SpecialCommentListener(tokens);
        // walker.walk(listener, tree);

        // 输出处理后的代码
        // System.out.println(listener.getResult());
	
    }
}
