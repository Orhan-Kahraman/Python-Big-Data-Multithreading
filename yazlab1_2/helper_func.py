# GİRİLEN DEĞERLERİN ARALIKLARINI DÜZENLEME
def check_input(entered_num, additemvar):
    if (entered_num != ""):
        entered_num = int(entered_num)
        if (entered_num > 100):
            entered_num = 100
            print(entered_num)
            additemvar.setText(str(entered_num))
        else:
            print(entered_num)
            additemvar.setText(str(entered_num))


# Sütunların benzerlik yüzdelerini bir listeye atan fonksiyon
def add_percentage(additem1, additem2, additem3, additem4, additem5, additem6,):
    column_percentage = []
    column_percentage.append(additem1.text())
    column_percentage.append(additem2.text())
    column_percentage.append(additem3.text())
    column_percentage.append(additem4.text())
    column_percentage.append(additem5.text())
    column_percentage.append(additem6.text())

    for i in range(len(column_percentage)):
        if (column_percentage[i] == ""):
            column_percentage[i] = "0"

    column_percentage = list(map(int, column_percentage))
    print(column_percentage)

    return column_percentage
