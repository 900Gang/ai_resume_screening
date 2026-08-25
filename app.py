from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")




@app.route("/file", methods=["POST"])
def upload_files():
    upload_file=request.files.get("resume")
    ALLOWED_EXTENSION={'pdf','docx'}
    
    if upload_file and upload_file.filename:
        filename = secure_filename(upload_file.filename)
        _, extension = os.path.splitext(filename)
        extension = extension.lower().lstrip('.')
        if extension in ALLOWED_EXTENSION:
            upload_folder='uploads'

            os.makedirs(upload_folder, exist_ok=True)
        
            file_path = os.path.join(upload_folder, filename)
            upload_file.save(file_path)
            return "Resume uploaded successfully"
        else:
            return "File type not allowed "
    else:
        return "No file selected"

if __name__ == "__main__":
    app.run(debug=True)