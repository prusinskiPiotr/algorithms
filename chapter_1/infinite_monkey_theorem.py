import random


def generate_random_string(klength):
    """
    Generate 28 random characters from alphabet including space
    """
    return "".join(random.choices('abcdefghijklmnopqrstuvwxyz ', k=klength))


def score_the_strings(astring, bstring):
    """
    Score each generated string by comparing randomly generated string to correct sentence
    """
    compare1 = [aword for aword in astring]
    compare2 = [aword for aword in bstring]
    comparedList = [i for i, j in zip(compare1, compare2) if i == j]
    score = "%.2f" % ((len(comparedList) / len(astring)) * 100)
    return float(score)


def follow_progress():
    """
    Call generate_random_string() and score_the_strings() repeatedly,
    finish the program if score is 100%,
    print out best string generated so far and its score after every 1000 tries
    """
    correct_sentence = 'methinks it is like a weasel'
    newstring = generate_random_string(28)
    best = 0
    iteration = 0
    newscore = score_the_strings(correct_sentence, newstring)
    while float(newscore) < 100.00:
        if newscore >= best:
            print(newscore, newstring)
            best = newscore
            iteration = iteration + 1
            if iteration == 10:
                # print(f'n-1000th iteration score: {str(newscore)} {newstring}')
                iteration = 0
        newstring = generate_random_string(28)
        newscore = score_the_strings(correct_sentence, newstring)
    else:
        print('Program finished')


follow_progress()
