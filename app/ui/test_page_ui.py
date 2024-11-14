# Form implementation generated from reading ui file 'app/ui/test_page.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from app.widgets.mode_button import ModeButton
from app.widgets.reset_button import ResetButton
from app.widgets.settings_button import SettingsButton
from app.widgets.local_profile_button import LocalProfileButton


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.reset_button = ResetButton(
			'app/assets/reset_light.svg', 'app/assets/reset_dark.svg', parent=Form
		)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setMinimumSize(QtCore.QSize(90, 90))
        self.reset_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.reset_button.setText("")
        self.reset_button.setIconSize(QtCore.QSize(90, 90))
        self.reset_button.setFlat(True)
        self.reset_button.setObjectName("reset_button")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.reset_button)
        self.horizontalLayout.addWidget(self.reset_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        logo = QtWidgets.QLabel('QTyper', Form)
        font = QtGui.QFont('monospace')
        font.setPointSize(36)
        logo.setFont(font)
        self.horizontalLayout_2.addWidget(logo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.mode_button = ModeButton(
			'app/assets/mode_light.svg', 'app/assets/mode_dark.svg', parent=Form, main_window=Form.main_window
		)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_button.sizePolicy().hasHeightForWidth())
        self.mode_button.setSizePolicy(sizePolicy)
        self.mode_button.setMinimumSize(QtCore.QSize(90, 90))
        self.mode_button.setSizeIncrement(QtCore.QSize(5, 5))
        self.mode_button.setBaseSize(QtCore.QSize(90, 90))
        self.mode_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.mode_button.setText("")
        self.mode_button.setIconSize(QtCore.QSize(90, 90))
        self.mode_button.setFlat(True)
        self.mode_button.setObjectName("mode_button")
        self.buttonGroup.addButton(self.mode_button)
        self.horizontalLayout_2.addWidget(self.mode_button)
        self.local_profile_button = LocalProfileButton(
			'app/assets/local_profile_light.svg',
			'app/assets/local_profile_dark.svg',
			Form,
		)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.local_profile_button.sizePolicy().hasHeightForWidth())
        self.local_profile_button.setSizePolicy(sizePolicy)
        self.local_profile_button.setMinimumSize(QtCore.QSize(90, 90))
        self.local_profile_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.local_profile_button.setText("")
        self.local_profile_button.setIconSize(QtCore.QSize(90, 90))
        self.local_profile_button.setFlat(True)
        self.local_profile_button.setObjectName("local_profile_button")
        self.buttonGroup.addButton(self.local_profile_button)
        self.horizontalLayout_2.addWidget(self.local_profile_button)
        self.settings_button = SettingsButton(
			'app/assets/settings_light.svg', 'app/assets/settings_dark.svg', parent=Form
		)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMinimumSize(QtCore.QSize(90, 90))
        self.settings_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.settings_button.setText("")
        self.settings_button.setIconSize(QtCore.QSize(90, 90))
        self.settings_button.setFlat(True)
        self.settings_button.setObjectName("settings_button")
        self.buttonGroup.addButton(self.settings_button)
        self.horizontalLayout_2.addWidget(self.settings_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.main_container = QtWidgets.QStackedWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setMinimumSize(QtCore.QSize(1200, 0))
        self.main_container.setMaximumSize(QtCore.QSize(1400, 16777215))
        # self.main_container.setBaseSize(QtCore.QSize(1400, 0))
        self.main_container.setObjectName("main_container")

        self.horizontalLayout_4.addWidget(self.main_container)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test Page"))
