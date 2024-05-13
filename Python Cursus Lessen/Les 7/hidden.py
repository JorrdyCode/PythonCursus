from random import shuffle, randint
shuffle = shuffle # every day
is_sorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l)-1))
secret_number = randint(0,10)