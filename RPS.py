import sys, random

wins = 0
loss = 0
ties = 0

while True:
    while True:
        print('%s wins, %s losses, %s ties' % (wins, loss, ties))
        print("enter (r)ock, (p)aper, (s)cissor or (q)uit")
        play = input()
        if play == 'r' or play == 'p' or play == 's':
            break
        elif play == 'q':
            sys.exit()
        else:
            print("type p, q, r or s")


    if play == 'p':
        play = 'paper'
    if play == 'r':
        play = 'rock'
    if play == 's':
        play = 'scissor'



    x = random.randint(1,3)
    if x == 1:
        bot = 'paper'
    elif x == 2:
        bot = 'scissor'
    else:
        bot = 'rock'

    if bot == play:
        print("bob(the bot) played " + bot + " too!!")
        ties = ties + 1
        print("draw!!")



    if bot == 'paper' and play == 'rock':
        print("bob(the bot) played " + bot)
        loss = loss + 1
        print("you loose :(")
    if bot == 'rock' and play == 'scissor':
        print("bob(the bot) played " + bot)
        print("you loose :(")
        loss = loss + 1
    if bot == 'scissors' and play == 'paper':
        print("bob(the bot) played " + bot)
        loss = loss + 1
        print("you loose :(")



    if bot == 'rock' and play == 'paper':
        print("bob(the bot) played " + bot)
        print('you win!!')
        wins = wins + 1
    if bot == 'scissor' and play == 'rock':
        print("bob(the bot) played " + bot)
        print('you win!!')
        wins = wins + 1
    if bot == 'paper' and play == 'scissor':
        print("bob(the bot) played " + bot)
        print('you win!!')
        wins = wins + 1





