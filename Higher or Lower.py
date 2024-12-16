from data import data
import random
def compare(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

list_length=len(data)
dict1_index=random.randint(0,list_length-1)

game_over=False
score=0
dict2_repeat=-1
while not game_over:
    while True:
        dict2_index=random.randint(0,list_length-1)
        if dict2_index!=dict1_index and dict2_index!=dict2_repeat:
            dict2_repeat=dict2_index
            break

    print(f"Compare A : {data[dict1_index]['name']}, {data[dict1_index]['occupation']}, from {data[dict1_index]['country']}")
    print('V/S')
    print(f"Compare B : {data[dict2_index]['name']}, {data[dict2_index]['occupation']}, from {data[dict2_index]['country']}")
    comparison=compare(data[dict1_index]['followers'],data[dict2_index]['followers'])
    user_input=input("Who has more insta followers? Type 'A' or 'B' : ").lower()
    print("\n"*20)
    if user_input=='a':
        if data[dict1_index]['followers']==comparison:
            score+=1
            print(f"You're Right! Current Score: {score}\n")
            #dict1_index=dict2_index
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over=True
    elif user_input=='b':
        if data[dict2_index]['followers']==comparison:
            score+=1
            print(f"You're Right! Current Score: {score}\n")
            dict1_index=dict2_index
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over=True 
    else:
        print("Wrong Input")
        break

