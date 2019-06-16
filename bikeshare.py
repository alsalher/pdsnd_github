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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = []
    while city not in cities:
        city = input("Enter a city from Chicago, New York City or Washington: ").lower()
        if city not in cities:
            print('You have not entered a valid city')
    # get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    month = []
    while month not in months:
        month = input("Enter a month from January to June, or enter '''All''': ").lower()
        if month not in months:
            print('You have not entered a valid month')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = []
    while day not in days:
        day = input("Enter a day of the week, or enter '''All''': ").lower()

    print('-'*40)
    return city, month, day


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
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('Most common day of the week: {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('Most common start hour: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most common end station: {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['combination'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    print('Most common combination: {}'.format(df['combination'].mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    print('Total travel time: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('Total travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types: {}'.format(df['User Type'].value_counts()))

    # Display counts of gender
    if city == 'new york city' or city == 'chicago':
        print('Counts of gender: {}'.format(df['Gender'].value_counts()))
    else:
        print('No information about gender available')
    # Display earliest, most recent, and most common year of birth
    if city == 'new york city' or city == 'chicago':
        print('Earliest year of birht: {}'.format(df['Birth Year'].min()))
        print('Most recent year of birht: {}'.format(df['Birth Year'].max()))
        print('Most Common year of birht: {}'.format(df['Birth Year'].mode()))
    else:
        print('No information about year of birth available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

<<<<<<< HEAD
        """Displays all statistics on bikeshare."""
||||||| parent of 76c5cdc... Add to code lines for displaying raw data
=======
        """Displays raw data if user requires."""

        raw_data = input('\nDo you want to take a look in the data? Enter yes or no.\n')

        count = 5
        while raw_data.lower() == 'yes':
            print(df.head(count))
            raw_data = input('\nDo you want to take 5 lines more? Enter yes or no.\n')
            count = count + 5

>>>>>>> 76c5cdc... Add to code lines for displaying raw data
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
