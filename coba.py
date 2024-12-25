from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/success/<name>/<cls>')
def success(name, cls):
    return f'Welcome {name} from {cls} class'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm', 'Guest')
        cls = request.form.get('cls', 'Unknown') 
        return redirect(url_for('success', name=user, cls=cls))  
    else:
        return render_template('login.html') 

if __name__ == '__main__':
    app.run(debug=True)
