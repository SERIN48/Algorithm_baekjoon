#2621
#카드게임

import random

card_color=[]
card_number={}


#card= random.choice(card_color) + str(random.choice(card_number))
print("chosen card")
for i in range(5) :
    color = random.choice(card_color)
    number = random.choice(card_number)
    card = [color,number]
    
    #list_card.append(card)
#print(list_card)



for _ in range(5) :
    color, num = input().split()
    card_color.append(color)
    
        