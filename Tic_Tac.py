def print_(l,msg):
    import os
    os.system("cls")
    print(f"{msg:^75}")
    print("\n\n\nYour Current Board is : ")
    s =f"""
                               -------------------------
                               |       |       |       |
                               |   {l[0]}   |   {l[1]}   |   {l[2]}   |
                               |       |       |       |
                               -------------------------
                               |       |       |       |
                               |   {l[3]}   |   {l[4]}   |   {l[5]}   |
                               |       |       |       |
                               -------------------------
                               |       |       |       |
                               |   {l[6]}   |   {l[7]}   |   {l[8]}   |
                               |       |       |       |
                               -------------------------"""
    print(s)


    
def __main__():
    import os
    from itertools import permutations
    l = [1,2,3,4,5,6,7,8,9]
    l1 = [1,2,3,4,5,6,7,8,9]
    A,B=[],[]
    win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    
    msg = "Here are the Positions to select your move."
    print_(l,msg)
    input("\n\n\n\nPress Enter to Continue ... \n")
    l = [" " for var in range(9)]
    print_(l,"After inital move the board is -> ")
    name_1 = input("Enter Player one name : ")
    name_2 = input("\n\nEnter Player two name : ")
    os.system("cls")
    print(f"Symbols --> X and 0\n\nChoosing the symbol for each Player.\n\n{name_1} Symbol is - 0\n\n{name_2} Symbol is - X")
    input("\n\n\n\nPress Enter to Start the Game\n")
    print_(l,"Initial status of board")
    print("\nLeft Positions -> ",end = "")
    print(*l1)
    j=1
    while j<=len(l):
        if l1:
            while True:
                print()
                n1 = int(input(f"{name_1} : "))-1        
                if n1+1 in list(range(1,10)):
                    if n1 not in A and n1 not in B:
                        l.pop(n1)
                        l.insert(n1,"x")
                        print_(l,f"\n\n\nAfter move {j} the board is")
                        j+=1
                        l1.remove(n1+1)
                        print("\n\nLeft Positions -> ",end = "")
                        print(*l1)


                        A.append(n1)
                        x = list(permutations(A,3))
                        for i in range(len(win)):
                            if win[i] in x:
                                print(f"\n\n{name_1} has won the game".center(75))
                                exit(1)
                                break
                        break

                    else:
                        print("\nInvalid Input!")
                        continue
                else:
                    print("\nInvalid Input!")
                    continue
            else:
                print("\nInvalid Input!")
                continue
        else:
            print("\nMatch is Tie")
            break
            
        if l1:
            while True:
                print()
                n2 = int(input(f"{name_2} : "))-1
                if n2+1 in list(range(1,10)):
                    if n2 not in B and n2 not in A:
                        l.pop(n2)
                        l.insert(n2,"0")
                        print_(l,f"\n\n\nAfter move {j} the board is")
                        j+=1
                        l1.remove(n2+1)
                        print("\n\nLeft Positions -> ",end = "")
                        print(*l1)
                        B.append(n2)
                        y = list(permutations(B,3))
                        for i in range(len(win)):
                            if win[i] in y:
                                print(f"\n\n{name_2} has won the game".center(75))
                                exit(1)
                                break
                        break
                    else:
                        print("\nInvalid Input!")
                        continue
                else:
                    print("\nInvalid Input!")
                    continue
            else:
                print("\nInvalid Input!")
                continue
        else:
            print("\nMatch is Tie")
            break
    
__main__()
