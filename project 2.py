print('   ')
R1=int(input('Hi welcome to 1\nwhere you want to watch movie?\n1.Mylapore\n2.Tambaram\n3.Koyambedu\nchoose your option: '))
print('  ')
def mylapore():
    print('1.PVP\n2.IMAX\n3.ICON')
    movie()
def tambaram():
    print('1.PVP\n2.IMAX\n3.ICON')
    movie()
def koyambedu():
    print('1.PVP\n2.IMAX\n3.ICON')
    movie()
def movie():
    R2=int(input('choose tour option:'))
    if R2==1:
        movie1()
    elif R2==2:
        movie1()
    elif R2==3:
        movie1()
    else:
        print('wrong choose')
def movie1():
    print('   ')
    print('1.Ponniyin Selvan\n2.RRR\n3.KGF\n4.Hridayam')
    R3=int(input('which movie would you like to watch\nchoose your option:'))

    if R3 == 1:
        screen()
    elif R3 == 2:
        screen()
    elif R3 == 3:
        screen()
    elif R3 == 4:
        screen()
    else:
        print('wrong choose')

def screen():
    print('   ')
    print('1.screen1\n2.screen2\n3.screen3')
    R4 = int(input('which screen would you like to watch\nchoose your option:'))

    if R4==1:
        ticket()
    elif R4==2:
        ticket()
    elif R4==3:
        ticket()
    else:
        print('wrong choose')


def ticket ():
    print('   ')
    R5=int(input('How many ticket you want'))
    T=0
    while T<R5:
        T+=1
        amount=T*150
    timing()
    print(f'NUMBER OF TICKETS={R5}\nTOTAL AMOUNT={amount}')



def timing():
    print('   ')
    D={1:'10.00AM -01.00PM',2:'02.00PM -04.00PM',3:'05.00PM-08.00PM',4:'09.00PM-12.00AM'}
    print(D)
    R6 = int(input('which time would you like to watch'))
    print('   ')
    print('YOUR BOOKING IS REDY\nMOVIE TIMING',{D[R6]})

if R1==1:
    mylapore()
elif R1==2:
    tambaram()
elif R1==3:
    koyambedu()
else:
    print('wrong choose')






