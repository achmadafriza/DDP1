# *******************************************************************
# lab08
# DDP1 / FPROG1 -- 2019
# Recursively translates words into a decimal integer
# with active web-based GUI
# *******************************************************************
from flask import Flask, render_template_string, request
from wtforms import Form, validators, StringField
app = Flask(__name__)
#THE MODEL
#Translate a non-empty sequence of words into a decimal integer
# Recursive function for translating a list of numeric words
# into a decimal integer
# Example:
# >>> translateDigits(['nol','dua','lima','nol'])
# 250
def translateDigits(listOfWords):
    if len(listOfWords) == 1: # base case
        return translateOneDigit(listOfWords[0])
    else: # recursive case
        return translateDigits(listOfWords[:-1])*10 + translateOneDigit(listOfWords[-1])

# Function for translating one word
def translateOneDigit(word):
    dictio = {"nol":0,
              "satu":1,
              "dua":2,
              "tiga":3,
              "empat":4,
              "lima":5,
              "enam":6,
              "tujuh":7,
              "delapan":8,
              "sembilan":9,}
    return dictio[str(word)]

#THE VIEW
page = '''
<html>
    <head>
        <title> Words Translation </title>
    </head>
    
    <body>
        <h1 style="color: blue"> Translate a Sequence of Words </h1>
        
        <form method=post action="">
            <b style="color: orange"> Hello Beloved Users! </b>
        <br>
        Enter a sequence of Indonesian numeric words
            {{ template_form.text_field }}
        <br>
        {% if result != None %}
            <b style = "color:green">{{ result }}</b>
        {% endif %}
        <br>
        <input type=submit value=Translate>
        </form>
    </body>
</html>
'''
# continue …

# THE CONTROLLER
# Using InputForm, a subclass of Form
# InputForm has a single TextField
class InputForm(Form):
    text_field = StringField(validators=[validators.InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_val = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        input_text = form.text_field.data
        words = input_text.split() # a list of words
        translated_val = translateDigits(words)
    return render_template_string(page, template_form=form, result=translated_val)

if __name__ == '__main__':
    app.run(debug= True)