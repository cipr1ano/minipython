# Generated from PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete generic visitor for a parse tree produced by PythonParser.

class PythonParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonParser#code.
    def visitCode(self, ctx:PythonParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#stat.
    def visitStat(self, ctx:PythonParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#query.
    def visitQuery(self, ctx:PythonParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#conditional.
    def visitConditional(self, ctx:PythonParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#function.
    def visitFunction(self, ctx:PythonParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#function_call.
    def visitFunction_call(self, ctx:PythonParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#while.
    def visitWhile(self, ctx:PythonParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#for.
    def visitFor(self, ctx:PythonParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonParser#expr.
    def visitExpr(self, ctx:PythonParser.ExprContext):
        return self.visitChildren(ctx)



del PythonParser