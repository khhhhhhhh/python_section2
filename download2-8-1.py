from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep
import os
opener=req.build_opener()
opener.addheaders=[('User-agent',"Mozilla/5.0")]
req.install_opener(opener)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote=rep.quote_plus("사자")
url=base+quote
res=req.urlopen(url)
print(url)
savePath="C:\\imagedown\\"#C:\imagedown\

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e :
    if e.errno != errno.EEXIST:
        print("폴더만들기 실패!")
        raise

soup=BeautifulSoup(res,"html.parser")
img_list=soup.select("div.photo_bx api_ani_send _photoBox")
print("test",img_list)
