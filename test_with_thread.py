from libs.ImageWebCrawlerThread import ImageWebCrawlerThread
import threading
import time

def Main():
    start_time = time.time()

    threads = []
    pages_number = 100
    for page in range(1, pages_number):
        iwc = ImageWebCrawlerThread()
        threads.append(threading.Thread(target=iwc.fetchAndDownloadImages, args=("C:/download_images/", "http://pt-br.tinypic.com/images.php?page=" + str(page))))

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print("--- %s seconds ---" % (time.time() - start_time))

Main()
