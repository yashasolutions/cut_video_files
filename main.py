import requests
from moviepy.video.io.VideoFileClip import VideoFileClip


def get_video_file(url, file_name):
    response = requests.get(url)

    with open(file_name,"wb") as f:
        f.write(response.content)

def create_video_clip(source, target, start, end):
    video = VideoFileClip(source)
    video = video.subclip(start, end)
    video.write_videofile(target)



def main():
    url = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"
    file_name = "sample.mp4"
    get_video_file(url, file_name)

    source = "sample.mp4"
    target = "output/sample-cut.mp4"
    start = 5
    end = 10
    create_video_clip(source, target, start, end)

if __name__ == "__main__":
    main()
