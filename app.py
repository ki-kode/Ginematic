from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.errorhandler(404)
def fuck(e):
    return redirect('/')


if __name__ == "__main__":
    app.run()
