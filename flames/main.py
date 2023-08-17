from flames import Flames
import os
name_1 = input("Enter your name: ")
name_2 = input("Enter your Lover name: ")
o = Flames(name_1,name_2)
o.remove_letters()
o.flames_process()
os.system("clear")
if o.flames[0] == "f":
    print(f"{name_2} is friend with you. ")
elif o.flames[0] == "l":
    print(f"{name_2} is love with you. ")
    
elif o.flames[0] == 'a':
    print(f"{name_2} is attract with you. ")
    
elif o.flames[0] == "m":
    print(f"{name_2} is marriage with you. ")
    
elif o.flames[0] =="e":
    print(f"{name_2} is enemy with you. ")
    
elif o.flames[0] == "s":
    print(f"{name_2} is sister with you. ")
    