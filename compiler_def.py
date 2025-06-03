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
        print(('Bem vindo ao code', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        print(('Bem vindo ao stat', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#query.
    def visitQuery(self, ctx:PythonParser.QueryContext):
        print(('Bem vindo ao query', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#conditional.
    def visitConditional(self, ctx:PythonParser.ConditionalContext):
        print(('Bem vindo ao conditional', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#function.
    def visitFunction(self, ctx:PythonParser.FunctionContext):
        print(('Bem vindo ao Function', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#function_call.
    def visitFunction_call(self, ctx:PythonParser.Function_callContext):
        print(('Bem vindo ao function call', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#while.
    def visitWhile(self, ctx:PythonParser.WhileContext):
        print(('Bem vindo ao while', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#for.
    def visitFor(self, ctx:PythonParser.ForContext):
        print(('Bem vindo ao for', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        if self.visitChildren(ctx)

        context = ctx.getText
        OPERATORS = ['+', '-', '*', '/', '**', '%']

        if context.isidenfier():
        class Compiler(PythonParserVisitor):
            def visitExpr(self, ctx: PythonParser.ExprContext):
                if context.isidentifier():
                    return self.visitID(ctx)

                elif context[0].isnumeric():
                    #É um inteiro
                    return self.visitINT(ctx)

                elif context == "None"
                    #É um None
                    return self.visitNone(ctx)

                elif any(op is contxt for op in OPERATORS):
                    return self.visitOperations(ctx)
                

        return self.visitChildren(ctx)

    def visitID(self, ctx:PythonParser.ExprContext):
        return self.visitChildren(ctx)


    def visitOperations(self, ctx:PythonParser.ExprContext):
        context = ctx.getText
        if '+' in context:
            a, b = context.split('+')
            output =  int(a) + int(b)

        elif '-' in context:
            a, b = context.split('-')
            output =  int(a) - int(b)

        elif '*' in context:
            a, b = context.split('*')
            output =  int(a) * int(b)

        elif '/' in context:
            a, b = context.split('/')
            output =  int(a) / int(b)

        elif '**' in context:
            a, b = context.split('**')
            output =  int(a) ** int(b)

        elif '%' in context:
            a, b = context.split('%')
            output =  int(a) % int(b)
        return output

del (PythonParser, PythonParserVisitor)
