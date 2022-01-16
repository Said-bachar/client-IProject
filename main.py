from flask import Flask, render_template, jsonify, Response, request
import time
import requests
import json

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

@app.route("/rules", methods=['POST', 'GET'])
def rules():
  return render_template('rules.html')




@app.route("/new-game", methods=['POST', 'GET'])
def new_game():
    return render_template('new-game.html') 

@app.route("/join-game", methods=['POST', 'GET'])
def join_game():
    return None
     # TO-DO

API_URL1 = "http://192.168.37.69:50000"

#GET PORTS :------------------------------------------------------

API_URL2 = "http://192.168.37.69:50000/port"

# @app.route("/test", methods=['GET'])
# def test():
#     res = requests.get(API_URL2)
#     port = res.json()
#     return 'Our port is :' + str(port.get('numport')) # our port
#    # return port


@app.route("/apitest", methods=['POST', 'GET'])
def apitest():
#     reqParms = request
#     return render_template('test.html', param=reqParms)
    x = request.get_json(silent=True)
    print(json.loads(request.data.decode("utf-8")))
    # log the user out
    return render_template('test.html', X = x)

# port = 0

# def getPort():
#     res = requests.get(API_URL2)
#     port = res.json()
#     return port.get('numport') # our port

# port = getPort()

# PORT = requests.get(API_URL2)





# @app.route("/some-url", methods=['GET'])
# def get_data():
#     res = requests.get("http://my-api.com")
#     return res.content


#TEST Here ...

@app.route("/getPixels", methods=['GET'])
def getPixels():
    return render_template('test.html')

# TODO : Req to Discovery service > CardManager
# Get All cards > store
# Send cards to the view
# Manipulate each card
# Implement the logic <> IA ):



#TO-DO :
   # WAIT CARDS 
   # SEND UR RESPONSE
   # SCORE ++ OR --
   # IF SCORE
   # Get the timer
   # Show it
   #  



if __name__ == "__main__":
    app.run(debug = True)   
