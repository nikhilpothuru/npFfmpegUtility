import subprocess

'''
Author: Nikhil Pothuru

Abstraction to download videos given a link
'''

class FFmpegUtil:

    '''
    Given a file path and a link, download the video to said location
    '''
    @staticmethod
    def downloadVideo(file_path, link):
        cmd = [
            "ffmpeg",
            "-i", link,  # input file
            "-c", "copy",  # copy without re-encoding
            file_path  # output file
        ]

        subprocess.run(cmd, check=True)