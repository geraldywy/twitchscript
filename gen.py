import random

def gen_userpass():
    with open("words.txt", 'r') as wordsfile:
        words_list = wordsfile.read().splitlines()

    # wordsfile = open("words.txt", 'r')
    # words_list = wordsfile.read().splitlines()

    random_userpass = words_list[random.randint(0, len(words_list)-1 )] + words_list[random.randint(0, len(words_list)-1 )] + str(random.randint(0,10000))
    random_userpass = random_userpass.replace("'", '')[:25]
    return random_userpass

def gen_name():
    with open('firstnames.txt', 'r') as first:
        firstnames = first.read().splitlines()
    with open('lastnames.txt', 'r') as last:
        lastnames = last.read().splitlines()
    name = (firstnames[random.randint(0, len(firstnames)-1 )], lastnames[random.randint(0, len(lastnames)-1 )])
    return name
