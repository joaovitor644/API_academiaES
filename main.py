from flask import Flask
from routes.Auth import auth
from routes.ctlAluno import aluno_route
from routes.ctlPlano import plano_route
from routes.ctlAula import aula_route
from routes.ctlAdm import adm_route
from routes.ctlInstrutor import instrutor_route
from routes.ctlVisitante import visitante_route
from routes.ctlGestMaterial import gestMaterial_route
from flask_cors import CORS
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")
CORS(app, supports_credentials=True)

app.register_blueprint(auth)
app.register_blueprint(aluno_route)
app.register_blueprint(plano_route)
app.register_blueprint(aula_route)
app.register_blueprint(adm_route)
app.register_blueprint(instrutor_route)
app.register_blueprint(visitante_route)
app.register_blueprint(gestMaterial_route)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
