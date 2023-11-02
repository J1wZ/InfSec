'''
    ГОСТ 28/47-89
    Работа Пирожковой А.Д. ИТ-41
'''

import binascii
import codecs
matrix = (
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9),
    (5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11),
    (7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3),
    (6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2),
    (4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14),
    (13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12),
    (1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12),
)

'''
    Превращает псевдо-биты(строчка) в символы
'''
def MakeText(Res):
    cup = int(Res,2)
    if cup % 2 !=0:
        cup = '0' + str(cup)
    CodeText = binascii.unhexlify('%x' % int(cup))
    return CodeText.decode('cp1251')

'''
    Превращает лист в псевдо-биты(строчка)
'''
def MakeBitStr(chunks):
    cup = ''
    for el in chunks:
        binEl = bin(el)[2:]
        while len(binEl)<4:
            binEl = '0' + binEl
        cup+=binEl
    return cup

'''
    По формуле определяет, какой из элиментов матрицы вставить в список
'''
def MatrixFun(chunks):
    i = 0
    while i < 8:
        c = int(chunks[i],2)
        chunks[i] = matrix[7-i][c]
        i+=1
    return chunks

'''
    Вычисляет номер исследуемого подключа
'''
def FindNumSubKey(i,flag):
    if flag:
        if i < 25:
            return (i-1) % 8
        else:
            return (32 - i) % 8
    else:
        if i <=8:
            return (i-1) % 8
        else:
            return (32 - i) % 8

'''
    Разбивает строчку на части размером n
'''
def MakeSubChunks(st,n):
    return [st[i:i+n] for i in range(0, len(st), n)]

'''
    Циклический сдвиг влево
'''
def LeftShift(n, s, N):  
    return ((n << s) % (1 << N)) | (n >> (N - s))

'''
    Шифрование
'''
def Gost(Text,key):
    
    Res = ''
    bitText=''
    bitKey =''
    for i in Text.encode('cp1251'):
        bitText +=bin(i)[2:]
    for i in key.encode('cp1251'):
        bitKey += bin(i)[2:]
    subText = MakeSubChunks(bitText,64)
    subKey = MakeSubChunks(bitKey,32)
    for T in subText:
        #Запоминаем кол-во добавленных битов, чтобы потом убрать лишние
        NumOfAddedBits = 0
        while len(T) < 64:
            T = '0' + T
            NumOfAddedBits += 1
        left = T[:32]
        right = T[32:]
        i = 1
        while i != 33:
            V = right
            j = FindNumSubKey(i,True)
            right = bin(int(right+subKey[j],2) % pow(2,32))[2:]
            chunksF = MakeSubChunks(right,4)
            chunksF = MatrixFun(chunksF)
            right = MakeBitStr(chunksF)
            right = bin(LeftShift(int(right,2),11,32))[2:]
            
            right = bin(int(right,2)^int(left,2))[2:]
            left = V
            while len(right)<32:
                right = '0'+ right
            while len(left)<32:
                left = '0'+ left
            i +=1
        PartRes = left + right
        if NumOfAddedBits !=0:
            if NumOfAddedBits == 64:
                PartRes = ''
            else:
                PartRes = PartRes[NumOfAddedBits:]
        Res = Res + PartRes
    return Res



'''
    Дешифрование
'''
def DeGost(Text,key):
    Res = ''
    bitText=''
    bitKey =''
    for i in Text.encode('cp1251'):
        binRes = bin(i)[2:]
        while len(binRes) < 8:
            binRes = '0' + binRes
        bitText += binRes
    for i in key.encode('cp1251'):
        bitKey += bin(i)[2:]
    subText = MakeSubChunks(bitText,64)
    subKey = MakeSubChunks(bitKey,32)
    for T in subText:
        #Запоминаем кол-во добавленных битов, чтобы потом убрать лишние
        NumOfAddedBits = 0
        while len(T) < 64:
            T = '0' + T
            NumOfAddedBits += 1
        left = T[:32]
        right = T[32:]
        i = 1
        while i != 33:
            V = left
            j = FindNumSubKey(i,False)
            left = bin(int(left+subKey[j],2) % pow(2,32))[2:]
            chunksF = MakeSubChunks(left,4)
            chunksF = MatrixFun(chunksF)
            left = MakeBitStr(chunksF)
            left = bin(LeftShift(int(left,2),11,32))[2:]
            left = bin(int(left,2)^int(right,2))[2:]
            right = V
            while len(right)<32:
                right = '0'+ right
            while len(left)<32:
                left = '0'+ left
            i +=1
        PartRes = left + right
        if NumOfAddedBits !=0:
            if NumOfAddedBits == 64:
                PartRes = ''
            else:
                PartRes = PartRes[NumOfAddedBits:]
        Res = Res + PartRes
    return Res

Text = input('Введите текст:\n', )
CodeText = ''
#Один символ соот. 8 битам => 256 бит = 32 символа
key = input('Введите ключ(32 символа):\n', )
if (len(key) != 32):
    print('Длина ключа должна быть 32 символа!')
else:
    CodeText = Gost(Text,key)
    print('Кодирование:')
    print(CodeText)
    DecodeText = MakeText(CodeText)
    print(DecodeText)
    print('Декодирование:')
    DecodeText = DeGost(DecodeText,key)
    print(DecodeText)
    print(MakeText(DecodeText))


