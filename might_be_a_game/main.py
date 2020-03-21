from world import AmazingWorld
import constants as c

def print_guys():
    print('-----------------')
    print("Hey, now there are {} guys".format(len(aw.guys)))
    print("Hey, there were {} interactions".format(aw.interaction_counter))
    print("Hey, there were {} love encounters".format(aw.love_counter))
    s = ""
    for i in range(c.map_x):
        for j in range(c.map_y):
            s += str(len(aw.map[i][j])) + "|"
        s +='\n'
        s += '-----------\n'
    print(s)
    print('-----------------')

    # print('========================================')
    # for id_ in aw.guys:
    #     print(aw.guys[id_])
    #     print('---------------')
    # print('========================================')



aw = AmazingWorld()
aw.setup_game()
print_guys()
input()
i = 1
while i:
    if (not i%100): 
        input()
    print("STEP "+str(i))
    aw.step()
    print_guys()
    if (len(aw.guys)) == 0:
        exit()
    i+=1
