from csv_file_parsing import *
from helper_func import *
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import os.path
import ast


def tokencsv(baslama, split):
    if (os.path.isfile("tokenize_new_rows.csv")):
        print("Tokenize dosya hazır")
        data_tokenize = pd.read_csv(
            "tokenize_new_rows.csv", index_col=0, skiprows=baslama, nrows=split)
        return data_tokenize

    else:
        csvSett = CsvSettings()
        data = csvSett.use_new_rows()
        regexp = RegexpTokenizer('\w+')
        print("Tokenize oluşmamış\nBekleyin dosya oluşturuluyor..")

        for column in data.columns:
            data[column] = data[column].astype(str).apply(regexp.tokenize)
        data.to_csv("tokenize_new_rows.csv")
        return tokencsv()


def mainComparisonF(listofpersentage, baslama, split, columnlist):

    trylist = listofpersentage
    aranan = 0
    karsilastirilan = 0
    colnumarasi = 0

    # Tokenize datayı fonksiyondan aldık
    data = tokencsv(baslama=baslama, split=split)
    # print(data.iloc[1])
    wanted_columns = {}
    newcollist = []
    columns_list = data.columns.values.tolist()

    for i in range(len(trylist)):
        if (trylist[i] != 0):
            wanted_columns.update({columns_list[i]: trylist[i]})
            newcollist.append(columnlist[i])

    for colkey, percentage in wanted_columns.items():
        a = 0
        aranan = 0
        for i in data[colkey]:
            aranan += 1

            i = ast.literal_eval(i)

            for j in data[colkey]:
                karsilastirilan += 1
                j = ast.literal_eval(j)

                same_words = list(set(i) & set(j))
                if (len(i) >= len(j)):
                    benzerlik_oranı = (len(same_words) / len(i))*100
                    if (benzerlik_oranı >= percentage):
                        print("{} column, {}. kayıt {}".format(
                            newcollist[colnumarasi], baslama+aranan, i))
                        print("{} column, {}. kayıt {}".format(
                            newcollist[colnumarasi], baslama+karsilastirilan, j))
                        print("{}% Benzerlik. İstenen {}% orandan büyük veya eşit.".format(
                            int(benzerlik_oranı), percentage))
                        print("---------------------------------")
                else:
                    benzerlik_oranı = (len(same_words) / len(j))*100
                    if (benzerlik_oranı >= percentage):
                        print("{} column, {}. kayıt {}".format(
                            newcollist[colnumarasi], baslama+aranan, i))
                        print("{} column, {}. kayıt {}".format(
                            newcollist[colnumarasi], baslama+karsilastirilan, j))
                        print("{}% Benzerlik. İstenen {}% orandan büyük veya eşit.".format(
                            int(benzerlik_oranı), percentage))
                        print("---------------------------------")

                a += 1
                if a == 10:
                    break
            break
        colnumarasi += 1
        if (len(wanted_columns) > 1):
            print("////////////////////////////// NEXT COLUMN \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
