import pandas as pd
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from ui import *
from functools import partial
from os import path
from csv import writer
from sklearn.metrics.pairwise import cosine_similarity
import json
import sys

with open('config.json') as json_file:
    config = json.load(json_file)

PATH_MAIN_DATA = config["PATH_MAIN_DATA"]
PATH_CUSTOM_DATA = config["PATH_CUSTOM_DATA"]

df = pd.read_csv(PATH_MAIN_DATA, encoding='latin1')
df_author = df[['author']]

author_list = set()
b = []
for i in df_author['author']:
    s = str(i).split('|')
    for j in s:
        author_list.add(j)

df_author['idpp'] = np.arange(df_author.shape[0])

df_pp = pd.get_dummies(df_author['idpp'], prefix='pp')

author_vt = np.zeros((len(author_list), df_author.shape[0]))
author_vt = pd.DataFrame(author_vt, index=list(author_list))

for i in range(df_author.shape[0]):
    str_author = str(df_author['author'][i]).split('|')
    for auth in str_author:
        author_vt.loc[auth, i] = author_vt.loc[auth, i] + 1

author_vt = author_vt.transpose()


def cosine_similar(author_name, top):
    cosine = {}
    for author in author_vt.columns:
        cosi = cosine_similarity(author_vt[[author_name]].values.reshape(1, -1),
                                 author_vt[[author]].values.reshape(1, -1))
        cosine[author] = cosi[0]

    df_cosine = pd.DataFrame(cosine, index=['cosine_similarity'])
    df_cosine = df_cosine.transpose()
    df_cosine.sort_values(by=['cosine_similarity'], ascending=False, inplace=True)
    df_cosine = df_cosine[:][:top + 1]
    df_cosine.drop([author_name], inplace=True)
    return df_cosine


