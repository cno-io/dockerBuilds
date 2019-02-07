#!/usr/bin/env python3

from flask import Flask, request, render_template, redirect
import base64

app = Flask(__name__)


@app.route('/')
def root_redirect():
    return redirect("/report", code=302)


@app.route('/report', methods=['GET'])
def report_reader():
    error = False
    error_message = ''
    report_found = False
    report_contents = ''
    name = request.args.get('name')

    try:

        if name:
            report_name = 'reports/' + request.args.get('name')

            if name.endswith('.png'):
                report_contents = base64.b64encode(open(report_name, 'rb').read()).decode('ascii')
            else:
                report_contents = open(report_name, 'rb').read().decode('utf-8')
            report_found = True

    except Exception as e:
        error = True
        error_message = str(e)

    return render_template('report.html',
                           error=error,
                           error_message=error_message,
                           report_found=report_found,
                           report_contents=report_contents,
                           report_name=name)

if __name__ == '__main__':
    app.run('0.0.0.0', 80)