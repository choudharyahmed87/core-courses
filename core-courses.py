class CoreCourse:
    def __init__(self, course_name, course_code):
         self.course_name = course_name
         self.course_code = course_code

    def get_course_details(self):
        return f"Course: {self.course_name}, Code: {self.course_code}"


class SchemeOfStudyManager:
    def __init__(self):
        self.core_courses = []

    def add_core_course(self, course_name, course_code):
        new_course = CoreCourse(course_name, course_code)
        self.core_courses.append(new_course)

    def display_core_courses(self):
        print("Core Courses:")
        for course in self.core_courses:
            print(course.get_course_details())


# Example usage of SchemeOfStudyManager
scheme_manager = SchemeOfStudyManager()

# Adding core courses
class CoreCourse:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def get_course_details(self):
        return f"Course: {self.course_name}, Code: {self.course_code}"


class SchemeOfStudyManager:
    def __init__(self):
        self.core_courses = []

    def add_core_course(self, course_name, course_code):
        new_course = CoreCourse(course_name, course_code)
        self.core_courses.append(new_course)

    def display_core_courses(self):
        print("Core Courses:")
        for course in self.core_courses:
            print(course.get_course_details())


# Example usage of SchemeOfStudyManager
scheme_manager = SchemeOfStudyManager()

# Adding core courses
scheme_manager.add_core_course("programing Fundamantal", "CS101")
scheme_manager.add_core_course("Object Orantated programing", "DS200")
scheme_manager.add_core_course("Data stracture", "ALG300")
scheme_manager.add_core_course("Data Base", "CS400")
scheme_manager.add_core_course("Mutal programing", "DS500")
scheme_manager.add_core_course("Mobile and Application Development ", "ALG600")
scheme_manager.add_core_course("Software Testing", "ALG700")
scheme_manager.add_core_course("Final year project", "ALG800")
# Displaying core courses
scheme_manager.display_core_courses()

