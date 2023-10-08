'''
    Квадрат Виженера 
    Работа Пирожковой А.Д. ИТ-41
'''


'''Русский алфавит'''
ABCru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

'''Английский алфавит'''
ABCen = "abcdefghijklmnopqrstuvwxyz"


'''
    Функция по кодированию сообщения на русском языке
'''
def EncodeRU(key, Text):
    table = []
    for i in range(33):
        row = ABCru[i:] + ABCru[:i]
        table.append(row)
    
    key = key.lower()
    i =-1
    CodeText = ''
    for Elm in Text:
        
        numElm = ABCru.find(Elm.lower())
        if numElm != -1:
            i+=1
            TempKey = i
            while TempKey >= len(key):
                TempKey -= len(key)
            row = ABCru.index(key[TempKey])
            if Elm == Elm.upper():
                CodeText += table[row][numElm].upper()
            else:
                CodeText += table[row][numElm]
        else:
            CodeText += Elm

    return CodeText

'''
    Функция по кодированию сообщения на английском языке
'''

def EncodeEN(key, Text):
    table = []
    for i in range(26):
        row = ABCen[i:] + ABCen[:i]
        table.append(row)
    
    key = key.lower()
    i = -1
    CodeText = ''
    for Elm in Text:
        
        numElm = ABCen.find(Elm.lower())
        if numElm != -1:
            i+=1
            TempKey = i
            while TempKey >= len(key):
                TempKey -= len(key)
            row = ABCen.index(key[TempKey])
            if Elm == Elm.upper():
                CodeText += table[row][numElm].upper()
            else:
                CodeText += table[row][numElm]
        else:
            CodeText += Elm
    return CodeText


'''
    Функция по декодированию сообщения на русском языке
'''
def DecodeRU(key, CodeText):
    table = []
    for i in range(33):
        row = ABCru[i:] + ABCru[:i]
        table.append(row)
 
    key = key.lower()
    Text = ''
    i=-1
    for Elm in CodeText:
        
        numElm = ABCru.find(Elm.lower())
        if numElm!=-1:
            i+=1
            TempKey = i
            while TempKey >= len(key):
                TempKey -= len(key)
            row = ABCru.index(key[TempKey])
            col = table[row].index(Elm.lower())
            if Elm == Elm.upper():
                Text += ABCru[col].upper()
            else:
                Text += ABCru[col]
        else:
            Text += Elm
    return Text


'''
    Функция по декодированию сообщения на английском языке
'''
def DecodeEN(key, CodeText):
    table = []
    for i in range(26):
        row = ABCen[i:] + ABCen[:i]
        table.append(row)
    
    key = key.lower()
    Text = ''
    i=-1
    for Elm in CodeText:
        
        numElm = ABCen.find(Elm.lower())
        if numElm!=-1:
            i+=1
            TempKey = i
            while TempKey >= len(key):
                TempKey -= len(key)
            row = ABCen.index(key[TempKey])
            col = table[row].index(Elm.lower())
            if Elm == Elm.upper():
                Text += ABCen[col].upper()
            else:
                Text += ABCen[col]
        else:
            Text += Elm
    return Text


Text = input('Введите текст:\n', )
CodeText = ''

key = input('Введите ключ:\n', )

lang = int(input('1 - Русский, 2 - Английский\n',))


''' 
    кодирование
'''
print('Закодированный текст:')
if lang == 1:
    CodeText = EncodeRU(key, Text)
else:
    if lang == 2:
        CodeText = EncodeEN(key, Text)
    else:
        print('Можно вводить только 1 или 2\n')
print(CodeText)

'''
    декодирование
'''
print('Декодированный текст:')
if lang == 1:
    Text = DecodeRU(key, CodeText)
else:
    if lang == 2:
        Text = DecodeEN(key, CodeText)
    else:
        Text=''
print(Text)



