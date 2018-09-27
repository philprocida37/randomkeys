import random
import pyautogui
import decimal

charList = [1,2,3,4,5,6,7,8,9,0,
       'q','w','e','r','t',
       'y','u','i','o','p',
       'a','s','d','f','g',
       'h','j','k','l','z',
       'x','c','v','b','n',
       'm','!','@','#','$',
       '%','^','&','*','(',
       ')','-','=','+','[',
       ']','{','}','|','<',
       '>',',','?','_','.']

try:

    while 1==1:

        rndChar = str(random.choice(charList))
        
        randInterval = float(decimal.Decimal(random.randrange(1, 2))/100000)

        pyautogui.typewrite(rndChar, randInterval)

except KeyboardInterrupt:

    pass
