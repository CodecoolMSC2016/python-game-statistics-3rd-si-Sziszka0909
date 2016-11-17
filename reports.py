
# Report functions


def count_games(file_name):
    with open(file_name) as f:        
        return sum(1 for sor in f)

def decide(file_name, year):
    with open((file_name), 'r') as f:
        line_list = f.readlines()
        exist = False
    for k in range(len(line_list)):
        line_list[k] = (line_list[k]).split('\t')
    for l in range(len(line_list)):
        if year == int(line_list[l][2]):
            return True
    return False


def get_latest(file_name):
    with open((file_name), 'r') as f:
        line_list = f.readlines()
    for k in range(len(line_list)):
        line_list[k] = (line_list[k]).split('\t')
    latest = 0
    for l in range(len(line_list)):
        if latest < int(line_list[l][2]):
            latest = int(line_list[l][2])
            latest_name = line_list[l][0]
    return latest_name



def count_by_genre(file_name, genre):
    with open((file_name), 'r') as f:
        line_list = f.readlines()
    for k in range(len(line_list)):
        line_list[k] = (line_list[k]).split('\t')
    count = 0
    for l in range(len(line_list)):
        if genre == line_list[l][3]:
            count += 1
    return count



def get_line_number_by_title(file_name, title):
    with open((file_name), 'r') as f:
            line_list = f.readlines()
    for k in range(len(line_list)):
        line_list[k] = (line_list[k]).split('\t')
        if (title.lower()).replace(" ", "") == (line_list[k][0].lower()).replace(" ", ""):
            return k+1
