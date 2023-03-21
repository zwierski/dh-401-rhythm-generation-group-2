import random
import music21

# fun to fill a bar with random notes


def random_bar():
    first = True
    # first decide how many notes are in the bar
    # (the tempo is always 3/4)
    bar = []
    for i in range(11):
        # decide if a note is played
        if first:
            bar.append(1.0)
            first = False
        elif random.randint(0, 4) < 2:  # 40% chance of a note to not collapse  a bar
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
print('random song: ')
print(random_song)

# convert into duration


def convert_to_duration(random_song_list):
    last = 4.0
    # read the list backwards
    random_song_list.reverse()
    # create a list with the duration of each note
    duration_list = []
    for bar in random_song_list:
        # reverse the inner list
        bar.reverse()
        for note in bar:
            duration_list.append(last - note)
            last = note
        last += 4.0
    # reverse the list again
    duration_list.reverse()
    return duration_list


# example
duration_list = convert_to_duration(random_song)
print('duration list: ')
print(duration_list)

# convert duration list into music21 stream


def convert_to_stream(duration_list):
    # create an empty stream
    stream = music21.stream.Stream()
    # define the tempo as 3/4
    stream.append(music21.meter.TimeSignature('3/4'))
    # create note
    # assign random pitch (C4)
    # assign duration (quarter)
    # append the note into empty stream
    for duration in duration_list:
        note = music21.note.Note(pitch='C4', quarterLength=duration)
        stream.append(note)
    return stream


# example
stream = convert_to_stream(duration_list)
# print(type(stream))
# stream.show()

# play the stream
stream.show('midi')
