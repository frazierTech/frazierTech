import math

while True:
    #var
    p = input('p: ')
    r = input('r: ')
    t = input('t: ')
    n = input('n: ')

    #cal
    if n == "e" or n == "c":
        print('A = '+str(p)+'e^'+str(r)+'*'+str(t))
        print(int(p)*pow(math.e, float(r)*int(t)) )# A = Pe^RT
        print('\n')
        
        
    elif n == "exit":
        break #escape
    else:
        try:
            print('A = '+str(p)+'(1+ '+str(r)+'/'+str(n)+')^'+str(n)+'*'+str(t))
            print(int(p) * pow( 1+ float(r)/int(n), (int(t) * int(n)) ))# A = P(1+ R/N)^NT
            print('\n')
        except ValueError:
            print('Invaid Input:\nEnter and int number for n. \n\"e\" for Euler\'s number.\n\"Exit\" to leave')
            print('\n')
    

    
