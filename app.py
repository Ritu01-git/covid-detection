from flask import Flask, render_template, request, url_for

app = Flask(__name__)

def detect_covid_contacts():
    return 100  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect-covid', methods=['POST'])
def detect_covid():
    if request.method == 'POST':
        result = detect_covid_contacts()
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


