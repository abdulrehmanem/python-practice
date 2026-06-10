# variable
var1 = "   variable one   "
var2 = "variable second"

var3 = var1 +" "+ var2  # variable one variable second

var4 = f"variable four contains : {var1} , {var2}"   # variable four contains : variable one , variable second

#print(var4)

#----------------------------------------------------
var5 = var1.split()   # ['variable', 'one']

var6 = var1.strip()  #variable one

#print(var1.rstrip())   #    variable one
#print(var1.lstrip())   # variable one  

var7 = 237 + 537
var8 = 500 - 343

var_first = var7
var_second = var8

#print(f"here two variables 1 : {var_first} ,2 : {var_second}") 
print(f"multiple ... {var_first * var_second}")
print(f"divided ... {var_second / var_first}")