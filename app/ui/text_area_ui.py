# Form implementation generated from reading ui file 'app/ui/text_area.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addStretch(0)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.first_row_display = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_row_display.sizePolicy().hasHeightForWidth())
        self.first_row_display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.first_row_display.setFont(font)
        self.first_row_display.setText("")
        self.first_row_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.first_row_display.setObjectName("first_row_display")
        self.gridLayout.addWidget(self.first_row_display, 0, 0, 1, 1)
        self.second_row_display = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.second_row_display.sizePolicy().hasHeightForWidth())
        self.second_row_display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.second_row_display.setFont(font)
        self.second_row_display.setText("")
        self.second_row_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.second_row_display.setObjectName("second_row_display")
        self.gridLayout.addWidget(self.second_row_display, 1, 0, 1, 1)
        self.third_row_display = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.third_row_display.sizePolicy().hasHeightForWidth())
        self.third_row_display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.third_row_display.setFont(font)
        self.third_row_display.setText("")
        self.third_row_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.third_row_display.setObjectName("third_row_display")
        self.gridLayout.addWidget(self.third_row_display, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_2.addStretch(0)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tex Area"))
