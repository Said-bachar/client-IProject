from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route("/choose-game", methods=['POST', 'GET'])
def choose_game():
    forward_message = "Moving Forward"
    # Get game's modes ....
    # r = requests.get('//API-TO-GAME-SERVER')
    # json_response = json.dumps(r.json())
    # rspone = Response(json_response, content_type='application/json; charset=utf-8')
    # response.headers.add('content-length', len(json_response))
    # response.status_code = 200
    # TO-DO : somthings with res ...
    

    return render_template('menu.html', forward_message=forward_message)

@app.route("/add-images", methods=['POST'])
def add_images():
    return None
    # TO-DO


@app.route("/new-game", methods=['POST', 'GET'])
def new_game():
    return render_template('new-game.html') 

@app.route("/join-game", methods=['POST', 'GET'])
def join_game():
    return None
     # TO-DO

API_URL = "http://192.168.37.69:50000"

@app.route("/test", methods=['GET'])
def test():
    res = requests.get(API_URL)
    return res.json()

@app.route("/some-url", methods=['GET'])
def get_data():
    res = requests.get("http://my-api.com")
    return res.content

     

if __name__ == "__main__":
    app.run(debug = True)   