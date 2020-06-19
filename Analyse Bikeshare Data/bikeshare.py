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
    city = input('Name the US city that you would like to explore:').lower()
    while city not in ['chicago','new york city','washington']:
        print("Data for this city is not available!! Please input city name out of chicago,new york city and washington:")
        city = input('Name the US city that you would like to explore:').lower

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list=['january','fabruary','march','april','may','june','all']
    month = input('Select the month you want to analyse:').lower()

    while month not in month_list:
        print('Invalid Month Name!! Please select month out of january,fabruary,march,april,may,june or all.')
        month = input('Select the month you want to analyse:').lower()

    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day = input('Select the day you want to analyse:').lower()

    while day not in day_list:
        print('Invalid day Name!! Please select day out of monday,tuesday,wednesday,thursday,friday,saturday,sunday or all.')
        day = input('Select the day you want to analyse:').lower()

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
    df = pd.read_csv(CITY_DATA[city])

    #data type of start time and end time is not correct
    #converting data type for same to datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #extract month from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    #extract week day from Start Time to create new column
    df['week_day'] = df['Start Time'].dt.weekday_name 


    #filter by month if applicable!!
    if month is not 'all':
        #use the index of the months list to get the corresponding integer value
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month) + 1

        #create a new data frame after filtering by month
        df=df[df['month'] == month]

    #filter by day of week if applicable!!!
    if day is not 'all':
        # filter by day of week to create the new data frame
        df=df[df['week_day'] == day.title()]


    return df


def time_stats(df,city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print("Displaying the most common month:",common_month)

    # TO DO: display the most common day of week
    common_day=df['week_day'].mode()[0]
    print("Displaying the most common day of the week:",common_day)


    # TO DO: display the most common start hour
    df['start_hr'] = df['Start Time'].dt.hour
    common_start_hr=df['start_hr'].mode()[0]
    print("Displaying the most common start hour:",common_start_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start staion is:',common_start_station)
    
        
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end staion is:',common_end_station)

    
    # TO DO: display most frequent combination of start station and end station trip
    df['combine_start_end'] = df['Start Station']+ " " + df['End Station']
    print('The most frequent combination of start station and end station trip:',df['combine_start_end'].mode().values[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['total_travel'] = df['End Time'] - df['Start Time']
    print('The total travel time:',df['total_travel'].sum())
    


    # TO DO: display mean travel time
    mean_travel = df['total_travel'].mean()
    print('The mean travel time :',mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if city != 'washington':
        # TO DO: Display counts of user types
        user_count=df['User Type'].value_counts()
        print('Now you got the count of various types of users:',user_count)


        # TO DO: Display counts of gender
        gender_count=df['Gender'].value_counts()
        print('The gender count of the users is:',gender_count)


        # TO DO: Display earliest, most recent, and most common year of birth
        #to get the earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest Birth year is:',str(int(earliest_birth_year)))

        #to get the most recent year of birth
        recent_birth_year = df['Birth Year'].max()
        print('The recent Birth year is:',str(int(recent_birth_year)))

        #to get the most common year of birth
        common_birth_year = df['Birth Year'].mode()
        print('The most common Birth year is:',str(int(common_birth_year)))


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("No user data found for washington city !!!!")

    
def display_raw_data(df,city):
    """Display the raw data requested by the user."""

    i=0
    j=5

    ask = input("Do you want to see the raw data?:").lower()

    if ask == 'yes':
        while j <= df.shape[0] - 1:

            print(df.iloc[i:j,:])
            i+= 5
            j+= 5

            again_ask = input("Do you want to see raw data again?:").lower()
            if again_ask == 'no':
                break
        
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,city)
        station_stats(df,city)
        trip_duration_stats(df,city)
        user_stats(df,city)
        display_raw_data(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
