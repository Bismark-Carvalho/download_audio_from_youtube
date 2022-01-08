import youtube_dl


def run():

    video_info = youtube_dl.YoutubeDL().extract_info(
        url="https://www.youtube.com/watch?v=9Ug8OdslZg4&list=RD9Ug8OdslZg4&start_radio=1&ab_channel=DeccaClassics",
        download=False,
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        "format": "bestaudio/best",
        "keepvideo": False,
        "outtmpl": filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info["webpage_url"]])

    print("Download complete... {}".format(filename))


if __name__ == "__main__":
    run()