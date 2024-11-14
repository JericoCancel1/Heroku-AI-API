from flask import Flask, render_template, url_for
from flask_cors import CORS
from io import BytesIO
from PIL import Image

app =Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://shielded-meadow-51410-81166774b395.herokuapp.com"}})

@app.route('/')
def index():
    return "Flask Heroku App"

# Route to handle image upload
@app.route('/api/upload', methods=['POST'])
def upload_image():
    # Check if the request has the image part
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Get the image file from the request
    image_file = request.files['image']

    # Process image here (currently returning a dummy image for testing)

    # Generate a dummy image (e.g., 100x100 red square) as a placeholder response
    dummy_image = Image.new('RGB', (100, 100), (255, 0, 0))
    img_io = BytesIO()
    dummy_image.save(img_io, 'PNG')
    img_io.seek(0)

    # Send the dummy image back
    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run()