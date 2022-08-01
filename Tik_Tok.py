from moviepy.editor import VideoFileClip
import requests
import os

print("put video url or press 's' to use default url")
v_url = input()
if v_url == 's':
    v_url = 'https://v16-webapp.tiktok.com/7b0ab1df6f82d163134e6ff8974f7ca1/62e81565/video/tos/useast2a/tos-useast2a-ve-0068c002/a3db8e7ce8f64d4dbef9109b426c758f/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C0%7C0&br=1372&bt=686&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZVgF1we2ND7JLl7Gb&mime_type=video_mp4&qs=0&rc=ZDw2Zzc3N2c5aGQ4Zjs3OEBpanZwdHR2cTd4czMzOzczM0BiNTBjXy8yNi8xYWEuMy0yYSMvaGdgajMwYGhfLS1gMTZzcw%3D%3D&l=2022080112023101019216116818241366'


def download_video(url):
    try:
        response = requests.get(url, allow_redirects=True, stream=True)

        with open('req_video.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)

        return 'Video successfully downloaded!'

    except Exception as _ex:

        return 'Error! Check the URL please!'



def main():
    print(download_video(v_url))


if __name__ == '__main__':
    main()

clip = VideoFileClip('req_video.mp4')
clip.write_gif('TikTok_test.gif', fps=10)
p = os.path.abspath('TikTok_test.gif')
print('You can see your gif file here:', p)
