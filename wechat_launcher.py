import sys
import json
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QLabel, QLineEdit, QPushButton,
                           QFileDialog, QMessageBox, QSpinBox)
from PyQt5.QtCore import Qt

CONFIG_FILE = 'config.json'

class WeChatLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadConfig()

    def initUI(self):
        self.setWindowTitle('WeChat启动器')
        self.setFixedSize(600, 200)

        # 主窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 文件路径选择
        path_layout = QHBoxLayout()
        path_label = QLabel('WeChat路径：')
        self.path_input = QLineEdit()
        self.path_input.setReadOnly(True)
        browse_btn = QPushButton('浏览')
        browse_btn.clicked.connect(self.browsePath)
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(browse_btn)

        # 启动次数设置
        count_layout = QHBoxLayout()
        count_label = QLabel('启动次数：')
        self.count_input = QSpinBox()
        self.count_input.setRange(1, 10)
        count_layout.addWidget(count_label)
        count_layout.addWidget(self.count_input)
        count_layout.addStretch()

        # 启动按钮
        launch_btn = QPushButton('启动WeChat')
        launch_btn.clicked.connect(self.launchWeChat)

        # 添加所有组件到主布局
        layout.addLayout(path_layout)
        layout.addLayout(count_layout)
        layout.addWidget(launch_btn)

    def browsePath(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            '选择WeChat可执行文件',
            '',
            'WeChat (Weixin.exe;WeChat.exe)'
        )
        if file_path:
            file_name = Path(file_path).name.lower()
            if file_name not in ['weixin.exe', 'wechat.exe']:
                QMessageBox.warning(self, '错误', '请选择WeChat.exe或Weixin.exe文件！')
                return
            self.path_input.setText(file_path)
            self.saveConfig()

    def launchWeChat(self):
        path = self.path_input.text()
        count = self.count_input.value()

        if not path:
            QMessageBox.warning(self, '错误', '请先选择WeChat可执行文件！')
            return

        if not Path(path).exists():
            QMessageBox.warning(self, '错误', '所选文件不存在！')
            return

        for _ in range(count):
            try:
                import subprocess
                subprocess.Popen([path])
            except Exception as e:
                QMessageBox.critical(self, '错误', f'启动失败：{str(e)}')
                return

        self.saveConfig()

    def loadConfig(self):
        try:
            if Path(CONFIG_FILE).exists():
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.path_input.setText(config.get('path', ''))
                    self.count_input.setValue(config.get('count', 1))
        except Exception as e:
            QMessageBox.warning(self, '警告', f'加载配置失败：{str(e)}')

    def saveConfig(self):
        try:
            config = {
                'path': self.path_input.text(),
                'count': self.count_input.value()
            }
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            QMessageBox.warning(self, '警告', f'保存配置失败：{str(e)}')

def main():
    app = QApplication(sys.argv)
    window = WeChatLauncher()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()