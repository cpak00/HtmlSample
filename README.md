# 物联平台样例
制造工程课程的全栈开发样例
## 说明
语言:Python3, XML, JavaScript
后端服务：Flask (0.12.2)
前端：HTML+CSS+JS
Windows下安装
```
pip install flask
```
如果是Linux环境下给python3装库需要使用pip3
```
pip3 install flask
```

## 文件树
* 主目录/
  - DB/
    * mainDb.db
  - templates/
    * index.html
    * home.html
    * car.html
    * dog.html
  - static/
    - js/
      * home.js
    - css/
      - img/
        * air.png
        * bulb.png
        * title.png
        * tmp.png
        * favicon.ico
      * sample.css
  - Node/
    * server.py
    * client.py
  - server.py
  - client.py

## 运行
分为服务器部分和物联网节点部分
### 服务器
主目录下的server.py是主程序
Windows环境下
```
python server.py
```
Linux环境下
```
python3 server.py
```
主目录下的client.py是测试程序，用于智能家居中的灯泡控制的灯泡端模拟，实际可采用stm32等硬件实现
### 物联网节点
Node目录下的server.py是主程序, 用于模拟一个物联网的中枢节点
client.py是节点程序，用于模拟一个物联网的分支节点
client.py在运行后会发送一条登陆请求到server.py，server.py即可获得ip地址
