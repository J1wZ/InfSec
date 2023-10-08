'''
    Шифр одноалфавитной замены 
    Работа Пирожковой А.Д. ИТ-41
'''



'''Русский алфавит'''
ABCru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

'''Английский алфавит'''
ABCen = "abcdefghijklmnopqrstuvwxyz"



'''
    Функция по кодированию сообщения на русском и английском языках
'''
def Encode(key, Text):
    CodeText =''
    for Elm in Text:
        numElm = ABCru.find(Elm.lower())
        if numElm != -1:
            TempKey = numElm + key
            if TempKey >= 32:
                TempKey -= 33
            if Elm == Elm.upper():
                CodeText += ABCru[TempKey ].upper()
            else:
                CodeText += ABCru[TempKey ]
        else:
            numElm = ABCen.find(Elm.lower())
            if numElm != -1:
                TempKey = numElm + key
                while TempKey >= 25:
                    TempKey -= 26
                if Elm == Elm.upper():
                    CodeText += ABCen[TempKey ].upper()
                else:
                    CodeText += ABCen[TempKey ]
            else:
                CodeText += Elm
    print(CodeText)
    return CodeText


'''
    Функция по декодированию сообщения на русском и английском языках
'''
def Decode(key, CodeText):
    Text = ''
    for Elm in CodeText:
        numElm = ABCru.find(Elm.lower())
        if numElm != -1:
            TempKey = numElm - key
            if TempKey < 0:
                TempKey += 33
            if Elm == Elm.upper():
                Text += ABCru[TempKey ].upper()
            else:
                Text += ABCru[TempKey ]
        else:
            numElm = ABCen.find(Elm.lower())
            if numElm != -1:
                TempKey = numElm - key
                while TempKey < 0:
                    TempKey += 26
                if Elm == Elm.upper():
                    Text += ABCen[TempKey ].upper()
                else:
                    Text += ABCen[TempKey ]
            else:
                Text += Elm
    print(Text)
    

Text = input('Введите текст:\n', )
CodeText = ''

import random
key = random.randint(0,32)
print(f'Рандомный ключ: {key}')


''' 
    кодирование
'''
print('Закодированный текст:')
CodeText = Encode(key, Text)


'''
    декодирование
'''
print('Декодированный текст:')
Decode(key,CodeText)


'''
    Взлом Закодированного сообщения
    
    Ищется самая часто встречаемая буква и находится смешение до одной из наиболее 
    часто используемой буквы в алфавите
'''

'''
    Русский
'''
count = [0]*33
i = -1
for ElmABC in ABCru:
    i +=1
    for ElmCode in CodeText:
        if ElmABC == ElmCode.lower():
            count[i] +=1
if max(count) != 0:
    '''
        О - 1-я по частоте буква русского алфавита
        ABCru[15] = о
    '''
    maxElm = count.index(max(count))
    
    if maxElm <= 15:
        key = 33 - (15 - maxElm)
    else:
        key = maxElm - 15
    print(f'Найденный ключ: {key}')
    print('Первая версия(RU):')
    Decode(key, CodeText)
    
    '''
        Е(Ё) - 2-я по частоте буква русского алфавита
        ABCru[5] = е 
    '''
    if maxElm <= 5:
        key = 33 - (5 - maxElm)
    else:
        key = maxElm - 5
    print(f'Найденный ключ: {key}')
    print('Вторая версия(RU):')
    Decode(key, CodeText)
    
    '''
        А - 3-я по частоте буква русского алфавита
        ABCru[0] = а
    '''
    if maxElm <= 0:
        key = 33 + maxElm
    else:
        key = maxElm
    print(f'Найденный ключ: {key}')
    print('Третья версия(RU):')
    Decode(key, CodeText)


'''
    Английский
'''

count = [0]*26
i = -1
for ElmABC in ABCen:
    i +=1
    for ElmCode in CodeText:
        if ElmABC == ElmCode.lower():
            count[i] +=1

if max(count) != 0:
    maxElm = count.index(max(count))
    '''
        E - 1-я по частоте буква латинского алфавита
        ABCen[4] = e
    '''
    if maxElm <= 4:
        key = 26 - (4 - maxElm)
    else:
        key = maxElm - 4
    print(f'Найденный ключ: {key}')
    print('Первая версия(EN):')
    Decode(key, CodeText)
    
    '''
        А - 3-я по частоте буква латинского алфавита
        ABCru[0] = a
    '''
    if maxElm <=0:
        key = 26 + maxElm
    else:
        key = maxElm
    print(f'Найденный ключ: {key}')
    print('Вторая версия(EN):')
    Decode(key, CodeText)
    
    '''
        T - 2-я по частоте буква латинского алфавита
        ABCru[19] = t
    '''
    if maxElm <= 19:
        key = 26 -(19 - maxElm)
    else:
        key = maxElm - 19
    print(f'Найденный ключ: {key}')
    print('Третья версия(EN):')
    Decode(key, CodeText)
    
    '''
        O - 4-я по частоте буква латинского алфавита
        ABCru[14] = o
    '''
    if maxElm <= 14:
        key = 26 -(14 - maxElm)
    else:
