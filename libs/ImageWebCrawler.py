import requests
import os
from bs4 import BeautifulSoup
import re
import mimetypes

class ImageWebCrawler:
    def __init__(self):
        self._url_list = ""
        self._path_to_download = ""
        self._image_regex = "(http)?s?:?(\/\/[^\"']*\.(?:png|jpg|jpeg|gif|png|svg))"
        self._image_pattern = re.compile(self._image_regex)
        self._images = list()

    def setUrl(self, url):
        self._url_list = url
        return self

    def getUrl(self):
        return self._url_list

    def setPathToDownload(self, ptd, create_if_not_exists=False):
        if create_if_not_exists:
            if not os.path.exists(ptd):
                os.makedirs(ptd)
        self._path_to_download = ptd
        return self

    def getPathToDownload(self):
        return self._path_to_download

    def repositoryExists(self, return_value=False):
        if return_value:
            return os.path.isdir(self.getPathToDownload())
        else:
            if not os.path.isdir(self.getPathToDownload()):
                raise Exception("The directory \"%s\" don't exists" %self.getPathToDownload())

    def downloadImage(self, image_url):
        self.repositoryExists()

        filename = image_url.split('/')[-1]
        if self.validImage(filename) and not os.path.isfile(os.path.join(self.getPathToDownload(), filename)):
            img_data = requests.get(image_url).content
            with open(r"" + self.getPathToDownload() + filename + "", 'wb') as handler:
                handler.write(img_data)
            handler.close()

    def validImage(self, image):
        valid_mimes = ["image/png", "image/jpg", "image/jpeg", "image/gif", "image/bmp", "image/svg+xml", "image/tiff", "image/x-icon"]
        guess_type = mimetypes.guess_type(image)
        return guess_type[0] in valid_mimes

    def fetchAndDownloadImages(self):
        print("Parsing and getting images from url \"%s\"" %self.getUrl())
        response = requests.get(self.getUrl())
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        for img in img_tags:
            self._images.append(img['src'])
        print("All images were taken from url \"%s\"." % self.getUrl())

        print("Downloading all images from \"%s\"..." % self.getUrl())
        for image in self._images:
            self.downloadImage(image)
        print("All images were downloaded from url \"%s\"" % self.getUrl())
