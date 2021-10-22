# Image-WebCrawler

install the requirements first

```
pip install -r requirements.txt
```

For bing.py

input keyword at 'async?q=' in R1 
example:

```
r1=requests.get('https://www.bing.com/images/async?q=people+bending...)
```

use 'range(START_AT,END_AT, STEP)' to set 'first' value control how many images you want to scrap.
example:
```
for count, i in enumerate(range(0,350, 35)):
```
Now I have a 10 times loop, and I will recive 35 images in each loop.
BE NOTICE: If your STEP is bigger than 35, it will only recive 35 images, that's the limit for now.

You can change the file name by changing 'x' & 'count', but be aware that they should be integer, or you can rewrite the code by your own.

Images will save in the path blow:
```
local = os.path.join('./image/bing-imgs/bending/%s-%s.jpg')
```
Please change the path before you use it.

----


For sogou.py

input keyword at '&query=' in url
example:

```
url = 'https://pic.sogou.com/napi/pc/searchList?mode=1&start='+start+'&xml_len=35&query=squatting'
```

use 'range(START_AT,END_AT, STEP)' to set 'start' value and control how many images you want to scrap.
example:
```
for count, i in enumerate(range(0,350, 35)):
```
Now I have a 10 times loop, and I will recive 35 images in each loop.


You can change the file name by changing 'm' & 'count', but be aware that they should be integer, or you can rewrite the code by your own.

Images will save in the path blow:
```
getSogouImag('./image/sogou-imgs/bending/')
```
Please change the path before you use it.
