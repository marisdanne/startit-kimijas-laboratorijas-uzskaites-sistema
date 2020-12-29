from flask import Flask, jsonify
import dati

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  return "Labrīt!"

@app.route('/api/v1/vielas')
def vielas():
  return jsonify(dati.vielas)

@app.route('/api/v1/viela/<vielasID>')
def viela(vielasID):

  viela = f"Viela ar doto id {vielasID} nav atrasta"

  for v in dati.vielas:
    if str(v['id']) == vielasID:
      viela = v

  return jsonify(viela)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
