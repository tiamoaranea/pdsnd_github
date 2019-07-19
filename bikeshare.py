# refactoring code
# refactoring code update 2nd. time

# the following changes are to meet the reviewer's requirements

# this part is for bug fix No.1

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


    while True:
      # use lower in order to get input in any format
      city = input("\nPlease enter the name of the city to analyze: Chicago, New York City or Washington.\n").lower()
      if city not in ('chicago', 'new york city', 'washington'):
        print("Invalid input. Please try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nPlease enter the name of the month: January, February, March, April, May, June or type 'all' to display data of all months.\n").lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Invalid input. Please try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nPlease enter the name of the day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type 'all' to display data of all days.\n").lower()
      if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print("Invalid input. Please try again.")
        continue
      else:
        break

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

    # converty date into date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    #create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # find index of month
        month = months.index(month) + 1
    	# filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month == month]

    # filter data by day
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Start Time'].dt.weekday_name == day.title()]
    print(df.head())
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)


    # TO DO: display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day:', most_common_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', end_station)


    # TO DO: display most frequent combination of start station and end station trip

    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost commonly used combinations of start station and end station trip:', start_station, " & ", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    time_1 = total_travel_time
    day= time_1//(24 * 3600)
    time_1 = time_1 % (24 * 3600)
    hour= time_1 // 3600
    time_1 %= 3600
    minutes = time_1 // 60
    time_1 %= 60
    seconds = round(time_1 , 2)
    print('Total travel time: {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    time_2 = mean_travel_time
    hour_2 = time_2 // 3600
    time_2 %= 3600
    minutes_2 = time_2 //60
    time_2 %= 60
    seconds_2 = round(time_2 , 2)
    print('Mean travel time: {} hours {} minutes {} seconds'.format(hour_2, minutes_2, seconds_2))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    num_subscribers = df['User Type'].str.count('Subscriber').sum()
    num_customers = df['User Type'].str.count('Customer').sum()
    print('\nNumber of subscribers are: {}\n'.format(int(num_subscribers)))
    print('\nNumber of customers are: {}\n'.format(int(num_customers)))

    # TO DO: Display counts of gender

    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are: {}\n'.format(int(male_count)))
        print('\nNumber of female users are: {}\n'.format(int(female_count)))

    # TO DO: Display earliest, most recent, and most common year of birth

    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest year of birth: " + str(earliest_year))
        print("\nMost recent year of birth: " + str(recent_year))
        print("\nMost common year of birth: " + str(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Asks if the user would like to see some lines of data from the filtered dataset.
        print("\nWould you like to see five rows of raw data ? Enter yes or no")
        raw_data = input()
        raw_data = raw_data.lower()

        i = 5
        while raw_data == 'yes':
            """ To display few rows of data for user view """
            print(df[:i])
            print("\nWould you like to see five more rows of raw data ? Enter yes or no")
            i += 5
            raw_data = input()
            raw_data = raw_data.lower()


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
