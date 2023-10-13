# ---------------------------------
# Autor:             terrasky
# Date:              2023-03-15
# Ver :              v1.3
# Des :              1.2--修复QClour错误
# Des :              1.3--优化界面布局，更新图标
# ---------------------------------


import os
from re import sub
from sys import argv
from sys import exit

from RenameToolui import Ui_window
# from PyQt5.Qt import *
from PyQt5.QtWidgets import QWidget,QApplication,QFileDialog,QTableWidgetItem
from PyQt5.QtGui import QTextCursor,QColor

class MainWindow(QWidget, Ui_window):
    def __init__(self):
        super().__init__()
        # 调用父类setupUi函数
        self.setupUi(self)
        self.list_names = []
        
        # =============更新table设定===============
        # 更新表头
        head = ["原文件名" ,"新文件名" ,"状态"]
        self.table.setHorizontalHeaderLabels(head)
        
        # 更新“原文件名”
        self.file_names = argv
        self.file_names.pop(0)
        self.reFlashTableOne()
        
        # 设置表头跟随内容自动调整宽度
        self.table.resizeColumnsToContents()
        # =============更新table设定===============
        
        # 信号绑定
        self.pb1.clicked.connect(self.pb1Fun)
        self.pb2.clicked.connect(self.pb2Fun)
        self.pb3.clicked.connect(self.pb3Fun)
        self.pb_do.clicked.connect(self.pbDoFun)
        self.pb_input.clicked.connect(self.pbInputFun)
        self.le.textChanged.connect(self.leFun)
        self.te.textChanged.connect(self.teFun)
        self.sBox_1.valueChanged.connect(self.reFlashTableTwo)
        self.sBox_2.valueChanged.connect(self.reFlashTableTwo)
        self.sBox_3.valueChanged.connect(self.reFlashTableTwo)
      
    def pb1Fun(self):
        """按钮1按下"""
        self.le.insert("[L]")
        
    def pb2Fun(self):
        """按钮2按下"""
        self.le.insert("[C]")
        
    def pb3Fun(self):
        """按钮3按下"""
        self.le.insert("[N]")
   
    def pbInputFun(self):
        """按钮导入文件名按下"""
        file_dialog = QFileDialog(parent= self, caption= '输入文件名')
        self.file_names = file_dialog.getOpenFileNames()[0]
        self.reFlashTableOne()
        
    def teFun(self):
        """textEdit内容变化后更新table内容"""
        # 获取当前光标并移动到文档首部
        cursor = self.te.textCursor()
        cursor.movePosition(QTextCursor.Start) 
        self.te.setFocus()
        
        block = cursor.block()
        document = self.te.document()
        
        # 更新 self.list_names
        self.list_names.clear()
        for i in range(document.blockCount()):
            self.list_names.append(block.text())
            cursor.movePosition(QTextCursor.NextBlock) 
            block = cursor.block()
        # 更新 table
        self.reFlashTableTwo()
        

    def leFun(self):
        """更新table的第二列"""
        self.reFlashTableTwo()
        
    def reFlashTableOne(self):
        """更新table的第一列（原文件名）"""
        row_count = len(self.file_names)
        self.table.setRowCount(row_count)
        row = 0
        for file in self.file_names:
            os.chdir(os.path.dirname(file))
            file = os.path.basename(file)
            
            item = QTableWidgetItem()
            item.setText(file)
            self.table.setItem(row,0,item)
            row += 1
        self.table.resizeColumnsToContents()
            
    def reFlashTableTwo(self):
        """更新table的第二列（新文件名）"""
        row_count = self.table.rowCount()
        num_start = self.sBox_1.value()
        num_step = self.sBox_2.value()
        num_dig = self.sBox_3.value()
        replace_num = "{:0>" + str(num_dig) + "d}"

        for i in range(row_count):
            item = QTableWidgetItem()
            text = self.le.text()
            # 如果有[L]  进行替换
            if i<len(self.list_names):
                replace_name = self.list_names[i]
            else:
                replace_name = ''
            text = sub("\[L\]", replace_name, text)
            
            # 如果有[C]  进行替换
            replace = replace_num.format(num_start)
            text = sub("\[C\]", replace, text)
            num_start = num_start + num_step
            
            # 如果有[N]  进行替换
            # replace = replace_num.format(num_start)
            file = self.table.item(i,0).text()
            replace = os.path.splitext(file)[0]
            text = sub("\[N\]", replace, text)

            # 补充扩展名
            file = self.table.item(i,0).text()
            file_exe = os.path.splitext(file)[1]
            text = text + file_exe
            
            # 更新新文件名
            item.setText(text)
            self.table.setItem(i,1,item)
            
        self.table.resizeColumnsToContents()
        
    def pbDoFun(self):
        row_count = self.table.rowCount()
        for i in range(row_count):
            item1 = self.table.item(i,0).text()
            item2 = self.table.item(i,1).text()
            item = QTableWidgetItem()
            print(item1,item2)
            try:
                os.rename(item1,item2)
                item.setText("成功")
                item.setForeground(QColor("green"))
            except:
                item.setText("错误")
                item.setForeground(QColor("red"))
            self.table.setItem(i,2,item)

            
      
if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    
    window.show()
    exit(app.exec_())
    
    