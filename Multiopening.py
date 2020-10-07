import os

Path = "/home/ht/PycharmProjects/PV_data_process/venv/TU-Gab   best days/"
filelist = os.listdir(Path)
try:
    PV_database = open('/home/ht/PycharmProjects/PV_data_process/venv/TU-Gab   best days/PV_database.txt')
    print('\nPlease delete file PV_database.txt from current directory')

except:
    for i in filelist:
        if i.endswith(".txt"):  #and i.startswith('Data-file-09-200804')
            with open(Path + i, 'r') as f:
                for line in f:
                    database = open('/home/ht/PycharmProjects/PV_data_process/venv/TU-Gab   best days/PV_database.txt',
                                    'a+')
                    database.write(line)
                    database.close()
                    print(line)
    f.close()

    with open('/home/ht/PycharmProjects/PV_data_process/venv/TU-Gab   best days/PV_database.txt', 'r+') as csv_2:
        csv_3 = csv_2.read().replace('\n', '')
        otherStr = csv_3.replace('0; 09;', '\n ')

    with open('/home/ht/PycharmProjects/PV_data_process/venv/TU-Gab   '
              'best days/.ipynb_checkpoints/new_data.csv', 'w') as replaced_data:
        replaced_data.write(otherStr)

    with open('/home/ht/PycharmProjects/PV_data_process/venv/TU-Gab   best days/'
              '.ipynb_checkpoints/new_data.csv', 'r') as database:
        string_data = database.read()
        list_data = string_data.split('; ')
        start_point = 2
        list_data2 = list_data.copy()

        for n, i in enumerate(list_data2):
            try:
                number_element = float(i)
                if number_element < 0:
                    list_data2[n] = 0
            except:
                for particle in i:
                    if particle == '-':
                        list_data2[n] = 0

                pass
        listToStr = ' '.join(map(str, list_data2))

        with open('/home/ht/PycharmProjects/PV_data_process/venv/TU-Gab   best days/'
                  '.ipynb_checkpoints/data_no_negative.csv', 'w') as database5:
            database5.write(listToStr)
