#!/usr/bin/env python3


def get_ones_value(num,ones_dic):
    print("{}".format("Ones"))
    return ones_dic[num].capitalize()              

def get_tens_value(num,dic_one,dic_two,posOne,posTwo):
    print("{}".format("Tens"))
    # get the first index value for key values in the dictionary. eg: for num = 20; key: 20, value: twenty; ....
    if num in dic_two:
        return dic_two[num][0].capitalize()
    else:
    # get second index value for key values not in dictionary. Range: 11-19. 
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


def get_hundreds_value(num,onesDic,tensDic,hundredsDic,posOne,posTwo):
    print("{}".format("Hundreds"))
    if num in hundredsDic:
        prefix = onesDic[posOne]
        return f"{prefix} " + hundredsDic[num].capitalize()
    else:
        number = posOne * 100
        if posTwo < 10:
            if number == 100:
                num_in_words = hundredsDic[number]
            else:
                num_in_words = hundredsDic[100]
                if posTwo == 0:
                    prefix = onesDic[posOne]
                    num_in_words = prefix + f" {num_in_words}"
                    return num_in_words.capitalize()
            prefix = onesDic[posOne]
            num_in_words = prefix + f" {num_in_words} and " + onesDic[posTwo]
        elif posTwo > 9:
            num_in_words = hundredsDic[100]
            prefix = onesDic[posOne]
            p1 = get_ones(posTwo, 10)
            p2 = get_tens(posTwo, 10)
            get_tens_digit = get_tens_value(posTwo,onesDic,tensDic,p1,p2)
            num_in_words = prefix + f" {num_in_words} and " + get_tens_digit 
    return num_in_words.capitalize()

def number_to_word(num):
    ones_dic = {
        0:"zero",
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
        90:["ninety","nineteen"]       
    }
    hundreds_dic = {
        100:"hundred"
    }
    if num < 100:
        ones_position = get_ones(num, 10)
        tens_position = get_tens(num,10)
        if ones_position == 0 and tens_position == num: # returns tens digits spelt words.
            ones_value = get_ones_value(num,ones_dic)
            print(f"{num} is spelt as {ones_value}")
        elif ones_position > 0 and tens_position < num: # returns tens digits spelt words.
                tens_value = get_tens_value(num,ones_dic,tens_dic, ones_position,tens_position)
                print(f"{num} is spelt as {tens_value}")
    else: 
        ones_position = get_ones(num, 100)
        tens_position = get_tens(num,100)
        if ones_position <1000:
            hundreds_value = get_hundreds_value(num,ones_dic,tens_dic,hundreds_dic,ones_position,tens_position)
            print(f"{num} is spelt as {hundreds_value}")

def get_ones(val,denom):
    ones = val/denom
    return int(ones)

def get_tens(num, denom):
    rem = num%denom
    return int(rem)

numb = int(input("Plse Enter a number: "))
while numb != -1:
    number_to_word(numb)
    numb = int(input("Plse Enter a number: "))
print("Thank You!")
print("Goodbye!!")