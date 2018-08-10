#test file
import time;
import os;
from modules import ch1_tuple_unpacking as ch1;
def main():
    print("Hello ", os.getlogin());
    print("This executable is to run different tests that are relevant to the book Fluent Python");

    start_time = time.time();


    ch1.chapter_one();









    #Record total time
    end_time = time.time();
    total_time = (end_time-start_time);
    print("Total time to execute: ", total_time);


if __name__ == "__main__":
    main();
