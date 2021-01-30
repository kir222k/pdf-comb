import copy
# a1='srt'
# a2='srt-2'
# a3='srt.3'
# b1='vrt'
# b2='vrt-2'
# b3='vrt.3'
# list_files=[a1, a2, a3, b1, b2, b3]
# print('\nFile list: ', list_files)

def list_files_x (list_files):
    #  словать, где элементы - списки имен файлов, имеющих один корень
    # print('!! list_files_x RUN')
    # lst_s=[] # список без рассм. элемента
    lst_x=[] # список для добавления в список списков
    lst_y=[] # список списков
    # f_dict={}
    for it in list_files: # по списку файлов
        # возьмем 1 эл. списка и сравним с остальными - если корень совпадает,
        # добавим в список, кот. затем б. эл. словаря
        lst_s = list_files.copy()
        lst_s.remove(it)
        # print('\nlist_files_x=file: ', it)
        # print('list: ', lst_s)
        lst_x.clear()
        for sf in lst_s: # по урезанному списку
            #
            if it in sf: # если корни файлов совпадают
                # f_dict_i={it: lst_s}
                # print(sf)
                lst_x.append(sf)
        if len(lst_x) > 0:
            lst_x.insert(0, it)
            # print(lst_x)
            lst_y.append(lst_x.copy())
    return lst_y
