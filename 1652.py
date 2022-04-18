#1652
#누울 자리를 찾아라

n = int(input("n: "))
room = []

#room만들기
for _ in range(n) :
    room.append(list(input()))

seat_h = 0
seat_v = 0

for i in range(n) :
    sum_h , sum_v = 0, 0
    for j in range(n) :
        if room[i][j] == '.' :
            sum_h += 1
        elif room[i][j] == 'X' :
            if sum_h >= 2 :
                seat_h += 1
            sum_h = 0
    
        if room[j][i] == '.' :
            sum_v += 1
        elif room[j][i] == 'X' :
            if sum_v >= 2 :
                seat_v += 1
            sum_v = 0

print(seat_h, seat_v)