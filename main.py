import time
from playsound import playsound

"""
This is the main file for Sleep Tracker.
"""


def main():
    print('\nSleep Tracker')

    # current_time = [day of the week, month, day, hour:minute:second, year]
    current_time = time.ctime().split()
    print(f'current time: {current_time[3][:5]}')

    # Takes the user's age
    print('\nIn order to give you the recommended hours of sleep, we want to know your age.')
    answer = input("Enter your age (enter 's' to skip): ")

    if answer != 's':
        age = int(answer)

        # Tells the user to reenter age if the age is negative
        while age < 0:
            print('\nInvalid age!')
            age = int(input('Enter your age again: '))

        # Gives a recommendation hours of sleep
        if age == 0:
            recommended_hours = '12-17'
        elif 1 <= age <= 2:
            recommended_hours = '11-14'
        elif 3 <= age <= 5:
            recommended_hours = '10-13'
        elif 6 <= age <= 13:
            recommended_hours = '9-11'
        elif 14 <= age <= 17:
            recommended_hours = '8-10'
        elif 18 <= age <= 64:
            recommended_hours = '7-9'
        else:
            recommended_hours = '7-8'
        print(f'\nThe National Sleep Foundation recommends {recommended_hours} hours of sleep.')

    # calculate the numbers of minutes the user want to sleep
    hours_of_sleep = float(input('Enter the number of hours you want to get: '))
    minutes_of_sleep = int(hours_of_sleep * 60)

    # current_time = [day of the week, month, day, hour:minute:second, year]
    current_time = time.ctime().split()
    current_hour = int(current_time[3][:2])
    current_minute = int(current_time[3][3:5])

    # Calculates the wake up time
    total_minutes = current_minute + minutes_of_sleep
    dm = divmod(total_minutes, 60)
    alarm_minute = dm[1]
    total_hour = current_hour + dm[0]
    alarm_hour = total_hour % 24

    confirm = input(f'\nAre you sure you want to set the alarm to {alarm_hour:02d}:{alarm_minute:02d}? (y/n) ')

    # If the user does not want to set the alarm at the given time, they can enter their desired wake up time
    if confirm == 'n':
        alarm = input('Please enter the time you want to wake up (hh:mm): ')
        alarm_hour, alarm_minute = int(alarm[:2]), int(alarm[3:])
        current_time = time.ctime().split()
        current_hour = int(current_time[3][:2])
        current_minute = int(current_time[3][3:5])
        if alarm_hour >= current_hour:
            minutes_of_sleep = (alarm_hour - current_hour) * 60 + (alarm_minute - current_minute)
        else:
            minutes_of_sleep = (alarm_hour - current_hour + 24) * 60 + (alarm_minute - current_minute)

    # Sets the alarm for the user
    print(f'\nAll set! Your alarm is set at {alarm_hour:02d}:{alarm_minute:02d}.')
    print('\nTips to Help You Sleep Faster')
    print('1. Put your phone away from your bed.')
    print('2. Change the room temperature to 65°F.')
    print('3. Take a deep breath and empty your mind.')
    print('4. Relax your face and all your muscles.')

    minutes = 0
    while minutes != minutes_of_sleep:
        if minutes % 60 == 0 and minutes != 0:
            if minutes == 60:
                print('1 hours has passed.')
            else:
                print(int(minutes / 60), 'hours has passed.')
        time.sleep(60)
        minutes += 1

    # The alarm goes off
    print('\nGood Morning.')
    playsound('alarm.mp3')


if __name__ == "__main__":
    main()
