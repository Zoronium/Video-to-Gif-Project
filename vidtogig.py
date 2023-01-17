from moviepy.editor import VideoFileClip, ImageSequenceClip

def video_to_gif(filepath, duration):
    clip = VideoFileClip(filepath).subclip(0,duration)
    gif_filepath = filepath.replace(".mp4", ".gif")
    clip.write_gif(gif_filepath)
    clip.close()


if __name__ == "__main__":
    video_to_gif("example.mp4", 5)
