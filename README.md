# WeChat启动器

一个简单的WeChat多开启动器，支持自定义WeChat路径和启动次数。

## 功能特点

- 支持选择WeChat.exe或Weixin.exe路径
- 可自定义启动次数（1-10次）
- 自动保存配置，下次使用时自动加载

## 安装步骤

1. 安装Python依赖：
```bash
pip install -r requirements.txt
```

2. 运行程序：
```bash
python wechat_launcher.py
```

3. 打包成exe（可选）：
```bash
pyinstaller --onefile --windowed wechat_launcher.py
```

## 使用说明

1. 点击"浏览"按钮选择WeChat可执行文件
2. 设置需要启动的WeChat实例数量
3. 点击"启动WeChat"按钮开始运行

## 注意事项

- 仅支持选择WeChat.exe或Weixin.exe文件
- 启动次数限制在1-10次之间
- 配置信息会自动保存在同目录下的config.json文件中