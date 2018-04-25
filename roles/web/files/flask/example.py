#!/usr/bin/python
"""An example Flask app just to jog my memory

to run and make available to LAN on port 5000...
    export FLASK_APP=example.py
    export FLASK_DEBUG=1
    flask run --host=0.0.0.0
"""
import json
import subprocess
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hello/<name>/')
def hello_name(name):
    return "Hello {n}!".format(n=name)

@app.route('/power/')
def is_the_power_on():
    response = {"power_state":"true"}
    return json.dumps(response)

@app.route('/isjondumb/')
def jonisdumb():
    return 'Of course! Jon is the dumbest. I mean, the guy likes WordPress...'

@app.route('/test2/')
def test():
    return 'test successful'

@app.route('/whoami/')
def whoami():
    output = subprocess.check_output(['whoami'])
    return output

@app.route('/ansible/')
def ansible_ping():
    cmds = ['ansible', '-m ping localhost']
    output = subprocess.check_output(cmds)
    return output

@app.route('/ansible/<playbook>/')
def ansible(playbook):
    playbook = '/var/ansible/{}.yml'.format(playbook)
    output = subprocess.check_output(['ansible-playbook', playbook])
    return output

if __name__ == "__main__":
    app.run()
