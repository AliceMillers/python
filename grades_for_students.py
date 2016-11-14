grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
#all of the grades
for grade in grades:
    print (grade)
def print_grades(grades):
    for grade in grades:
        print (grade)

#sum of grades
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total
print (grades_sum(grades))

#average grade
def grades_average(scores):
    sum_of_grades = grades_sum(scores)
    average_1 = sum_of_grades / float(len(scores))
    return average_1
print (grades_average(grades))

#variance
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    var_score = 0
    for score in scores:
        variance += (average - score) ** 2
    var_score = variance / (len(scores))
    return var_score
print (grades_variance(grades))

#standard deviation
def grades_std_deviation(variance):
    return variance ** 0.5
variance = grades_variance(grades)
print (grades_std_deviation(variance))