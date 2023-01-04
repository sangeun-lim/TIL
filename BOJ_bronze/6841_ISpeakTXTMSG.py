dic = {
"CU":"see you",
":-)":"I’m happy",
":-(":"I’m unhappy",
";-)":"wink",
":-P":"stick out my tongue",
"(~.~)":"sleepy",
"TA":"totally awesome",
"CCC":"Canadian Computing Competition",
"CUZ":"because",
"TY":"thank-you",
"YW":"you’re welcome",
"TTYL":"talk to you later"}

while True:
    x = input()
    if x == 'TTYL':
        print(dic[x])
        break
    elif x in dic:
        print(dic[x])
    else:
        print(x)