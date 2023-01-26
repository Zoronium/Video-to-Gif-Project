from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from vidtogig import video_to_gif
from os import remove, mkdir, rmdir, path, getenv

app = Flask(
    __name__,
    static_url_path="",
    static_folder="./templates",
    template_folder="./templates",
)


@app.route("/", methods=["GET"])
def upload_form():
    return render_template("upload_form.html")


@app.route("/", methods=["POST"])
def upload_file():
    file = request.files["file"]
    duration = request.form["duration"]
    if file and allowed_files(file.filename):
        filename = secure_filename(file.filename)
        file.save("./temp/userfile.mp4")
        video_to_gif("./temp/userfile.mp4", int(duration))
        gif_path = filename.replace(".mp4", ".gif")
        return_data = "./temp/userfile.gif"
        remove("./temp/userfile.mp4")
        return send_file(
            return_data,
            mimetype="video/mp4",
            download_name=gif_path,
            as_attachment=True,
        )
    else:
        return "File not supported"


@app.after_request
def after_request_del_file(response):
    if path.isfile("./temp/userfile.mp4"):
        remove("./temp/userfile.gif")
    if not path.isdir("./temp"):
        mkdir("./temp")
    return response


def allowed_files(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


ALLOWED_EXTENSIONS = {"mp4"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=getenv("PORT", default=5000), debug=True)
