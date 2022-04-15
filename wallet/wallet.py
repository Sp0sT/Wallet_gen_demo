#!/usr/bin/python3





print("""   
    
    
    
    
 __          __     _      _      ______ _______    _____ ______ _   _ 
 \ \        / /\   | |    | |    |  ____|__   __|  / ____|  ____| \ | |
  \ \  /\  / /  \  | |    | |    | |__     | |    | |  __| |__  |  \| |
   \ \/  \/ / /\ \ | |    | |    |  __|    | |    | | |_ |  __| | . ` |
    \  /\  / ____ \| |____| |____| |____   | |    | |__| | |____| |\  |
     \/  \/_/    \_\______|______|______|  |_|     \_____|______|_| \_|
                                                                       
                                                                       
    

    
    
    
                                                                                        """)

def main():
    n = input("1-Wallet adress gen\n2- Gen 12 Word Exodus\n\nSelect option : ")
    if n == 1:
        wallet()
    elif n == 2:
        word_gen()



def word_gen():

    print("1______________________________________________________________________________")

    f = open('word.txt', 'r')
    n = f.read(85)
    f.close
    print(n)
    if n == 12:
        print("success")


    print("2______________________________________________________________________________")

    i = open('word2.txt', 'r')
    p = f.read(75)
    f.close
    print(n)
    if n == 12:
        print("success")

    print("3______________________________________________________________________________")

    f = open('word3.txt', 'r')
    n = f.read(69)
    f.close
    print(n)

word_gen()

def wallet():
    print("wait\n...\n...\n...\n...\n...\n...\n...\n...")
    f = open('walletadress.txt', 'r')
    PublicKey = f.read()
    f.close
    print(PublicKey)
    if PublicKey == 1:
        print("The signature is NOT valid!")
    else:
        print("The signature is valid!")

wallet()



if __name__ == '__main__':
    main()

















def wallet():
    f = open('walletadress.txt', 'r')
    PublicKey = f.read()
    f.close
    print(PublicKey)
    if PublicKey == 1:
        print("The signature is NOT valid!")
    elif PublicKey == 0:
        print("The signature is valid!")
    


if __name__ == "__main__":
    main()