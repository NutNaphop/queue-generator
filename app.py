from flask import Flask, render_template,request,render_template,make_response,send_file
from pdf2image import convert_from_path
import pdfkit
import os
import datetime
app = Flask(__name__)
config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

x = datetime.datetime.now()
year = (x.year)
day = (x.strftime("%A"))
date = (x.day)
month = (x.month)
display = 'Has create in  %s %s %s %s' %(date,day,month,year)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        way = request.form['way']
        id = request.form['id']
        time = request.form['time']
        day = request.form['day']
        
        render = render_template('pdf.html',name=name,lastname=lastname,way=way,id=id,time=time,day=day,date_enter=display)
        pdfkit.from_string(render,'queue.pdf',configuration=config)
        
        
        pages = convert_from_path('queue.pdf', 500 , poppler_path=r'C:\Program Files\poppler-22.04.0\Library\bin') 
        for page in pages:
            page.save('.\static\img\queue.jpg', 'JPEG')
        
    
        
        # response = make_response(img_save) #ทําให้เห็น
        # response.headers['Content-Type'] = 'test/jpg'
        # response.headers['Content-Disposition'] = 'attachment;filename=output.png'
        load = 'static/img/queue.jpg'
        return send_file(load,as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
