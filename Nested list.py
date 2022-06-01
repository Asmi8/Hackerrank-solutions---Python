if __name__ == '__main__':
    score_list = []
    mark_sheet = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    mark_sheet.append([name,score])
    score_list.append(score)


second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]

for name,marks in sorted(mark_sheet):
    if marks == second_lowest_mark:
        print(name)
     
        
    
