from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index.html')
def index1():
    return render_template('index.html')
@app.route('/admin_dashboard.html')
def admin():
    return render_template('admin_dashboard.html')
@app.route('/subscribe.html')
def subscribe():
    return render_template('subscribe.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
