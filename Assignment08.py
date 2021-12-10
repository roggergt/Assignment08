#------------------------------------------#
# Title: Assignment08.py
# Desc: Assignment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# RTovar, 2021-Dec-05, added menu
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
cd_id = 0
cd_title = ''
cd_artist = ''

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODO Add Code to the CD class
    # - - Contructor - - #
    def __init__(self, cd_id, cd_title, cd_artist):
        # - - Attributes - - #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
       
    
    @property
    def cd_id(self):
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, value: int):
        if str(value).isnumeric():
            raise Exception('This should be a number')
        else:
            self.__cd_id = value
    @property
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self, value):
        if str(value).isnumeric():
            raise Exception('This should be a string')
        else:
            self.__cd_title = value
    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self,value):
        if str(value).isnumeric():
            raise Exception('This should be a string value')
        else:
            self.__cd_artist = value

        
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file
    @staticmethod
    def read_file(strFileName, table):
        table.clear()
        objFile = open(strFileName, 'a+')
        for line in objFile:
            data = line.strip().split(',')
            tbl = [data[0], data[1], data[2]]
            lstOfCDObjects.append(tbl)
        objFile.close()
    # TODO Add code to process data to a file
    def write_file(strFileName, lstOfCDObjects):
        objFile = open(strFileName, 'w')
        for row in lstOfCDObjects:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        print('\nYou have successfully saved your file.\n')    
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    # TODO add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Main Menu\n-----------------------------------\n\n[i] Display Current Inventory\n[a] Add CD')
        print('[s] Save Inventory to File\n[l] Load Inventory\n[x] exit\n')
    
    # TODO add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        try:
            while choice not in ['l', 'a', 'i', 's', 'x']:
                choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
                print()  # Add extra space for layout
                return choice
        except Exception as e:
            print(e)
           
         
    # TODO add code to display the current data on screen
    @staticmethod
    def show_inventory(tbl):    
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in tbl:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
                  
        
                  
        
        # TODO add code to get CD data from user
    def add_inventory():     
        # Ask user for new ID, CD Title and Artist
        while True:
            try:
                cd_id = int(input('Enter ID: ').strip())
                break
            except Exception as e:
                print(e)
                print('Please enter a number and try again. ')
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        cd_entry = CD(cd_id, cd_title, cd_artist)
        lstOfCDObjects.append(CD)
        
        return cd_entry

# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.read_file(strFileName, lstOfCDObjects)
IO.show_inventory(lstOfCDObjects)
# Display menu to user
while True:
    IO.print_menu()
    choice = IO.menu_choice()
  
        # show user current inventory
    if choice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user add data to the inventory
    elif choice == 'a':
      IO.add_inventory() 
      continue
       # let user save inventory to file
    elif choice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Are you sure you want to save Inventory file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('Inventory was NOT save to file. Press any key to return to Main Menu.')
        continue
    # let user load inventory from file
    elif choice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        try:
            if strYesNo.lower() == 'yes':
                print('Reloading...')
                FileIO.read_file(strFileName, lstOfCDObjects)
            elif strYesNo.lower() != '':
                print('Start over...') 
        except Exception as e:
            print(e)
        
        FileIO.read_file(strFileName, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user exit program
   
    elif choice == 'x':
        input('Ok, bye bye!')
        break
else:
    print('\nYou may want to try again\n')
    

