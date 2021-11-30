from os import listdir
from os.path import isfile, join, realpath, dirname
import shlex


cwd = dirname(realpath(__file__))
onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]
onlyfiles.sort()
print(onlyfiles)
vid_list = []

for f in onlyfiles:
    if ".mp4" in f:
        if "-smaller" not in f:
            frename = f.strip(".mp4")+"-smaller.mp4"
            cmd = f"ffmpeg -i {f} -vcodec libx264 -crf 28 -filter:v scale=600:-1 -c:a copy {frename}"
            print(cmd)
            html = """
                    <li>
            <video width="600" controls>
                <source src="files/{}" type="video/mp4">
            </video>
        </li>""".format(frename)
            vid_list.append(html)

for li in set(vid_list):
    print(li)
