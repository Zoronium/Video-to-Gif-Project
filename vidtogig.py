from moviepy.editor import VideoFileClip, ImageSequenceClip
import os.path as p


def video_to_gif(filepath, duration):
    try:
        if duration < 0:
            raise ValueError("Duration should be positive")

        clip = VideoFileClip(filepath).subclip(0, duration)
        gif_filepath = filepath.replace(".mp4", ".gif")
        clip.write_gif(gif_filepath)
        clip.close()

        return gif_filepath
    except ValueError:
        return "Invalid Duaration"


if __name__ == "__main__":
    video_to_gif("example.mp4", -1)