def group_cosine_similar(group_author_vector, authors_name, top):
    cosine = {}
    for author in author_vt.columns:
        cosi = cosine_similarity(group_author_vector, author_vt[[author]].values.reshape(1, -1))
        cosine[author] = cosi[0]

    df_cosine = pd.DataFrame(cosine, index=['cosine_similarity'])
    df_cosine = df_cosine.transpose()
    df_cosine.sort_values(by=['cosine_similarity'], ascending=False, inplace=True)
    df_cosine.drop(authors_name, inplace=True)
    df_cosine = df_cosine[:][:top]
    return df_cosine


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #4 biến này phục vụ cho việc phân trang
        self.nextP3 = 10
        self.reVertP3 = 0
        self.nextP4 = 10
        self.reVertP4 = 0


        self.df_main = None #biến để lưu bộ dữ liệu đầy đủ (bộ dữ liệu để tìm kiếm trong việc thêm tác giả mới)
        self.all_author_list = set()

        # page1: nhom cong tac tuong tu nhat
        self.ui.btTabNhomNguoiCongTac.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pNhomCongTacTuongTuNhat))
        self.ui.btSearchP1.clicked.connect(self.getAuthorFromAuthor)

        # page2: cong tac tuong tu nhat
        self.ui.btNguoiCongTac.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pCongTacTuongTuNhat))
        self.ui.btSearchP2.clicked.connect(self.getAuthorFromGroupAuthor)

        # page3: danh sach bai bao
        self.ui.btTabDanhSachBaiBao.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pDnhachBaiBao))
        self.ui.btShowP3.clicked.connect(partial(self.getListPaper, flag=0))
        self.ui.btNextP3.clicked.connect(partial(self.getListPaper, flag=1))
        self.ui.btRevertP3.clicked.connect(partial(self.getListPaper, flag=2))

        # page4: them tac gia thu cong
        self.ui.btTabThemTacGia.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pThemTacGia))
        self.ui.btChooseDBP4.clicked.connect(partial(self.browDB))
        self.ui.btLoadDBP4.clicked.connect(partial(self.loadDB))
        self.ui.btAddP4.clicked.connect(partial(self.addAuthor))
        self.ui.btChoosePathNewDBP4.clicked.connect(partial(self.browNewDB))
        self.ui.btShowP4.clicked.connect(partial(self.getListNewPaper, flag=0))
        self.ui.btNextP4.clicked.connect(partial(self.getListNewPaper, flag=1))
        self.ui.btRevertP4.clicked.connect(partial(self.getListNewPaper, flag=2))

        self.show()

    # lấy Danh sách tác giả từ dữ liệu mới
    def getListNewPaper(self, flag):

        path_new_data = self.ui.lNewDBP4.text()
        if path.exists(path_new_data) == False:
            path_new_data = PATH_CUSTOM_DATA
            if path.exists(path_new_data) == False:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Không tồn tại dữ liệu trong :%s" % path_new_data)
                msg.setWindowTitle("Warning")
                msg.exec_()
                return 0
        df_new = pd.read_csv(path_new_data, encoding='latin1')
        if flag == 1:

            if self.nextP4 + 9 < df_new.shape[0]:
                self.reVertP4 = self.reVertP4 + 10
                self.nextP4 = self.nextP4 + 10
            elif self.nextP4 - df_new.shape[0] > -10 and self.reVertP4 + 10 < df_new.shape[0]:
                self.reVertP4 = self.reVertP4 + 10
                self.nextP4 = df_new.shape[0]
        elif flag == 2:
            if self.nextP4 == df_new.shape[0]:
                self.nextP4 = self.nextP4 - (df_new.shape[0] - self.reVertP4)
                self.reVertP4 = self.reVertP4 - 10
            elif self.reVertP4 - 10 >= 0:
                self.reVertP4 = self.reVertP4 - 10
                self.nextP4 = self.nextP4 - 10
        else:
            self.reVertP4 = 0
            self.nextP4 = 10
        self.ui.tblP4.setRowCount(self.nextP4 - self.reVertP4)
        papers = df_new.loc[self.reVertP4:self.nextP4, ("author", "title")].transpose()

        for i, _ in enumerate(papers):
            self.ui.tblP4.setItem(i, 0, QTableWidgetItem(str(i + self.reVertP4)))
            self.ui.tblP4.setItem(i, 1, QTableWidgetItem(str(papers.iloc[1, i])))
            self.ui.tblP4.setItem(i, 2, QTableWidgetItem(str(papers.iloc[0, i])))

    def browDB(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'File (*.csv)')
        self.ui.lPathP4.setText(fname)

    def browNewDB(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'File (*.csv)')
        self.ui.lNewDBP4.setText(fname)

    # Nạp dữ liệu để cho phần thêm tác giả thủ công
    def loadDB(self):
        path_data = self.ui.lPathP4.text()

        if path.exists(path_data):
            self.ui.lbLoadDataP4.setVisible(True)
            self.ui.lbLoadDataP4.repaint()

            if self.df_main is None:
                self.df_main = pd.read_csv(path_data, sep=';')
                self.df_main.dropna(subset=["author"], inplace=True)
                df_author_all = self.df_main[['author']]

                for i in df_author_all['author']:
                    s = str(i).split('|')
                    for j in s:
                        self.all_author_list.add(j)
                self.ui.lbLoadDataP4.setText("Nạp dữ liệu thành công !")
                self.ui.lbLoadDataP4.setVisible(True)
            else:
                self.ui.lbLoadDataP4.setText("Nạp dữ liệu thành công !")
                self.ui.lbLoadDataP4.setVisible(True)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Đường dẫn cơ sở dữ liệu không tồn tại !")
            msg.setWindowTitle("Warning")
            msg.exec_()

    # thêm tác giả
    def addAuthor(self):
        if self.df_main is None:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Chưa tải dữ liệu !")
            msg.setWindowTitle("Warning")
            msg.exec_()
        else:
            path_new_data = self.ui.lNewDBP4.text()
            name_author = self.ui.lNameAuthorP4.text()

            if name_author in self.all_author_list:
                self.ui.lbAddP4.setVisible(True)
                self.ui.lbAddP4.setText("Đang thêm vào cơ sở dữ liệu ... !")
                self.ui.lbAddP4.repaint()
                df_search = self.df_main['author'].str.findall(name_author)
                index_search = [i for i, value in enumerate(df_search) if len(value) > 0]
                print(index_search)
                if len(index_search) > 0:
                    df_list_of_author = self.df_main.iloc[index_search, :]

                    if path.exists(path_new_data):
                        with open(path_new_data, 'a+', newline='') as write_obj:
                            csv_writer = writer(write_obj)
                            # Ghi vào file csv
                            for i in range(df_list_of_author.shape[0]):
                                csv_writer.writerow(list(df_list_of_author.iloc[i, :]))
                            self.ui.lbAddP4.setText("Thêm thành công !")

                    else:
                        if path.exists(PATH_CUSTOM_DATA):
                            with open(PATH_CUSTOM_DATA, 'a+', newline='') as write_obj:
                                csv_writer = writer(write_obj)
                                # Add contents of list as last row in the csv file
                                for i in range(df_list_of_author.shape[0]):
                                    csv_writer.writerow(list(df_list_of_author.iloc[i, :]))
                                self.ui.lbAddP4.setText("Thêm thành công !")

                        else:
                            df_list_of_author.to_csv(PATH_CUSTOM_DATA, index=False)
                            self.ui.lbAddP4.setText("Thêm thành công !")

                else:
                    self.ui.lbAddP4.setVisible(False)
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("Không tồn tác giả trong tập dữ liệu")
                    msg.setWindowTitle("Warning")
                    msg.exec_()

            else:
                self.ui.lbAddP4.setVisible(False)
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Không tồn tác giả trong tập dữ liệu")
                msg.setWindowTitle("Warning")
                msg.exec_()

    # Tìm kiếm các tác giả công tác xuôi
    def getAuthorFromAuthor(self):

        name_authors = author_vt.columns
        author_name = self.ui.lTacGiaP1.text()
        if author_name in name_authors:
            self.ui.lbSearchP1.setVisible(True)
            self.ui.lbSearchP1.repaint()

            df_author_name = cosine_similar(author_name, 10)
            # print(df_author_name)
            # self.ui.teditNhomCongTac.setText(str(df_author_name))
            row = 0
            self.ui.tblP1.setRowCount(df_author_name.shape[0])
            for i in range(df_author_name.shape[0]):
                item = dict(df_author_name.iloc[i, :])
                print(item)
                self.ui.tblP1.setItem(i, 0, QTableWidgetItem(str(i)))
                self.ui.tblP1.setItem(i, 1, QTableWidgetItem(str(df_author_name.index[i])))
                self.ui.tblP1.setItem(i, 2, QTableWidgetItem(str(np.round(df_author_name.iloc[i, 0], 4))))
            self.ui.lbSearchP1.setVisible(False)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Tên cộng tác viên không tồn tại")
            msg.setWindowTitle("Warning")
            msg.exec_()

    # Tìm kiếm các tác giả cộng tác ngược
    def getAuthorFromGroupAuthor(self):
        name_authors = author_vt.columns

        authors = []
        author_name_1 = self.ui.lTacGia1.text()
        author_name_2 = self.ui.lTacGia2.text()
        author_name_3 = self.ui.lTacGia3.text()
        author_name_4 = self.ui.lTacGia4.text()
        author_name_5 = self.ui.lTacGia5.text()
        author_name_6 = self.ui.lTacGia6.text()
        author_name_7 = self.ui.lTacGia7.text()
        author_name_8 = self.ui.lTacGia8.text()
        author_name_9 = self.ui.lTacGia9.text()
        author_name_10 = self.ui.lTacGia10.text()

        if author_name_1 in name_authors:
            authors.append(author_name_1)
        if author_name_2 in name_authors:
            authors.append(author_name_2)
        if author_name_3 in name_authors:
            authors.append(author_name_3)
        if author_name_4 in name_authors:
            authors.append(author_name_4)
        if author_name_5 in name_authors:
            authors.append(author_name_5)
        if author_name_6 in name_authors:
            authors.append(author_name_6)
        if author_name_7 in name_authors:
            authors.append(author_name_7)
        if author_name_8 in name_authors:
            authors.append(author_name_8)
        if author_name_9 in name_authors:
            authors.append(author_name_9)
        if author_name_10 in name_authors:
            authors.append(author_name_10)
        if len(authors) > 0:

            self.ui.lbSearchP2.setVisible(True)
            self.ui.lbSearchP2.repaint()

            group_author_vector = np.zeros_like((author_vt.shape[0],))
            for author_name in authors:
                group_author_vector = group_author_vector + author_vt[author_name]
            group_author_vector = np.array(group_author_vector).reshape(1, -1)
            author_name = self.ui.lTacGiaP1.text()
            df_author_name = group_cosine_similar(group_author_vector, authors, 10)

            self.ui.tblP2.setRowCount(df_author_name.shape[0])
            for i in range(df_author_name.shape[0]):
                item = dict(df_author_name.iloc[i, :])
                print(item)
                self.ui.tblP2.setItem(i, 0, QTableWidgetItem(str(i)))
                self.ui.tblP2.setItem(i, 1, QTableWidgetItem(str(df_author_name.index[i])))
                self.ui.tblP2.setItem(i, 2, QTableWidgetItem(str(np.round(df_author_name.iloc[i, 0], 4))))
            self.ui.lbSearchP2.setVisible(False)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Phải có ít nhất một tác giả trong nhóm cộng tác tồn tại")
            msg.setWindowTitle("Warning")
            msg.exec_()

    # Lấy danh sách các bài báo từ bộ dữ liệu ban đầu(bộ dữ liệu để tìm kiếm cộng tác)
    def getListPaper(self, flag):
        if flag == 1:

            if self.nextP3 + 9 < df.shape[0]:
                self.reVertP3 = self.reVertP3 + 10
                self.nextP3 = self.nextP3 + 10

            elif self.nextP3 - df.shape[0] > -10 and self.reVertP3 + 10 < df.shape[0]:
                self.reVertP3 = self.reVertP3 + 10
                self.nextP3 = df.shape[0]

        elif flag == 2:

            if self.nextP3 == df.shape[0]:
                self.nextP3 = self.nextP3 - (df.shape[0] - self.reVertP3)
                self.reVertP3 = self.reVertP3 - 10

            elif self.reVertP3 - 10 >= 0:
                self.reVertP3 = self.reVertP3 - 10
                self.nextP3 = self.nextP3 - 10
        else:
            self.reVertP3 = 0
            self.nextP3 = 10

        self.ui.tblP3.setRowCount(self.nextP3 - self.reVertP3)
        papers = df.loc[self.reVertP3:self.nextP3, ("author", "title")].transpose()

        for i, _ in enumerate(papers):
            self.ui.tblP3.setItem(i, 0, QTableWidgetItem(str(i + self.reVertP3)))
            self.ui.tblP3.setItem(i, 1, QTableWidgetItem(str(papers.iloc[1, i])))
            self.ui.tblP3.setItem(i, 2, QTableWidgetItem(str(papers.iloc[0, i])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
