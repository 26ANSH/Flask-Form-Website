from flask import Flask, render_template, url_for
from website import start_app
app = start_app()

@app.route('/')
def index():
    return render_template('index.html')

# starting our app
if __name__ == '__main__':
    app.run(debug=True)
