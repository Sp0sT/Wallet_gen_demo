#!/usr/bin/python3


import bitcoin
from bitcoinutils.setup import setup
from bitcoinutils.keys import P2pkhAddress, PrivateKey, PublicKey



print("""   
    
    
    
    
 __          __     _      _      ______ _______    _____ ______ _   _ 
 \ \        / /\   | |    | |    |  ____|__   __|  / ____|  ____| \ | |
  \ \  /\  / /  \  | |    | |    | |__     | |    | |  __| |__  |  \| |
   \ \/  \/ / /\ \ | |    | |    |  __|    | |    | | |_ |  __| | . ` |
    \  /\  / ____ \| |____| |____| |____   | |    | |__| | |____| |\  |
     \/  \/_/    \_\______|______|______|  |_|     \_____|______|_| \_|
                                                                       
                                                                       
    

    
    
    
                                                                                        """)



print("wait\n...\n...\n...\n...\n...\n...\n...\n...")
f = open('walletadress.txt', 'r')
PublicKey = f.read()
f.close
print(PublicKey)
if PublicKey == 1:
    print("The signature is NOT valid!")
else:
    print("The signature is valid!")
    