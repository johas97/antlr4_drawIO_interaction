import antlr4
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser

class ParseTreeExtractor:
    def __init__(self, tree):
        self.tree = tree

    def __str__(self):
        return self.tree_string(self.tree, "")

    def tree_string(self, node, prefix: str):
        if isinstance(node, Python3Parser.Star_exprContext) and node.getChildCount() == 1:
            return self.visit_primary(node)
        if isinstance(node, TerminalNode):
            return self.visit_terminal(node)
        if not isinstance(node, RuleNode):
            return ""

        name = Python3Parser.ruleNames[node.getRuleContext().getRuleIndex()]
        builder = [name]
        for i in range(node.getChildCount()):
            at_end = (i == node.getChildCount() - 1)
            symbol = "└──" if at_end else "├──"
            child = node.getChild(i)
            child_symbol = "   " if at_end else "│   "
            child_str = self.tree_string(child, f"{prefix}{child_symbol}")
            builder.append(f"\n{prefix}{symbol} {child_str}")

        return "".join(builder)

    def visit_primary(self, node: Python3Parser.Star_exprContext):
        name = Python3Parser.ruleNames[node.getRuleContext().getRuleIndex()]
        child_str = self.visit_terminal(node.getChild(0))
        return f"{name} ── {child_str}"

    def visit_terminal(self, node: TerminalNode):
        id = Python3Lexer.ruleNames[node.symbol.type - 1]
        id = 'P' if "T__" in id else id[0]
        return f"{id}'{node}'"
