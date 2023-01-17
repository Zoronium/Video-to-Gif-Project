from flask import Flask , request , render_template , send_file
from werkzeug.utils import secure_filename
from vidtogig import video_to_gif

app = Flask(__name__)

@app.route("/" , methods=["GET"])
def upload_form():
    return render_template("upload_form.html")

@app.route("/", methods=["POST"])
def upload_file():
    file = request.files["file"]
    duration = request.form['duration']
    if file and allowed_files(file.filename):
        filename = secure_filename(file.filename)
        file.save(filename)
        video_to_gif(filename , int(duration))
        gif_path = filename.replace(".mp4", ".gif")
        return send_file(gif_path , as_attachment=True)
    
    else:
        return "File not supported"

def allowed_files(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

ALLOWED_EXTENSIONS = {"mp4"}

if __name__ == "__main__":
    app.run(debug=True)