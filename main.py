from pytube import YouTube, Playlist

def Progress(stream, data_chunk, bytes_remaining):
    size = stream.filesize
    current = (size - bytes_remaining)/size
    percent = ('{0:.1f}').format(current*100)
    print("Downloading video... " + percent + "%")

def Download(link):
    youtubeObject = YouTube(link, on_progress_callback=Progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has ocurred downloading the video")
    print("Video download is completed successfully")

def SingleVideoOption():
    link = input("Enter the YouTube video URL: ")
    Download(link)
    MainMenu()

def PlaylistOption():
    link = input("Enter the YouTube playtlist URL: ")
    playlistObject = Playlist(link)
    video_counter = 1
    for videoUrl in playlistObject.video_urls:
        print("Downloading video " + str(video_counter) + " of " + str(len(playlistObject.video_urls)))
        Download(videoUrl)
        video_counter += 1
    MainMenu()

def MainMenu():
    print(" ")
    print("Welcome, please choose a download option: ")
    print("1. Single video")
    print("2. Playlist")
    print("3. Channel")
    print("0. Exit")
    option = input("Your option: ")
    try:
        option = int(option)
        if option == 0:
            return
        elif option == 1:
            SingleVideoOption()
        elif option == 2:
            PlaylistOption()
        else:
            print("Invalid option")
            MainMenu()
    except Exception as e:
        print("An error ocurred:", e)
        MainMenu()

MainMenu()
