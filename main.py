import sys
import os
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from . import __version__

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 371, 123))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_root = QtWidgets.QLabel(self.groupBox)
        self.label_root.setObjectName("label_root")
        self.verticalLayout.addWidget(self.label_root)
        self.label_user = QtWidgets.QLabel(self.groupBox)
        self.label_user.setObjectName("label_user")
        self.verticalLayout.addWidget(self.label_user)
        self.label_ScriptPath = QtWidgets.QLabel(self.groupBox)
        self.label_ScriptPath.setObjectName("label_ScriptPath")
        self.verticalLayout.addWidget(self.label_ScriptPath)
        self.label_Time = QtWidgets.QLabel(self.groupBox)
        self.label_Time.setObjectName("label_Time")
        self.verticalLayout.addWidget(self.label_Time)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 351, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(290, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        NowDate = datetime.datetime.now()
        self.label_Time.setText(f'Time :{x}'.format(x=NowDate))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test_forNuke {}").format(x=__version__))
        self.groupBox.setTitle(_translate("Form", "information"))
        self.label_root.setText(_translate("Form", "Root : "))
        self.label_user.setText(_translate("Form", "User :"))
        self.label_ScriptPath.setText(_translate("Form", "Script Path : "))
        self.label_Time.setText(_translate("Form", "Time :"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.pushButton.setText(_translate("Form", "Ok"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
