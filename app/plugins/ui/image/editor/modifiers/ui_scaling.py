# -*- coding: utf-8 -*-

#  This file is part of DeepSpineTool
#  Copyright (C) 2021 VG-Lab (Visualization & Graphics Lab), Universidad Rey Juan Carlos
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Form implementation generated from reading ui file 'scaling.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_scaling_widget(object):
    def setupUi(self, scaling_widget):
        scaling_widget.setObjectName("scaling_widget")
        scaling_widget.resize(414, 366)
        self.horizontalLayout = QtWidgets.QHBoxLayout(scaling_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.methods_widget = QtWidgets.QWidget(scaling_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methods_widget.sizePolicy().hasHeightForWidth())
        self.methods_widget.setSizePolicy(sizePolicy)
        self.methods_widget.setObjectName("methods_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.methods_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.methods_groupBox = QtWidgets.QGroupBox(self.methods_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methods_groupBox.sizePolicy().hasHeightForWidth())
        self.methods_groupBox.setSizePolicy(sizePolicy)
        self.methods_groupBox.setObjectName("methods_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.methods_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.none_radioButton = QtWidgets.QRadioButton(self.methods_groupBox)
        self.none_radioButton.setChecked(True)
        self.none_radioButton.setObjectName("none_radioButton")
        self.verticalLayout.addWidget(self.none_radioButton)
        self.normalization_radioButton = QtWidgets.QRadioButton(self.methods_groupBox)
        self.normalization_radioButton.setObjectName("normalization_radioButton")
        self.verticalLayout.addWidget(self.normalization_radioButton)
        self.meanNormamalization_radioButton = QtWidgets.QRadioButton(self.methods_groupBox)
        self.meanNormamalization_radioButton.setObjectName("meanNormamalization_radioButton")
        self.verticalLayout.addWidget(self.meanNormamalization_radioButton)
        self.standarization_radioButton = QtWidgets.QRadioButton(self.methods_groupBox)
        self.standarization_radioButton.setObjectName("standarization_radioButton")
        self.verticalLayout.addWidget(self.standarization_radioButton)
        self.verticalLayout_2.addWidget(self.methods_groupBox)
        self._resize_widget1 = QtWidgets.QWidget(self.methods_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._resize_widget1.sizePolicy().hasHeightForWidth())
        self._resize_widget1.setSizePolicy(sizePolicy)
        self._resize_widget1.setObjectName("_resize_widget1")
        self.verticalLayout_2.addWidget(self._resize_widget1)
        self.horizontalLayout.addWidget(self.methods_widget)
        self.params_widget = QtWidgets.QWidget(scaling_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.params_widget.sizePolicy().hasHeightForWidth())
        self.params_widget.setSizePolicy(sizePolicy)
        self.params_widget.setObjectName("params_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.params_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.input_widget = QtWidgets.QWidget(self.params_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_widget.sizePolicy().hasHeightForWidth())
        self.input_widget.setSizePolicy(sizePolicy)
        self.input_widget.setObjectName("input_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.input_widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.inputRange_widget = QtWidgets.QWidget(self.input_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputRange_widget.sizePolicy().hasHeightForWidth())
        self.inputRange_widget.setSizePolicy(sizePolicy)
        self.inputRange_widget.setObjectName("inputRange_widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.inputRange_widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.selectInputRange_checkBox = QtWidgets.QCheckBox(self.inputRange_widget)
        self.selectInputRange_checkBox.setObjectName("selectInputRange_checkBox")
        self.verticalLayout_9.addWidget(self.selectInputRange_checkBox)
        self.customInputRange_widget = QtWidgets.QWidget(self.inputRange_widget)
        self.customInputRange_widget.setObjectName("customInputRange_widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.customInputRange_widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.minInputValue_label = QtWidgets.QLabel(self.customInputRange_widget)
        self.minInputValue_label.setObjectName("minInputValue_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minInputValue_label)
        self.minInputValue_lineEdit = QtWidgets.QLineEdit(self.customInputRange_widget)
        self.minInputValue_lineEdit.setObjectName("minInputValue_lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minInputValue_lineEdit)
        self.maxInputValue_lineEdit = QtWidgets.QLineEdit(self.customInputRange_widget)
        self.maxInputValue_lineEdit.setObjectName("maxInputValue_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxInputValue_lineEdit)
        self.maxInputValue_label = QtWidgets.QLabel(self.customInputRange_widget)
        self.maxInputValue_label.setObjectName("maxInputValue_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxInputValue_label)
        self.verticalLayout_9.addWidget(self.customInputRange_widget)
        self.verticalLayout_7.addWidget(self.inputRange_widget)
        self.verticalLayout_3.addWidget(self.input_widget)
        self.average_widget = QtWidgets.QWidget(self.params_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.average_widget.sizePolicy().hasHeightForWidth())
        self.average_widget.setSizePolicy(sizePolicy)
        self.average_widget.setObjectName("average_widget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.average_widget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.selectCustomAverage_checkBox = QtWidgets.QCheckBox(self.average_widget)
        self.selectCustomAverage_checkBox.setObjectName("selectCustomAverage_checkBox")
        self.verticalLayout_10.addWidget(self.selectCustomAverage_checkBox)
        self.customAverage_widget = QtWidgets.QWidget(self.average_widget)
        self.customAverage_widget.setObjectName("customAverage_widget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.customAverage_widget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.average_Value_label = QtWidgets.QLabel(self.customAverage_widget)
        self.average_Value_label.setObjectName("average_Value_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.average_Value_label)
        self.average_lineEdit = QtWidgets.QLineEdit(self.customAverage_widget)
        self.average_lineEdit.setObjectName("average_lineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.average_lineEdit)
        self.stdDevValue_lineEdit = QtWidgets.QLineEdit(self.customAverage_widget)
        self.stdDevValue_lineEdit.setObjectName("stdDevValue_lineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.stdDevValue_lineEdit)
        self.stdDevValue_label = QtWidgets.QLabel(self.customAverage_widget)
        self.stdDevValue_label.setObjectName("stdDevValue_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.stdDevValue_label)
        self.verticalLayout_10.addWidget(self.customAverage_widget)
        self.verticalLayout_3.addWidget(self.average_widget)
        self.output_widget = QtWidgets.QWidget(self.params_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_widget.sizePolicy().hasHeightForWidth())
        self.output_widget.setSizePolicy(sizePolicy)
        self.output_widget.setObjectName("output_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.output_widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.output_groupBox = QtWidgets.QGroupBox(self.output_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_groupBox.sizePolicy().hasHeightForWidth())
        self.output_groupBox.setSizePolicy(sizePolicy)
        self.output_groupBox.setObjectName("output_groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.output_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.keepDataTypes_radioButton = QtWidgets.QRadioButton(self.output_groupBox)
        self.keepDataTypes_radioButton.setChecked(True)
        self.keepDataTypes_radioButton.setObjectName("keepDataTypes_radioButton")
        self.verticalLayout_4.addWidget(self.keepDataTypes_radioButton)
        self.keepRange_radioButton = QtWidgets.QRadioButton(self.output_groupBox)
        self.keepRange_radioButton.setObjectName("keepRange_radioButton")
        self.verticalLayout_4.addWidget(self.keepRange_radioButton)
        self.convertToReal_radioButton = QtWidgets.QRadioButton(self.output_groupBox)
        self.convertToReal_radioButton.setObjectName("convertToReal_radioButton")
        self.verticalLayout_4.addWidget(self.convertToReal_radioButton)
        self.verticalLayout_5.addWidget(self.output_groupBox)
        self.outputRange_widget = QtWidgets.QWidget(self.output_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputRange_widget.sizePolicy().hasHeightForWidth())
        self.outputRange_widget.setSizePolicy(sizePolicy)
        self.outputRange_widget.setObjectName("outputRange_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.outputRange_widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.selectOuptutRange_checkBox = QtWidgets.QCheckBox(self.outputRange_widget)
        self.selectOuptutRange_checkBox.setObjectName("selectOuptutRange_checkBox")
        self.verticalLayout_6.addWidget(self.selectOuptutRange_checkBox)
        self.customOutputRange_widget = QtWidgets.QWidget(self.outputRange_widget)
        self.customOutputRange_widget.setObjectName("customOutputRange_widget")
        self.formLayout = QtWidgets.QFormLayout(self.customOutputRange_widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.minOutputValue_label = QtWidgets.QLabel(self.customOutputRange_widget)
        self.minOutputValue_label.setObjectName("minOutputValue_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.minOutputValue_label)
        self.minOutputValue_lineEdit = QtWidgets.QLineEdit(self.customOutputRange_widget)
        self.minOutputValue_lineEdit.setObjectName("minOutputValue_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.minOutputValue_lineEdit)
        self.maxOutputValue_label = QtWidgets.QLabel(self.customOutputRange_widget)
        self.maxOutputValue_label.setObjectName("maxOutputValue_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxOutputValue_label)
        self.maxOutputValue_lineEdit = QtWidgets.QLineEdit(self.customOutputRange_widget)
        self.maxOutputValue_lineEdit.setObjectName("maxOutputValue_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxOutputValue_lineEdit)
        self.verticalLayout_6.addWidget(self.customOutputRange_widget)
        self.verticalLayout_5.addWidget(self.outputRange_widget)
        self.verticalLayout_3.addWidget(self.output_widget)
        self._resize_widget3 = QtWidgets.QWidget(self.params_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._resize_widget3.sizePolicy().hasHeightForWidth())
        self._resize_widget3.setSizePolicy(sizePolicy)
        self._resize_widget3.setObjectName("_resize_widget3")
        self.verticalLayout_3.addWidget(self._resize_widget3)
        self.horizontalLayout.addWidget(self.params_widget)
        self._resize_widget2 = QtWidgets.QWidget(scaling_widget)
        self._resize_widget2.setObjectName("_resize_widget2")
        self.horizontalLayout.addWidget(self._resize_widget2)

        self.retranslateUi(scaling_widget)
        self.selectOuptutRange_checkBox.toggled['bool'].connect(self.customOutputRange_widget.setVisible)
        self.selectCustomAverage_checkBox.toggled['bool'].connect(self.customAverage_widget.setVisible)
        self.selectInputRange_checkBox.toggled['bool'].connect(self.customInputRange_widget.setVisible)
        QtCore.QMetaObject.connectSlotsByName(scaling_widget)

    def retranslateUi(self, scaling_widget):
        _translate = QtCore.QCoreApplication.translate
        scaling_widget.setWindowTitle(_translate("scaling_widget", "Form"))
        self.methods_groupBox.setTitle(_translate("scaling_widget", "Scaling"))
        self.none_radioButton.setText(_translate("scaling_widget", "None"))
        self.normalization_radioButton.setText(_translate("scaling_widget", "Normalization"))
        self.meanNormamalization_radioButton.setText(_translate("scaling_widget", "Mean normalization"))
        self.standarization_radioButton.setText(_translate("scaling_widget", "Standardization"))
        self.selectInputRange_checkBox.setText(_translate("scaling_widget", "Select custom input range"))
        self.minInputValue_label.setText(_translate("scaling_widget", "Min. value"))
        self.maxInputValue_label.setText(_translate("scaling_widget", "Max. value"))
        self.selectCustomAverage_checkBox.setText(_translate("scaling_widget", "Select custom average"))
        self.average_Value_label.setText(_translate("scaling_widget", "Average"))
        self.stdDevValue_label.setText(_translate("scaling_widget", "Std. dev."))
        self.output_groupBox.setTitle(_translate("scaling_widget", "Output"))
        self.keepDataTypes_radioButton.setText(_translate("scaling_widget", "Keep image data type"))
        self.keepRange_radioButton.setText(_translate("scaling_widget", "Keep image range"))
        self.convertToReal_radioButton.setText(_translate("scaling_widget", "Convert to float"))
        self.selectOuptutRange_checkBox.setText(_translate("scaling_widget", "Select custom output range"))
        self.minOutputValue_label.setText(_translate("scaling_widget", "Min. value"))
        self.maxOutputValue_label.setText(_translate("scaling_widget", "Max. value"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    scaling_widget = QtWidgets.QWidget()
    ui = Ui_scaling_widget()
    ui.setupUi(scaling_widget)
    scaling_widget.show()
    sys.exit(app.exec_())
