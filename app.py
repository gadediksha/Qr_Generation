from flask import Flask, render_template, request
from qr_logic import generate_qr, create_payment_uri
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_image = None
    if request.method == 'POST':
        qr_type = request.form.get('qr_type')
        
        if qr_type == 'text':
            content = request.form.get('content')
            qr_image = generate_qr(content, 'text_qr.png')
            
        elif qr_type == 'url':
            url = request.form.get('url')
            qr_image = generate_qr(url, 'url_qr.png')
            
        elif qr_type == 'pay':
            upi = request.form.get('upi')
            name = request.form.get('name')
            amt = request.form.get('amount')
            pay_data = create_payment_uri(upi, name, amt)
            qr_image = generate_qr(pay_data, 'pay_qr.png')

    return render_template('index.html', qr_image=qr_image)

if __name__ == '__main__':
    if not os.path.exists('static/qrcodes'):
        os.makedirs('static/qrcodes')
    app.run(debug=True)