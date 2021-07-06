# for i in range(1,28): # First Model
#     print("Fizz"*(i%3<1)+"Buzz"*(i%5<1) or i)

# for i in range(1,28):  # second model
#     output=''
#     if i%3==0:output= "Fizz"
#     if i%5==0:output+="Buzz"
#     print(output or i)

for i in range(1,28):    # Third model
    out=''
    out = "Fizz" if i%3 else ""
    out += "Buzz" if i%5 else ""
    print(i if out=="" else out)