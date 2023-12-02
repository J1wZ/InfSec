import random
from decimal import Decimal
import codecs
import binascii

#массив нескольких первых простых чисел
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]
 

def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)
 
 
def getLowLevelPrime(n):
    while True:
        pc = nBitRandom(n)

        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else:
            return pc
 
 
def isMillerRabinPassed(mrc):
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
 
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
 
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True
 

def MakeText(cup):
    if int(cup) % 2 !=0:
        cup = '0' + str(cup)
    CodeText = binascii.unhexlify('%x' % int(cup))
    return CodeText.decode('cp1251')

def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
    gcd,x1,y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x,y


def NODEvk(a,b):
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a != 0:
        return a
    else:
        return b
    


def PrimeNum(num):
    i = 2
    while i*i <= num and num%i != 0:
        i += 1
    return (i*i > num)

      

def GenP(n,p):
    res = getLowLevelPrime(n)
    while not isMillerRabinPassed(res) and p !=res:
        res = getLowLevelPrime(n)
    return res


Text = input('Введите текст:\n', )
CodeText = ''
q = GenP(1024,0)
print('Сгенерированая р = ' + str(p))
q = GenP(258,p)   
print('Сгенерированая q = ' + str(q))
n = p * q
print('Получившаяся n = ' + str(n))
FunEyl = (p-1)*(q-1)
print('Получившаяся Функция Эйлера = ' + str(FunEyl))
e = random.randint(2,FunEyl-1)
NodE = NODEvk(e,FunEyl)
while NodE != 1:
    e = random.randint(2,FunEyl-1)
    NodE = NODEvk(e,FunEyl)
print('Получившаяся e = ' + str(e))

gcd, x, y = gcdExtended(e, FunEyl)
if gcd == 1:
    d = Decimal((x % FunEyl + FunEyl) % FunEyl)
else:
    d = -1

print('Получившийся d = ' + str(d))
bitText= list(Text)
ii = 0
for i in Text.encode('cp1251'):
        bitText[ii] = str(i)
        ii = ii + 1
print(bitText)

print('Шифровка:')
ii = 0
for i in bitText:
    bitText[ii] = str(pow(int(i),e, mod = n))
    ii = ii + 1
print(bitText)

print('Дешифровка:')
ii = 0
for i in bitText:
    bitText[ii] = str(pow(int(i),int(d), mod =n))
    CodeText += MakeText(bitText[ii])
    ii = ii + 1
print(bitText)
print(CodeText)
