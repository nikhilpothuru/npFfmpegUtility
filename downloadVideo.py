import sys

from downloader.downloader import Downloader

'''
Author: Nikhil Pothuru

Main method to download videos 
'''
def main(manifest_path):
    Downloader.download(manifest_path)

if __name__ == "__main__":

    # Get command line arguments
    args = sys.argv[1:]

    # Argument validation
    if len(args) != 1:
        print("Error: Please provide exactly one parameter")

    # Process manifest
    main(args[0])