from flask import Flask, render_template, jsonify
import check_garage_open

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('garage_button_page.html')


@app.route('/trigger_action_button', methods=['POST'])
def trigger_action_button():
    # Perform your action here

    if check_garage_open.isGarageOpen():
        result = "Garage door is open!"

    else:
        result = "Garage door is closed!"

    # You can also send the result to the client
    return jsonify({'result': result})


# @app.route('/trigger_action_link', methods=['POST'])
# def trigger_action_link():
#     # Perform your action here
#     result = "Action triggered! This is where you would perform your action."

#     # You can also send the result to the client
#     return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
