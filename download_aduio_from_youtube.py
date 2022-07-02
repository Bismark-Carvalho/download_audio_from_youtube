import youtube_dl


def run():

    file = open('link.txt')

    urls = file.read().split('\n')

    for url in urls:

        video_info = youtube_dl.YoutubeDL().extract_info(
            url=url,
            download=False,
        )
        filename = f"{video_info['title']}.mp3"
        options = {
            "format": "bestaudio/best",
            "keepvideo": False,
            "outtmpl": 'musicas/' + filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info["webpage_url"]])

        print("Download complete... {}".format(filename))


if __name__ == "__main__":
    run()
