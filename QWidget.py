import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建应用程序,sys.argv获取命令行参数
    app = QApplication(sys.argv)
    # 创建应用窗口
    window = QWidget()
    # 设置窗口尺寸
    window.resize(300, 200)
    # 设置窗口位置
    window.move(100, 200)
    # 设置窗口标题
    window.setWindowTitle('第一个pyqt5应用程序')
    # 显示窗口
    window.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全退出,app.exec()是程序退出码，正常退出为0，异常退出为1
    sys.exit(app.exec())