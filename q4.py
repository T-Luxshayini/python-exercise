def evaluate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"


print(evaluate_grade(91))  
print(evaluate_grade(83))  
print(evaluate_grade(76))  
print(evaluate_grade(65))  
print(evaluate_grade(50))  
