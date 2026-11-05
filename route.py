from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file, response
import json

app = Bottle()
ctl = Application()

# -----------------------------------------------------------------------------
# Rotas:

# AQUI ESTÁ A MUDANÇA: Rota ajustada para entregar qualquer imagem (png, jpg, etc.)
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/')
def index():
    return ctl.render('helper')

@app.route('/helper')
def helper(info=None):
    return ctl.render('helper')

# -----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/api/status', method='GET')
def api_status():
    response.content_type = 'application/json'
    return json.dumps({
        "status": "online",
        "sistema": "PixelCoffee",
        "mensagem": "Todos os serviços do backend Bottle estão operacionais!"
    })

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)