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
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city = str(input('name of the city to analyse:')).lower()
            if city == 'chicago':
                city ='chicago.csv'
            elif city == 'new york city':
                city = 'new_york_city.csv'
            elif city == 'washington':
                city = 'washington.csv'
            else: 
                print('I do not get that')
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
            month = str(input('name of the month to filter by, or "all" to apply no month filter:')).lower()
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if month == 'january':
                month = months[0]
            elif month == 'february':
                month = months[1]
            elif month == 'march':
                month = months[2]
            elif month == 'april':
                month = months[3]
            elif month =='may':
                month = months[4]
            elif month == 'june':
                month = months[5]
            elif month == "all":
                print('all')
            else: 
                print('I did not get that')
            break 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            day = str(input('name of the day of week to filter by, or "all" to apply no day filter:')).lower()
            days = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']

            if day == 'monday':
                day = days[0]
            elif day == 'tuesday':
                day = days[1]
            elif day == 'wednesday':
                day = days[2]
            elif day == 'thursday':
                day = days[3]
            elif day =='friday':
                day = days[4]
            elif day == 'saturday':
                day = days[5]
            elif day == 'sunday':
                day = days[6]
            elif day == 'all':
                print('all')
            else: 
                print('I did not get that')
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
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
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

    # TO DO: display the most common month
    month_mode = pd.Series(pd.DatetimeIndex(df['Start Time'])).dt.month.mode()
    print("Most Common Month :", month_mode, sep = " ")
    
    # TO DO: display the most common day of week
    
    weekday_mode = pd.Series(pd.DatetimeIndex(df['Start Time'])).dt.weekday_name.mode()
    print("Most Common Day of the Week :",weekday_mode, sep = " ")

    # TO DO: display the most common start hour
    
    hour_mode = pd.Series(pd.DatetimeIndex(df['Start Time'])).dt.hour.mode()
    print ("Most Common Start Hour :",hour_mode, sep = " ")    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    ss = df['Start Station']
    start_station = ss.mode()
    print ("Most Common Used Start Station :",start_station,sep = " ")

    # TO DO: display most commonly used end station
    es = df['Start Station'].mode()
    print("Most Common Used End Station:",es, sep = " ")


    # TO DO: display most frequent combination of start station and end station trip
    df["frequent stations"] = df["Start Station"].map(str) + " to " + df["End Station"]
    fs_mode = df["frequent stations"].mode()
    print ("Most Frequent Combination of Start and End Station:", fs_mode, sep = " ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt = df['Trip Duration'].sum()
    print("Total Travel Time:",ttt, sep = " ")


    # TO DO: display mean travel time
    td_mean = df['Trip Duration'].mean()
    print ("Mean Travel :",td_mean, sep= " ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Subscribers = len(df[df["User Type"] == "Subscriber"])
    Customers = len(df[df["User Type"] == "Customer"])
    print ('subscribers:' , Subscribers, sep = " ")
    print ('customers:', Customers, sep = " ")


    # TO DO: Display counts of gender
    try:    
        Males = len(df[df["Gender"] == "Male"])
        Females = len(df[df["Gender"] == "Female"])
    except:    
        print('There is no Gender data')
    else:
        print('Males :', Males, sep = " ")
        print('Females :', Females, sep = " ")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:    
        earliest = df['Birth Year'].min() 
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()
    except:
        print('There is no Birth Year data')
    else:
        print ('Earliest :', earliest, sep = " ")
        print ('Most recent :', most_recent, sep = " ")
        print ('Most common :', most_common, sep = " ")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
#----------------------Descriptive Statistics-----------------------
def descriptive_stats(df):
    
    while True:
        show_me_more = str(input('Do you need to see more data ? yes or no')).lower() 
        if show_me_more == 'yes':
            print(df.describe())
        else:
            print('Done')
        break
        
#-------------------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        descriptive_stats(df) #checking
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
