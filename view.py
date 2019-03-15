

def welcome_screen():
    print('Welcome to the terminal line menu for the Quandl data')



def home_menu():
    print('1. View List of Databases')
    print('2. View Databases by Category')
    print('3. Set Favorites')
    print('4. View Dataset using Code')
    selection = input('Select your choice: ')



def view_list_of_database():
    for row in df:
        print(df.iloc[row]['Name'], df.iloc[row]['Code'])
    print('Press \'esc\' to return to Main Menu. \n\
            Enter the database code to view more info.')
    selection = input()


def view_list_of_databases_by_category():
    pass


def set_favorites():
    pass


def view_dataset_using_code():
    print('Enter the database code (not the dataset code): ')
    db_code = input()
    print('Enter the dataset code: ')
    dataset_code = input()

    return db_code, dataset_code

