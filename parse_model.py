import os 

def format_labels(file):
    with open(file, 'r') as openfile:
        data = openfile.readlines()

    line = data[0].replace('\n', '') + '; ' + data[1]

    with open(file, 'w') as file:
        file.writelines(line)


def format_snap(snap):
    os.rename(snap,'modelgender.caffemodel')