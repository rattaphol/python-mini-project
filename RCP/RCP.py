import random

game_cnt = 0
npc_win_cnt = 0
player_win_cnt = 0

def rcp(NPC, player):
    global game_cnt
    global npc_win_cnt
    global player_win_cnt
    npc_win = 0
    # print(NPC)
    # print(player)

    if NPC == "Rock" and player == "Scissor":
        npc_win = 1
    elif NPC == "Scissor" and player == "Paper":
        npc_win = 1
    elif NPC == "Paper" and player == "Rock":
        npc_win = 1
    elif NPC == "Rock" and player == "Paper":
        npc_win = 0
    elif NPC == "Scissor" and player == "Rock":
        npc_win = 0
    elif NPC == "Paper" and player == "Scissor":
        npc_win = 0
    else:
        npc_win = 2 #draw
    
    if npc_win == 1:
        print("You lose NPC [" + NPC + "] and you choose [" + player + "]\n")
        npc_win_cnt = npc_win_cnt + 1
    elif npc_win == 0:
        print("You win NPC [" + NPC + "] and you choose [" + player + "]\n")
        player_win_cnt = player_win_cnt + 1
    else:
        print("Draw game NPC [" + NPC + "] and you choose [" + player + "]\n")

# main
print("\nHello and Welcome to Rock, Scissor, Paper game!!\n")
while 1:
    NPC= random.choice(["Rock","Scissor","Paper"])
    #NPC="Rock"
    while 1:
        player = input("\nWhat is your choice [R]ock, [S]cissor, [P]aper :")
        if player.lower() == "r":
            player = "Rock"
            break
        elif player.lower() == "s":
            player = "Scissor"
            break
        elif player.lower() == "p":
            player = "Paper"
            break
        else:
            print("Wrong choice try again please")

    game_cnt+=1
    rcp(NPC, player)
    play_again = input("Do you want to continue (y/n)?")
    if play_again.lower() == "n":
        break

print("Summary total game:" + str(game_cnt) + "\nYou win " + str(player_win_cnt) + " and NPC win " + str(npc_win_cnt))
print("\nThank you please come again!!\n")
