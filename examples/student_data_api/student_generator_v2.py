import student_class as student
from datetime import datetime
"""
Function to write error log file 
Input: error message 
Output: none
"""
def write_to_error_log(error_message):
    try: 
        #open log file
        log_file = open("error_log.text", "a")
        
        #write error message to log file 
        log_file.write(f"{datetime.now()}: {error_message}\n")
       
        #close log file
        log_file.close()
    except Exception as err:
        print(err)

    return


def load_students(file_name):
    list_of_students = []

    student_file = open(file_name, "r")
    student_file.readline()

    line_number = 1
    for line_of_data in student_file:
        line_number += 1 
        student_data = line_of_data.split(",")

        try:
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}\n")
        except Exception as err:
            write_to_error_log(str(err))
            continue
        
        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            id_number = student_data[5]
        except Exception as err:
            write_to_error_log(f"Error: {err} on line {line_number}")
            continue

        new_student = student.Student(first_name, last_name, major, credit_hours, gpa, id_number)

        list_of_students.append(new_student)

    student_file.close()
    return list_of_students

#create a fucntion called student_to_dictionary that creates a student dictionary for each student object
#add student dictionaries to a list
#function to create a list of student dictionaries
#input: list of student objects 
#output: list of student dictionaries
def student_to_dictionary(list_of_students):
    list_of_student_dictionaries = []
    
    #loop through the list of students: for loop
    for the_student in list_of_students:
        #create a dictionary for each student object 
        student_dictionary = {
            "first_name": the_student.get_first_name(),
            "last_name": the_student.get_last_name(),
            "id": the_student.get_id_number(),
            "major": the_student.get_major(),
            "credit_hours": the_student.get_credit_hours(),
            "gpa": the_student.get_gpa(), 
            "class": the_student.get_class_level(),
        }

        list_of_student_dictionaries.append(student_dictionary)
    
    return list_of_student_dictionaries


def get_student_dictionaries():
    student_list = load_students("student_data.csv")

    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries

