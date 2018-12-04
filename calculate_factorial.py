def findFak():
    try:
        girdi=int(input("Enter a number to calculate thefatorial = "))
        fak=1
        for i in range(1,girdi+1):
            fak=fak*i
        print(fak)
    except:
        print("Invalid job")
    
    
findFak()
