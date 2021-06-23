from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox, QAbstractItemView

tokens = []

token = {
    'if': 'Reserved word',
    'then': 'Reserved word',
    'end': 'Reserved word',
    'repeat': 'Reserved word',
    'until': 'Reserved word',
    'read': 'Reserved word',
    'write': 'Reserved word',

    '+': 'Addition operator',
    '-': 'Subtract operator',
    '*': 'Multiplication operator',
    '/': 'Division operator',
    '=': 'Equal operator',
    '<': 'Less than operator',
    '>': 'Greater than operator',
    '(': 'Open bracket',
    ')': 'Closed bracket',
    ';': 'Semicolon operator',
    ':=': 'Assign operator'

}

tokentype = []


def get_tokens():
    for i in tokens:
        if i in token.keys():
            tokentype.append(token.get(i))
        elif str(i[0]).isnumeric():
            tokentype.append("Number")
        else:
            tokentype.append("Identifier")


def scan():
    error = ""
    infl = open('inputfile.txt', 'r')
    xline = infl.readlines()
    state = "start"
    x = ""
    line = 0
    for i in xline:
        character = 0
        line += 1
        i = i + " "
        while character < len(i):
            if state == "comment":
                if i[character] == '}':
                    state = "start"
            elif state == "start":
                if i[character] == '{':
                    state = "comment"
                elif i[character] == '+':
                    tokens.append('+')
                elif i[character] == '-':
                    tokens.append('-')
                elif i[character] == '*':
                    tokens.append('*')
                elif i[character] == '/':
                    tokens.append('/')
                elif i[character] == '=':
                    tokens.append('=')
                elif i[character] == ':':
                    character += 1
                    state = "assg"
                elif i[character] == '<':
                    tokens.append('<')
                elif i[character] == '>':
                    tokens.append('>')
                elif i[character] == '(':
                    tokens.append('(')
                elif i[character] == ')':
                    tokens.append(')')
                elif i[character] == ';':
                    tokens.append(';')
                elif i[character].isalpha():
                    state = "letter"
                elif i[character].isdigit():
                    state = "Num"
                elif i[character].isspace():
                    pass
                else:
                    get_tokens()
                    error = f"token: {i[character]} is invalid in line: {line}"
                    return error
            if state == "letter":
                if i[character].isalpha():
                    x = x + i[character]
                elif i[character].isdigit():
                    get_tokens()
                    error = f"invalid symbol for identifier in line : {line}"
                    return error
                elif not i[character].isalpha():
                    state = "start"
                    tokens.append(x)
                    character -= 1
                    x = ""
            if state == "assg":
                if i[character] == "=":
                    tokens.append(':=')
                    state = "start"
                else:
                    error = f"token: {i[character]} is invalid in line: {line}"
                    get_tokens()
                    return error

            if state == "decimal":
                if i[character].isdigit():
                    state = "Num"
                elif not i[character].isdigit():
                    x = x + i[character]
                    error = f"token: {x} is invalid in line: {line}"
                    get_tokens()
                    return error

            if state == "Num":
                if i[character].isdigit():
                    x = x + i[character]
                elif i[character].isalpha():
                    get_tokens()
                    error = f"invalid symbol for identifier in line: {line}"
                    return error
                elif i[character] == ".":
                    state = "decimal"
                    x = x + i[character]
                else:
                    tokens.append(x)
                    character -= 1
                    state = "start"
                    x = ""
            character = character + 1

    get_tokens()
    return error


##  GUI CODE
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setMaximumSize(1080, 720)
        Form.setMinimumSize(1080, 720)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMaximumSize(QtCore.QSize(403, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.tableWidget.setColumnWidth(0, 0)
        self.tableWidget.setColumnWidth(1, 0)
        self.tableWidget.resizeColumnsToContents()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.textEdit, self.pushButton)
        Form.setTabOrder(self.pushButton, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.tableWidget)
        self.pushButton_2.clicked.connect(lambda: self.browse())
        self.pushButton.clicked.connect(lambda: self.scan())
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CSE 439 - Scanner Project"))
        self.textEdit.setPlaceholderText(_translate("Form", "Write Code here..."))
        self.pushButton.setText(_translate("Form", "Scan Code"))
        self.pushButton.setShortcut(_translate("Form", "Return"))
        self.label.setText(_translate("Form", "OR"))
        self.pushButton_2.setText(_translate("Form", "Choose File"))
        self.label_2.setText(_translate("Form", "No File Chosen"))

    def browse(self):
        print("Button Pressed!")
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        with open(path, "r") as f:
            self.label_2.setText("File Chosen")
            x = f.read()
            f.close()
        infl = open('inputfile.txt', 'w')
        infl.write(x)
        infl.close()
        self.textEdit.setText(x)

    def scan(self):
        tokens.clear()
        tokentype.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        s = self.textEdit.toPlainText()
        infl = open('inputfile.txt', 'w')
        infl.write(s)
        infl.close()
        t = scan()
        self.populateTable()
        print(tokens)
        print(tokentype)
        if t != "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid Token!")
            msg.setInformativeText(t)
            msg.setWindowTitle("Error")
            msg.exec_()

    def populateTable(self):
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(tokens) - 1)
        self.tableWidget.setHorizontalHeaderLabels(['Token Name', 'Token Type'])

        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        row = 0
        for r in tokens:
            col = 0
            cell = QTableWidgetItem(str(r))
            self.tableWidget.setItem(row, col, cell)
            cell.setTextAlignment(Qt.AlignCenter)
            row += 1

        row = 0
        for r in tokentype:
            col = 1
            cell = QTableWidgetItem(str(r))
            self.tableWidget.setItem(row, col, cell)
            cell.setTextAlignment(Qt.AlignCenter)
            row += 1


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
