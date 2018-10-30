def validTime(time):
    return int(str(time[:2])) < 24 and int(str(time[-2:])) < 60


"""
Check if the given string is a correct time 
representation of the 24-hour clock.

Example

    For time = "13:58", the output should be
    validTime(time) = true;
    For time = "25:51", the output should be
    validTime(time) = false;
    For time = "02:76", the output should be
    validTime(time) = false.

"""

time = "13:58"
if __name__ == '__main__':
    print(validTime(time))
