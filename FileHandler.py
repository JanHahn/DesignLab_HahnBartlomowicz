#class that handling all file operations for locker application

class FileHandler:
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
                    if int(tab[0]) == locker.locker_id:
                        return tab[1]

        except FileNotFoundError:
            print(f"File '{self.file_path}' does not exist.")
        except Exception as e:
            print(f"Error occured: {e}")

    def change_status(self, locker, info):
        # Read the current contents of the file
        with open(self.file_path, 'r') as locker_file:
            lines = locker_file.readlines()

        # Check if the locker ID already exists, and update its info if it does
        updated = False
        for i, line in enumerate(lines):
            locker_id, _ = line.strip().split(":")
            if int(locker_id) == locker:
                lines[i] = f"{locker}:{info}\n"
                updated = True
                break

        # If the locker ID does not exist, append the new info
        if not updated:
            lines.append(f"{locker}:{info}\n")

        # Write the updated content back to the file
        with open(self.file_path, 'w') as locker_file:
            locker_file.writelines(lines)