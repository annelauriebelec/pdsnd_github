import time
import datetime as dt
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    while city not in ('chicago', 'new_york_city', 'washington') :
        city = input("Enter the city you would like to analyse; chicago, new_york_city or washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = 99
    while month not in (0, 1, 2, 3, 4, 5, 6) :
        month = int(input("Enter the month in number you would like to analyse; january=1, febuary=2, march=3, april=4, may=5, june=6 or all=0: "))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 99
    while day not in (0, 1, 2, 3, 4, 5, 6, 10) :
        day = int(input("Enter the day in number you would like to analyse; monday=0, tuesday=1, wednesday=2, thursday=3, friday=4, saturday=5, sunday=6 or all=10: "))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - name of the month to filter by, or "0" to apply no month filter
        (int) day - name of the day of week to filter by, or "10" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv('{}.csv'.format(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    if month != 0 :
        df = df[df['month'] == month]
    if day != 10 :
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"}
    popular_month = df['month'].value_counts().idxmax()
    print('The most popular month is {}'.format(months.get(popular_month)))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3:  "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    print('The most popular day is {}'.format(days.get(popular_day, "erreur")))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('The most popular hour is {}h'.format(popular_hour))
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station is {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('most commonly used end station is {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['station_combi'] = df['Start Station'] + " - " + df['End Station']
    popular_combi=df['station_combi'].value_counts().idxmax()
    print('most commonly used combination of stations is {}'.format(popular_combi))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['Trip Duration'] = pd.to_numeric(df['Trip Duration'])
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {} hours'.format(round(total_travel_time / 360, 2)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is {} minutes'.format(round(mean_travel_time / 60, 2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of user types is \n{}'.format(user_types)) 
    
    if city != "washington" :
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('\nThe count of gender is \n{}'.format(gender)) 
    
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_dob = int(df['Birth Year'].min())
        print('\nThe earliest year of birth is {}'.format(earliest_dob)) 
        recent_dob = int(df['Birth Year'].max())
        print('\nThe most recent year of birth is {}'.format(recent_dob)) 
        common_dob = int(df['Birth Year'].mode()[0])
        print('\nThe most common year of birth is {}'.format(common_dob))
    else: print("\nGender and year of birth information are not available for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    see_data = input("Would you like to see sample raw data? Enter yes or no.\n")
    if see_data == "yes" :
        print(df.iloc[:5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
   
