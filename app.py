from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the landing page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/takeout', methods=['GET', 'POST'])
def takeout():
    if request.method == 'POST':
        addresses = request.form.get('addresses').split(',')
        return render_template('takeout.html', addresses=addresses)
    return render_template('takeout.html')

@app.route('/takeoutv2', methods=['GET'])
def takeoutv2():
    return render_template('takeout_v2.html')

if __name__ == '__main__':
    app.run(debug=True)