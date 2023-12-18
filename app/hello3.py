import os
import time
import subprocess
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('run_script_by_btn_click.html')

@app.route('/do_something')
def do_something():
    home_dir = "/home/uriziv"
    # home_dir = os.getenv('HOME')
    file_basename = str(time.time())
    file_extension = "txt"
    touch_cli = ["touch", "{}/Downloads/{}.{}".format(home_dir, file_basename, file_extension)]
    res = subprocess.run(touch_cli)
    print(res)
    return str(res)


app.run(host='0.0.0.0', port=81)
