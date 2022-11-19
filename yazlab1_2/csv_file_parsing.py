from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import os.path


class CsvSettings():
    isdata_exist = False

    def csv_parser(self):
        nltk.download('stopwords')

        stop_words = set(stopwords.words('english'))
        regexp = RegexpTokenizer('\w+')

        data = pd.read_csv("rows.csv")

        data.drop(columns=["Date received", "Sub-product", "Sub-issue",
                           "Consumer complaint narrative", "Company public response", "Tags",
                           "Consumer consent provided?", "Submitted via", "Date sent to company",
                           "Company response to consumer", "Timely response?", "Consumer disputed?"],
                  inplace=True, axis=1)

        # Null kayıtların silinmesi
        data = data.dropna()

        for column in data.columns:
            data[column] = data[column].astype(str).str.lower()
            data[column] = data[column].apply(regexp.tokenize)
            data[column] = data[column].apply(
                lambda x: [item for item in x if item not in stop_words])
            data[column] = data[column].apply(
                lambda x: ' '.join([item for item in x if len(item) > 1]))
            data[column] = data[column].astype(
                str).str.replace(r'[^\w\s]+', "", regex=True)

        data = data.dropna()

        data.to_csv("new_rows.csv")

    def use_new_rows(self):

        if (os.path.isfile("new_rows.csv")):
            self.isdata_exist = True
            data = pd.read_csv("new_rows.csv", index_col=0)
            print("Dosya kullanıma hazır.")
            return data
        else:
            print("Dosya Oluşturulmamış.\nYeni dosya oluşturluyor.\nLütfen bekleyiniz.. ")
            self.csv_parser()
            self.use_new_rows()

    def get_column_names(self):
        data = self.use_new_rows()
        if (self.isdata_exist):
            data_top = data.columns.values.tolist()
            print("Sütunlar", data_top)
            return data_top
        else:
            print("Sütunlar bulunamadı çünkü dosya oluşturulmamış")
