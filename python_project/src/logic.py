from __future__ import print_function
from PySide2.QtWidgets import QApplication,QMainWindow, QFileDialog
from src.form import Ui_MainWindow
import threading
from src.table_logic import *
from src.reading import *
import re
import cmath
from datetime import datetime
from PySide2.QtGui import QIcon
import os
from src.root import *
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("rsc/icon.png"))
        pixmap = QtGui.QPixmap('rsc/cinv.png')
        self.ui.label_image.setPixmap(pixmap)
        data = [['','','','','','','','','']]
        self.model = TableModel(data)
        self.ui.tableView_temp.setModel(self.model)
        header = self.ui.tableView_temp.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        #self.get_data()

        frameStyle = QtWidgets.QFrame.Sunken | QtWidgets.QFrame.Panel

        #self.openFileNameLabel = QtWidgets.QLabel()
        #self.openFileNameLabel.setFrameStyle(frameStyle)

        #self.iconComboBox.currentIndexChanged.connect(self.setIcon)
        self.ui.comboBox_file.currentIndexChanged.connect(self.show_data)
        self.ui.pushButton_open_dut.clicked.connect(self.get_root_dut)
        self.ui.pushButton_open_thru.clicked.connect(self.get_root_thru)
        self.ui.pushButton_open_line.clicked.connect(self.get_root_line)
        self.ui.pushButton_open_open.clicked.connect(self.get_root_open)
        self.ui.pushButton_correct_dut.clicked.connect(self.create_dut)
        self.root_dut = Root('', '')
        self.root_thru = Root('', '')
        self.root_line = Root('', '')
        self.root_open = Root('', '')
        self.root_correct_dut = Root('', '')
        self.matrix_dut = []
        self.matrix_thru = []
        self.matrix_line = []
        self.matrix_open = []
        self.matrix_correct_dut = []

        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def show_data(self):
        root = self.ui.comboBox_file.currentText()
        print(root)
        print(self.root_correct_dut.file_name)
        mat = []
        name = ''
        if root == self.root_dut.file_name:
            mat = self.matrix_dut
            name = self.root_dut.name
        if root == self.root_thru.file_name:
            mat = self.matrix_thru
            name = self.root_thru.name
        if root == self.root_line.file_name:
            mat = self.matrix_line
            name = self.root_line.name
        if root == self.root_open.file_name:
            mat = self.matrix_open
            name = self.root_open.name
        if root == self.root_correct_dut.file_name:
            mat = self.matrix_correct_dut
            name = self.root_correct_dut.name
            #print('entre')
        if len(mat) > 0:
            #print('volvi a entrar')
            #print(len(mat))
            self.model = TableModel(mat)
            self.ui.tableView_temp.setModel(self.model)
            self.ui.label_file.setText(name)

    def create_dut(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", '')
        self.root_correct_dut = Root(file_name, 'correct_dut')
        self.get_data(self.root_dut.root, self.root_thru.root, self.root_line.root, self.root_open.root,self.root_correct_dut.root)
        self.update_combo_box()

    def update_combo_box(self):
        self.ui.comboBox_file.clear()
        to_add = []
        if self.ui.lineEdit_dut.text():
            to_add.append(self.ui.lineEdit_dut.text())
        if self.ui.lineEdit_thru.text():
            to_add.append(self.ui.lineEdit_thru.text())
        if self.ui.lineEdit_line.text():
            to_add.append(self.ui.lineEdit_line.text())
        if self.ui.lineEdit_open.text():
            to_add.append(self.ui.lineEdit_open.text())
        if self.root_correct_dut.root != '':
            to_add.append(self.root_correct_dut.file_name)
        self.ui.comboBox_file.addItems(set(to_add))

    def get_root_dut(self):
        options = QtWidgets.QFileDialog.Options()
        root, f = QtWidgets.QFileDialog.getOpenFileName(self,"","","(*.s2p)", "", options)
        if root:
            self.root_dut = Root(root, 'dut')
            self.ui.lineEdit_dut.setText(self.root_dut.file_name)
            obj = self.create_objects(self.root_dut.root)
            self.matrix_dut = []
            for o in obj:
                self.matrix_dut.append([str(o.frequency), str(o.s11.real), str(o.s11.imag),
                            str(o.s21.real), str(o.s21.imag), str(o.s12.real),
                            str(o.s12.imag), str(o.s22.real), str(o.s22.imag)])
            self.update_combo_box()

    def get_root_thru(self):
        options = QtWidgets.QFileDialog.Options()
        root, f = QtWidgets.QFileDialog.getOpenFileName(self,"","","(*.s2p)", "", options)
        if root:
            self.root_thru = Root(root, 'thru')
            self.ui.lineEdit_thru.setText(self.root_thru.file_name)
            obj = self.create_objects(self.root_thru.root)
            self.matrix_thru = []
            for o in obj:
                self.matrix_thru.append([str(o.frequency), str(o.s11.real), str(o.s11.imag),
                                        str(o.s21.real), str(o.s21.imag), str(o.s12.real),
                                        str(o.s12.imag), str(o.s22.real), str(o.s22.imag)])
            self.update_combo_box()

    def get_root_line(self):
        options = QtWidgets.QFileDialog.Options()
        root, f = QtWidgets.QFileDialog.getOpenFileName(self,"","","(*.s2p)", "", options)
        if root:
            self.root_line = Root(root, 'line')
            self.ui.lineEdit_line.setText(self.root_line.file_name)
            obj = self.create_objects(self.root_line.root)
            self.matrix_line = []
            for o in obj:
                self.matrix_line.append([str(o.frequency), str(o.s11.real), str(o.s11.imag),
                                        str(o.s21.real), str(o.s21.imag), str(o.s12.real),
                                        str(o.s12.imag), str(o.s22.real), str(o.s22.imag)])
            self.update_combo_box()

    def get_root_open(self):
        options = QtWidgets.QFileDialog.Options()
        root, f = QtWidgets.QFileDialog.getOpenFileName(self,"","","(*.s2p)", "", options)
        if root:
            self.root_open = Root(root, 'open')
            self.ui.lineEdit_open.setText(self.root_open.file_name)
            obj = self.create_objects(self.root_open.root)
            self.matrix_open = []
            for o in obj:
                self.matrix_open.append([str(o.frequency), str(o.s11.real), str(o.s11.imag),
                                        str(o.s21.real), str(o.s21.imag), str(o.s12.real),
                                        str(o.s12.imag), str(o.s22.real), str(o.s22.imag)])
            self.update_combo_box()

    def get_data(self, dut_path, thru_path, line_path, open_path, correct_path):
        dut_path = dut_path
        thru_path = thru_path
        line_path = line_path
        open_path = open_path
        correct_path = correct_path

        dut_list = self.create_objects(dut_path)
        thru_list = self.create_objects(thru_path)
        line_list = self.create_objects(line_path)
        open_list = self.create_objects(open_path)

        # Creating text file
        file = open(correct_path, "w")
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        file.write("! Created on " + dt_string + "\n")
        file.write("! CINVESTAV" + "\n\n")

        file.write("! S-Parameter data\n")
        file.write("! freq S11 S21 S12 S22\n")
        file.write("# Hz S RI R 50\n")
        self.matrix_correct_dut = []
        for i in range(len(dut_list)):
            frequency, s11, s21, s12, s22 = self.get_correct_dut(dut_list[i], thru_list[i], line_list[i], open_list[i])
            self.matrix_correct_dut.append([frequency, str(s11.real), str(s11.imag), str(s21.real), str(s21.imag), str(s12.real), str(s12.imag), str(s22.real), str(s22.imag)])
            file.write(str(frequency) + " " + "{:.15f}".format(s11.real) + " " + "{:.15f}".format(s11.imag) + " "
                       + "{:.15f}".format(s21.real) + " " + "{:.15f}".format(s21.imag) + " "
                       + "{:.15f}".format(s12.real) + " " + "{:.15f}".format(s12.imag) + " "
                       + "{:.15f}".format(s22.real) + " " + "{:.15f}".format(s22.imag) + "\n")
        file.close()
        # for i in self.data_to_show:
        #     print(i)
        self.model = TableModel(self.matrix_correct_dut)
        self.ui.tableView_temp.setModel(self.model)


    def clean_lines(self, lines):
        valid_list = []
        for line in lines:
            # Start with !
            r = re.match("^[!\n\#]", line)
            if not r:
                valid_list.append(line.rstrip("\n"))
        return valid_list

    def create_objects(self,path):
        file = open(path, 'r')
        lines = file.readlines()
        file.close()
        lines = self.clean_lines(lines)
        list_obj = []
        for line in lines:
            line = line.split()
            obj = Reading(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8])
            list_obj.append(obj)
        return list_obj

    def get_b_ac(self, thru, line):
        # T2 * inv(T1)
        new_t_mat = line.t_mat * thru.t_mat_inv
        # Getting b (a = t21, b = t22-t11, c = -t12)
        a = new_t_mat[1][0]
        b = (new_t_mat[1][1]) - (new_t_mat[0][0])
        c = -(new_t_mat[0][1])
        # x = (-b + sqre(b**2-4*ac))/2
        sqre = cmath.sqrt((b * b) - (4 * a * c))
        x1 = (-b + sqre) / (2 * a)
        x2 = (-b - sqre) / (2 * a)
        if abs(x1) < abs(x2):
            b = x1
            ac = x2
        else:
            b = x2
            ac = x1
        return b, ac

    def get_aest(self, b, w1, ca):
        # Gamma = 1
        aest = (b - w1) / ((w1 * ca) - 1)
        return aest

    def get_correct_dut(self, dut, thru, line, open):
        b, ac = self.get_b_ac(thru, line)
        # with t1 - g = t22, f = t21/g, e = t12/g, d = t11/g
        g = thru.t22
        f = thru.t21 / g
        e = thru.t12 / g
        d = thru.t11 / g
        w1 = open.s11
        w2 = open.s22
        ca = 1 / ac
        beta_alfa = (e - b) / (d - (b * f))
        fi = ((ac * f) - d) / (ac - e)
        # Getting a
        aest = self.get_aest(b, w1, ca)
        term_1 = (d - (b * f)) * (b - w1) * (1 + (beta_alfa * w2))
        term_2 = (1 - (ca * e)) * (fi + w2) * ((ca * w1) - 1)
        a_temp = cmath.sqrt(term_1 / term_2)
        a1 = +a_temp
        a2 = -a_temp
        dif_a1 = aest - a1
        dif_a2 = aest - a2
        if abs(dif_a1) < abs(dif_a2):
            a = a1
        else:
            a = a2
        # Getting c
        c = a / ac
        # Getting alfa
        alfa = ((d - (b * f)) / (1 - (ca * e))) / a
        # Getting beta
        beta = beta_alfa * alfa
        # Getting r22Ro22
        r22ro22 = (g * (ac - e)) / (ac - b)


        # Getting S11
        term_1 = r22ro22 * (a - (b * c)) * (alfa - (beta * fi)) * (
                    (alfa * dut.t12) - (beta * dut.t11) + (b * beta * dut.t21) - (b * alfa * dut.t22))
        term_2 = (c * beta * dut.t11) - (c * alfa * dut.t12) - (a * beta * dut.t21) + (a * alfa * dut.t22)
        s11 = term_1 / term_2
        # Getting S22
        term_1 = r22ro22 * (a - (b * c)) * (alfa - beta * fi) * (
                    (c * fi * dut.s12) - (c * dut.t11) + (a * (dut.t21 - (fi * dut.t22))))
        term_2 = (c * beta * dut.t11) - (c * alfa * dut.t12) - (a * beta * dut.t21) + (a * alfa * dut.t22)
        s22 = -term_1 / term_2
        # Getting S21
        term_1 = r22ro22 * (a - (b * c)) * (alfa - (beta * fi))
        term_2 = (c * beta * dut.t11) - (c * alfa * dut.t12) - (a * beta * dut.t21) + (a * alfa * dut.t22)
        s21 = term_1 / term_2
        # Getting S12
        sub_term_1 = r22ro22 * (a - (b * c)) * (alfa - (beta * fi)) * (
                    dut.t11 - (fi * dut.t12) - (b * dut.t21) + (b * fi * dut.t22))
        sub_term_2 = (c * beta * dut.t11) - (c * alfa * dut.t12) - (a * beta * dut.t21) + (a * alfa * dut.t22)
        term_1 = (sub_term_1 / sub_term_2) + (s11 * s22)
        term_2 = s21
        s12 = term_1 / term_2

        return dut.frequency, s11, s21, s12, s22


