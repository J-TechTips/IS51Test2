"""
The program is going to display the grades by three catagories 
Number of grades, The average Grade, and percentage of grades above average 
retrive the students grades first.
Then calculate the percentage of grades above 
display the number of grades
display the average grade
display the percentage of grades that are above the average grade
"""

"""
main
    runs the applicaiton 
    FinalGrades = for each grade (total amount)
        display the amount of students that have
    Calculate the avearage 
        display the amount of studnets that have
    calculate the percent that is above average

grades
    read in the Final.txt
    create a list of integers with the grades
    close the file 

main() 
"""

def main():
    g = open("Final.txt", "r")
    grades = g.read()
    grades_list = grades.split()
    g.close
    

    len(grades_list)
    print("Total amount of grades is", len(grades_list))

    return sum(grades_list) / len(grades_list)
    average = Average(grades_list)
    print(" ", round(average, 2))

main()