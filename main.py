from PyQt5 import QtCore, QtGui, QtWidgets
import nltk
import PyPDF2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tkinter import filedialog, messagebox

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 362)
        MainWindow.setMinimumSize(QtCore.QSize(371, 362))
        MainWindow.setMaximumSize(QtCore.QSize(371, 362))
        MainWindow.setStyleSheet("background-color: gray;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 20, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 70, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 100, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(40, 130, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(40, 160, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(210, 70, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(210, 100, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(210, 130, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(210, 160, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(40, 190, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(210, 190, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 400, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 240, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resume parser"))
        self.pushButton.setText(_translate("MainWindow", "open file"))
        self.label.setText(_translate("MainWindow", "Choose resume"))
        self.checkBox.setText(_translate("MainWindow", "python"))
        self.checkBox_2.setText(_translate("MainWindow", "C++"))
        self.checkBox_3.setText(_translate("MainWindow", "Software"))
        self.checkBox_4.setText(_translate("MainWindow", "Java"))
        self.checkBox_5.setText(_translate("MainWindow", "OOP"))
        self.checkBox_6.setText(_translate("MainWindow", "SQL"))
        self.checkBox_7.setText(_translate("MainWindow", "Communication"))
        self.checkBox_8.setText(_translate("MainWindow", "Database"))
        self.checkBox_9.setText(_translate("MainWindow", "B.Tech"))
        self.checkBox_10.setText(_translate("MainWindow", "Django"))
        self.label_2.setText(_translate("MainWindow", "----------"*4))
        self.pushButton_2.setText(_translate("MainWindow", "check"))
        
        self.pushButton.setStyleSheet("background-color: black; border: 1px solid black; color: white;")
        self.pushButton_2.setStyleSheet("background-color: black; border: 1px solid black; color: white;")
        
        self.label.setStyleSheet("color: white;")
        self.label_2.setStyleSheet("color: white;")
        
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.clicked)

    def parse_resume(self, resume_text, job_keywords):
    # Tokenize the resume text
        tokens = word_tokenize(resume_text)

        # Remove stopwords from the tokens
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words]

        # Calculate the matching score
        matching_score = len(set(filtered_tokens) & set(job_keywords))

        return matching_score

    def open_file(self):
        self.file_path = filedialog.askopenfilename(initialdir="\\", title="Select Resume",
                                     filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
        try:
            if open(self.file_path,'r'):
                self.label.setText("file Choosed.")
                self.label.setStyleSheet("background-color: green;")
        except:
            pass
        
        
    def clicked(self):
        try:
            with open(self.file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                resume_text = ''
                for page in range(len(pdf_reader.pages)):
                    resume_text += pdf_reader.pages[page].extract_text()
        except:
            messagebox.askokcancel("Error message", "Please choose file first!")
            return None

        
        ##############
        self.job_keywords = []
        self.job_keywords.append("python") if self.checkBox.isChecked() == True else None
        self.job_keywords.append("c++") if self.checkBox_2.isChecked() == True else None
        self.job_keywords.append("software") if self.checkBox_3.isChecked() == True else None
        self.job_keywords.append("java") if self.checkBox_4.isChecked() == True else None
        self.job_keywords.append("oop") if self.checkBox_5.isChecked() == True else None
        self.job_keywords.append("sql") if self.checkBox_6.isChecked() == True else None
        self.job_keywords.append("communication") if self.checkBox_7.isChecked() == True else None
        self.job_keywords.append("database") if self.checkBox_8.isChecked() == True else None
        self.job_keywords.append("b.tech") if self.checkBox_9.isChecked() == True else None
        self.job_keywords.append("django") if self.checkBox_10.isChecked() == True else None
        
        ########
        self.matching_score = self.parse_resume(resume_text, self.job_keywords)
        result = f"Skills match: {self.matching_score} out of {len(self.job_keywords)}"
        self.label_2.setText(result)
        
    
    
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
