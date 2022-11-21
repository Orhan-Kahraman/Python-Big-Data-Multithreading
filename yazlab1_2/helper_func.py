from main_comparison import *
import threading
import sys
from csv_file_parsing import *

# GİRİLEN DEĞERLERİN ARALIKLARINI DÜZENLEME


def check_input(entered_num, additemvar, thread_content=False):
    if (entered_num != ""):
        entered_num = int(entered_num)
        if thread_content:
            if (entered_num > 10):
                entered_num = 10
                print(entered_num)
                additemvar.setText(str(entered_num))
            elif (entered_num < 1):
                entered_num = 1
                print(entered_num)
                additemvar.setText(str(entered_num))
            else:
                print(entered_num)
                additemvar.setText(str(entered_num))

        else:
            if (entered_num > 100):
                entered_num = 100
                print(entered_num)
                additemvar.setText(str(entered_num))
            else:
                print(entered_num)
                additemvar.setText(str(entered_num))


# Sütunların benzerlik yüzdelerini bir listeye atan fonksiyon
def add_percentage(additem1, additem2, additem3, additem4, additem5, additem6, addthreadNum):
    csvSet = CsvSettings()
    size = len(csvSet.use_new_rows())

    num_thread = addthreadNum.text()
    column_percentage = []
    threads = []
    column_percentage.append(additem1.text())
    column_percentage.append(additem2.text())
    column_percentage.append(additem3.text())
    column_percentage.append(additem4.text())
    column_percentage.append(additem5.text())
    column_percentage.append(additem6.text())

    for i in range(len(column_percentage)):
        if (column_percentage[i] == ""):
            column_percentage[i] = "0"
    if num_thread == "":
        num_thread = "1"
    num_thread = int(num_thread)

    split_size = int(size/num_thread)
    # print(split_size)
    column_percentage = list(map(int, column_percentage))
    # print(column_percentage)
    print("{} tane thread oluşturuluyor..".format(num_thread))
    count_data = 0
    for i in range(num_thread):

        my_thread = threading.Thread(target=mainComparisonF(
            listofpersentage=column_percentage, baslama=count_data, split=split_size, columnlist=csvSet.get_column_names()))
        my_thread.name = "Thread..{}".format(i+1)
        count_data += split_size
        threads.append(my_thread)
        my_thread.start()

    print(threads)
