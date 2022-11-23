from random import shuffle

def shuffle_list():
    my_list = ['⎡⎤','o','⎡⎤']
    shuffle(my_list)
    return my_list

def player_guess():
    guess = ''
    print("Choose your cup -> ", end='')
    while guess not in [1,2,3]:
        guess = int(input("⎡1⎤ ⎡2⎤ ⎡3⎤ : "))
    return guess

def check_guess():
    mix_list = shuffle_list()
    guess = player_guess()
    if mix_list[guess-1] == 'o':
        res = "   ".join(mix_list)
        print("\n", res, "\tYay!\n")
        return True
    else:
        res = "   ".join(mix_list)
        print("\n", res, "\tOops!\n")
        return False

res = False
while not res:
    res = check_guess()