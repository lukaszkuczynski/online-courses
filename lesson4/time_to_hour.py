import pandas


def time_to_hour(time):
    '''
    Given an input variable time that represents time in the format of:
    "00:00:00" (hour:minutes:seconds)

    Write a function to extract the hour part from the input variable time
    and return it as an integer. For example:
        1) if hour is 00, your code should return 0
        2) if hour is 01, your code should return 1
        3) if hour is 21, your code should return 21

    Please return hour as an integer.
    '''

    hour = int(time[:2])
    return hour


if __name__ == '__main__':
    hour = time_to_hour("00:00:00")
    assert hour == 0
    hour = time_to_hour("01:00:00")
    assert hour == 1
    hour = time_to_hour("21:00:00")
    assert hour == 21
