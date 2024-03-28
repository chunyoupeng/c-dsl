import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class SpecialCommentListener extends CBaseListener {

    private TokenStreamRewriter rewriter;
    private Set<Token> processedTokens;

    public SpecialCommentListener(BufferedTokenStream tokens) {
        this.rewriter = new TokenStreamRewriter(tokens);
        this.processedTokens = new HashSet<>();
    }

    @Override
    public void enterEveryRule(ParserRuleContext ctx) {
        for (int i = 0; i < rewriter.getTokenStream().size(); i++) {
            Token token = rewriter.getTokenStream().get(i);
            if (token.getChannel() == Lexer.HIDDEN && token.getType() == CParser.SpecialComment) {
                // 检查是否已经处理过这个令牌
                if (!processedTokens.contains(token)) {
                    processedTokens.add(token);
                    String commentText = token.getText();
		    // System.out.println("commentTest is " + commentText);
		    String rt = runPython(commentText);
		    // System.out.println("The result after python is " + rt);
		    rewriter.replace(token, rt);
                }
            }
        }
    }

    public String getResult() {
        return rewriter.getText();
    }
public String runPython(String text){
    StringBuilder output = new StringBuilder(); // 使用StringBuilder来累积输出
    try {
        String[] cmd = {
            "python",
            "main.py",
            text,
        };
        Process p = Runtime.getRuntime().exec(cmd);

        // 正常输出
        BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String line;
        while ((line = stdInput.readLine()) != null) {
            // System.out.println("Output is: " + line);
            output.append(line).append("\n"); // 累加输出并添加换行符
        }

        // 错误输出
        BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
        while ((line = stdError.readLine()) != null) {
            System.out.println("Error: " + line);
            output.append(line).append("\n"); // 同样累加错误输出
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
    return output.toString(); // 返回累积的输出结果
}



}
