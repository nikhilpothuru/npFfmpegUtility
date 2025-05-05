import os
from deserializer.manifestDeserializer import ManifestDeserializer
from util.ffmpegUtil import FFmpegUtil
import time
import random

'''
Author: Nikhil Pothuru

Simple class to take a manifest and download all videos associated to
said manifest 
'''
class Downloader:

    '''
    A method to download all videos associated to the manifest

    :param manifestPath: the path of the manifest
    '''
    @staticmethod
    def download(manifest_path):

        # Step 1: Deserialize manifest
        manifest = ManifestDeserializer.deserialize(manifest_path)

        # Step 2: Process each section
        root = manifest.root
        for section in manifest.sections:
            folder_name = section.foldername
            prefix = section.prefix
            links = section.links

            # Create new folder if it doesn't exist in 'root'
            folder_path = os.path.join(root, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Folder '{folder_path}' created")
            else:
                print(f"Folder '{folder_path}' exists")

            # Create the video file name using the prefix + video title
            counter = 1
            for video_title, link in links.items():
                time.sleep(random.uniform(1, 8))
                file_name = prefix + str(counter) + "_" + video_title + ".mp4"
                counter += 1
                file_path = os.path.join(folder_path, file_name)

                # Delete file if it already exists
                if os.path.exists(file_name):
                    os.remove(file_name)
                    print(f"Existing file '{file_name}' deleted")

                # Call the util utility to download the file
                FFmpegUtil.downloadVideo(file_path, link)

        return
