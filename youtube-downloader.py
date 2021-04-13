
import os
import pytube
import subprocess

yt=pytube.YouTube(input("입력"))
videos=yt.streams.all()

cNum=int(input("다운 받을 화질은?(0~21입력가능)"))#

down_dir="C:\youtube"
videos[cNum].download(down_dir)


newFileName=input('변환 할 mp3 파일명은?')
oriFileName=videos[cNum].default_filename


subprocess.call(['ffmpeg','-i',
      os.path.join(down_dir,oriFileName),
      os.path.join(down_dir,newFileName)
])



print('동영상 다운로드 및 변환 완료!!')
