# coding infinite monkey theorem in python.
# replace a monkey with a Python function
#  The sentence to generate is: “methinks it is like a weasel”

import random


# import argparse as a

def gen_sentence(str_len):
    alphabets = "abcdefghijklmnopqrstuvwxyz "
    string = ""
    for i in range(str_len):
        string += alphabets[random.randrange(27)]
    return string


def score(goal, test):
    sc = 0
    for i in range(len(goal)):
        if goal[i] == test[i]:
            sc = sc + 1
    pscore = (sc / len(goal)) * 100
    return pscore


def run_main():
    goal = "methinks it is like a weasel"
    test = gen_sentence(len(goal))
    best = 0
    iters = 0
    iscore = score(goal, test)
    while iscore < 100:
        if iscore > best:
            best = iscore
            print("iteration %d, string: %s\nscore= %f" % (iters, test, best))
            print("\n--------------------------")
        test = gen_sentence(len(goal))
        iscore = score(goal, test)
        iters = iters + 1
        if iscore==100:
            print("Summary:\n")
            print("To produce string: %s \nTotal iteration  = %d " % (test, iters))

run_main()

