def latest(scores):
    return scores[-1]


def personal_best(scores):
    best = 0
    for score in scores:
        if score > best:
            best = score
    return best


def personal_top_three(scores):
    top_three = []
    scores.sort(reverse = True)
    for i in scores:
        if len(top_three) < 3:
            top_three.append(i)
    return top_three
