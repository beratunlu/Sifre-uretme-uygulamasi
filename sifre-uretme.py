import random 
    

import string 


  


def pass_uzunlugu(size): 
        
 
    
    generate_pass = "".join(random.choice( string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)   
    for n in range(size)) 
                            
    return generate_pass 




    
# Driver Code 
size = int(input("Lutfen olmasını istediginiz sifre uzunlugunu belirtiniz: ")) 
password = pass_uzunlugu(size)

print(password) 
