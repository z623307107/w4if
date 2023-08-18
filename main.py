import sys
import time
import math
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QSlider
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QTimer

from draw import Ui_Draw

class Draw(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Draw()
        self.ui.setupUi(self)

        # 以下是所有的参数 及其默认值 可在控件处调整 程序自动重绘

        self.bgcolor = QColor(169, 169, 169) # 背景色
        self.color1 = QColor(0, 0, 0)        # 颜色1
        self.color2 = QColor(255, 255, 255)  # 颜色2

        self.line_dist = 27 # 线间距
        self.line_width = 9 # 线宽度
        self.block_length = 3 # 块长度

        self.a = 230 # 主图边长
        self.r = -45 # 主图角度

        self.up = 0 # 上留边
        self.down = 0 # 下留边
        self.left = 0 # 左留边
        self.right = 0 # 右留边

        self.shake_algle = 0 # 摇晃角度
        self.shake_frequency = 333 # 往复一次花费时间 单位毫秒
        self.shake_range = 50 # 晃动距离
        self.w_offset = 0
        self.h_offset = 0

        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.update_offsets)
        self.animation_timer.start(1000//60) # 每秒60帧

        # 以下是控件的事件注册

        self.ui.pushButton.clicked.connect(self.choose_color1)
        self.ui.pushButton_2.clicked.connect(self.choose_color2)
        self.ui.pushButton_3.clicked.connect(self.choose_bgcolor)
        self.ui.horizontalSlider.valueChanged[int].connect(self.on_slider_value_changed)
        self.ui.horizontalSlider_2.valueChanged[int].connect(self.on_slider_2_value_changed)

        self.ui.spinBox_2.valueChanged.connect(self.set_line_width)
        self.ui.spinBox_4.valueChanged.connect(self.set_size)

        self.ui.lineEdit.textEdited.connect(self.on_slider_value_changed)
        self.ui.lineEdit_2.textEdited.connect(self.on_slider_2_value_changed)

    def update_offsets(self):

        # 取时间戳 单位毫秒
        t = time.time() * 1000
        # 将时间戳转换成[0, shake_frequency]之间的值
        p = (t % (self.shake_frequency*2) - self.shake_frequency)
        # 将p转换成相位[-1, 1] 其移动方式为 -1 -> 0 -> 1 -> 0-> -1
        p = (abs(p) - self.shake_frequency/2) / self.shake_frequency/2
        # 将相位移动至真实的shake范围
        p *= self.shake_range
        # 计算xy的偏移度数
        self.w_offset = p * math.cos(math.radians(self.shake_algle))
        self.h_offset = p * math.sin(math.radians(self.shake_algle))
        self.repaint() # 重绘窗口

    def choose_color1(self):
        self.color1 = QColorDialog().getColor()
        self.update()

    def choose_color2(self):
        self.color2 = QColorDialog().getColor()
        self.update()

    def choose_bgcolor(self):
        self.bgcolor = QColorDialog().getColor()
        self.update()

    # 主图角度
    def on_slider_value_changed(self, value):
        try:
            self.r = int(value)
            self.ui.lineEdit.setText(str(value))
            self.update()
        except ValueError:
            return

    # shake角度
    def on_slider_2_value_changed(self, value):
        try:
            self.shake_algle = int(value)
            self.ui.lineEdit_2.setText(str(value))
            self.update()
        except ValueError:
            return

    def set_line_width(self, value):
        self.line_width = value
        self.update()

    def set_size(self, value):
        self.line_dist = value * 3
        self.block_length = (value+1)// 3
        self.update()

    # 画图函数
    # 由于主图和背景图的规律相同
    # 使用此函数传递不同的参数即可分别绘制主图和背景图
    # 参数是边长和角度
    def drawxxx(self, a=400, r=0, w_offset = 0, h_offset = 0):

            # 初始化画板 找到合适的位置和角度
            p = QPainter(self)
            # p.translate(self.height()//2, self.height()//2)
            p.translate(self.height()//2 + w_offset, self.height()//2 + h_offset)
            p.rotate(r)
            p.translate(-a//2, -a//2)

            # 设置画笔和笔刷 即边框色和填充色
            p.setPen(QPen(self.bgcolor))
            p.setBrush(QBrush(self.bgcolor))

            # 绘制背景 根据设置的留余
            p.drawRect(0 - self.left, 0 - self.up, a + self.left + self.right, a + self.up + self.down)

            # 重置边框参数 使边框透明
            p.setPen(QPen(QColor(0, 0, 0, 0)))

            # 核心算法 根据x和y 选择颜色1或颜色2
            # 并按照线间距，线宽度，块长度三个参数，绘制所有的小方块。
            # 错位的思路是看似是一个小方块其实是三个同色的小方块
            # 而每行错一位计算颜色
            for y in range(0, (a+1)//self.line_dist):
                for x in range(0, (a+1)//self.block_length):
                    p.setBrush(QBrush(self.color1 if (x + y % 6) % 6 < 3 else self.color2))
                    p.drawRect(x*self.block_length, y*self.line_dist + self.line_dist//2, self.block_length, self.line_width)

    # 绘制事件 被自动调用
    def paintEvent(self, evt):

        # 预览颜色的窗口
        self.ui.label.setStyleSheet(f'background-color: rgb({self.color1.red()}, {self.color1.green()}, {self.color1.blue()})')
        self.ui.label_2.setStyleSheet(f'background-color: rgb({self.color2.red()}, {self.color2.green()}, {self.color2.blue()})')
        self.ui.label_3.setStyleSheet(f'background-color: rgb({self.bgcolor.red()}, {self.bgcolor.green()}, {self.bgcolor.blue()})')

        # 绘制背景图

        if self.ui.checkBox.isChecked():
            self.drawxxx(900, 45, self.w_offset, self.h_offset)
        else:
            self.drawxxx(a = 900, r=45)

        # 遮住被画到控件区域的线
        p = QPainter(self)
        p.setPen(QPen(QColor(255,255,255)))
        p.setBrush(QBrush(QColor(255,255,255)))
        p.drawRect(self.height(), 0, self.width() - self.height(), self.height())

        # 绘制主图
        if self.ui.checkBox.isChecked():
            self.drawxxx(self.a, self.r, self.w_offset, self.h_offset)
        else:
            self.drawxxx(self.a, self.r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    draw = Draw()
    draw.show()
    sys.exit(app.exec_())
