""" Python version 3.6.3 """
from random import randint
import os
import time
import timeit

def mix_search(list_db,num_search,list_index):
    tic = timeit.default_timer()
    end , begin = sequencial_search(num_search,list_index)
    toc = timeit.default_timer()
    print("| Time sequencial_search in index_list: {} |".format(toc-tic))
    print("---------------------------------------------------------------")
    print("| Sub set list_db end: {} begin: {}              |".format(end,begin))
    print("-------------------------------------------------")
    if not(end or begin):
        return -1
    tic = timeit.default_timer()
    number = search_binary(list_db , num_search, begin, end)
    toc = timeit.default_timer()
    print("| Time search_binary: {}     |".format(toc-tic))
    print("-------------------------------------------------")
    return number

def insertion_sort(list_db = []):
    for current_item in range(0,len(list_db)):

        next_item = current_item

        while next_item != 0 and list_db[next_item] < list_db[next_item -1]:
            aux = list_db[next_item]
            list_db[next_item] = list_db[next_item - 1]
            list_db[next_item - 1] = aux
            next_item-=1

def index_list(list_db = []):
    index = [index-1 for index in range(0,len(list_db),30)]
    #print(index)
    index.append(len(list_db)-1)
    index[0]+=1
    #print(index)
    list_values = []
    for code in index:
        #print(code)
        list_values.append([list_db[code],code])
    #print(list_values)
    return list_values

def sequencial_search(num_search,list_num):
    count = 0
    for item in list_num:
        if item[0] >= num_search:
            if item[1] == 0:
                return 9,0
            return item[1] , list_num[count-1][1]
        count+=1
    return -1,-1

def search_binary(list_db,number,begin,end):
    while begin <= end :
        find = int((begin + end) / 2)
        if list_db[find] == number:
            return find;
        if list_db[find] < number:
            begin = find + 1
        else:
            end = find - 1
    return -1

def insert_list(ans_1,list_db):
    list_db.append(ans_1)

def choise(answer,list_db,list_index):
    if answer == 0:
        print("Good bye!!")

    if answer == 1:
        print("Sorted list :\n {}".format(list_db))
    #################################################
    if answer == 2:
        flag=False
        print("Write a number of your choise!\n")
        ans_1 = int(input())
        tic = timeit.default_timer()
        for each in list_db:
            if each == ans_1:
                flag=True
                print("Found: {}".format(each))
                break;
        toc = timeit.default_timer()
        print("Time: {}".format(toc-tic))
        if not flag:
            print("Don't find anything\n")
    ###############################################
    if answer == 3:
        print("Write a number of your choise!\n")
        ans_1 = int(input())
        tic = timeit.default_timer()

        ans_2 = mix_search(list_db,ans_1,list_index)

        toc = timeit.default_timer()
        if ans_2 != -1:
            print("Found: {} in time: {}".format(list_db[ans_2],toc-tic))

        else:
            print("Don't find anything\n")
    ##############################################
    if answer == 4:
        print("What number you want to insert: ")
        ans_1 = int(input())
        insert_list(ans_1,list_db)
        insertion_sort(list_db)
        list_index = index_list(list_db)
    ##############################################
    if answer == 5:
        print("Write a number of your choise!\n")
        ans_1 = int(input())
        tic = timeit.default_timer()
        ans_2 = mix_search(list_db,ans_1,list_index)
        toc = timeit.default_timer()
        if ans_2 != -1:
            print("Delete: {} in time: {}".format(list_db[ans_2],toc-tic))
            list_db.pop(ans_2)
            insertion_sort(list_db)
        else:
            print("Don't find anything\n")




if __name__ == "__main__":
    list_db=[]
    list_index=[]
    print("Write the len, you want, of your list:")
    max_len=int(input())
    path = os.path.dirname(os.path.abspath(__file__))
    for count in range(0,max_len):
        list_db.append(randint(0,99999))
    insertion_sort(list_db)
    list_index = index_list(list_db)
    answer = 10
    while answer > 0:
        print("Choose one of choises bellow:\n1-Print order list.\n2-sequencial search.\n3-Mix search\n4-Insert item\n5-Delete item\n0-Getout here.")
        answer = int(input())
        choise(answer,list_db,list_index)
        list_index = index_list(list_db)
        print("Press enter to continue!!!")
        try:
            input()
        except:
            print("You are in python2 please press enter again !!!")
            raw_input()
        os.system("clear")
