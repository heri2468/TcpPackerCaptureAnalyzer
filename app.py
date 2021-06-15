
from flask import Flask,render_template,Response, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/ShowProtocol')
def Protocol():
    return render_template('ShowProtocol.html')

@app.route('/Size-No')
def Size():
    return render_template('/Size-No.html')

@app.route('/ViewContent')
def ViewContent():
    return render_template('/Simply_print_output.html')

@app.route('/Time')
def TimeNo():
    return render_template('/Time_No_output.html')


if __name__ == '__main__':
    app.run(debug=False,port=8000)