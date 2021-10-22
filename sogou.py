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
     
    for count, i in enumerate(range(0,350, 35)):
        start = str(i)
        url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start='+start+'&xml_len=35&query=蹲'
        # 訪問網頁
        try:
            imgs = requests.get(url)
        except:
            print('網路錯誤')
            break
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
            print('*********' +str(count),'-',str(m) + '.jpg********' + 'Downloading...')
            
            # 下載圖片並且儲存
            try:
                urllib.request.urlretrieve(img_url, path+str(count)+'-'+str(m) + '.jpg')
            except:
                print('下載錯誤')
                continue
            m = m + 1
            print('Download complete !')
 
getSogouImag('./image/')
