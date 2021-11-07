from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

texts = []
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def get_text():
    new_text = request.form.get('get_text')
    texts.append(new_text)
    print(texts)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)