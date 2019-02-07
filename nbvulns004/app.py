from flask import Flask, request, redirect, render_template
from lxml import etree

app = Flask(__name__)


@app.route('/')
def root_redirect():
    return redirect("/report_creation", code=302)


# xml external entities and DTD
@app.route('/report_creation', methods = ['POST', 'GET'])
def xml_report_processor():
    parsed_xml = None
    error = False
    error_message = ''

    if request.method == 'POST':
        xml = request.form['xml']
        parser = etree.XMLParser(no_network=False, dtd_validation=False)
        try:
            doc = etree.fromstring(xml)
            parsed_xml = etree.tostring(doc).decode("utf-8")
        except Exception as e:
            error = True
            error_message = str(e)

    return render_template('report_creation.html',
                           error=error,
                           error_message=error_message,
                           results=parsed_xml)

if __name__ == '__main__':
    app.run()