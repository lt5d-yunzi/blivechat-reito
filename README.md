# blivechat

支持扫码登录的 blivechat， 避免身份码（开放平台）部分信息缺失。

只熊KUMA版的请看 [bear-reito 分支](https://github.com/cnSchwarzer/blivechat-reito/tree/bear-reito)

注：未修补只熊版，需要自行替换构建

需要替换如下文件：

1. requirements.txt
2. ./utils/request.py 
3. ./api/login.py 

## 声明

必须使用小号进行扫码，一个号同一时间只能进入一个直播间。凭据会本地储存，如执意使用大号扫码所造成的一切损失与我无关。

## 下载

[前往下载](https://github.com/lt5d-yunzi/blivechat-reito/releases/tag/release)

记得复制原作者的发行版中部分资源文件，如 `data/emoticons` 或其他 `frontend` 中需要使用的样式资源文件

## 打包

```shell
git clone --recursive https://github.com/cnSchwarzer/blivechat-reito.git -b orig-reito

cd frontend
npm i
npm run build
cd ..

conda create -n blivechat python=3.9
pip install -r requirements.txt
pyinstaller main.py -n blivechat --add-data "data;data" --add-data "log;log" --add-data "frontend/dist;frontend/dist" --hidden-import aiohttp --noconfirm
```

[原文档](https://github.com/xfgryujk/blivechat/blob/dev/README.md)
