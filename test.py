import unittest 
import os 
import vidtogig

class TestVideoToGif(unittest.TestCase):
    def test_valid_input(self):
        video_file="example.mp4"
        duration = 1
        gif_file = vidtogig.video_to_gif(video_file , duration)
        self.assertEqual(gif_file , 'example.gif')
        self.assertTrue(os.path.isfile(gif_file))
        print(" Valid input Passed ✅ ")
    
    def test_invalid_file_input(self):
        video_file="example.gif"
        duration = -1
        gif_file = vidtogig.video_to_gif(video_file , duration)
        self.assertEqual(gif_file , 'Invalid Duaration')
        print(" Invalid duration input test Passed ✅ ")
    
    def test_invalid_file_size_input(self):
        video_file="example.gif"
        duration = 1
        gif_file = vidtogig.video_to_gif(video_file , duration)
        size =os.path.getsize(gif_file)
        self.assertLess(size , 3000000)
        print(" Valid File size Passed ✅ ")

if __name__ == '__main__':
    unittest.main()