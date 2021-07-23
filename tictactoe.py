import random

def ans_x():
    ans_x_1=['x','x','x']
    if list[0]==ans_x_1 or list[1]==ans_x_1 or list[2]==ans_x_1:
        return False
    if ((list[0][0]=='x' and list[1][0]=='x' and list[2][0]=='x') or (list[0][1]=='x' and list[1][1]=='x' and list[2][1]=='x') or (list[0][2]=='x' and list[1][2]=='x' and list[2][2]=='x')):
        return False
    if (((list[0][0]=='x' and list[1][1]=='x' and list[2][2]=='x') or (list[0][2]=='x' and list[1][1]=='x' and list[2][0]=='x'))):
        return False
    return True

def ans_o():
    ans_o_1=['o','o','o']
    if list[0]==ans_o_1 or list[1]==ans_o_1 or list[2]==ans_o_1:
        return False
    if ((list[0][0]=='o' and list[1][0]=='o' and list[2][0]=='o') or (list[0][1]=='o' and list[1][1]=='o' and list[2][1]=='o') or (list[0][2]=='o' and list[1][2]=='o' and list[2][2]=='o')):
        return False
    if (((list[0][0]=='o' and list[1][1]=='o' and list[2][2]=='o') or (list[0][2]=='o' and list[1][1]=='o' and list[2][0]=='o'))):
        return False
    return True

def isNotFull():
    for i in range(3):
        for j in range(3):
            if(list[i][j]=='b'):
                return True
    return False
     
list = [['b', 'b', 'b'],
        ['b', 'b', 'b'],
        ['b', 'b', 'b']]
print(list)
print('\n')

while(True):
    i = input("Do you want to play tictactoe: Y/N ? ")
    print('\n')

    a=1
    if(i=="n" or i=="N"):
        break
    elif(i=="y" or i=="Y"):
        A = input("Enter Player 1 ")
        print('\n')
        B = input("Enter Player 2 ")
        print('\n')
        p = random.randint(1, 2)
        # print(p)
        if(p==1):
            print(f"It's {A}'s turn first")
            print('\n')
            while ans_x() and ans_o() and isNotFull():
                print('\n')
                print(list)
                # print(ans_x(), " ",ans_o())
                print('\n')
                while True:
                    n = int(input("Enter your position "))
                    if(n%3==0):
                        x=(n//3)-1
                        y=2
                    else:
                        x=n//3 
                        y=(n%3)-1
                    if(list[x][y]=='b'):
                        if(a):
                            a=0
                            list[x][y]='x'
                        else:
                            a=1
                            list[x][y]='o'
                        break
            if(ans_x() and ans_o()):
                print(('\n'))
                print("It's a tie!")
                print(list)
                print('\n')
            else:
                if(ans_x()==False):
                    print(('\n'))
                    print(f"{A} wins!")
                    print(list)
                    print('\n')
                elif(ans_o()==False):
                    print(('\n'))
                    print(f"{B} wins!")
                    print(list)
                    print('\n')

        else:
            print(f"It's {B}'s turn first")
            print('\n')
            while ans_x() and ans_o() and isNotFull():
                print('\n')
                print(list)
                # print(ans_x(), " ",ans_o())
                print('\n')
                while True:
                    n = int(input("Enter your position "))
                    if(n%3==0):
                        x=(n//3)-1
                        y=2
                    else:
                        x=n//3 
                        y=(n%3)-1
                    if(list[x][y]=='b'):
                        if(a):
                            a=0
                            list[x][y]='x'
                        else:
                            a=1
                            list[x][y]='o'
                        break
            if(ans_x() and ans_o()):
                print('\n')
                print("It's a tie!")
                print(list)
                print('\n')
            else:
                if(ans_x()==False):
                    print('\n')
                    print(f"{B} wins!")
                    print(list)
                    print('\n')
                elif(ans_o()==False):
                    print('\n')
                    print(f"{A} wins!")
                    print(list)
                    print('\n')

    else:
        print("Wrong input")


