from flask import Flask, request
import timeout_decorator
import re;
app = Flask(__name__)


form_template = """
Enter Regex:
<form method="post">
<input type="text" name="regex">
</form>
"""
success = """
SUCCESS!
<br>
Flag: R72RgywkscucjgbQq8V6cwXT
"""
fail = """
FAILED
"""
timeout = """
TIMEOUT
"""

STRINGS = []
with open("strings.txt", "r") as f:
    STRINGS = [l.strip() for l in f.readlines()]

@app.route('/', methods=['GET', 'POST'])
def regexer():
    if request.method == 'POST':
        regex = request.form['regex']
        try:
            if validate_regex(regex):
                return success
        except StopIteration:
            return timeout
        return fail
    return form_template


@timeout_decorator.timeout(5, timeout_exception=StopIteration, use_signals=False)
def validate_regex(regex):
    reg = re.compile(regex)
    return all(reg.fullmatch(string) for string in STRINGS)
