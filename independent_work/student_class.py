
class Student():
    #define a constructor
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = int(credit_hours)
        self.__gpa = float(gpa)
        self.__id_number = int(id_number)

    #get and set methods
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_major(self):
        return self.__major
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, additional_hours):
        self.__credit_hours = additional_hours

    def update_credit_hours(self, additional_hours):
        self.__credit_hours += additional_hours
    
    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa):
        try:
            self.__gpa = float(new_gpa)
        except:
            print("ERROR: GPA must be a number")
    
    def get_id_number(self):
        return self.__id_number

    def get_class_level(self):
        if self.__credit_hours >= 0 and self.__credit_hours <= 30:
            class_level = "Freshman"
            return class_level
        if self.__credit_hours > 30 and self.__credit_hours <= 60:
            class_level = "Sophomore"
            return class_level
        if self.__credit_hours > 60 and self.__credit_hours <= 90:
            class_level = "Junior"
            return class_level
        else: 
            class_level = "Senior"
            return class_level

    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}: {self.__major}")
        print(f"Student ID: {self.__id_number}")
        print(f"Credit hours: {self.__credit_hours} hrs, GPA: {self.__gpa}, Grade Level: {self.get_class_level()}\n")