from flask import Flask, request
from brainfuck.Nice import NiceInterpreter
import timeout_decorator
import re;
app = Flask(__name__)

class Interpreter(NiceInterpreter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output = ""

    def putChar(self):
        char = self.array[self.ptr]
        self.output += chr(char)

    def getChar(self):
        self.array[self.ptr] = 0

    def get_output(self):
        return self.output


form_template = """
Enter Brainfuck code:
<form method="post">
<input type="text" name="brainfuck">
</form>
"""
success = """
SUCCESS!
<br>
Flag: 6pdfJXt6tNIszbbpeSZw
"""
fail = """
FAILED
"""
timeout = """
TIMEOUT
"""

@app.route('/', methods=['GET', 'POST'])
def brainfuck():
    if request.method == 'POST':
        code = request.form['brainfuck']
        try:
            if validate_brainfuck(code):
                return success
        except StopIteration:
            return timeout
        return fail
    return form_template

TARGET = "losaltoshacks"

@timeout_decorator.timeout(3, timeout_exception=StopIteration, use_signals=False)
def validate_brainfuck(code):
    i = Interpreter()
    i.execute(code)
    out = i.get_output()
    return out == TARGET
