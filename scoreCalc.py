# An integer x - Record a new score of x
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be
# two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a
# previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a
# previous score.

def scoreCalc(ops):
    scores = []
    for i in ops:
        if i == "C":
            scores.pop()
        elif i == "D":
            scores.append(2 * scores[-1])
        elif i == "+":
            scores.append(scores[-1] + scores[-2])
        else:
            scores.append(int(i))
    return sum(scores)
    