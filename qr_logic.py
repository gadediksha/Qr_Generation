import qrcode
import os

def generate_qr(data, filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    path = os.path.join('static/qrcodes', filename)
    img.save(path)
    return filename

def create_payment_uri(upi_id, name, amount):
    # Standard UPI String format
    return f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"