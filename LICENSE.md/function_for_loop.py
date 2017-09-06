# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

dic = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}

def num_teachers(dic):
    count = 0
    for x in dic:
        count += 1
    return count

def num_courses(dic):
    sum = 0
    for value in dic.values():
        sum += len(value)
    return sum

def courses(dic):
    liso = []
    for value in dic.values():
        liso += value
    return liso

def most_courses(dic):
    max_count = 0
    teacher_most_classes = " "
    for key in dic:
        if len(dic[key]) > max_count:
            max_count = len(dic[key])
            teacher_most_classes = key
    return key

def stats(dic):
    outer_list = []
    for key in dic:
        inner_list = []
        inner_list.append(key)
        inner_list.append(len(dic[key]))
        outer_list.append(inner_list)
    return outer_list
