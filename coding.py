import os




def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    except OSError:
        print(f"Oops! Something went wrong with file: {file_path}")
        return None

def find_folder(year, race, folder_path):
    abs_path = os.path.abspath(folder_path)

    for root, dirs, files in os.walk(abs_path):
        for dir in dirs:
            if year in dir:
                dir_path = os.path.join(abs_path, dir)
                find_files(race, dir_path) 

def find_files(race, folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if race in file:
                file_path = os.path.join(folder_path, file)
                races.append(read_file(file_path))

year = '2018'
racetype = "Final"
races = []

find_folder(year, racetype, "resources")

for race in races:
    lines = race.split('\n')

    for line in lines[1:]:
        print(line)