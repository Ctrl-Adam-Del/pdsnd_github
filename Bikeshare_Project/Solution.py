import time
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
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ['chicago', 'new york city', 'washington']
    input_city = input("Would you like to look at data from Chicago, New York City, or Washington? ").lower()
    while input_city not in city:
        print("Whoops!  Something went wrong.  Please check your spelling and choose from one of the four available options! ", end='')
        input_city = input("Try again? ")
    print('Mmm.  I love the nachos they have in {}!'.format(input_city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    input_month = input("Alright, which month would you like to select? Please choose between January through June, or All: ").lower()
    while input_month not in month:
        print("Whoops!  I didn't recognize that month. ", end='')
        input_month = input("Try again? ")
    print('Interesting, {} is a very popular choice!'.format(input_month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    input_day = input("Okay, and what day of the week would you like to choose?  Please enter the full day, no abbreviations, or all: ").lower()
    while input_day not in day:
        print("Hmm, I didn\'t quite get that. ", end= '')
        input_day = input("Try again? ")
    print('I had a feeling you were going to pick {}.'.format(input_day))

    print('-'*40)
    return input_city, input_month, input_day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month !='all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating the most frequent times of travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    if common_month == 1:
        actual_month = "January"
    elif common_month == 2:
        actual_month = "February"
    elif common_month == 3:
        actual_month = "March"
    elif common_month == 4:
        actual_month = "April"
    elif common_month == 5:
        actual_month = "May"
    else: actual_month = "June"
    print('Most common month: ',actual_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of the week: ',common_day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    start_hour = df['hour'].mode()[0]
    print('Most common hour of the week: ',start_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    station_start = df['Start Station'].mode()[0]
    print('Most common START station: ',station_start)

    # TO DO: display most commonly used end station
    station_end = df['End Station'].mode()[0]
    print('Most common END station: ',station_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + ' to ' + df['End Station']
    common_combo = df['combo'].mode()[0]
    print('The most common combination of start and end stations: ',common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('The total trip duration was: ',trip_duration)

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('The total mean time of the trip duration was: ',mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print("User Type count:\n",user_types)
        print('\n')
    except:
        print('No user type data available')

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('\nThe gender count:\n',user_gender)
        print('\n')
    except:
        print('No gender data available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest birth year: ',earliest_birth_year)
    except:
        print('No birth year data available')

    try:
        recent_birth_year = df['Birth Year'].max()
        print('Most recent birth year: ',recent_birth_year)
    except:
        print('No recent birth year data available')

    try:
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most common birth year: ',common_birth_year)
    except:
        print('No common birth year data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Gets five rows of raw data until user declines."""

    a = 0
    b = 5
    dat = input('Would you like to see the first five rows of raw data?  Please enter yes or no:')
    while True:
        if dat.lower() == 'yes':
            print(df.iloc[a:b])
        if dat.lower() == 'no':
            print('Thank you, please come again!')
            break
        dat = input('\nWould you like to see the next five rows of raw data?  Please enter yes or no:')
        a=a+5
        b=b+5


def main():
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)
        print(df.head())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        break



if __name__ == "__main__":
	main()
