from pytube import YouTube

def Progress(stream, data_chunk, bytes_remaining):
    size = stream.filesize
    current = (size - bytes_remaining)/size
    percent = ('{0:.1f}').format(current*100)
    print("Downloading... " + percent + "%")

def Download(link):
    youtubeObject = YouTube(link, on_progress_callback=Progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has ocurred")
    print("Download is completed successfully")

link = input("Enter the YouTube video URL: ")
Download(link)