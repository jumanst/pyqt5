import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import json
import math

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("project01.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #self.students = {"김민지": [100,100,100], "박정후": [100,90,80], "차진명": [90,80,70]}

        with open("data.json", "r" , encoding="utf-8") as file:
            self.students  = json.load(file)
        
        self.listWidget.addItems(self.students.keys())
        self.listWidget.itemClicked.connect(self.list_click)
        self.국어평균 = sum([self.students[x][0] for x in self.students])//3
        self.수학평균 = sum([self.students[x][1] for x in self.students])//3
        self.영어평균 = sum([self.students[x][2] for x in self.students])//3
        self.a = self.calculate_std_dev(0, self.국어평균)
        self.b = self.calculate_std_dev(1, self.수학평균)
        self.c = self.calculate_std_dev(2, self.영어평균)

    def calculate_std_dev(self,n ,평균 ):
        scores = [self.students[x][n] for x in self.students]
        variance = sum((score - 평균) ** 2 for score in scores) / len(scores)
        std_dev = math.sqrt(variance)
        return std_dev


    def list_click(self,item):
        self.one = int(self.students[item.text()][0])
        self.two = int(self.students[item.text()][1])
        self.thr = int(self.students[item.text()][2])
        self.variance = sum( (x - (self.one + self.two + self.thr) // 3) ** 2 for x in self.students[item.text()]) / 2
        self.std_dev = math.sqrt(self.variance)
        self.tableWidget.setItem(2, 1, QTableWidgetItem(str(round(self.a, 1))))
        self.tableWidget.setItem(2, 2, QTableWidgetItem(str(round(self.b, 1))))
        self.tableWidget.setItem(2, 3, QTableWidgetItem(str(round(self.c, 1))))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(str(self.국어평균)))
        self.tableWidget.setItem(1, 2, QTableWidgetItem(str(self.수학평균)))
        self.tableWidget.setItem(1, 3, QTableWidgetItem(str(self.영어평균)))
        self.tableWidget.setItem(0, 0, QTableWidgetItem(item.text()))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(str(self.one)))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(str(self.two)))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(str(self.thr)))
        self.tableWidget.setItem(0, 4, QTableWidgetItem(str((self.one+self.two+self.thr)//3)))
        self.tableWidget.setItem(0, 5, QTableWidgetItem(str(round(self.std_dev, 1))))







if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()