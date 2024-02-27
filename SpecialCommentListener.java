import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;


public class SpecialCommentListener extends CBaseListener {

    String rocketStruct = 
	"\n \ntypedef struct {\n" +
	"    char name[50];          // 火箭的名称\n" +
	"    double height;          // 火箭的高度（米）\n" +
	"    double weight;          // 火箭的重量（千克）\n" +
	"    double thrust;          // 火箭的推力（牛顿）\n" +
	"    double fuelCapacity;    // 燃料容量（升）\n" +
	"    int numberOfEngines;    // 发动机数量\n" +
	"    char engineType[30];    // 发动机类型\n" +
	"    double maxAltitude;     // 最大飞行高度（米）\n" +
	"    char missionType[50];   // 任务类型（例如，载人、卫星发射等）\n" +
	"    bool isReusable;        // 是否可重复使用\n" +
	"} Rocket;\n//@height";

    String missileStruct = 
	"\ntypedef struct {\n" +
	"    char name[50];         // 导弹的名称\n" +
	"    double length;         // 导弹的长度（米）\n" +
	"    double diameter;       // 导弹的直径（米）\n" +
	"    double weight;         // 导弹的重量（千克）\n" +
	"    double range;          // 射程（千米）\n" +
	"    double speed;          // 速度（马赫）\n" +
	"    char warheadType[30];  // 弹头类型\n" +
	"    double warheadWeight;  // 弹头重量（千克）\n" +
	"    char guidanceSystem[50]; // 导引系统\n" +
	"} Missile;\n";

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
		    System.out.println("commentTest is " + commentText);
		    String structToInsert = getStructToInsert(commentText);
		    String nestedString = "";
		    // 对插入的结构体进行解析，查找并处理嵌套的特殊注释
		    // try {
		    // 	nestedString = parseAndProcessNestedComments(structToInsert);
		    // } catch (IOException e) {
		    // 	e.printStackTrace(); // 或其他错误处理逻辑
		    // }
		    rewriter.replace(token, structToInsert);
		    
                }
            }
        }
    }

    public String getResult() {
        return rewriter.getText();
    }

    private String getStructToInsert(String commentText) {
	if (commentText.contains("rocket")) {
	    return rocketStruct; // 替换为实际的结构体定义
	} 
	// else if (commentText.contains("missile")) {
	//     return missileStruct; // 替换为实际的结构体定义
	// } 
	else if (commentText.contains("height")) {
	    return "\n float height = 100;";
	}
	return ""; // 如果没有匹配的特殊注释，返回空字符串
    }


private String parseAndProcessNestedComments(String struct) throws IOException {
    System.out.println("Entering nest");
    System.out.println("The struct to be processed is " + struct);
    InputStream stream = new ByteArrayInputStream(struct.getBytes(StandardCharsets.UTF_8));
    CharStream input = CharStreams.fromStream(stream);

    CLexer lexer = new CLexer(input);
    CommonTokenStream tokens = new CommonTokenStream(lexer);
    CParser parser = new CParser(tokens);

    // 只处理struct部分，而不是整个文本
    CParser.CompilationUnitContext structCtx = parser.compilationUnit();

    // 创建一个新的TokenStreamRewriter，以防影响当前的TokenStreamRewriter
    TokenStreamRewriter nestedRewriter = new TokenStreamRewriter(tokens);

    SpecialCommentListener nestedListener = new SpecialCommentListener(tokens);
    nestedListener.rewriter = nestedRewriter; // 设置新的TokenStreamRewriter

    ParseTreeWalker walker = new ParseTreeWalker();
    walker.walk(nestedListener, structCtx);

    // 输出处理后的代码
    System.out.println("The resulting code is " + nestedListener.getResult());
    System.out.println("Ending nest");
    return nestedListener.getResult();
}

//     private String parseAndProcessNestedComments(String struct) throws IOException {


// 	System.out.println("Entering nest");
// 	System.out.println("The struct to be processed is " + struct);
// 	InputStream stream = new ByteArrayInputStream(struct.getBytes(StandardCharsets.UTF_8));
//         CharStream input = CharStreams.fromStream(stream);

//         CLexer lexer = new CLexer(input);

// 	CommonTokenStream tokens = new CommonTokenStream(lexer);
//         CParser parser = new CParser(tokens);

//         ParseTree tree = parser.compilationUnit(); // 或其他适当的起始规则
//         ParseTreeWalker walker = new ParseTreeWalker();

//         walker.walk(this, tree);

//         // 输出处理后的代码
//         System.out.println("The resulting code is " + this.getResult()); 
// 	System.out.println("Ending nest");
// 	return this.getResult();
//     }

}
