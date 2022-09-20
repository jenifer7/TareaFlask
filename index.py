from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo!"

#debug=True es para mantener el servidor reiniciando 
#despues de los cambios mientras aun esta en desarrollo
if __name__=='__main__':
    app.run(debug=True)

