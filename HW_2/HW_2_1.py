import os, pandas as pd
import transliterate
import numpy as np


def get_data():
    columns = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
    main_data = []
    main_data.append(columns)
    for i in columns:
        list = globals()[transliterate.translit(i.replace(" ", "_"), reversed=True)] = []
        for folder, subfolders, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith('.txt'):
                    with open(file, encoding='cp1251') as f:
                        lines = f.read().splitlines()
                        for j in lines:
                            if i in j:
                                j_list = j.split(': ')
                                list.append(j_list[1].strip())
        else:
            main_data.append(list)
    else:
        return pd.DataFrame(np.array(main_data[1:]).transpose(), columns=main_data[0])


def write_to_csv(csv_file):
    get_data().to_csv(csv_file, index=False)


write_to_csv('csv_file.csv')
