# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from final_bill import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_stage(object):
    def check_out(self):
        if (self.checkBox.isChecked() == True and self.spinBox.value() != 0):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_TC()
            self.ui.setupUi(self.window)
            self.window.show()
            o = "orange"
            self.ui.TD_label.setText(o)

            self.ui.spinny.setText(f"{self.spinBox.value()}")
            total = self.spinBox.value() * 1.06
            self.ui.label_4.setText(f"${total}")
            final_total = total
            self.ui.label_5.setText(f"${final_total}")

            if (self.checkBox_2.isChecked() == True and self.spinBox_2.value() !=0):
                o = "Apple"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_2.value()}")
                total_1 = self.spinBox_2.value() * 1.25
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")

            elif self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0:
                o = "Bananas"
                self.ui.label_9.setText(o)
                self.ui.label_10.setText(f"{self.spinBox_3.value()}")
                total_1 = self.spinBox_3.value() * 0.75
                self.ui.label_14.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")


            elif (self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0):
                o = "Poptarts"
                self.ui.label_12.setText(o)
                self.ui.label_13.setText(f"{self.spinBox_4.value()}")
                total_1 = self.spinBox_4.value() * 2.67
                self.ui.label_15.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")

                if self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_3.value()}")
                    total_2 = self.spinBox_3.value() * 0.75
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1  + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if (self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0):
                        o = "Apple"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_2.value()}")
                        total_3 = self.spinBox_2.value() * 1.25
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1  + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

                if self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0:
                    o = "Apple"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_2.value()}")
                    total_2 = self.spinBox_2.value() * 1.25
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
                        o = "Bananas"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_3.value()}")
                        total_3 = self.spinBox_3.value() * 0.75
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

        if (self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_TC()
            self.ui.setupUi(self.window)
            self.window.show()

            o = "Apple"
            self.ui.TD_label.setText(o)
            self.ui.spinny.setText(f"{self.spinBox_2.value()}")
            total = self.spinBox_2.value() * 1.25
            self.ui.label_4.setText(f"${total}")
            final_total = total
            self.ui.label_5.setText(f"${final_total}")

            if (self.checkBox.isChecked() == True and self.spinBox.value() != 0):
                o = "Orange"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_2.value()}")
                total_1 = self.spinBox.value() * 1.06
                self.ui.label_8.setText(f"{total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")
                if self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_3.value()}")
                    total_2 = self.spinBox_3.value() * 0.75
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if (self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0):
                        o = "Poptarts"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_4.value()}")
                        total_3 = self.spinBox_4.value() * 2.67
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

                elif self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0:
                    o = "Poptarts"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_4.value()}")
                    total_2 = self.spinBox_4.value() * 2.67
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
                        o = "Bananas"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_3.value()}")
                        total_3 = self.spinBox_3.value() * 0.75
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

            if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
                o = "Bananas"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_3.value()}")
                total_1 = self.spinBox_3.value() * 0.75
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")
                if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox.value()}")
                    total_2 = self.spinBox.value() * 1.06
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if (self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0):
                        o = "Poptarts"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_4.value()}")
                        total_3 = self.spinBox_4.value() * 2.67
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

                elif self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0:
                    o = "Poptarts"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_4.value()}")
                    total_2 = self.spinBox_4.value() * 2.67
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                        o = "Oranges"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox.value()}")
                        total_3 = self.spinBox.value() * 1.06
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")
            if (self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0):
                o = "Orange"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_4.value()}")
                total_1 = self.spinBox_4.value() * 2.67
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")
                if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox.value()}")
                    total_2 = self.spinBox.value() * 1.06
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
                        o = "Bananas"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_3.value()}")
                        total_3 = self.spinBox_3.value() * 0.75
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_3
                        self.ui.label_5.setText(f"${final_total}")

                elif self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_3.value()}")
                    total_2 = self.spinBox_3.value() * 0.76
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total +  total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                        o = "Oranges"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox.value()}")
                        total_3 = self.spinBox.value() * 1.06
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

        if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_TC()
            self.ui.setupUi(self.window)
            self.window.show()

            o = "Bananas"
            self.ui.TD_label.setText(o)
            self.ui.spinny.setText(f"{self.spinBox_3.value()}")
            total = self.spinBox_3.value() * 0.75
            self.ui.label_4.setText(f"${total}")
            final_total = total
            self.ui.label_5.setText(f"${final_total}")

            if (self.checkBox.isChecked() == True and self.spinBox.value() != 0):
                o = "Orange"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_2.value()}")
                total_1 = self.spinBox.value() * 1.06
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")
                if self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0:
                    o = "Apple"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_2.value()}")
                    total_2 = self.spinBox_2.value() * 1.25
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if (self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0):
                        o = "Poptarts"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_4.value()}")
                        total_3 = self.spinBox_4.value() * 2.67
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1  + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

                elif self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0:
                    o = "Poptarts"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_4.value()}")
                    total_2 = self.spinBox_4.value() * 2.67
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 +total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
                        o = "Bananas"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_3.value()}")
                        total_3 = self.spinBox_3.value() * 0.75
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 +total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

            if (self.checkBox_2.isChecked() == True and self.spinBox_3.value() != 0):
                o = "Orange"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_3.value()}")
                total_1 = self.spinBox_3.value() * 0.75
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")
                if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                    o = "Orange"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox.value()}")
                    total_2 = self.spinBox.value() * 1.06
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if (self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0):
                        o = "Poptarts"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_4.value()}")
                        total_3 = self.spinBox_4.value() * 2.67
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

                elif self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0:
                    o = "Poptarts"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_4.value()}")
                    total_2 = self.spinBox_4.value() * 2.67
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                        o = "Oranges"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox.value()}")
                        total_3 = self.spinBox.value() * 1.06
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

            if (self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0):
                o = "Orange"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_4.value()}")
                total_1 = self.spinBox_4.value() * 2.67
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")
                if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox.value()}")
                    total_2 = self.spinBox.value() * 1.06
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 +total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if (self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0):
                        o = "Bananas"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_2.value()}")
                        total_3 = self.spinBox_2.value() * 0.75
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

                elif self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0:
                    o = "Apple"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_3.value()}")
                    total_2 = self.spinBox_3.value() * 1.25
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")

                    if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                        o = "Oranges"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox.value()}")
                        total_3 = self.spinBox.value() * 1.06
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")

        if (self.checkBox_4.isChecked() == True and self.spinBox_4.value() != 0):
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_TC()
            self.ui.setupUi(self.window)
            self.window.show()

            o = "Poptarts"
            self.ui.TD_label.setText(o)
            self.ui.spinny.setText(f"{self.spinBox_4.value()}")
            total = self.spinBox_4.value() * 2.67
            self.ui.label_4.setText(f"${total}")
            final_total = total
            self.ui.label_5.setText(f"${final_total}")
            if (self.checkBox.isChecked() == True and self.spinBox.value() != 0):
                o = "Orange"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox.value()}")
                total_1 = self.spinBox.value() * 1.06
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")
                if self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0:
                    o = "Apple"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_2.value()}")
                    total_2 = self.spinBox_2.value() * 1.25
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
                        o = "Bananas"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_3.value()}")
                        total_3 = self.spinBox_3.value() * 0.75
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")
                if self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_3.value()}")
                    total_2 = self.spinBox_3.value() * 0.75
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if (self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0):
                        o = "Apple"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_2.value()}")
                        total_3 = self.spinBox_2.value() * 1.25
                        self.ui.label_15.setText(f"${total_3}")
                        final_total =total + total_1 + total_2 +total_3
                        self.ui.label_5.setText(f"${final_total}")
            if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
                o = "Bananas"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_3.value()}")
                total_1 = self.spinBox_3.value() * 0.75
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")

                if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                    o = "Orange"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox.value()}")
                    total_2 = self.spinBox.value() * 1.06
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if (self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0):
                        o = "Apple"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_2.value()}")
                        total_3 = self.spinBox_2.value() * 2.67
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")
                elif self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0:
                    o = "Apple"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_2.value()}")
                    total_2 = self.spinBox_2.value() * 2.67
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                        o = "Oranges"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox.value()}")
                        total_3 = self.spinBox.value() * 1.06
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")
            if (self.checkBox_2.isChecked() == True and self.spinBox_2.value() != 0):
                o = "Apple"
                self.ui.label_6.setText(o)
                self.ui.label_7.setText(f"{self.spinBox_2.value()}")
                total_1 = self.spinBox_2.value() * 2.67
                self.ui.label_8.setText(f"${total_1}")
                final_total = total + total_1
                self.ui.label_5.setText(f"${final_total}")
                if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox.value()}")
                    total_2 = self.spinBox.value() * 1.06

                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if (self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0):
                        o = "Bananas"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox_3.value()}")
                        total_3 = self.spinBox_3.value() * 0.75
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 + total_3
                        self.ui.label_5.setText(f"${final_total}")
                elif self.checkBox_3.isChecked() == True and self.spinBox_3.value() != 0:
                    o = "Bananas"
                    self.ui.label_9.setText(o)
                    self.ui.label_10.setText(f"{self.spinBox_3.value()}")
                    total_2 = self.spinBox_3.value() * 0.75
                    self.ui.label_14.setText(f"${total_2}")
                    final_total = total + total_1 + total_2
                    self.ui.label_5.setText(f"${final_total}")
                    if self.checkBox.isChecked() == True and self.spinBox.value() != 0:
                        o = "Oranges"
                        self.ui.label_12.setText(o)
                        self.ui.label_13.setText(f"{self.spinBox.value()}")
                        total_3 = self.spinBox.value() * 1.06
                        self.ui.label_15.setText(f"${total_3}")
                        final_total = total + total_1 + total_2 +total_3
                        self.ui.label_5.setText(f"${final_total}")


        else:
            if self.checkBox.isChecked() == False and self.spinBox.value() == 0:
                self.fixer.setText("Not possible")
            if self.checkBox_2.isChecked() == False and self.spinBox_2.value() == 0:
                self.fixer.setText("Not possible")
            if self.checkBox_3.isChecked() == False and self.spinBox_3.value() == 0:
                self.fixer.setText("Not possible")
            if self.checkBox_4.isChecked() == False and self.spinBox_4.value() == 0:
                self.fixer.setText("Not possible")
    def setupUi(self, menu_stage):
        menu_stage.setObjectName("menu_stage")
        menu_stage.setEnabled(True)
        menu_stage.resize(286, 330)
        self.centralwidget = QtWidgets.QWidget(menu_stage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 91, 21))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 70, 35, 10))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 100, 35, 10))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 130, 35, 10))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(90, 150, 35, 16))
        self.label_9.setObjectName("label_9")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 60, 53, 14))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 90, 53, 14))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 120, 53, 14))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 150, 53, 14))
        self.checkBox_4.setObjectName("checkBox_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(160, 60, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 90, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(160, 120, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(160, 150, 42, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.check_out())
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.fixer = QtWidgets.QLabel(self.centralwidget)
        self.fixer.setGeometry(QtCore.QRect(80, 190, 61, 31))
        self.fixer.setText("")
        self.fixer.setObjectName("fixer")
        menu_stage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu_stage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 286, 18))
        self.menubar.setObjectName("menubar")
        menu_stage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menu_stage)
        self.statusbar.setObjectName("statusbar")
        menu_stage.setStatusBar(self.statusbar)

        self.retranslateUi(menu_stage)
        QtCore.QMetaObject.connectSlotsByName(menu_stage)

    def retranslateUi(self, menu_stage):
        _translate = QtCore.QCoreApplication.translate
        menu_stage.setWindowTitle(_translate("menu_stage", "MainWindow"))
        self.label.setText(_translate("menu_stage", "  GROCERIES LIST"))
        self.label_6.setText(_translate("menu_stage", "$1.00"))
        self.label_7.setText(_translate("menu_stage", "$1.25"))
        self.label_8.setText(_translate("menu_stage", "$0.75"))
        self.label_9.setText(_translate("menu_stage", "$2.67"))
        self.checkBox.setText(_translate("menu_stage", "Oranges"))
        self.checkBox_2.setText(_translate("menu_stage", "Apple"))
        self.checkBox_3.setText(_translate("menu_stage", "Bananas"))
        self.checkBox_4.setText(_translate("menu_stage", "PopTarts"))
        self.pushButton.setText(_translate("menu_stage", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_stage = QtWidgets.QMainWindow()
    ui = Ui_menu_stage()
    ui.setupUi(menu_stage)
    menu_stage.show()
    sys.exit(app.exec_())
