from flask import Flask , jsonify , render_template
import qrcode
import io
import base64
import time

app= Flask(__name__)
@app.route('/generate_qr')
def generate_qr():
    # Create a unique token based on the current time (changes every 30 seconds)
    timestamp_token = str(int(time.time() / 30))
    secret_code = f"ACTIVITY_001_{timestamp_token}"
    
    # Generate QR Code image
    img = qrcode.make(secret_code)
    buf = io.BytesIO()
    img.save(buf)
    # Convert image to a format HTML can display
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    return jsonify({"qr_image": img_base64, "secret": secret_code})
