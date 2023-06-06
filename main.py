import os, subprocess, sys, shlex

from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/execute', methods=['POST'])
def execute():
    command = request.form.get("command")
    print('Begin_of_Command>>' + command + '<<End_Of_Command')
    data = run_command(command)
    response = make_response(data)
    response.headers['Content-Type'] = 'text/txt; charset=UTF-8'
    return response


def run_command(command):
    command = command.replace('\\\n', '')
    command = escape_double_quotes(command)
    print('Single line Command>>' + command)
    return subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE).stdout.read()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


def escape_double_quotes(string):

  escaped_string = ""
  for char in string:
    if char == '"' and not string[string.index(char) - 1] == '\\':
      escaped_string += "\\\""
    else:
      escaped_string += char
  return escaped_string    
