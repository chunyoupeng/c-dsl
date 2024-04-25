# 使用方法

## 先调主程序部份
```sh
antlr4 C.g4
rm -rf *.class
java *.java
java Main . < test.c
```
> 第一个参数是当前路径，因为要配合vscode插件的编写。

## 把java部分打包成`jar`

```sh
jar cfm comment.jar MANIFEST.MF *.class
java -jar comment.jar . < test.c
```

## 把所有代码打包成一个vscode插件

```sh
npm install -g vsce
vsce package
```
>生成一个.vsix文件。之后在vscode插件里面安装.