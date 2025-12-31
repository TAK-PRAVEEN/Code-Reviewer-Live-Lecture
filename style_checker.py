import ast

def show_style_corrected(code):
    tree = ast.parse(code)
    return ast.unparse(tree)

student = "def hello(x,y):unused=1;return x+y"

corrected = show_style_corrected(student)
print(corrected)