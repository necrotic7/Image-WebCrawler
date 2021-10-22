import requests
import urllib
import json
import os
import shutil  # 用來刪除資料夾
  

def getSogouImag(path):
  # 判斷資料夾是否存在，存在則刪除
    if os.path.exists(path):
         shutil.rmtree(path)
              # 建立資料夾
    os.mkdir(path)
     
    
    url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start=48&xml_len=48&query=%E7%AB%99%E7%AB%8B'
     # 訪問網頁
    imgs = requests.get(url)
     # 獲取網頁內容
    imgs_text = imgs.text
    
     # 字串轉換成json格式
    imgs_json = json.loads(imgs_text)
    
     # 得到圖片資訊列表
    imgs_items = imgs_json['data']['items']
    m = 0
     # 儲存每個想要儲存的圖片連結，為了後續
    for i in imgs_items:
        img_url = i['picUrl']
        print('*********' + str(m) + '.png********' + 'Downloading...')
        print('下載的url: ', img_url)
         # 下載圖片並且儲存
        try:
            urllib.request.urlretrieve(img_url, path+str(m) + '.jpg')
        except:
            continue
        m = m + 1
        print('Download complete !')
 
getSogouImag('./sougo-img/')
