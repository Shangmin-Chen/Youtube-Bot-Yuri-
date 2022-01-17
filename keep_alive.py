from flask import Flask, render_template, request
from threading import Thread
from time import sleep
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
  if request.method == "POST":
    link = request.form["link"]
    title = request.form["title"]
    video = request.form.get("video")
    audio = request.form.get("audio")
    progress = 0
    # this portion needs to be fixed, probably with javascript
    """while True:
      data = progress
      progress += 1
      return render_template("downloading.html", data=data)
      sleep(1)"""


def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()