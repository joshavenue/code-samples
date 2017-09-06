# Let's write some functions to explore set math a bit more. We're going to be using this COURSES dict in all of the examples. Don't change it, though!
So, first, write a function named covers that accepts a single parameter, a set of topics. Have the function return a list of courses from COURSES where the supplied set and the course's value (also a set) overlap.
For example, covers({"Python"}) would return ["Python Basics"].

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topics):
    new_list = []
    for topic in topics:
        for basics in COURSES:
            if topic in COURSES[basics]:
                new_list.append(basics)
    return new_list

# OK, let's create something a bit more refined. Create a new function named covers_all that takes a single set as an argument. Return the names of all of the courses, in a list, where all of the topics in the supplied set are covered.
# For example, covers_all({"conditions", "input"}) would return ["Python Basics", "Ruby Basics"]. Java Basics and PHP Basics would be exclude because they don't include both of those topics.

def covers_all(topics):
    new_list = []
    temp_list = []
    for basics in COURSES:
        for topic in topics:
            if topic in COURSES[basics]:              
                temp_list.append(topic)
        if len(topics) == len(temp_list):
            if basics not in new_list:
                new_list.append(basics)
                temp_list = []
        else:
            temp_list = []
    return new_list
