import string 

password=input("Enter your password : ")
print("---------------------------------")
upper_case=[]
lower_case=[]
digits=[]
special=[]
for c in password:
    if c in string.ascii_uppercase:
        upper_case.append(1)
    else:
        upper_case.append(0)

for c in password:
    if c in string.ascii_lowercase:
        lower_case.append(1)
    else:
        lower_case.append(0)

for c in password:
    if c in string.punctuation:
       special.append(1)
    else:
        special.append(0)

for c in password:
    if c in string.digits:
       digits.append(1)
    else:
       digits.append(0)
with open('common.txt','r') as f:
    common=f.read().splitlines()    
def True_values(List):
    number=0
    for i in List:
        if i==1:
            number+=1
    return number

characters=[upper_case,lower_case,special,digits]
score=0


if password in common:
    print("Password was found in a list of common passwords : Score:0/9")
    exit()
def digit_points(digits):
    score=0
    if  True_values(digits)==0:
      print("0 points for no digit")
    elif True_values(digits)==1:
        print("2 points for exactly one digit")
        score+=2
    elif  (True_values(digits)>1 and True_values(digits)<4):
        print("1 point for more than one digits")
        score+=1
    else:
        print("0 points for exceeding the allowed number of digits")
    return score
def special_points(special):
    score=0
    if True_values(special)==0:
        print("0 points for no special character")

    elif True_values(special)==1 :
        print("2 points for exactly one special character")
        score+=2
    elif (True_values(special)>1 and True_values(special)<4) :
        print("1 point for more than one special characters")
        score+=1
    else:
        print("0 points for exceeding the allowed number of special characters")
    return score
def Lower_points(lower):
    score=0
    trues=True_values(lower)
    if trues>0 and trues<=8:
        score+=2
        print("2 points for the allowed number of Lower case characters")
    else:
        if trues>8:
            print("0 points for exceeding the allowed number of Lower case character")
        else:
            print("0 points for no Lower case character")
    return score
def Upper_points(upper):
    score=0
    trues=True_values(upper)
    if trues>0 and trues<=2:
        score+=2
        print("2 points for the allowed number of Upper case characters")
    else:
        if trues>2:
            print("0 points for the exceeding allowed number of Upper case characters")
        else:
            print("0 points for no Upper case character")
    return score

if len(password)>=8 and len(password)<=16:
    print("1 point for at least 8 characters")
    score+=1
    score+=special_points(special)
    score+=digit_points(digits)
    score+=Lower_points(lower_case)
    score+=Upper_points(upper_case)
else:
    print("0 pointS for less than 8 characters")
print("---------------------------------")
print(f"Score : {str(score)}/9 ")
