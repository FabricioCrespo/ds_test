## Script to read a txt file and change a specifig line
import os 

def edit_ds_transfer(ds_transfer_path,model_name,output_folder_path,video_name):

    """ Function to change the lines of ds_transfer conf file.

        Inputs:
            - ds_transfer_path : path to ds_transfer file
            - model name : name of the used model.
            - output_folder_path: path to desired putput folder where the results like images_cropped and csv file will be saved.
            - video_name: name of the video to be used inside /samples/streams/ folder.

        Output: 
            - ds_transfer txt file with changed lines. 
    """

    # Open the txt file and read lines.
    with open(ds_transfer_path, 'r') as my_file:
        lines= my_file.readlines()

    # To change folder output path
    for index, line in enumerate(lines):
        if line[:18]=="output-folder-path":
            part_to_change=line.split('/')[1:]
            #If there is not the directory, we mkdir it.
            if not os.path.exists(output_folder_path):
                os.makedirs(output_folder_path)
            str1="/"
            for words in part_to_change:
                str1+=words+"/"
            str1=str1[:-2]
            lines[index]=line.replace(str1,output_folder_path)+"\n"
    
    # To change uri video
    for index, line in enumerate(lines):
        if line[:8]=="uri=file":
            part_to_change=line.split('/')[-1]
            lines[index]=line.replace(part_to_change,video_name)+"\n"

    # To change output-file

    for index, line in enumerate(lines):
        if line[:11]=="output-file":
            part_to_change=line.split('/')[-1]
            lines[index]=line.replace(part_to_change,model_name+"_transfer_"+video_name)+"\n"
    
    #Save the new lines
    my_file = open(ds_transfer_path, "w")
    for line in lines:
        str1=""
        for words in line:
            str1+=words
        my_file.write(str1)
    my_file.close()
    

def edit_secondary_gie(file, model_folder):
    with open(file, 'r') as openfile:
        data = openfile.readlines()

    for i in range(len(data)):
        if 'model-file=' in data[i]:
            model = os.path.join(model_folder, 'modelgender.caffemodel')
            data[i]=f'model-file={model}\n'
        if 'proto-file=' in data[i]:
            proto = os.path.join(model_folder, 'deploy.prototxt')
            data[i]=f'proto-file={proto}\n'
        if 'labelfile-path=' in data[i]:
            labels = os.path.join(model_folder, 'labels.txt')
            data[i]=f'labelfile-path={labels}\n'
        
    with open(file, 'w') as file:
        file.writelines( data )

