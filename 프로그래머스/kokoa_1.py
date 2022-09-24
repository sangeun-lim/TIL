def solution(today, terms, privacies):
    answer = []

    privacy = []
    for i in range(len(privacies)):
        for j in range(len(terms)):
            if privacies[i][11] == terms[j][0]:
                if int(privacies[i][5:7])+int(terms[j][1:]) < 10 :
                    privacy.append(str(privacies[i][:5])+'0'+ (str(int(privacies[i][5:7])+int(terms[j][1:])) + str(privacies[i][7:])))
                else:
                    privacy.append(str(privacies[i][:5]) + (str(int(privacies[i][5:7]) + int(terms[j][1:])) + str(privacies[i][7:])))

    privacy2 = []

    for i in range(len(privacy)):
        # 월이 100이 안 넘어가면
        if '.' in privacy[i][5:8]:
            if int(privacy[i][5:7]) <= 12:
                privacy2.append(privacy[i])

            elif int(privacy[i][5:7]) <= 24:
                if int(privacy[i][5:7])-12 < 10 :
                    privacy2.append(str(int(privacy[i][:4])+1) +'.0' + str(int(privacy[i][5:7])-12) + str(privacy[i][7:]))
                else:
                    privacy2.append(str(int(privacy[i][:4])+1) +'.' + str(int(privacy[i][5:7])-12) + str(privacy[i][7:]))

            elif int(privacy[i][5:7]) <= 36:
                if int(privacy[i][5:7]) - 24 < 10:
                    privacy2.append(str(int(privacy[i][:4]) + 2) + '.0' + str(int(privacy[i][5:7]) - 24) + str(privacy[i][7:]))
                else:
                    privacy2.append(str(int(privacy[i][:4]) + 2) +'.' +str(int(privacy[i][5:7]) - 24) + str(privacy[i][7:]))

            elif int(privacy[i][5:7]) <= 48:
                if int(privacy[i][5:7]) - 36 < 10:
                    privacy2.append(str(int(privacy[i][:4]) + 3) + '.0' + str(int(privacy[i][5:7]) - 36) + str(privacy[i][7:]))
                else:
                    privacy2.append(str(int(privacy[i][:4]) + 3) +'.' +str(int(privacy[i][5:7]) - 36) + str(privacy[i][7:]))

            elif int(privacy[i][5:7]) <= 60:
                if int(privacy[i][5:7]) - 48 < 10:
                    privacy2.append(str(int(privacy[i][:4]) + 4) + '.0' + str(int(privacy[i][5:7]) - 48) + str(privacy[i][7:]))
                else:
                    privacy2.append(str(int(privacy[i][:4]) + 4) +'.' +str(int(privacy[i][5:7]) - 48) + str(privacy[i][7:]))

            elif int(privacy[i][5:7]) <= 72:
                if int(privacy[i][5:7]) - 60 < 10:
                    privacy2.append(str(int(privacy[i][:4]) + 5) + '.0' + str(int(privacy[i][5:7]) - 60) + str(privacy[i][7:]))
                else:
                    privacy2.append(str(int(privacy[i][:4]) + 5) +'.' +str(int(privacy[i][5:7]) - 60) + str(privacy[i][7:]))

            elif int(privacy[i][5:7]) <= 84:
                if int(privacy[i][5:7]) - 72 < 10:
                    privacy2.append(str(int(privacy[i][:4]) + 6) + '.0' + str(int(privacy[i][5:7]) - 72) + str(privacy[i][7:]))
                else:
                    privacy2.append(str(int(privacy[i][:4]) + 6) +'.' +str(int(privacy[i][5:7]) - 72) + str(privacy[i][7:]))

            elif int(privacy[i][5:7]) <= 96:
                if int(privacy[i][5:7]) - 84 < 10:
                    privacy2.append(str(int(privacy[i][:4]) + 7) + '.0' + str(int(privacy[i][5:7]) - 84) + str(privacy[i][7:]))
                else:
                    privacy2.append(str(int(privacy[i][:4]) + 7) +'.' +str(int(privacy[i][5:7]) - 84) + str(privacy[i][7:]))

            else:
                privacy2.append(str(int(privacy[i][:4]) + 8) + '.0' + str(int(privacy[i][5:7]) - 96) + str(privacy[i][7:]))
        # 월이 100이 넘어가면
        else:
            if int(privacy[i][5:8]) <= 108:
                if int(privacy[i][5:8]) - 96 < 10:
                    privacy2.append(str(int(privacy[i][:4]) + 8) + '.0' + str(int(privacy[i][5:8]) - 96) + str(privacy[i][8:]))
                else:
                    privacy2.append(str(int(privacy[i][:4]) + 8) +'.' +str(int(privacy[i][5:8]) - 96) + str(privacy[i][8:]))
            else:
                privacy2.append(str(int(privacy[i][:4]) + 9) + '.0' + str(int(privacy[i][5:8]) - 108) + str(privacy[i][8:]))


    for i in range(len(privacy2)):
        if int(privacy2[i][:4]) < int(today[:4]):
            answer.append(i+1)
        elif (int(privacy2[i][:4]) == int(today[:4])) and (int(privacy2[i][5:7]) < int(today[5:7])):
            answer.append(i+1)
        elif (int(privacy2[i][:4]) == int(today[:4])) and (int(privacy2[i][5:7]) == int(today[5:7])) and (int(privacy2[i][8:10]) <= int(today[8:10])):
            answer.append(i+1)

    return answer
