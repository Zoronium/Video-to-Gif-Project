# Video to Gif Converter
+ This is a simple web application that allows users to upload a video file and convert it to a GIF. The user can specify the duration of the GIF.
+ The application is built using Flask, a micro web framework for Python, and uses the `moviepy` library for video editing and compression.
+ [Click Here for Demo](#demo)

### Deployment Link
[Link](https://video-to-gif-project.up.railway.app/)

![image](https://user-images.githubusercontent.com/89680252/212937441-b3828a0b-820b-4d5b-a6f6-c2c2ff8e606f.png)
>Done on railway

## Requirements
- Python 3.x
- Flask
- moviepy
- imageio
- opencv-python-headless
>More can be seen in [requirements.txt](./requirements.txt)

## Usage
1. Clone the repository:
```
 git clone https://github.com/Zoronium/video-to-gif
```
2. Install the required packages: 
```
pip install -r requirements.txt
```
3. Run the server: 
```
python server.py
```
4. Open the application in a web browser: http://localhost:5000/
5. Select a video file and enter the desired duration, then click the upload button to upload the file and receive the gif as a response.
### Note
- The gif file will not be stored in the same folder as the script but in the `temp` folder. You can store the gif file in a separate folder or in cloud storage by changing the following lines
```py
    file.save(filename)
    video_to_gif(filename, int(duration))
    gif_filepath = filename.replace(".mp4", ".gif")
    response = send_file(gif_filepath, as_attachment=True) 
  
    # change the file path here
```
- The application is in development mode and it is may not be ok recommended to use it in a production environment.

## Demo
![vidtogif](https://user-images.githubusercontent.com/89680252/213863340-2809241e-1d8d-4f4f-a4b5-d7ca447fb98e.gif)


## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository and make changes as you like. If you have any suggestions for improvements, please open a pull request.
