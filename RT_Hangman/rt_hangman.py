import random
from re import I

turn = 10
q_display = ""
guess_list = ""
complete_word = ""

question_word = random.choice(["Ferrari","Volvo","Toyota","Mazda","Tesla","Honda","Nissan","Chevrolet","BMW"])

# print(question_word)

def make_q_display():
  global q_display
  global guess_list
  q_display = ""
  for i, in_chr in enumerate(question_word.lower()):
    if in_chr in guess_list:
        q_display = q_display + question_word[i] + " "
    else:
        q_display = q_display + "_"  + " "
  print("Question word is : " + q_display)

def update_complete_word():
  global complete_word
  global guess_list
  complete_word = ""
  for i, in_chr in enumerate(question_word.lower()):
    if in_chr in guess_list:
        complete_word = complete_word + question_word[i]
  # print("Complete word is : " + complete_word)

# Main
print("Hello and welcome to hangman game!!\nPlease guess one character at a time you have 10 turn to win the game!\n")
make_q_display()


while 1:
    get_char = input("Guess a character please:")
    get_char = get_char.lower()

    # print("[DEBUG] Your input: " + get_char + "\n")

    # update guess list
    if get_char not in guess_list:
        guess_list = guess_list + get_char
        if get_char not in question_word.lower():
            turn = turn - 1
    
    print("Used character list :" + guess_list + "\n")
    
    update_complete_word()

    if complete_word == question_word:
        print("You Win!! the answer is [" + question_word + "] Congratulation!!\n")
        break

    if turn <= 0:
        print("Sorry you lose!!\n Come again next time\n")
        break

    make_q_display()
    print("No of turn left [" + str(turn) + "]\n")
    

    
