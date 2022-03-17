N = int(input())

dp = [False for i in range(1001)] # 1<= N <= 1000

dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5,N+1):

    # if not (dp[i-1] and dp[i-3] and dp[i-4]) : # not False 면 dp[i] = True  , dp[i]= True 면 SK 승
    #     dp[i] = True
    # else :                                     # dp[i] = False 면 CY 승
    #     dp[i] = False

    if dp[i-1] and dp[i-3] and dp[i-4] :
        dp[i] = False
    else :
        dp[i] = True

if dp[N]: # True 이면
    print('SK')
else :
    print('CY')

###################
# n = int(input())
#
# if(n%7 == 0 or n%7 == 2):
#     print("CY")
# else:
#     print("SK")
