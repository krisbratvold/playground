from flask import Flask, render_template
app = Flask(__name__)                         
@app.route('/')
def index():
    return "Hey"
@app.route('/play')
# def display_three_boxes():
#     return render_template("index.html", times = 3)    
@app.route("/play/<times>")
# def display_x_boxes(times):
#     return render_template("index.html", times = int(times))
@app.route("/play/<times>/<color>")
def color_boxes(times = 3, color = "rgb(159,197,248)"):
    return render_template("index.html", times = int(times), color=color)
if __name__=="__main__":
    app.run(debug=True)