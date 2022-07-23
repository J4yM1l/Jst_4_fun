#!/usr/bin/env python3


def get_ones_value(num,ones_dic):
    print("{}".format("Ones"))
    return ones_dic[num].capitalize()              

def get_tens_value(num,dic_one,dic_two,posOne,posTwo):
    print("{}".format("Tens"))
    # use cases numbers: 11, 21
    # get the first index value for key values in the dictionary. eg: for num = 20; key: 20, value: twenty; ....
    if num in dic_two:
        # print("{} is spelt as {}".format(num,dic_one[num].capitalize()
        return dic_two[num][0].capitalize()
    else:
    # get second index value for key values not dictionary. Range: 11-19. 
    # eg: for key: 11, Value: eleven
        number = posOne * 10
        if posOne <= 1 and posTwo >= 1:
            number = posTwo * 10           
            num_in_words = dic_two[number][1]
        else:
        # get second index value for key values not dictionary. Range: 21-99. 
            num_in_words = dic_two[number][0]
            num_in_words = f"{num_in_words} " + dic_one[posTwo]
        return num_in_words.capitalize()


def get_hundreds_value(num,onesDic,tensDic,hundredsDic,firstPos,secondPos):
    print("{}".format("Hundreds"))
    val = ""
    if num in hundredsDic:
        # print("{} is spelt as {} {}".format(num, onesDic[1][0].capitalize(),hundredsDic[num]))
        # elif number_grp
        return hundredsDic[num]
    else:
        if firstPos > 10 and firstPos < 20:            
            # ones_position = get_ones(firstPos)          
            # indexPos = get_ones(firstPos) # 110:11 -> 11/10=1 
            rem = num%100#get_tens(num)
            # tens = indexPos * 10 + rem
            indexPos_one = get_ones(firstPos)
            indexPos_two = get_tens(rem)
            val = get_ones_value(rem,onesDic,indexPos_one,indexPos_two)
        else:
             rem = num%100
             indexPos_one = get_tens(firstPos)
             val = get_tens_value(rem,onesDic,tensDic,indexPos_one,secondPos)
            # number = firstPos * 10
            # if number > 100:                
        num_in_words = hundredsDic[100]
        num_in_words = onesDic[1][0] + f" {num_in_words} and " + val            
        # print("{} is spelt as {}".format(num,num_in_words.capitalize()))
        return num_in_words.capitalize()

def number_to_word(num):
    ones_dic = {
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"
    }
    tens_dic = {
        10:["ten","eleven"],      
        20:["twenty","twelve"],
        30:["thirty","thirteen"],
        40:["fourty","fourteen"],
        50:["fifty","fifteen"],
        60:["sixty","sixteen"],
        70:["seventy","seventeen"],
        80:["eighty","eighteen"],
        90:["ninety","nineteen"],       
    }
    hundreds_dic = {
        100:"hundred"
    }
    ones_position = get_ones(num)
    tens_position = get_tens(num)
    if ones_position == 0 and tens_position == num:
        ones_value = get_ones_value(num,ones_dic)
        print(f"{num} is spelt as {ones_value}")
    elif ones_position > 0 and tens_position < num:
            tens_value = get_tens_value(num,ones_dic,tens_dic, ones_position,tens_position)
            print(f"{num} is spelt as {tens_value}")
    elif ones_position > 9 and ones_position <100:
        hundreds_value = get_hundreds_value(num,ones_dic,tens_dic,hundreds_dic,ones_position,tens_position)
        print(f"{num} is spelt as {hundreds_value}")

def get_ones(val):
    ones = val/10
    # print("remender {}".format(rem))
    # print("division found index {}".format(int(ones)))
    return int(ones)

def get_tens(num):
    rem = num%10
    # print(f"remender found val is {rem}")
    return int(rem)

# def get_hundreds(num):
#     rem = num/100
#     print(f"remender found val is {rem}")
#     return int(rem)

numb = int(input("Plse Enter a number: "))
while numb != 0:
    number_to_word(numb)
    numb = int(input("Plse Enter a number: "))
print("Thank You!")
print("Goodbye!!")



'''

1: one -> 1/10=0.1, 1%10=1
11: eleven -> 11/10=1.1, 11%10=1
12: twelve -> 12/10=1.2, 12%10=2
13: thirteen
14: fourteen
15: fiftteen
16: sixteen
20: twenty -> 20/10=2, 20%10=0

21: twenty one -> 21/10=2.1, 21%10=1
'''
