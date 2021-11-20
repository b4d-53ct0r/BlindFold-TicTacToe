def is_free(x,y,Board):
    if Board[x][y] == "X" or Board[x][y] == "O" :
        print("[!] wrong move.")
        return False
    return True
def Check_Win(Board):
    win = [            
            [       
                        [0,0],[0,1],[0,2]       
                    ],[       
                        [1,0],[1,1],[1,2]       
                    ],[
                        [2,0],[2,1],[2,2]
                    ],[
                        [0,0],[1,0],[2,0]
                    ],[
                        [0,1],[1,1],[2,1]
                    ],[
                        [0,2],[1,2],[2,2]
                    ],[
                        [0,0],[1,1],[2,2]
                    ],[
                        [2,0],[1,1],[0,2]
                ]
            ]
    for check in win:
        if Board[check[0][0]][check[0][1]] == Board[check[1][0]][check[1][1]] == Board[check[2][0]][check[2][1]]:
            return True
    return False

    
def main():
    location = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
    }
    Board = [
             ["1","2","3"],
             ["6","5","4"],
             ["7","8","9"]
    ]
    F = 0
    C = 0
    while True:
        if C == 9:
            print("[+] DRAW")
            break
        if F == 0:
            while True:
                M = list()
                while M==[]:
                    try:
                        M = list(input('[*] player 1 : '))
                        if is_free(int(M[1])-1,location[M[0]],Board):
                            break
                    except:
                        M=list()
                
            C += 1
            Board[int(M[1])-1][location[M[0]]] = "X" 
            F = 1
            if(Check_Win(Board)):
                print("[+] the winner is player 1")
                break
        else :
            while True:
                M = list()
                while M==[]:
                    try:
                        M = list(input('[*] player 2 : '))
                        if is_free(int(M[1])-1,location[M[0]],Board):
                            break
                    except:
                        M=list()
                        
                
            C += 1
            Board[int(M[1])-1][location[M[0]]] = "O"
            F = 0
            if(Check_Win(Board)):
                print("[+] the winner is player 2")
                break
if __name__ == "__main__":
    main()
