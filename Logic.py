from pytube import YouTube

import re

class mainApp():

    def __init__(self,quality,links):

        self.checked_one = None
        self.quality = quality
        self.links = links
        self.theOne()

    def theOne(self):

        for link in self.links:

            print(link)
            video = YouTube(link, on_progress_callback=self.progress_function)

            multiple_qualities = video.streams.filter(progressive=True)

            self.checked_one = self.check(multiple_qualities)

            self.checked_one.download()

    def progress_function(self,stream, chunk, bytes_remaining):
        lol = round((1-bytes_remaining/self.checked_one.filesize)*100, 3)
        print(f"{lol} done ...",end="\r")

    def check(self,link):

        for x in link :

            checker = re.search(f'res="{self.quality}p"',str(x))
            if checker==None:

                continue
            else:

                self.checked_one = x

        return self.checked_one




