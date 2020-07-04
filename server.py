from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)



def write_to_text(data):
    with open('database.txt', 'a') as textdata:
        email = data['email']
        subject = data['subject']
        message = data['message']
        textdata.write(f'{email},{subject},{message}'+'\n')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as textdata2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(textdata2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/')
def blank():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'
