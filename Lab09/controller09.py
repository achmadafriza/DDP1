from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from model09 import plot

app = Flask(__name__)

class InputForm(Form):
    A = FloatField(label='A', validators = [validators.InputRequired()])
    B = FloatField(label='B', validators = [validators.InputRequired()])
    C = FloatField(label='C', validators = [validators.InputRequired()])
    D = FloatField(label='D', validators = [validators.InputRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    result = None
    if request.method == 'POST' and form.validate():
        A = form.A.data
        B = form.B.data
        C = form.C.data
        D = form.D.data
        result = plot(A,B,C,D)
    return render_template("viewlab09.html", template_form = form, template_result = result)


if __name__ == '__main__':
    app.run(debug=True)