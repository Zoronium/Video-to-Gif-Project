# Video to Gif Converter
This is a simple web application that allows users to upload a video file and convert it to a GIF. The user can specify the duration of the GIF.

The application is built using Flask, a micro web framework for Python, and uses the `moviepy` library for video editing and compression.

## Requirements
- Python 3.x
- Flask
- moviepy
- imageio
- opencv-python-headless
more can be seen in [requirements.txt](./requirements.txt)

## Usage
1. Clone the repository: git clone https://github.com/Zoronium/video-to-gif
1. Install the required packages: pip install -r requirements.txt
1. Run the server: python app.py
1. Open the application in a web browser: http://localhost:5000/
1. Select a video file and enter the desired duration, then click the upload button to upload the file and receive the gif as a response.
### Note
- The gif file will be stored in the same folder as the script, it is not recommended in production. You should store the gif file in a separate folder or in cloud storage.
- The application is in development mode and it is not recommended to use it in a production environment.
License
This project is licensed under the MIT License.

Contributing
Feel free to fork this repository and make changes as you like. If you have any suggestions for improvements, please open a pull request.