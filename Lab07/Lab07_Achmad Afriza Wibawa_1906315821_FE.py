from flask import Flask, render_template_string
app = Flask(__name__)
@app.route('/<askedString>')
#This all is a template from the slide 11.32, i do not understand the Flask component one bit.
def named_page(askedString):
    reversedString = recReverse(askedString)
    page = '''
    <html>
        <head> <title>Lab 07 Page</title> </head>
        <body>
            <h1 style="color: red">Lab 07 Dasar-Dasar Pemrograman 1</h1>
            <p>The reverse of <i style="color: green">{{ prev }}</i> is <b style="color: blue">{{ after }}</b>.</p>
        </body>
    </html>
    '''

    return render_template_string(page, prev = askedString, after = reversedString)

def recReverse(s): # This is a recursive function to reverse a String
    if s == '': # Base case of empty string
        return s
    else:
        return s[-1] + recReverse(s[:-1]) # returns the last chr of string and iterates over the rest string

if __name__ == '__main__': app.run(debug=True)