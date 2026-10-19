from course_template import Course


def main():

    # Create 7 Course objects
    myCourse1 = Course("MIS 101", "Intro. to Info. Systems", 140, 3)
    myCourse2 = Course("MIS 301", "Systems Analysis", 35, 3)
    myCourse3 = Course("MIS 441", "Database Management", 12, 3)
    myCourse4 = Course("CS 155", "Programming in C++", 90, 3)
    myCourse5 = Course("MIS 451", "Web-Based Systems", 30, 3)
    myCourse6 = Course("MIS 551", "Advanced Web", 30, 3)
    myCourse7 = Course("MIS 651", "Advanced Java", 30, 3)

    courses = [
        myCourse1,
        myCourse2,
        myCourse3,
        myCourse4,
        myCourse5,
        myCourse6,
        myCourse7
    ]

    print("Course Information\n")

    # Print data attributes and total fees for all 7 objects
    for course in courses:
        course.printCourseInfo()
        print(
            "Total Fees =",
            course.CalculateTotalFees(),
            "$"
        )
        print()

    # Update myCourse7 using end-user input
    print("Setting new data attributes for myCourse7 Object:")

    course_no = input("Please enter the course number: ")
    course_name = input("Please enter the course title: ")
    credits = int(input("Please enter course credits: "))
    max_enrl = int(input("Please enter the max student enrolled: "))

    # Use setter methods
    myCourse7.setCourseNo(course_no)
    myCourse7.setCourseName(course_name)
    myCourse7.setCredits(credits)
    myCourse7.setMaxEnrl(max_enrl)

    print("\nData attributes of myCourse7 after entered by end user:")

    myCourse7.printCourseInfo()

    print(
        "Total fees of myCourse7 is",
        myCourse7.CalculateTotalFees(),
        "$"
    )

    # Use getter methods
    print("\nData attributes of myCourse7 by invoking the getter methods:")

    print(
        myCourse7.getCourseNo(),
        "-",
        myCourse7.getCourseName(),
        "-",
        myCourse7.getCredits(),
        "-",
        myCourse7.getMaxEnrl()
    )


main()