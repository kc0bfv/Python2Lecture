#!/usr/bin/env python

import school
# To do this I had to setup school/__init__.py

if __name__ == "__main__":
    class_names = ["english","spanish","opera","math","science"]
    schools = {
            "John Booker High": school.high, 
            "James Knight Middle": school.middle, 
            "Little Tykes Elementary": school.elementary,
            }

    for school_name, school_type in schools.items():
        school_type.name = school_name
        for name in class_names:
            school_type.add_class(name)

    for school_type in schools.values():
        print "Classes at {}:".format(school_type.name)
        for course in school_type.list_classes():
            print "\t{}".format(course)
