import json
import requests
import base64
from io import BytesIO
from sys import version_info
from PIL import Image
def image(element,filename):
   left = element.location['x']
   top = element.location['y']
   right = element.location['x'] + element.size['width']
   bottom = element.location['y'] + element.size['height']
   im = Image.open(filename)#截取对应位置
   im = im.crop((left, top, right, bottom))#保存覆盖原有截图
   im.save(filename)
   uname = 'xx' #用户名
   pwd = 'admin123.' #密码
   img = Image.open(filename)
   img = img.convert('RGB')
   buffered = BytesIO()
   img.save(buffered, format="JPEG")
   if version_info.major >= 3:
    b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')
   else:
    b64 = str(base64.b64encode(buffered.getvalue()))
   data = {"username": uname, "password": pwd, "image": b64}
   result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)  #第三方识别接口
   if result['success']:
    return result["data"]["result"]
   else:
    return result["message"]
   return ""

'''

import json
import requests
import base64
from io import BytesIO
from PIL import Image
from sys import version_info


def base64_api(uname, pwd,  img):
    img = img.convert('RGB')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    if version_info.major >= 3:
        b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')
    else:
        b64 = str(base64.b64encode(buffered.getvalue()))
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    img_path = "C:/Users/Administrator/Desktop/file.jpg"
    img = Image.open(img_path)
    result = base64_api(uname='你的账号', pwd='你的密码', img=img)
    print(result)
    
'''