from flask import Flask, render_template, jsonify

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




if __name__ == "__main__":
    app.run(debug = True)   