import random

# fun to fill a bar with random notes
def random_bar():
    # first decide how many notes are in the bar
    # (the tempo is always 3/4)
    bar = []
    for i in range(11):
        # decide if a note is played
        if random.randint(0, 4) < 2: # 40% chance of a note to not collapse  a bar
            # if yes, decide which note
            bar.append((i/4)+1)
        # check that the bar is not empty
    if len(bar) == 0:
        bar = random_bar()
    return bar

# create random song
def create_random_song():
    # make a list with 8 lists inside
    random_song = [[] for j in range(8)]
    # for each list in random_song fill it with random notes
    for i in range(8):
        random_song[i] = random_bar()
    return random_song

# example
random_song = create_random_song()
print(random_song)
