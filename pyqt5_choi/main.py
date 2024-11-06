import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import uic
import json


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("count.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :   # 생성자 메소드 : 클래스를 사용해서 객체를 만들 때 바로 실행
        super().__init__()
        self.setupUi(self)
        self.bt_up.clicked.connect(self.func1)
        self.bt_down.clicked.connect(self.func2)
        self.num = 0
        for row in range(4):
            for colum in range(4):
                a = self.gridLayout.itemAtPosition(row, colum).widget()
                if row == 3 and colum == 2:
                    a.clicked.connect(self.back_stay)
                else:
                    a.clicked.connect( (lambda _ , s = a.text(): self.string_stay(s)))
        self.cal = ""
        self.bt_equal.clicked.connect(self.result)
        self.listWidget.itemClicked.connect(self.list_click)
        self.items = []

        self.bt_save.clicked.connect(self.save)
        self.bt_load.clicked.connect(self.load)
    def save(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "파일 저장", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)


    def load(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "파일 열기", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)
        with open(file_name , 'r', encoding='utf-8') as json_file:
            loaded_data = json.load(json_file)
            self.items = loaded_data
        self.listWidget.clear()
        for i in self.items:
            self.listWidget.addItems([i])
    def list_click(self, item):
        self.cal = item.text()
        self.textEdit.setText(item.text())

    def result(self):
        self.items.append(self.cal)
        self.listWidget.addItems([self.cal])
        print(self.cal,self.items)
        answer = str(eval(self.cal))
        self.textEdit.setText(answer)           # eval: "54+32" 이런 string을 알아서 계산해줌
        self.cal = ""

    def back_stay(self):
        self.cal = self.cal[0:len(self.cal)-1]
        self.textEdit.setText(self.cal)
    def string_stay(self , s):
        self.cal += s
        self.textEdit.setText(self.cal)


    def func1(self):
        self.num += 1
        self.label.setText(f"숫자 : {self.num}")
        print("up")
    def func2(self):
        self.num -= 1
        self.label.setText(f"숫자 : {self.num}")
        print("down")
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()