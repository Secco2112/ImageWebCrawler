from libs.ImageWebCrawler import ImageWebCrawler
import time

def Main():
    start_time = time.time()

    iwc = ImageWebCrawler()
    iwc.setPathToDownload("C:/download_images/")

    pages_number = 100
    for page in range(1, pages_number):
        iwc.setUrl("http://pt-br.tinypic.com/images.php?page=" + str(page))
        iwc.fetchAndDownloadImages()

    print("--- %s seconds ---" % (time.time() - start_time))

Main()
