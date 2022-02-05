#2022/1/31 Bryce W. Frazier
import math

#modes
mode = 0
xLoc = 0

#input/output
num1 = 0
num2 = 0
x = 0

while True:
    print('1: sin SOH')
    print('2: cos CAH')
    print('3: tan TOA')
    mode = input('> ')

    print('1:Deg, 2:Opp, 3:Hyp')
    XLoc = input('> ')

    #sin
    if int(mode) == 1:
        if int(XLoc) == 1:
            print('O?')
            num1 = int(input('> '))
            print('H?')
            num2 = int(input('> '))

            x = (math.asin( (num1/num2) )) * 180/math.pi

            print('sin(x)=O/H')
            print('x=sin^-1(O/H)')
            print('x='+str(x))


        elif int(XLoc) == 2:
            print('A?')
            num1 = int(input('> '))
            print('H?')
            num2 = int(input('> '))

            x = num2 * ((math.sin(num1)) * 180/math.pi)

            print('sin(A)=X/H')
            print('x=sin(A)*H')
            print('x='+str(x))


        elif int(XLoc) == 3:
            print('A?')
            num1 = int(input('> '))
            print('O?')
            num2 = int(input('> '))

            x = num2/ ((math.sin(num1)) * 180/math.pi)

            print('sin(A)=O/x')
            print('x*sin(A)=O')
            print('x=O/sin(A)')
            print('x='+str(x))
        #

    #cos
    elif int(mode) == 2:
        if int(XLoc) == 1:
            print('O?')
            num1 = int(input('> '))
            print('adj?')
            num2 = int(input('> '))

            x = (math.acos( (num1/num2) )) * 180/math.pi

            print('cos(x)=O/adj')
            print('x=cos^-1(O/adj)')
            print('x='+str(x))


        elif int(XLoc) == 2:
            print('A?')
            num1 = int(input('> '))
            print('adj?')
            num2 = int(input('> '))

            x = num2 * ((math.cos(num1)) * 180/math.pi)

            print('cos(A)=X/adj')
            print('x=cos(A)*adj')
            print('x='+str(x))


        elif int(XLoc) == 3:
            print('A?')
            num1 = int(input('> '))
            print('O?')
            num2 = int(input('> '))

            x = num2/ ((math.cos(num1)) * 180/math.pi)

            print('cos(a)=O/x')
            print('x*cos(a)=O')
            print('x=O/cos(a)')
            print('x='+str(x))
        #

    #tan
    elif int(mode) == 3:
        if int(XLoc) == 1:
            print('adj?')
            num1 = int(input('> '))
            print('H?')
            num2 = int(input('> '))

            x = (math.atan( (num1/num2) )) * 180/math.pi

            print('tan(x)=adj/H')
            print('x=tan^-1(adj/H)')
            print('x='+str(x))


        elif int(XLoc) == 2:
            print('A?')
            num1 = int(input('> '))
            print('adj?')
            num2 = int(input('> '))

            x = num2 * ((math.tan(num1)) * 180/math.pi)

            print('tan(A)=X/adj')
            print('x=tan(A)*adj')
            print('x='+str(x))


        elif int(XLoc) == 3:
            print('A?')
            num1 = int(input('> '))
            print('O')
            num2 = int(input('> '))

            x = num2/ ((math.tan(num1)) * 180/math.pi)

            print('tan(a)=O/x')
            print('x*tan(a)=O')
            print('x=O/tan(a)')
            print('x='+str(x))
        #
    #
#
