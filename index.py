from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#debug=True es para mantener el servidor reiniciando 
#despues de los cambios mientras aun esta en desarrollo
if __name__=='__main__':
    app.run(debug=True)