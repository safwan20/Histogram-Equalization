from flask import Flask, request
from Equalize import hist_equal, hist_equal_color
import constant

app = Flask(__name__)

@app.route('/equalize', methods=['GET','POST'])
def equalize() :
    if request.method == 'POST' :
        image = request.files['media']
        image.save(image.filename)
        img_out = hist_equal(image)
        return "Ok"
    else :
        return "NOT Ok"


@app.route('/equalize_color', methods=['GET','POST'])
def equalize_color() :
    if request.method == 'POST' :
        image = request.files['media']
        image.save(image.filename)
        img_out = hist_equal_color(image)
        return "Ok"
    else :
        return "NOT Ok"


app.run(debug=constant.DEBUG_MODE)