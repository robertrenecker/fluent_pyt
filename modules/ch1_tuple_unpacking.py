import os;
from collections import namedtuple;

def lbreak():
 print()
 print("-----------------------------------------------");
 print();

def named_tuples():
    print("Named tuples example: \n")
    City = namedtuple("City", 'name country population coordinates')
    tokyo = City("Tokyo", "Japan", 100, (35.689,139.698));
    print(tokyo);
    print("Now print tokyo's country only: (tokyo.country): ", tokyo.country)

def chapter_one():
    #Tuple Unpacking
    print("Tuple unpacking tests");
    cordinates = (33.04918, 48.43922);
    a,b = cordinates;
    print("%s %s" % cordinates);
    a,b = b,a; #Switch values without temp var
    print(a,b);

    lbreak();

    #Named tuples

    named_tuples();










    return 0;
