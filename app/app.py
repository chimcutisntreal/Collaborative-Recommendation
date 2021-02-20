import pandas as pd
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QListWidgetItem
from main_ui import *
from data.XML import *
from functools import partial
from os import path
import os
from csv import writer
from sklearn.metrics.pairwise import cosine_similarity
import json
import sys

with open('config.json') as json_file:
    config = json.load(json_file)

PATH_MAIN_DATA = config["PATH_MAIN_DATA"]
PATH_CUSTOM_DATA = config["PATH_CUSTOM_DATA"]
PATH_DTD = config["PATH_DTD"]
PATH_XML_TO_CSV = config["PATH_XML_TO_CSV"]
#PATH_RECCOMENT_DATA = config["PATH_RECCOMENT_DATA"]

# def twodata_consine_similar(author, author_name, top):
#     consine = {}
#     for author in author_vt.columns:
#         cosi = consine_similarity(author_vt[[author_name]].values.reshape(1,-1),
#                                   author_vt[[author]].values.reshape(1,-1))
#         consine[author] = consi[0]

def cosine_similar_ortherdata(author_vt, author_name, top):
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

def cosine_similar(author_vt, author_name, top):
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


def group_cosine_similar(author_vt, group_author_vector, authors_name, top):
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

        # 4 biến này phục vụ cho việc phân trang
        self.nextP3 = 10
        self.reVertP3 = 0
        self.nextP4 = 10
        self.reVertP4 = 0

        # biến lưu tên các file data đầu vào
        self.list_df_name = []

        self.author_vt = {}
        self.df = {}

        self.author_vt_rcm = None
        self.df_rcm = None

        self.df_main = None # biến để lưu bộ dữ liệu đầy đủ (bộ dữ liệu để tìm kiếm trong việc thêm tác giả mới)
        self.all_author_list = set()

        # page 0: Import data
        self.ui.btTabImportData.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pImportData))
        self.ui.btChoose.clicked.connect(self.choose_path)
        self.ui.btLoad.clicked.connect(self.load)
        self.ui.lblPath.setText("/Users/chutrieuchinh/Documents/pyqt5/data/output_article_10k_2.csv")

        # page 1: nhom cong tac tuong tu nhat
        self.ui.btTabNhomNguoiCongTac.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pNhomCongTacTuongTuNhat))
        self.ui.tblP1.cellDoubleClicked.connect(partial(self.show_item, flag=0))
        self.ui.btSearchP1.clicked.connect(self.getAuthorFromAuthor)

        # page 1 new: nhom cong tac tuong tu nhat new
        self.ui.btTabNhomNguoiCongTacNew.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pNhomCongTacTuongTuNhatNew))
        self.ui.tblP1New.cellDoubleClicked.connect(partial(self.show_item, flag=1))
        self.ui.btSearchP1New.clicked.connect(self.getAuthorFromAuthorNew)

        # page 2: cong tac tuong tu nhat
        self.ui.btNguoiCongTac.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pCongTacTuongTuNhat))
        self.ui.tblP2.cellDoubleClicked.connect(self.show_item_group)
        self.ui.btSearchP2.clicked.connect(self.getAuthorFromGroupAuthor)

        # page 3: danh sach bai bao
        self.ui.btTabDanhSachBaiBao.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pDnhachBaiBao))
        self.ui.btShowP3.clicked.connect(partial(self.getListPaper, flag=0))
        self.ui.btNextP3.clicked.connect(partial(self.getListPaper, flag=1))
        self.ui.btRevertP3.clicked.connect(partial(self.getListPaper, flag=2))

        # page 4: them tac gia thu cong
        self.ui.btTabThemTacGia.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pThemTacGia))
        self.ui.btChooseDBP4.clicked.connect(partial(self.browDBP4))
        self.ui.btLoadDBP4.clicked.connect(partial(self.loadDBP4))
        self.ui.btAddP4.clicked.connect(partial(self.addAuthor))
        self.ui.btChoosePathNewDBP4.clicked.connect(partial(self.browNewDB))
        self.ui.btShowP4.clicked.connect(partial(self.getListNewPaper, flag=0))
        self.ui.btNextP4.clicked.connect(partial(self.getListNewPaper, flag=1))
        self.ui.btRevertP4.clicked.connect(partial(self.getListNewPaper, flag=2))

        self.show()

    def show_item(self, flag):
        self.newWidget = NewWidgetPopup()
        if flag == 0:
            current_df = self.df[self.ui.cbChooseTarget_1.currentText()]
        else:
            current_df = self.df[self.ui.cbChooseTarget_1_new.currentText()]
        author_base = self.ui.lTacGiaP1.text()
        author_cell = self.ui.tblP1.currentItem().text()
        df_paper_base = self.filterPaperByAuthor(current_df, author_base)
        df_paper_cell = self.filterPaperByAuthor(current_df, author_cell)
        merge_df = df_paper_base.append(df_paper_cell)
        same_df = merge_df[merge_df.duplicated(["title"])]
        list_same_paper = []
        list_same_id = []
        if not same_df.empty:
            list_same_paper = same_df['title'].values.tolist()
            list_same_id = same_df['id'].values.tolist()
        data = {
            'max_row': max(len(df_paper_base.index), len(df_paper_cell.index)) - len(list_same_id),
            'author_base': [author_base],
            'author_cell': author_cell,
            'df': merge_df,
            'list_paper': list_same_paper,
            'list_id': list_same_id
        }
        self.newWidget.init_table(author_base, author_cell)
        self.newWidget.generate_data(data)
        self.newWidget.show()

    def show_item_group(self):
        self.newWidget = NewWidgetPopup()
        current_df = self.df[self.ui.cbChooseTarget_2.currentText()]
        list_author = []
        list_author.append(self.ui.lTacGia1.text())
        list_author.append(self.ui.lTacGia2.text())
        list_author.append(self.ui.lTacGia3.text())
        list_author.append(self.ui.lTacGia4.text())
        list_author.append(self.ui.lTacGia5.text())
        list_author.append(self.ui.lTacGia6.text())
        list_author.append(self.ui.lTacGia7.text())
        list_author.append(self.ui.lTacGia8.text())
        list_author.append(self.ui.lTacGia9.text())
        list_author.append(self.ui.lTacGia10.text())
        author_cell = self.ui.tblP2.currentItem().text()
        df_paper_base = self.filterPaperByListAuthor(current_df, list_author)
        df_paper_cell = self.filterPaperByAuthor(current_df, author_cell)
        merge_df = df_paper_base.append(df_paper_cell)
        same_df = merge_df[merge_df.duplicated(["title"])]
        list_same_paper = []
        list_same_id = []
        if not same_df.empty:
            list_same_paper = same_df['title'].values.tolist()
            list_same_id = same_df['id'].values.tolist()
        data = {
            'max_row': max(len(df_paper_base.index), len(df_paper_cell.index)) - len(list_same_id),
            'author_base': list_author,
            'author_cell': author_cell,
            'df': merge_df,
            'list_paper': list_same_paper,
            'list_id': list_same_id
        }
        self.newWidget.init_table("Nhóm tác giả được khuyến nghị", author_cell)
        self.newWidget.generate_data(data)
        self.newWidget.show()

    # lấy Danh sách tác giả từ dữ liệu mới
    def getListNewPaper(self, flag):
        path_new_data = self.ui.lNewDBP4.text()
        if not path.exists(path_new_data):
            path_new_data = PATH_CUSTOM_DATA
            if not path.exists(path_new_data):
                self.raise_notice(text="Không tồn tại dữ liệu trong :%s" % path_new_data)
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
            self.ui.tblP4.setItem(i, 1, QTableWidgetItem(str(i + self.reVertP4)))
            self.ui.tblP4.setItem(i, 2, QTableWidgetItem(str(papers.iloc[1, i])))
            self.ui.tblP4.setItem(i, 3, QTableWidgetItem(str(papers.iloc[0, i])))

    def choose_path(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'File (*.csv *.xml)')
        self.ui.lblPath.setText(fname)

    def browDBP4(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'File (*.csv)')
        self.ui.lPathP4.setText(fname)

    def browNewDB(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'File (*.csv)')
        self.ui.lNewDBP4.setText(fname)

    def load(self):
        path_data = self.ui.lblPath.text()
        is_xml = False
        if path_data.endswith('.xml'):
            output_name = path_data.split('/').pop().split('.')[0] + '.csv'
            output_path = path.join(PATH_XML_TO_CSV, output_name)
            # abs_dtd_path = os.path.abspath(PATH_DTD)
            xml_to_csv(path_data, PATH_DTD, output_path)
            path_data = output_path
            is_xml = True
        if path.exists(path_data):
            self.ui.lbLoad.setText("Đang tải dữ liệu... !")
            self.ui.lbLoad.setVisible(True)
            self.ui.lbLoad.repaint()

            if not self.df_main:
                df_key = path_data.split('/').pop()
                if df_key not in self.list_df_name:
                    self.list_df_name.append(df_key)
                    if is_xml:
                        self.df[df_key] = pd.read_csv(path_data, encoding='latin1', error_bad_lines=False, sep=';')
                    else:
                        self.df[df_key] = pd.read_csv(path_data, encoding='latin1', error_bad_lines=False)
                #    self.df.drop_duplicates(keep=True,inplace=True)
                    self.df[df_key].reset_index(inplace=True)
                    df_author = self.df[df_key][['author']]
                    author_list = set()
                    for i in df_author['author']:
                        s = str(i).split('|')
                        for j in s:
                            author_list.add(j)

                    df_author['idpp'] = np.arange(df_author.shape[0])
                    self.author_vt[df_key] = np.zeros((len(author_list), df_author.shape[0]))
                    self.author_vt[df_key] = pd.DataFrame(self.author_vt[df_key], index=list(author_list))

                    for i in range(df_author.shape[0]):
                        str_author = str(df_author['author'][i]).split('|')
                        for auth in str_author:
                            self.author_vt[df_key].loc[auth, i] = self.author_vt[df_key].loc[auth, i] + 1

                    self.author_vt[df_key] = self.author_vt[df_key].transpose()
                    self.ui.lbLoad.setText("Tải thành công !")
                    self.ui.lbLoad.setVisible(True)
                    item_uploaded = QListWidgetItem(df_key)
                    self.ui.lstUploaded.addItem(item_uploaded)
                    self.ui.cbChooseTarget_1.addItem(df_key)
                    self.ui.cbChooseSource_1_new.addItem(df_key)
                    self.ui.cbChooseTarget_1_new.addItem(df_key)
                    self.ui.cbChooseTarget_2.addItem(df_key)
                    self.ui.cbChooseTarget_3.addItem(df_key)
                else:
                    self.ui.lbLoad.setText("Dữ liệu đã được nạp !")
            else:
                self.ui.lbLoad.setText("Tải thành công !")
                self.ui.lbLoad.setVisible(True)
        else:
            self.raise_notice(text="Đường dẫn cơ sở dữ liệu không tồn tại !")

    # Nạp dữ liệu để cho phần thêm tác giả thủ công
    def loadDBP4(self):
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
                b = self.all_author_list
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
            self.raise_notice(text="Chưa tải dữ liệu !")
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
                    self.raise_notice(text="Không tồn tại tác giả trong tập dữ liệu")
            else:
                self.ui.lbAddP4.setVisible(False)
                self.raise_notice(text="Không tồn tại tác giả trong tập dữ liệu")

    # Tìm kiếm tác giả trọng cụm
    def getAuthorFromOrherdata (self) :
        if not self.author_vt:
            self.raise_notice(text='no_data')
        else:
            name_authors = self.author_vt.colums

    # Tìm kiếm các tác giả công tác xuôi
    def getAuthorFromAuthor(self):
        df_key = str(self.ui.cbChooseTarget_1.currentText())
        if not df_key:
            self.raise_notice(text='no_key')
        elif df_key and self.author_vt[df_key].empty:
            self.raise_notice(text='no_data')
        else:
            name_authors = self.author_vt[df_key].columns
            author_name = self.ui.lTacGiaP1.text()
            if author_name in name_authors:
                self.ui.lbSearchP1.setVisible(True)
                self.ui.lbSearchP1.repaint()

                df_author_name = cosine_similar(self.author_vt[df_key], author_name, 10)
                row = 0
                self.ui.tblP1.setRowCount(df_author_name.shape[0])
                for i in range(df_author_name.shape[0]):
                    item = dict(df_author_name.iloc[i, :])
                    print(item)
                    self.ui.tblP1.setItem(i, 0, QTableWidgetItem(str(i+1)))
                    self.ui.tblP1.setItem(i, 1, QTableWidgetItem(str(df_author_name.index[i])))
                    self.ui.tblP1.setItem(i, 2, QTableWidgetItem(str(np.round(df_author_name.iloc[i, 0], 4))))
                self.ui.lbSearchP1.setVisible(False)

            else:
                self.raise_notice(text="Tên cộng tác viên không tồn tại")

    # Tìm kiếm các tác giả công tác xuôi new
    def getAuthorFromAuthorNew(self):
        df_key_source = str(self.ui.cbChooseSource_1_new.currentText())
        df_key_target = str(self.ui.cbChooseTarget_1_new.currentText())
        if not df_key_source or not df_key_target:
            self.raise_notice(text='no_key')
        elif (df_key_target and self.author_vt[df_key_target].empty) or (df_key_source and self.author_vt[df_key_source].empty):
            self.raise_notice(text='no_data')
        else:
            name_authors = self.author_vt[df_key_target].columns
            author_name = self.ui.lTacGiaP1New.text()
            if author_name not in self.author_vt[df_key_source].columns:
                self.raise_notice(text="Không tìm thấy tác giả từ dữ liệu đích!")
                return
            if author_name in name_authors:
                self.ui.lbSearchP1New.setVisible(True)
                self.ui.lbSearchP1New.repaint()

                df_author_name = cosine_similar(self.author_vt[df_key_target], author_name, 10)
                row = 0
                self.ui.tblP1New.setRowCount(df_author_name.shape[0])
                for i in range(df_author_name.shape[0]):
                    item = dict(df_author_name.iloc[i, :])
                    print(item)
                    self.ui.tblP1New.setItem(i, 0, QTableWidgetItem(str(i+1)))
                    self.ui.tblP1New.setItem(i, 1, QTableWidgetItem(str(df_author_name.index[i])))
                    self.ui.tblP1New.setItem(i, 2, QTableWidgetItem(str(np.round(df_author_name.iloc[i, 0], 4))))
                self.ui.lbSearchP1New.setVisible(False)

            else:
                self.raise_notice(text="Tên cộng tác viên không tồn tại")

    # Tìm kiếm các tác giả cộng tác ngược
    def getAuthorFromGroupAuthor(self):
        df_key = str(self.ui.cbChooseTarget_2.currentText())
        if not df_key:
            self.raise_notice(text='no_key')
        elif df_key and self.author_vt[df_key].empty:
            self.raise_notice(text='no_data')
        else:
            name_authors = self.author_vt[df_key].columns

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

                group_author_vector = np.zeros_like((self.author_vt[df_key].shape[0],))
                for author_name in authors:
                    group_author_vector = group_author_vector + self.author_vt[df_key][author_name]
                group_author_vector = np.array(group_author_vector).reshape(1, -1)
                author_name = self.ui.lTacGiaP1.text()
                df_author_name = group_cosine_similar(self.author_vt[df_key], group_author_vector, authors, 10)

                self.ui.tblP2.setRowCount(df_author_name.shape[0])
                for i in range(df_author_name.shape[0]):
                    self.ui.tblP2.setItem(i, 0, QTableWidgetItem(str(i+1)))
                    self.ui.tblP2.setItem(i, 1, QTableWidgetItem(str(df_author_name.index[i])))
                    self.ui.tblP2.setItem(i, 2, QTableWidgetItem(str(np.round(df_author_name.iloc[i, 0], 4))))
                self.ui.lbSearchP2.setVisible(False)
            else:
                self.raise_notice(text="Phải có ít nhất một tác giả trong nhóm cộng tác tồn tại")

    # def searchListPaper(self):
    #     df_key = str(self.ui.cbChooseTarget_3.currentText())
    #     # search_type =
    #     if not df_key:
    #         self.raise_notice(text='no_key')
    #     elif df_key and self.df[df_key].empty:
    #         self.raise_notice(text='no_data')
    #     else:
    #         current_df = self.df[df_key]
    #         list_author = current_df.loc[current_df['author']]

    # Lọc bài báo theo 1 tác giả
    def filterPaperByAuthor(self, df, author):
        indexs = []
        authors = df['author']
        for item in authors.iteritems():
            if isinstance(item[1], str) and author in item[1].split('|'):
                indexs.append(item[0])
        df = df.iloc[indexs, :]
        if not df.empty:
            return df
        self.raise_notice(text=f"Không tìm thấy bài báo với tác giả {author}")

    # Lọc bài báo theo 1 tác giả
    def filterPaperByListAuthor(self, df, list_author):
        indexs = []
        authors = df['author']
        for item in authors.iteritems():
            if isinstance(item[1], str) and any(i in item[1].split('|') for i in list_author):
                indexs.append(item[0])
        indexs = list(dict.fromkeys(indexs))
        df = df.iloc[indexs, :]
        if not df.empty:
            return df
        self.raise_notice(text=f"Không tìm thấy bài báo nào!")


    # Lấy danh sách các bài báo từ bộ dữ liệu ban đầu(bộ dữ liệu để tìm kiếm cộng tác)
    def getListPaper(self, flag):
        df_key = str(self.ui.cbChooseTarget_3.currentText())
        search_type = self.ui.cbSearchType_3.currentData()
        search_data = str(self.ui.lSearchP3.text())
        self.ui.tblP3.clearContents()
        if not df_key:
            self.raise_notice(text='no_key')
        elif df_key and self.df[df_key].empty:
            self.raise_notice(text='no_data')
        else:
            current_df = self.df[df_key]
            if bool(search_data):
                if search_type == 0:
                    current_df = current_df.loc[search_data == current_df['title']]
                elif search_type == 1:
                    current_df = self.filterPaperByAuthor(current_df, search_data)
            if flag == 1:
                if self.nextP3 + 9 < current_df.shape[0]:
                    self.reVertP3 = self.reVertP3 + 10
                    self.nextP3 = self.nextP3 + 10

                elif self.nextP3 - current_df.shape[0] > -10 and self.reVertP3 + 10 < current_df.shape[0]:
                    self.reVertP3 = self.reVertP3 + 10
                    self.nextP3 = current_df.shape[0]

            elif flag == 2:

                if self.nextP3 == current_df.shape[0]:
                    self.nextP3 = self.nextP3 - (current_df.shape[0] - self.reVertP3)
                    self.reVertP3 = self.reVertP3 - 10

                elif self.reVertP3 - 10 >= 0:
                    self.reVertP3 = self.reVertP3 - 10
                    self.nextP3 = self.nextP3 - 10
            else:
                self.reVertP3 = 0
                self.nextP3 = 10

            self.ui.tblP3.setRowCount(self.nextP3 - self.reVertP3)
            papers = current_df.loc[self.reVertP3:self.nextP3, ("author", "title")].transpose()

            for i, _ in enumerate(papers):
                self.ui.tblP3.setItem(i, 0, QTableWidgetItem(str(i + self.reVertP3)))
                self.ui.tblP3.setItem(i, 1, QTableWidgetItem(str(papers.iloc[1, i])))
                self.ui.tblP3.setItem(i, 2, QTableWidgetItem(str(papers.iloc[0, i])))

    def raise_notice(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if text == 'no_key':
            msg.setText("Chọn dữ liệu đích!")
        elif text == 'no_data':
            msg.setText("Không có dữ liệu!")
        else:
            msg.setText(str(text))
        msg.setWindowTitle("Warning")
        msg.exec_()


class NewWidgetPopup(QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("List Paper")
        self.setGeometry(300, 150, 1000, 600)

        self.centralwidget_popup = QtWidgets.QWidget(self)
        self.centralwidget_popup.setObjectName("centralwidget_popup")
        self.centralwidget_popup.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.centralwidget_popup.setGeometry(QtCore.QRect(0, 0, 1000, 600))

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget_popup)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

    def init_table(self, author_base, author_cell):
        self.lblSamePaper = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblSamePaper.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(70)
        self.lblSamePaper.setFont(font)
        self.lblSamePaper.setObjectName("lblSamePaper")
        self.lblSamePaper.setText("BÀI BÁO GIỐNG NHAU")
        self.verticalLayout.addWidget(self.lblSamePaper)

        self.tblSamePaper = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tblSamePaper.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblSamePaper.sizePolicy().hasHeightForWidth())
        self.tblSamePaper.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.tblSamePaper.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblSamePaper.setFont(font)
        self.tblSamePaper.setMinimumSize(QtCore.QSize(0, 200))
        self.tblSamePaper.setMouseTracking(True)
        self.tblSamePaper.setStyleSheet("selection-background-color: rgb(119, 162, 255);")
        self.tblSamePaper.setDragEnabled(False)
        self.tblSamePaper.setDragDropOverwriteMode(True)
        self.tblSamePaper.setTextElideMode(QtCore.Qt.ElideRight)
        self.tblSamePaper.setAutoScrollMargin(2)
        self.tblSamePaper.setShowGrid(True)
        self.tblSamePaper.setGridStyle(QtCore.Qt.SolidLine)
        self.tblSamePaper.setWordWrap(True)
        self.tblSamePaper.setCornerButtonEnabled(True)
        self.tblSamePaper.setObjectName("tblSamePaper")
        self.tblSamePaper.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem("STT")
        self.tblSamePaper.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("Tên bài báo")
        self.tblSamePaper.setHorizontalHeaderItem(1, item)
        self.tblSamePaper.horizontalHeader().setVisible(True)
        self.tblSamePaper.horizontalHeader().setCascadingSectionResizes(True)
        self.tblSamePaper.horizontalHeader().setHighlightSections(True)
        self.tblSamePaper.horizontalHeader().setMinimumSectionSize(90)
        self.tblSamePaper.horizontalHeader().setSortIndicatorShown(False)
        self.tblSamePaper.horizontalHeader().setStretchLastSection(True)
        self.tblSamePaper.verticalHeader().setVisible(False)
        self.tblSamePaper.verticalHeader().setCascadingSectionResizes(False)
        self.tblSamePaper.verticalHeader().setHighlightSections(False)
        self.tblSamePaper.verticalHeader().setMinimumSectionSize(23)
        self.tblSamePaper.verticalHeader().setSortIndicatorShown(False)
        self.tblSamePaper.verticalHeader().setStretchLastSection(False)
        self.tblSamePaper.setColumnWidth(0, 80)
        self.tblSamePaper.setColumnWidth(1, 920)
        self.verticalLayout.addWidget(self.tblSamePaper)

        self.lblDifferencePaper = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblDifferencePaper.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(70)
        self.lblDifferencePaper.setFont(font)
        self.lblDifferencePaper.setObjectName("lblDifferencePaper")
        self.lblDifferencePaper.setText("BÀI BÁO KHÁC NHAU")
        self.verticalLayout.addWidget(self.lblDifferencePaper)

        self.tblDifferencePaper = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tblDifferencePaper.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblDifferencePaper.sizePolicy().hasHeightForWidth())
        self.tblDifferencePaper.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.tblDifferencePaper.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblDifferencePaper.setFont(font)
        self.tblDifferencePaper.setMinimumSize(QtCore.QSize(0, 500))
        self.tblDifferencePaper.setMouseTracking(True)
        self.tblDifferencePaper.setStyleSheet("selection-background-color: rgb(119, 162, 255);")
        self.tblDifferencePaper.setDragEnabled(False)
        self.tblDifferencePaper.setDragDropOverwriteMode(True)
        self.tblDifferencePaper.setTextElideMode(QtCore.Qt.ElideRight)
        self.tblDifferencePaper.setAutoScrollMargin(2)
        self.tblDifferencePaper.setShowGrid(True)
        self.tblDifferencePaper.setGridStyle(QtCore.Qt.SolidLine)
        self.tblDifferencePaper.setWordWrap(True)
        self.tblDifferencePaper.setCornerButtonEnabled(True)
        self.tblDifferencePaper.setObjectName("tblDifferencePaper")
        self.tblDifferencePaper.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem("STT")
        self.tblDifferencePaper.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem(author_base)
        self.tblDifferencePaper.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem(author_cell)
        self.tblDifferencePaper.setHorizontalHeaderItem(2, item)
        self.tblDifferencePaper.horizontalHeader().setVisible(True)
        self.tblDifferencePaper.horizontalHeader().setCascadingSectionResizes(True)
        self.tblDifferencePaper.horizontalHeader().setHighlightSections(True)
        self.tblDifferencePaper.horizontalHeader().setMinimumSectionSize(90)
        self.tblDifferencePaper.horizontalHeader().setSortIndicatorShown(False)
        self.tblDifferencePaper.horizontalHeader().setStretchLastSection(True)
        self.tblDifferencePaper.verticalHeader().setVisible(False)
        self.tblDifferencePaper.verticalHeader().setCascadingSectionResizes(False)
        self.tblDifferencePaper.verticalHeader().setHighlightSections(False)
        self.tblDifferencePaper.verticalHeader().setMinimumSectionSize(23)
        self.tblDifferencePaper.verticalHeader().setSortIndicatorShown(False)
        self.tblDifferencePaper.verticalHeader().setStretchLastSection(False)
        self.tblDifferencePaper.setColumnWidth(0, 80)
        self.tblDifferencePaper.setColumnWidth(1, 460)
        self.tblDifferencePaper.setColumnWidth(2, 460)
        self.verticalLayout.addWidget(self.tblDifferencePaper)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def generate_data(self, data):
        self.tblSamePaper.clearContents()
        if data:
            df = data['df']
            if data['list_paper']:
                self.tblSamePaper.setRowCount(len(data['list_paper']) + 1)
                for index, value in enumerate(data['list_paper']):
                    self.tblSamePaper.setItem(index, 0, QTableWidgetItem(str(index+1)))
                    self.tblSamePaper.setItem(index, 1, QTableWidgetItem(str(value)))
            if data['list_id']:
                df = df.loc[~df['id'].isin(data['list_id'])]

            self.tblDifferencePaper.clearContents()
            self.tblDifferencePaper.setRowCount(data['max_row'] + 1)
            index = index_1 = index_2 = 0
            for _, row in df.iterrows():
                self.tblDifferencePaper.setItem(index, 0, QTableWidgetItem(str(index + 1)))
                author = str(row.author).split("|")
                if any(i in author for i in data['author_base']):
                    self.tblDifferencePaper.setItem(index_1, 1, QTableWidgetItem(str(row.title)))
                    index_1 += 1
                elif data['author_cell'] in author:
                    self.tblDifferencePaper.setItem(index_2, 2, QTableWidgetItem(str(row.title)))
                    index_2 += 1
                index += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    
    sys.exit(app.exec_())
