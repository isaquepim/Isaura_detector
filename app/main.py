from flask import Flask, render_template, request, url_for, redirect
from model import Pipeline

app = Flask(__name__)

pipeline = Pipeline()
flag_label = False
label = 0

@app.route('/')
def index():
    global label, flag_label
    return render_template('index.html', flag = flag_label, label = label)

@app.route('/add', methods=['POST'])
def get_text():
    global flag_label, label
    flag_label = True
    new_text = request.form.get('get_text')
    dic = {0:'FALSO', 1:'VERDADEIRO'}

    output = pipeline.classify(new_text)
    label = dic[output[0]]

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)