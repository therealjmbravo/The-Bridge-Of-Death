import random

print('Stop! Who would cross the Bridge of Death must answer me these questions three, \'ere the other side he see.') 

input('What is your name? ')

input('What is your quest? ')

rand_int = random.randint(0,3) #(Inclusive)

if rand_int == 1:
    colorls = ['green', 'blue', 'yellow', 'red', 'orange', 'magenta', 'white', 'black', 'maroon', 'violet', 'gray', 'brown']
    color = input('What is your favorite color? ')
    if color in colorls:
        print('Right. Off you go.')
    else:
        print('*casts you into the abyss* Heh heh heh...')
elif rand_int == 2:
    capls = ['Ashur', 'Nimrud', 'Dur Sarukin', 'Nineveh']
    cap_of_assyria = input('What is the capitol of Assyria? ')
    if cap_of_assyria in capls:
        print('Right. Off you go.')
    else:
        print('*casts you into the abyss* Heh heh heh...')
else:
    swallow = input('What is the airspeed velocity of an unladen swallow?(in mph) ')
    if '23' < swallow < '25':
        print('Right. Off you go.')
    elif swallow == 'What do you mean? An African or European swallow?':
        print('What? I don\'t know that! Auuuuuuuugh! *is cast into the abyss*')
    else:
        print('*casts you into the abyss* Heh heh heh...')
