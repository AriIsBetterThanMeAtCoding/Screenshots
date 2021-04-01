x = input()
temp = ""
for r in range(int (x)):

    num = int(input())

    code = input()
    
    temp = ""

    for i in range(num):

        if (code[i]=='G'):

            temp+='C'

        elif (code[i]=='A'):

            temp+='T'

        elif (code[i]=='T'):

            temp+='A'

        elif (code[i]=='C'):

            temp+='G'

        elif (code[i]=='U'):

            print('Error RNA nucleobases found!')

            break
    else:
        print(temp)
