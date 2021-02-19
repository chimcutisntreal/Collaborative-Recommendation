# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1191, 711)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1251, 671))
        self.frame.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frame.setAcceptDrops(False)
        self.frame.setStyleSheet("background-color: rgb(163, 163, 163);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.btTabImportData = QtWidgets.QPushButton(self.frame)
        self.btTabImportData.setGeometry(QtCore.QRect(0, 0, 200, 31))
        self.btTabImportData.setMouseTracking(False)
        self.btTabImportData.setObjectName("btTabImportData")

        self.btTabNhomNguoiCongTac = QtWidgets.QPushButton(self.frame)
        self.btTabNhomNguoiCongTac.setGeometry(QtCore.QRect(201, 0, 200, 31))
        self.btTabNhomNguoiCongTac.setMouseTracking(False)
        self.btTabNhomNguoiCongTac.setObjectName("btTabNhomNguoiCongTac")

        self.btTabNhomNguoiCongTacNew = QtWidgets.QPushButton(self.frame)
        self.btTabNhomNguoiCongTacNew.setGeometry(QtCore.QRect(402, 0, 200, 31))
        self.btTabNhomNguoiCongTacNew.setMouseTracking(False)
        self.btTabNhomNguoiCongTacNew.setObjectName("btTabNhomNguoiCongTacNew")

        self.btNguoiCongTac = QtWidgets.QPushButton(self.frame)
        self.btNguoiCongTac.setGeometry(QtCore.QRect(603, 0, 200, 31))
        self.btNguoiCongTac.setObjectName("btNguoiCongTac")

        self.btTabDanhSachBaiBao = QtWidgets.QPushButton(self.frame)
        self.btTabDanhSachBaiBao.setGeometry(QtCore.QRect(804, 0, 200, 31))
        self.btTabDanhSachBaiBao.setObjectName("btTabDanhSachBaiBao")

        self.btTabThemTacGia = QtWidgets.QPushButton(self.frame)
        self.btTabThemTacGia.setGeometry(QtCore.QRect(1005, 0, 200, 31))
        self.btTabThemTacGia.setObjectName("btTabThemTacGia")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 30, 1241, 641))
        self.stackedWidget.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.stackedWidget.setObjectName("stackedWidget")

        #Tab 0
        self.pImportData = QtWidgets.QWidget()
        self.pImportData.setEnabled(True)
        self.pImportData.setToolTip("")
        self.pImportData.setAccessibleDescription("")
        self.pImportData.setAutoFillBackground(False)
        self.pImportData.setObjectName("pImportData")

        self.widget = QtWidgets.QWidget(self.pImportData)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1301, 641))
        self.widget.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget.setObjectName("widget")

        self.lblPath = QtWidgets.QLineEdit(self.widget)
        self.lblPath.setGeometry(QtCore.QRect(30, 40, 630, 40))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lblPath.setFont(font)
        self.lblPath.setMouseTracking(False)
        self.lblPath.setText("")
        self.lblPath.setReadOnly(True)
        self.lblPath.setObjectName("lblPath")

        self.btChoose = QtWidgets.QPushButton(self.widget)
        self.btChoose.setGeometry(QtCore.QRect(30, 90, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btChoose.setFont(font)
        self.btChoose.setObjectName("btChoose")

        self.btLoad = QtWidgets.QPushButton(self.widget)
        self.btLoad.setGeometry(QtCore.QRect(360, 90, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btLoad.setFont(font)
        self.btLoad.setObjectName("btLoad")

        self.lbLoad = QtWidgets.QLabel(self.widget)
        self.lbLoad.setGeometry(QtCore.QRect(720, 50, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbLoad.setFont(font)
        self.lbLoad.setAutoFillBackground(False)
        self.lbLoad.setText("")
        self.lbLoad.setObjectName("lbLoad")

        self.lblUploaded = QtWidgets.QLabel(self.widget)
        self.lblUploaded.setGeometry(QtCore.QRect(30, 180, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lblUploaded.setFont(font)
        self.lblUploaded.setObjectName("lblUploaded")

        self.lstUploaded = QtWidgets.QListWidget(self.widget)
        self.lstUploaded.setGeometry(QtCore.QRect(30, 240, 630, 180))
        self.lstUploaded.setStyleSheet("background-color: rgb(210,210,210);")
        self.lstUploaded.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lstUploaded.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstUploaded.setViewMode(QtWidgets.QListView.ListMode)
        self.lstUploaded.setObjectName("lstUploaded")
        self.stackedWidget.addWidget(self.pImportData)

        #Tab 1
        self.pNhomCongTacTuongTuNhat = QtWidgets.QWidget()
        self.pNhomCongTacTuongTuNhat.setEnabled(True)
        self.pNhomCongTacTuongTuNhat.setToolTip("")
        self.pNhomCongTacTuongTuNhat.setAccessibleDescription("")
        self.pNhomCongTacTuongTuNhat.setAutoFillBackground(False)
        self.pNhomCongTacTuongTuNhat.setObjectName("pNhomCongTacTuongTuNhat")
        
        self.widget_1 = QtWidgets.QWidget(self.pNhomCongTacTuongTuNhat)
        self.widget_1.setEnabled(True)
        self.widget_1.setGeometry(QtCore.QRect(0, 0, 1301, 641))
        self.widget_1.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget_1.setObjectName("widget_1")

        self.cbChooseTarget_1 = QtWidgets.QComboBox(self.widget_1)
        self.cbChooseTarget_1.setGeometry(QtCore.QRect(140, 27, 221, 21))
        self.cbChooseTarget_1.setObjectName("cbChooseTarget_1")
        self.lblChooseTarget_1 = QtWidgets.QLabel(self.widget_1)
        self.lblChooseTarget_1.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.lblChooseTarget_1.setObjectName("lblChooseTarget_1")

        self.lTacGiaP1 = QtWidgets.QLineEdit(self.widget_1)
        self.lTacGiaP1.setGeometry(QtCore.QRect(690, 30, 221, 21))
        self.lTacGiaP1.setObjectName("lTacGiaP1")

        self.btSearchP1 = QtWidgets.QPushButton(self.widget_1)
        self.btSearchP1.setGeometry(QtCore.QRect(930, 28, 75, 23))
        self.btSearchP1.setObjectName("btSearchP1")

        self.tblP1 = QtWidgets.QTableWidget(self.widget_1)
        self.tblP1.setEnabled(True)
        self.tblP1.setGeometry(QtCore.QRect(20, 180, 1131, 401))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblP1.sizePolicy().hasHeightForWidth())
        self.tblP1.setSizePolicy(sizePolicy)
        self.tblP1.setMaximumSize(QtCore.QSize(1131, 401))
        font = QtGui.QFont()
        font.setKerning(True)
        self.tblP1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblP1.setFont(font)
        self.tblP1.setMouseTracking(True)
        self.tblP1.setStyleSheet("selection-background-color: rgb(119, 162, 255);")
        self.tblP1.setAutoScrollMargin(16)
        self.tblP1.setDragEnabled(False)
        self.tblP1.setDragDropOverwriteMode(True)
        self.tblP1.setTextElideMode(QtCore.Qt.ElideRight)
        self.tblP1.setShowGrid(True)
        self.tblP1.setGridStyle(QtCore.Qt.SolidLine)
        self.tblP1.setWordWrap(True)
        self.tblP1.setCornerButtonEnabled(True)
        self.tblP1.setObjectName("tblP1")
        self.tblP1.setColumnCount(3)
        self.tblP1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblP1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP1.setHorizontalHeaderItem(2, item)
        self.tblP1.horizontalHeader().setVisible(True)
        self.tblP1.horizontalHeader().setCascadingSectionResizes(True)
        self.tblP1.horizontalHeader().setHighlightSections(True)
        self.tblP1.horizontalHeader().setMinimumSectionSize(90)
        self.tblP1.horizontalHeader().setSortIndicatorShown(False)
        self.tblP1.horizontalHeader().setStretchLastSection(True)
        self.tblP1.verticalHeader().setVisible(False)
        self.tblP1.verticalHeader().setCascadingSectionResizes(False)
        self.tblP1.verticalHeader().setHighlightSections(False)
        self.tblP1.verticalHeader().setMinimumSectionSize(23)
        self.tblP1.verticalHeader().setSortIndicatorShown(False)
        self.tblP1.verticalHeader().setStretchLastSection(False)
        self.tblP1.setColumnWidth(0, 101)
        self.tblP1.setColumnWidth(1, 515)
        self.tblP1.setColumnWidth(2, 515)
        self.tblP1.setColumnWidth(3, 101)
        self.label_14 = QtWidgets.QLabel(self.widget_1)
        self.label_14.setGeometry(QtCore.QRect(20, 110, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lbSearchP1 = QtWidgets.QLabel(self.widget_1)
        self.lbSearchP1.setGeometry(QtCore.QRect(1030, 30, 141, 16))
        self.lbSearchP1.setObjectName("lbSearchP1")
        self.stackedWidget.addWidget(self.pNhomCongTacTuongTuNhat)

        # Tab 1 New
        self.pNhomCongTacTuongTuNhatNew = QtWidgets.QWidget()
        self.pNhomCongTacTuongTuNhatNew.setEnabled(True)
        self.pNhomCongTacTuongTuNhatNew.setToolTip("")
        self.pNhomCongTacTuongTuNhatNew.setAccessibleDescription("")
        self.pNhomCongTacTuongTuNhatNew.setAutoFillBackground(False)
        self.pNhomCongTacTuongTuNhatNew.setObjectName("pNhomCongTacTuongTuNhatNew")

        self.widget_1_new = QtWidgets.QWidget(self.pNhomCongTacTuongTuNhatNew)
        self.widget_1_new.setEnabled(True)
        self.widget_1_new.setGeometry(QtCore.QRect(0, 0, 1301, 641))
        self.widget_1_new.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget_1_new.setObjectName("widget_1_new")

        self.cbChooseSource_1_new = QtWidgets.QComboBox(self.widget_1_new)
        self.cbChooseSource_1_new.setGeometry(QtCore.QRect(140, 27, 221, 21))
        self.cbChooseSource_1_new.setObjectName("cbChooseSource_1_new")
        self.lblChooseSource_1_new = QtWidgets.QLabel(self.widget_1_new)
        self.lblChooseSource_1_new.setGeometry(QtCore.QRect(20, 30, 120, 16))
        self.lblChooseSource_1_new.setObjectName("lblChooseSource_1_new")

        self.cbChooseTarget_1_new = QtWidgets.QComboBox(self.widget_1_new)
        self.cbChooseTarget_1_new.setGeometry(QtCore.QRect(140, 57, 221, 21))
        self.cbChooseTarget_1_new.setObjectName("cbChooseTarget_1_new")
        self.lblChooseTarget_1_new = QtWidgets.QLabel(self.widget_1_new)
        self.lblChooseTarget_1_new.setGeometry(QtCore.QRect(20, 60, 120, 16))
        self.lblChooseTarget_1_new.setObjectName("lblChooseTarget_1_new")

        self.lTacGiaP1New = QtWidgets.QLineEdit(self.widget_1_new)
        self.lTacGiaP1New.setGeometry(QtCore.QRect(690, 30, 221, 21))
        self.lTacGiaP1New.setObjectName("lTacGiaP1New")

        self.btSearchP1New = QtWidgets.QPushButton(self.widget_1_new)
        self.btSearchP1New.setGeometry(QtCore.QRect(930, 28, 75, 23))
        self.btSearchP1New.setObjectName("btSearchP1New")

        self.tblP1New = QtWidgets.QTableWidget(self.widget_1_new)
        self.tblP1New.setEnabled(True)
        self.tblP1New.setGeometry(QtCore.QRect(20, 180, 1131, 401))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblP1New.sizePolicy().hasHeightForWidth())
        self.tblP1New.setSizePolicy(sizePolicy)
        self.tblP1New.setMaximumSize(QtCore.QSize(1131, 401))
        font = QtGui.QFont()
        font.setKerning(True)
        self.tblP1New.setFont(font)
        self.tblP1New.setMouseTracking(True)
        self.tblP1New.setStyleSheet("selection-background-color: rgb(119, 162, 255);")
        self.tblP1New.setAutoScrollMargin(16)
        self.tblP1New.setDragEnabled(False)
        self.tblP1New.setDragDropOverwriteMode(True)
        self.tblP1New.setTextElideMode(QtCore.Qt.ElideRight)
        self.tblP1New.setShowGrid(True)
        self.tblP1New.setGridStyle(QtCore.Qt.SolidLine)
        self.tblP1New.setWordWrap(True)
        self.tblP1New.setCornerButtonEnabled(True)
        self.tblP1New.setObjectName("tblP1")
        self.tblP1New.setColumnCount(3)
        self.tblP1New.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblP1New.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP1New.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP1New.setHorizontalHeaderItem(2, item)
        self.tblP1New.horizontalHeader().setVisible(True)
        self.tblP1New.horizontalHeader().setCascadingSectionResizes(True)
        self.tblP1New.horizontalHeader().setHighlightSections(True)
        self.tblP1New.horizontalHeader().setMinimumSectionSize(90)
        self.tblP1New.horizontalHeader().setSortIndicatorShown(False)
        self.tblP1New.horizontalHeader().setStretchLastSection(True)
        self.tblP1New.verticalHeader().setVisible(False)
        self.tblP1New.verticalHeader().setCascadingSectionResizes(False)
        self.tblP1New.verticalHeader().setHighlightSections(False)
        self.tblP1New.verticalHeader().setMinimumSectionSize(23)
        self.tblP1New.verticalHeader().setSortIndicatorShown(False)
        self.tblP1New.verticalHeader().setStretchLastSection(False)
        self.tblP1New.setColumnWidth(0, 101)
        self.tblP1New.setColumnWidth(1, 515)
        self.tblP1New.setColumnWidth(2, 515)
        self.tblP1New.setColumnWidth(3, 101)
        self.label_14_new = QtWidgets.QLabel(self.widget_1_new)
        self.label_14_new.setGeometry(QtCore.QRect(20, 110, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_14_new.setFont(font)
        self.label_14_new.setObjectName("label_14")
        self.lbSearchP1New = QtWidgets.QLabel(self.widget_1_new)
        self.lbSearchP1New.setGeometry(QtCore.QRect(1030, 30, 141, 16))
        self.lbSearchP1New.setObjectName("lbSearchP1")
        self.stackedWidget.addWidget(self.pNhomCongTacTuongTuNhatNew)

        #Tab 2
        self.pCongTacTuongTuNhat = QtWidgets.QWidget()
        self.pCongTacTuongTuNhat.setObjectName("pCongTacTuongTuNhat")
        self.widget_2 = QtWidgets.QWidget(self.pCongTacTuongTuNhat)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1271, 641))
        self.widget_2.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget_2.setObjectName("widget_2")

        self.cbChooseTarget_2 = QtWidgets.QComboBox(self.widget_2)
        self.cbChooseTarget_2.setGeometry(QtCore.QRect(170, 32, 221, 21))
        self.cbChooseTarget_2.setObjectName("cbChooseTarget_2")
        self.lblChooseTarget_2 = QtWidgets.QLabel(self.widget_2)
        self.lblChooseTarget_2.setGeometry(QtCore.QRect(40, 35, 111, 16))
        self.lblChooseTarget_2.setObjectName("lblChooseTarget_2")

        self.lTacGia1 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia1.setGeometry(QtCore.QRect(120, 120, 235, 20))
        self.lTacGia1.setText("")
        self.lTacGia1.setObjectName("lTacGia1")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(40, 120, 60, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lTacGia2 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia2.setGeometry(QtCore.QRect(120, 160, 235, 20))
        self.lTacGia2.setText("")
        self.lTacGia2.setObjectName("lTacGia2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 47, 21))
        self.label_3.setObjectName("label_3")
        self.lTacGia3 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia3.setGeometry(QtCore.QRect(120, 200, 235, 20))
        self.lTacGia3.setText("")
        self.lTacGia3.setObjectName("lTacGia3")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 47, 21))
        self.label_4.setObjectName("label_4")
        self.lTacGia4 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia4.setGeometry(QtCore.QRect(120, 240, 235, 20))
        self.lTacGia4.setText("")
        self.lTacGia4.setObjectName("lTacGia4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(40, 240, 47, 21))
        self.label_5.setObjectName("label_5")
        self.lTacGia5 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia5.setGeometry(QtCore.QRect(120, 280, 235, 20))
        self.lTacGia5.setText("")
        self.lTacGia5.setObjectName("lTacGia5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 47, 21))
        self.label_6.setObjectName("label_6")
        self.lTacGia6 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia6.setGeometry(QtCore.QRect(120, 320, 235, 20))
        self.lTacGia6.setText("")
        self.lTacGia6.setObjectName("lTacGia6")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(40, 320, 47, 21))
        self.label_7.setObjectName("label_7")
        self.lTacGia7 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia7.setGeometry(QtCore.QRect(120, 360, 235, 20))
        self.lTacGia7.setText("")
        self.lTacGia7.setObjectName("lTacGia7")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(40, 360, 47, 21))
        self.label_8.setObjectName("label_8")
        self.lTacGia8 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia8.setGeometry(QtCore.QRect(120, 400, 235, 20))
        self.lTacGia8.setText("")
        self.lTacGia8.setObjectName("lTacGia8")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(40, 400, 47, 21))
        self.label_9.setObjectName("label_9")
        self.lTacGia9 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia9.setGeometry(QtCore.QRect(120, 440, 235, 20))
        self.lTacGia9.setText("")
        self.lTacGia9.setObjectName("lTacGia9")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(40, 440, 47, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(40, 480, 51, 21))
        self.label_11.setObjectName("label_11")
        self.lTacGia10 = QtWidgets.QLineEdit(self.widget_2)
        self.lTacGia10.setGeometry(QtCore.QRect(120, 480, 235, 20))
        self.lTacGia10.setText("")
        self.lTacGia10.setObjectName("lTacGia10")
        self.btSearchP2 = QtWidgets.QPushButton(self.widget_2)
        self.btSearchP2.setGeometry(QtCore.QRect(250, 530, 101, 21))
        self.btSearchP2.setObjectName("btSearchP2")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(590, 40, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.tblP2 = QtWidgets.QTableWidget(self.widget_2)
        self.tblP2.setEnabled(True)
        self.tblP2.setGeometry(QtCore.QRect(590, 120, 571, 381))
        self.tblP2.setMaximumSize(QtCore.QSize(571, 381))
        font = QtGui.QFont()
        font.setKerning(True)
        self.tblP2.setFont(font)
        self.tblP2.setMouseTracking(True)
        self.tblP2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tblP2.setAutoFillBackground(False)
        self.tblP2.setStyleSheet("selection-background-color: rgb(119, 162, 255);")
        self.tblP2.setAutoScrollMargin(16)
        self.tblP2.setDragEnabled(False)
        self.tblP2.setDragDropOverwriteMode(True)
        self.tblP2.setShowGrid(True)
        self.tblP2.setGridStyle(QtCore.Qt.SolidLine)
        self.tblP2.setObjectName("tblP2")
        self.tblP2.setColumnCount(3)
        self.tblP2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblP2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP2.setHorizontalHeaderItem(2, item)
        self.tblP2.horizontalHeader().setVisible(True)
        self.tblP2.horizontalHeader().setCascadingSectionResizes(True)
        self.tblP2.horizontalHeader().setHighlightSections(True)
        self.tblP2.horizontalHeader().setMinimumSectionSize(90)
        self.tblP2.horizontalHeader().setSortIndicatorShown(True)
        self.tblP2.horizontalHeader().setStretchLastSection(True)
        self.tblP2.verticalHeader().setVisible(False)
        self.tblP2.verticalHeader().setCascadingSectionResizes(False)
        self.tblP2.verticalHeader().setHighlightSections(False)
        self.tblP2.verticalHeader().setSortIndicatorShown(False)
        self.tblP2.verticalHeader().setStretchLastSection(False)
        self.tblP2.setColumnWidth(0, 50)
        self.tblP2.setColumnWidth(1, 270)
        self.tblP2.setColumnWidth(2, 270)
        self.lbSearchP2 = QtWidgets.QLabel(self.widget_2)
        self.lbSearchP2.setGeometry(QtCore.QRect(250, 570, 141, 16))
        self.lbSearchP2.setObjectName("lbSearchP2")
        self.stackedWidget.addWidget(self.pCongTacTuongTuNhat)

        # Tab 3
        self.pDnhachBaiBao = QtWidgets.QWidget()
        self.pDnhachBaiBao.setObjectName("pDnhachBaiBao")
        self.widget_3 = QtWidgets.QWidget(self.pDnhachBaiBao)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 1251, 641))
        self.widget_3.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget_3.setObjectName("widget_3")

        self.cbChooseTarget_3 = QtWidgets.QComboBox(self.widget_3)
        self.cbChooseTarget_3.setGeometry(QtCore.QRect(770, 27, 221, 21))
        self.cbChooseTarget_3.setObjectName("cbChooseTarget_3")
        self.lblChooseTarget_3 = QtWidgets.QLabel(self.widget_3)
        self.lblChooseTarget_3.setGeometry(QtCore.QRect(650, 30, 111, 16))
        self.lblChooseTarget_3.setObjectName("lblChooseTarget_3")

        self.tblP3 = QtWidgets.QTableWidget(self.widget_3)
        self.tblP3.setGeometry(QtCore.QRect(20, 130, 1121, 421))
        self.tblP3.setObjectName("tblP3")
        self.tblP3.setColumnCount(3)
        self.tblP3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblP3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP3.setHorizontalHeaderItem(2, item)
        self.tblP3.horizontalHeader().setCascadingSectionResizes(True)
        self.tblP3.horizontalHeader().setSortIndicatorShown(False)
        self.tblP3.horizontalHeader().setStretchLastSection(True)
        self.tblP3.setColumnWidth(0, 121)
        self.tblP3.setColumnWidth(1, 500)
        self.tblP3.setColumnWidth(2, 500)

        self.label_15 = QtWidgets.QLabel(self.widget_3)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.btShowP3 = QtWidgets.QPushButton(self.widget_3)
        self.btShowP3.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.btShowP3.setObjectName("btShowP3")
        self.btRevertP3 = QtWidgets.QPushButton(self.widget_3)
        self.btRevertP3.setGeometry(QtCore.QRect(940, 570, 81, 23))
        self.btRevertP3.setObjectName("btRevertP3")
        self.btNextP3 = QtWidgets.QPushButton(self.widget_3)
        self.btNextP3.setGeometry(QtCore.QRect(1060, 570, 81, 23))
        self.btNextP3.setObjectName("btNextP3")
        self.stackedWidget.addWidget(self.pDnhachBaiBao)

        #Tab 4
        self.pThemTacGia = QtWidgets.QWidget()
        self.pThemTacGia.setObjectName("pThemTacGia")
        self.widget_4 = QtWidgets.QWidget(self.pThemTacGia)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 1231, 641))
        self.widget_4.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget_4.setObjectName("widget_4")
        self.lNameAuthorP4 = QtWidgets.QLineEdit(self.widget_4)
        self.lNameAuthorP4.setGeometry(QtCore.QRect(430, 90, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lNameAuthorP4.setFont(font)
        self.lNameAuthorP4.setObjectName("lNameAuthorP4")

        self.btAddP4 = QtWidgets.QPushButton(self.widget_4)
        self.btAddP4.setGeometry(QtCore.QRect(690, 88, 131, 23))
        self.btAddP4.setObjectName("btAddP4")

        self.tblP4 = QtWidgets.QTableWidget(self.widget_4)
        self.tblP4.setGeometry(QtCore.QRect(20, 190, 1121, 351))
        self.tblP4.setObjectName("tblP4")
        self.tblP4.setColumnCount(3)
        self.tblP4.setRowCount(0)
        self.tblP4.setColumnWidth(0, 121)
        self.tblP4.setColumnWidth(1, 500)
        self.tblP4.setColumnWidth(2, 500)
        item = QtWidgets.QTableWidgetItem()
        self.tblP4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblP4.setHorizontalHeaderItem(2, item)
        self.tblP4.horizontalHeader().setCascadingSectionResizes(True)
        self.tblP4.horizontalHeader().setSortIndicatorShown(False)
        self.tblP4.horizontalHeader().setStretchLastSection(True)

        self.btShowP4 = QtWidgets.QPushButton(self.widget_4)
        self.btShowP4.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.btShowP4.setObjectName("btShowP4")
        self.btNextP4 = QtWidgets.QPushButton(self.widget_4)
        self.btNextP4.setGeometry(QtCore.QRect(1060, 570, 81, 23))
        self.btNextP4.setObjectName("btNextP4")
        self.btRevertP4 = QtWidgets.QPushButton(self.widget_4)
        self.btRevertP4.setGeometry(QtCore.QRect(940, 570, 81, 23))
        self.btRevertP4.setObjectName("btRevertP4")
        self.lbAddP4 = QtWidgets.QLabel(self.widget_4)
        self.lbAddP4.setEnabled(True)
        self.lbAddP4.setGeometry(QtCore.QRect(860, 90, 211, 16))
        self.lbAddP4.setObjectName("lbAddP4")
        self.lPathP4 = QtWidgets.QLineEdit(self.widget_4)
        self.lPathP4.setGeometry(QtCore.QRect(20, 32, 211, 20))
        self.lPathP4.setObjectName("lPathP4")
        self.btChooseDBP4 = QtWidgets.QPushButton(self.widget_4)
        self.btChooseDBP4.setGeometry(QtCore.QRect(250, 30, 131, 23))
        self.btChooseDBP4.setObjectName("btChooseDBP4")
        self.btLoadDBP4 = QtWidgets.QPushButton(self.widget_4)
        self.btLoadDBP4.setGeometry(QtCore.QRect(430, 30, 75, 23))
        self.btLoadDBP4.setObjectName("btLoadDBP4")
        self.lbLoadDataP4 = QtWidgets.QLabel(self.widget_4)
        self.lbLoadDataP4.setEnabled(True)
        self.lbLoadDataP4.setGeometry(QtCore.QRect(530, 32, 211, 16))
        self.lbLoadDataP4.setObjectName("lbLoadDataP4")
        self.lNewDBP4 = QtWidgets.QLineEdit(self.widget_4)
        self.lNewDBP4.setGeometry(QtCore.QRect(20, 90, 211, 20))
        self.lNewDBP4.setObjectName("lNewDBP4")
        self.btChoosePathNewDBP4 = QtWidgets.QPushButton(self.widget_4)
        self.btChoosePathNewDBP4.setGeometry(QtCore.QRect(250, 88, 131, 23))
        self.btChoosePathNewDBP4.setObjectName("btChoosePathNewDBP4")
        self.stackedWidget.addWidget(self.pThemTacGia)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ỨNG DỤNG KHUYẾN NGHỊ CỘNG TÁC"))
        self.btTabImportData.setText(_translate("MainWindow", "Import Data"))
        self.lblPath.setPlaceholderText(_translate("MainWindow", "Đường dẫn"))
        self.btChoose.setText(_translate("MainWindow", "Chọn đường dẫn"))
        self.btLoad.setText(_translate("MainWindow", "Nạp dữ liệu"))
        self.lblUploaded.setText(_translate("MainWindow", "Các file tải lên"))
        self.btTabNhomNguoiCongTac.setText(_translate("MainWindow", "Reccoment from author"))
        self.btTabThemTacGia.setText(_translate("MainWindow", "Thêm tác giả thủ công"))
        self.btNguoiCongTac.setText(_translate("MainWindow", "Reccomment from group"))
        self.btTabDanhSachBaiBao.setText(_translate("MainWindow", "Hiển thị danh sách bài báo"))
        self.lTacGiaP1.setPlaceholderText(_translate("MainWindow", "Nhập Thông tin tác giả"))
        self.btSearchP1.setText(_translate("MainWindow", "Tìm Kiếm"))
        self.tblP1.setSortingEnabled(False)
        item = self.tblP1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STT"))
        item = self.tblP1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên tác giả"))
        item = self.tblP1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Độ tương tự"))
        self.lblChooseTarget_1.setText(_translate("MainWindow", "Chọn dữ liệu đích"))
        self.label_14.setText(_translate("MainWindow", "Thông tin tác giả tác tương tự nhất:"))
        self.lbSearchP1.setText(_translate("MainWindow", "Đang tìm kiếm ..."))
        self.lbSearchP1.setVisible(False)

        self.btTabNhomNguoiCongTacNew.setText(_translate("MainWindow", "Reccoment from author new"))
        self.lTacGiaP1New.setPlaceholderText(_translate("MainWindow", "Nhập Thông tin tác giả"))
        self.btSearchP1New.setText(_translate("MainWindow", "Tìm Kiếm"))
        self.tblP1New.setSortingEnabled(False)
        item = self.tblP1New.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STT"))
        item = self.tblP1New.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên tác giả"))
        item = self.tblP1New.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Độ tương tự"))
        self.lblChooseSource_1_new.setText(_translate("MainWindow", "Chọn dữ liệu nguồn"))
        self.lblChooseTarget_1_new.setText(_translate("MainWindow", "Chọn dữ liệu đích"))
        self.label_14_new.setText(_translate("MainWindow", "Thông tin tác giả tác tương tự nhất:"))
        self.lbSearchP1New.setText(_translate("MainWindow", "Đang tìm kiếm ..."))
        self.lbSearchP1New.setVisible(False)

        self.lblChooseTarget_2.setText(_translate("MainWindow", "Chọn dữ liệu đích"))
        self.lTacGia1.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 1"))
        self.label.setText(_translate("MainWindow", "Tác giả 1"))
        self.label_2.setText(_translate("MainWindow", "Nhập thông tin nhóm cộng tác:"))
        self.lTacGia2.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 2"))
        self.label_3.setText(_translate("MainWindow", "Tác giả 2"))
        self.lTacGia3.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 3"))
        self.label_4.setText(_translate("MainWindow", "Tác giả 3"))
        self.lTacGia4.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 4"))
        self.label_5.setText(_translate("MainWindow", "Tác giả 4"))
        self.lTacGia5.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 5"))
        self.label_6.setText(_translate("MainWindow", "Tác giả 5"))
        self.lTacGia6.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 6"))
        self.label_7.setText(_translate("MainWindow", "Tác giả 6"))
        self.lTacGia7.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 7"))
        self.label_8.setText(_translate("MainWindow", "Tác giả 7"))
        self.lTacGia8.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 8"))
        self.label_9.setText(_translate("MainWindow", "Tác giả 8"))
        self.lTacGia9.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 9"))
        self.label_10.setText(_translate("MainWindow", "Tác giả 9"))
        self.label_11.setText(_translate("MainWindow", "Tác giả 10"))
        self.lTacGia10.setPlaceholderText(_translate("MainWindow", "Thông tin tác giả 10"))
        self.btSearchP2.setText(_translate("MainWindow", "Tìm kiếm"))
        self.label_13.setText(_translate("MainWindow", "Thông tin tác giả tác tương tự nhất:"))
        self.tblP2.setSortingEnabled(False)
        item = self.tblP2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STT"))
        item = self.tblP2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên tác giả"))
        item = self.tblP2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Độ tương tự"))
        self.lbSearchP2.setText(_translate("MainWindow", "Đang tìm kiếm ..."))
        self.lbSearchP2.setVisible(False)
        item = self.tblP3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STT"))
        item = self.tblP3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên bài báo"))
        item = self.tblP3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Các tác giả"))
        self.lblChooseTarget_3.setText(_translate("MainWindow", "Chọn dữ liệu đích"))
        self.label_15.setText(_translate("MainWindow", "Danh sách các bài báo:"))
        self.btShowP3.setText(_translate("MainWindow", "Hiển thị"))
        self.btRevertP3.setText(_translate("MainWindow", "Lùi"))
        self.btNextP3.setText(_translate("MainWindow", "Tiếp"))
        self.lNameAuthorP4.setPlaceholderText(_translate("MainWindow", "Nhập thông tin tác giả"))
        self.btAddP4.setText(_translate("MainWindow", "Thêm vào"))
        item = self.tblP4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STT"))
        item = self.tblP4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên bài báo"))
        item = self.tblP4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Các tác giả"))
        self.btShowP4.setText(_translate("MainWindow", "Hiển thị"))
        self.btNextP4.setText(_translate("MainWindow", "Tiếp"))
        self.btRevertP4.setText(_translate("MainWindow", "Lùi"))
        self.lbAddP4.setText(_translate("MainWindow", "Đang thêm vào cơ sở dữ liệu ..."))
        self.lbAddP4.setVisible(False)
        self.lPathP4.setPlaceholderText(_translate("MainWindow", "Đường dẫn file dữ liệu chính"))
        self.btChooseDBP4.setText(_translate("MainWindow", "Chọn cơ sở dữ liệu"))
        self.btLoadDBP4.setText(_translate("MainWindow", "Nạp dữ liệu"))
        self.lbLoadDataP4.setText(_translate("MainWindow", "Đang tải dữ liệu..."))
        self.lbLoadDataP4.setVisible(False)
        self.lNewDBP4.setPlaceholderText(_translate("MainWindow", "Đường dẫn file dữ liệu mới(nếu đã tồn tại)"))
        self.btChoosePathNewDBP4.setText(_translate("MainWindow", "Chọn đường dẫn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
