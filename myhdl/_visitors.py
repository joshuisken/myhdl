import ast

from myhdl import AlwaysCombError
from myhdl._Signal import _Signal, _isListOfSigs

class _error:
    pass

_error.ArgType = "always_comb argument should be a classic function"
_error.NrOfArgs = "always_comb argument should be a function without arguments"
_error.Scope = "always_comb argument should be a local function"
_error.SignalAsInout = "signal (%s) used as inout in always_comb function argument"
_error.EmbeddedFunction = "embedded functions in always_comb function argument not supported"
_error.EmptySensitivityList= "sensitivity list is empty"

INPUT, OUTPUT, INOUT = range(3)



class _SigNameVisitor(ast.NodeVisitor):
    def __init__(self, symdict):
        self.inputs = set()
        self.outputs = set()
        self.toplevel = 1
        self.symdict = symdict
        self.context = INPUT

    def visit_Module(self, node):
        inputs = self.inputs
        outputs = self.outputs
        for n in node.body:
            self.visit(n)
        for n in inputs:
            if n in outputs:
                raise AlwaysCombError(_error.SignalAsInout % n)

    def visit_FunctionDef(self, node):
        if self.toplevel:
            self.toplevel = 0 # skip embedded functions
            for n in node.body:
                self.visit(n)
        else:
            raise AlwaysCombError(_error.EmbeddedFunction)

    def visit_If(self, node):
        if not node.orelse:
            if isinstance(node.test, ast.Name) and \
               node.test.id == '__debug__':
                return # skip
        self.generic_visit(node)

    def visit_Name(self, node):
        id = node.id
        if id not in self.symdict:
            return
        s = self.symdict[id]
        if isinstance(s, _Signal) or _isListOfSigs(s):
            if self.context == INPUT:
                self.inputs.add(id)
            elif self.context == OUTPUT:
                self.outputs.add(id)
            elif self.context == INOUT:
                raise AlwaysCombError(_error.SignalAsInout % id)
            else:
                raise AssertionError("bug in always_comb")

    def visit_Assign(self, node):
        self.context = OUTPUT
        for n in node.targets:
            self.visit(n)
        self.context = INPUT
        self.visit(node.value)

    def visit_Attribute(self, node):
        self.visit(node.value)

    def visit_Call(self, node):
        fn = None
        if isinstance(node.func, ast.Name):
            fn = node.func.id
        if fn == "len":
            pass
        else:
            self.generic_visit(node)
            

    def visit_Subscript(self, node, access=INPUT):
        self.visit(node.value)
        self.context = INPUT
        self.visit(node.slice)

    def visit_AugAssign(self, node, access=INPUT):
        self.context = INOUT
        self.visit(node.target)
        self.context = INPUT
        self.visit(node.value)

    def visit_ClassDef(self, node):
        pass # skip

    def visit_Exec(self, node):
        pass # skip

    def visit_Print(self, node):
        pass # skip
