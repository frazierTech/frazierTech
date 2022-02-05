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

    print('1:Deg, 2:Num, 3:Dom')
    XLoc = input('> ')

    #sin
    if int(mode) == 1:
        if int(XLoc) == 1:
            print('opp?')
            num1 = int(input('> '))
            print('hyp?')
            num2 = int(input('> '))

            x = math.degrees(math.asin( (num1/num2) ) )

            print('sin(x)=opp/hyp')
            print('x=sin^-1(opp/hyp)')
            print('x='+str(x))


        elif int(XLoc) == 2:
            print('A?')
            num1 = int(input('> '))
            print('hyp?')
            num2 = int(input('> '))

            x = num2*math.sin( math.radians(num1) )

            print('sin(A)=X/hyp')
            print('x=sin(A)*hyp')
            print('x='+str(x))


        elif int(XLoc) == 3:
            print('A?')
            num1 = int(input('> '))
            print('opp?')
            num2 = int(input('> '))

            x = num2/math.sin( math.radians(num1) )

            print('sin(A)=opp/x')
            print('x*sin(A)=opp')
            print('x=opp/sin(A)')
            print('x='+str(x))
        #

    #cos
    elif int(mode) == 2:
        if int(XLoc) == 1:
            print('opp?')
            num1 = int(input('> '))
            print('hyp?')
            num2 = int(input('> '))

            x = math.degrees(math.acos( (num1/num2) ) )

            print('cos(x)=opp/hyp')
            print('x=cos^-1(opp/hyp)')
            print('x='+str(x))


        elif int(XLoc) == 2:
            print('A?')
            num1 = int(input('> '))
            print('hyp?')
            num2 = int(input('> '))

            x = num2*math.cos( math.radians(num1) )

            print('cos(A)=X/hyp')
            print('x=cos(A)*hyp')
            print('x='+str(x))


        elif int(XLoc) == 3:
            print('A?')
            num1 = int(input('> '))
            print('adj?')
            num2 = int(input('> '))

            x = num2/math.cos( math.radians(num1) )

            print('cos(a)=adj/x')
            print('x*cos(a)=adj')
            print('x=adj/cos(a)')
            print('x='+str(x))
        #

    #tan
    elif int(mode) == 3:
        if int(XLoc) == 1:
            print('opp?')
            num1 = int(input('> '))
            print('adj?')
            num2 = int(input('> '))

            x = math.degrees(math.atan( (num1/num2) ) )

            print('tan(x)=opp/adj')
            print('x=tan^-1(opp/adj)')
            print('x='+str(x))


        elif int(XLoc) == 2:
            print('A?')
            num1 = int(input('> '))
            print('adj?')
            num2 = int(input('> '))

            x = num2*math.tan( math.radians(num1) )

            print('tan(A)=X/adj')
            print('x=tan(A)*adj')
            print('x='+str(x))


        elif int(XLoc) == 3:
            print('A?')
            num1 = int(input('> '))
            print('opp')
            num2 = int(input('> '))

            x = num2/math.tan( math.radians(num1) )

            print('tan(a)=opp/x')
            print('x*tan(a)=opp')
            print('x=opp/tan(a)')
            print('x='+str(x))
        #
    #
#
