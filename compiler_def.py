if "." in __name__:
    from .PythonParser import PythonParser
    from .PythonParserVisitor import PythonParserVisitor
else:
    from PythonParser import PythonParser
    from PythonParserVisitor import PythonParserVisitor
class Compiler(PythonParserVisitor):
    def __init__(self):
        super(Compiler, self).__init__()
        self.vars = {}
        return None

   # Visit a parse tree produced by PythonParser#code.
    def visitCode(self, ctx:PythonParser.CodeContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#query.
    def visitQuery(self, ctx:PythonParser.QueryContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#conditional.
    def visitConditional(self, ctx:PythonParser.ConditionalContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#function.
    def visitFunction(self, ctx:PythonParser.FunctionContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#function_call.
    def visitFunction_call(self, ctx:PythonParser.Function_callContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#while.
    def visitWhile(self, ctx:PythonParser.WhileContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#for.
    def visitFor(self, ctx:PythonParser.ForContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

del (PythonParser, PythonParserVisitor)
