#class that handling all file operations for locker application

class FileHandler():
    def __init__(self, file_path):
        self.file_path = file_path

    #function that returns if locker is open or closed
    #parameter is locker object defined in file "Locker.py"
    def check_status(self, locker):
        try:
            with open(self.file_path, 'r') as locker_file:
                text = locker_file.read()
                locker_list = text.split("\n")
                for locker_info in locker_list:
                    tab = locker_info.split(':')
                    if tab[0] == locker.locker_id:
                        return tab[1]

        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")
        except Exception as e:
            print(f"Error occured: {e}")

    #TODO finish replacing file
    def change_status(self, locker):
        with open(self.file_path, 'r') as locker_file:
            text = locker_file.read()