def give_letter_grade(score):
    if score >= 9.0:
        return "A"
    elif score >= 7.0 and score <= 8.9:
        return "B"
    elif score >= 5.0 and score <= 6.9:
        return "C"
    elif score >= 3.0 and score <= 4.9:
        return "D"
    else:
        return "F"
    return score

score_1 = 9.5
score_2 = 7.0
score_3 = 5.5
score_4 = 3.2
score_5 = 1.1

print("Score 9.5 -->", give_letter_grade(score_1))
print("Score 7.0 -->", give_letter_grade(score_2))
print("Score 5.5 -->", give_letter_grade(score_3))
print("Score 3.2 -->", give_letter_grade(score_4))
print("Score 1.1 -->", give_letter_grade(score_5))


