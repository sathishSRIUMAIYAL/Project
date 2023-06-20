
inp=(input("well come to our SRI UMAIYAL hotel\nwould you like to order('yes or no'): "))
if 'yes'==inp:
    D={1:'veg',2:'non-veg'}
    print(D)
    inp1=int(input())
    if 1==inp1:
        D1={1:'Dhosa',2:'itly'}
        print(D1)
        inp2=int(input())
        if 1 == inp2:
            D2 = {1: 'masaldhosa', 2: 'oniondhosa'}
            print(D2)
            inp3 = int(input())
            if 1==inp3:
                print('do you like eat', D2[1], 'with vada (yes or no)')
                inp4 = (input())
                if 'yes' == inp4:
                    print('YOUR ORDER IS READY\nDHOSA=30\nVADA=10\nGST=0.5\nTOTAL AMOUNT=40.5')
                elif 'no' == inp4:
                    print('YOUR ORDER IS READY\nDHOSA=30\nGST=0.5\nTOTAL AMOUNT=30.5')
                else:
                    print('enter the right value')
            else:
                print('enter the right value')


            if 2 == inp3:
                print('do you like eat', D2[2], 'with vada (yes or no)')
                inp5 = (input())
                if 'yes' == inp5:
                    print('YOUR ORDER IS READY\nDHOSA=40\nVADA=10\nGST=0.5\nTOTAL AMOUNT=50.5')
                elif 'no' == inp5:
                    print('YOUR ORDER IS READY\nDHOSA=30\nGST=0.5\nTOTAL AMOUNT=30.5')
                else:
                    print('enter the right value')


            else:
                print('enter the right value')

        if 2 == inp2:
            D3 = {1: 'Ravaitly', 2: 'kushpuidly'}
            print(D3)
            inp6 = int(input())
            if 1 == inp6:
                print('YOUR ORDER IS READY\nRAVADHOSA=40\nGST=0.5\nTOTAL AMOUNT=40.5')
            elif 2 == inp6:
                print('YOUR ORDER IS READY\nKUSHPUITLY=20\nGST=0.5\nTOTAL AMOUNT=20.5')
            else:
                print('enter the right value')


        else:
            print('enter the right value')
    if 2==inp1:
        d={1:'chicken biryani',2:'mutton biryani'}
        print(d)
        IN=int(input())
        if 1==IN:
            print('do you like eat', d[1], 'with chicken 65(yes or no)')
            IN1=input()
            if IN1=='yes':
                print('YOUR ORDER IS READY\nCHICKEN BIRYANI=120\nCHICKEN 65=40\nGST=0.5\nTOTAL AMOUNT=160.5')
            elif IN1=='no':
                print('YOUR ORDER IS READY\nCHICKEN BIRYANI=120\nGST=0.5\nTOTAL AMOUNT=120.5')
            else:
                print('enter the ritht value')
        if 2==IN:
            print('do you like eat', d[2], 'with chicken 65(yes or no)')
            IN2=(input())
            if IN2=='yes':
                print('YOUR ORDER IS READY\nMUTTON BIRYANI=220\nCHICKEN 65=40\nGST=0.5\nTOTAL AMOUNT=260.5')
            elif IN2=='no':
                print('YOUR ORDER IS READY\nMUTTON BIRYANI=220\nGST=0.5\nTOTAL AMOUNT=220.5')
            else:
                print('enter the right value')

    else:
        print('enter the right value')



elif 'no'==inp:
    print('ok we will meet next time')

else:
    print('enter the right value')



