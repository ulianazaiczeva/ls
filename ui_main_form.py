from PyQt5 import QtCore, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(600, 450)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(MainForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(250, 0))
        self.widget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.building_params_group_box = QtWidgets.QGroupBox(self.widget)
        self.building_params_group_box.setObjectName("building_params_group_box")
        self.formLayout_2 = QtWidgets.QFormLayout(self.building_params_group_box)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.building_params_group_box)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.evolution_step_spin = QtWidgets.QSpinBox(self.building_params_group_box)
        self.evolution_step_spin.setMinimum(1)
        self.evolution_step_spin.setMaximum(12)
        self.evolution_step_spin.setObjectName("evolution_step_spin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.evolution_step_spin)
        self.label_3 = QtWidgets.QLabel(self.building_params_group_box)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.init_x_spin = QtWidgets.QSpinBox(self.building_params_group_box)
        self.init_x_spin.setMinimum(1)
        self.init_x_spin.setMaximum(10000)
        self.init_x_spin.setObjectName("init_x_spin")
        self.horizontalLayout_3.addWidget(self.init_x_spin)
        self.init_y_spin = QtWidgets.QSpinBox(self.building_params_group_box)
        self.init_y_spin.setMinimum(1)
        self.init_y_spin.setMaximum(10000)
        self.init_y_spin.setObjectName("init_y_spin")
        self.horizontalLayout_3.addWidget(self.init_y_spin)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_4 = QtWidgets.QLabel(self.building_params_group_box)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.step_length_spin = QtWidgets.QSpinBox(self.building_params_group_box)
        self.step_length_spin.setMinimum(1)
        self.step_length_spin.setMaximum(1000)
        self.step_length_spin.setProperty("value", 10)
        self.step_length_spin.setObjectName("step_length_spin")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.step_length_spin)
        self.verticalLayout_2.addWidget(self.building_params_group_box)
        self.definition_group_box = QtWidgets.QGroupBox(self.widget)
        self.definition_group_box.setObjectName("definition_group_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.definition_group_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.definition_group_box)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.file_name_edit = QtWidgets.QLineEdit(self.definition_group_box)
        self.file_name_edit.setReadOnly(True)
        self.file_name_edit.setObjectName("file_name_edit")
        self.horizontalLayout_2.addWidget(self.file_name_edit)
        self.open_file_button = QtWidgets.QToolButton(self.definition_group_box)
        self.open_file_button.setObjectName("open_file_button")
        self.horizontalLayout_2.addWidget(self.open_file_button)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.definition_text = QtWidgets.QPlainTextEdit(self.definition_group_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.definition_text.sizePolicy().hasHeightForWidth())
        self.definition_text.setSizePolicy(sizePolicy)
        self.definition_text.setDocumentTitle("")
        self.definition_text.setReadOnly(True)
        self.definition_text.setObjectName("definition_text")
        self.verticalLayout_3.addWidget(self.definition_text)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.definition_group_box)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.widget)
        self.paint_frame = LSystemPaintWidget(MainForm)
        self.paint_frame.setAutoFillBackground(False)
        self.paint_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.paint_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.paint_frame.setObjectName("paint_frame")
        self.horizontalLayout.addWidget(self.paint_frame)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)
        MainForm.setTabOrder(self.evolution_step_spin, self.init_x_spin)
        MainForm.setTabOrder(self.init_x_spin, self.init_y_spin)
        MainForm.setTabOrder(self.init_y_spin, self.step_length_spin)
        MainForm.setTabOrder(self.step_length_spin, self.open_file_button)
        MainForm.setTabOrder(self.open_file_button, self.file_name_edit)
        MainForm.setTabOrder(self.file_name_edit, self.definition_text)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "L-системы"))
        self.building_params_group_box.setTitle(_translate("MainForm", "Параметры построения"))
        self.label.setText(_translate("MainForm", "Этап эволюции:"))
        self.label_3.setText(_translate("MainForm", "Начальная точка (X ; Y):"))
        self.label_4.setText(_translate("MainForm", "Длина шага построения:"))
        self.definition_group_box.setTitle(_translate("MainForm", "Определение L-системы"))
        self.label_5.setText(_translate("MainForm", "Файл определения:"))
        self.open_file_button.setText(_translate("MainForm", "..."))
from ui.widgets.lsystem_paint_widget import LSystemPaintWidget
