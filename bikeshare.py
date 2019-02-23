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
    city = None
    month = None
    day = None
    while day == None:
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
            city = input("Please enter a city name (either Chicago, New York City, or Washington): ")
            city = city.lower()
            while city != 'chicago' and city != 'new york city' and city !='washington':
                city = input("This is not a valid city.  Please enter one of the listed cities: ")
                city = city.lower()
                if city == 'chicago' or city == 'new york city' or city =='washington':
                    print('\n')
                    break

            month = input("Please enter a month between January and June, or enter 'all' to see data for all months: ")
            month = month.lower()
            while month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month !=                 'june':
                month = input ("This is not a valid month.  Please enter a month between January and June or 'all' to see unfiltered data: ")
                month = month.lower()
                if month == 'all' or month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month ==                           'june':
                    print('\n')
                    break

            day = input("Please enter a day of the week, or enter 'all' to see data for all days: ")
            day = day.lower()
            while day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day !=                       'saturday' and day != 'sunday':
                day = input ("This is not a valid day.  Please enter a day of the week or 'all' to see unfiltered data: ")
                day = day.lower()
                if day == 'all' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day ==                                 'saturday' or day == 'sunday':
                    print('\n')
                    break

    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Start and End Stations'] = df['Start Station'] + ' and ' + df['End Station']

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    #df['month'] = df['Start Time'].dt.month
    months = { 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    popular_month = df['month'].mode()[0]
    name = months.get(popular_month)
    print("Most common month: ", name)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day of the week: ", popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most common start station is: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most common end station is: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df['Start and End Stations'].mode()[0]
    print("Most popular start and end station combination: ", popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (sum(df['Trip Duration']))/60
    print("Total travel time for this time frame was: ", total_travel_time, "minutes")

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean())/60
    print("Mean travel time for this time frame was: ", mean_travel_time, "minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User type counts: ")
    print(user_types)

    if 'Gender' not in df:
        print("\nThere is no data on gender or birth year for this city.")

    else:
        # TO DO: Display counts of gender
        df_cleanup = df.dropna(subset = ['Gender'])
        gender_counts = df_cleanup['Gender'].value_counts()
        print('\n')
        print("Gender counts: ")
        print(gender_counts)

        # TO DO: Display earliest, most recent, and most common year of birth
        df_birthyear_cleanup = df.dropna(subset = ['Birth Year'])
        min_birthyear = df_birthyear_cleanup['Birth Year'].min()
        print('\n')
        print("Earliest birth year: ", int(min_birthyear))

        max_birthyear = df_birthyear_cleanup['Birth Year'].max()
        print("Most recent birth year: ", int(max_birthyear))

        mode_birthyear = df_birthyear_cleanup['Birth Year'].mode()
        print("Most common year of birth: ", int(mode_birthyear))

        print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)

def raw_data(df):
    """ Displays 5 lines of raw data upon user request """
    x = 0
    y = 5
    user_response = None
    user_response = input("Would you like to see five lines of raw data from this data set? ")
    user_response = user_response.lower()

    if user_response != 'yes' and user_response != 'no':
        user_response = input("This is not a valid response.  Please enter 'yes' or 'no'. ")
        user_response = user_response.lower()


    while user_response == 'yes':
        print(df[x:y])
        user_response = input("Would you like to see the next five lines of raw data from this data set? ")
        user_response = user_response.lower()
        while user_response == 'yes':
            x += 5
            y += 5
            print(df[(x):(y)])
            user_response = input("\nWould you like to see the next five lines of raw data from this data set? ")
            user_response = user_response.lower()
            if user_response != 'yes' and user_response != 'no':
                user_response = input("This is not a valid response.  Please enter 'yes' or 'no'. ")
                user_response = user_response.lower()
            else:
                print('Done')

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
