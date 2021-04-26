## Script to read a txt file and change a specifig line
import os 

def edit_ds_transfer(ds_transfer_path,model_name,output_folder_path,video_path):

    """ Function to change the lines of ds_transfer conf file.

        Inputs:
            - ds_transfer_path : path to ds_transfer file
            - model name : name of the used model.
            - output_folder_path: path to desired putput folder where the results like images_cropped and csv file will be saved.
            - video_name: name of the video to be used inside /samples/streams/ folder.

        Output: 
            - ds_transfer txt file with changed lines. 
    """

    vide_name =video_path.split("/")[-1]
    # Open the txt file and read lines.
    with open(ds_transfer_path, 'r') as my_file:
        lines= my_file.readlines()

    # To change folder output path
    for index, line in enumerate(lines):
        if line.startswith("output-folder-path"):
            lines[index] = 'output-folder-path=' + output_folder_path
            #line="output-folder-path="+output_folder_path
            #part_to_change=line.split('/')[1:]
            #If there is not the directory, we mkdir it.
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)
    
    # To change uri video
    for index, line in enumerate(lines):
        #if line[:8]=="uri=file":
        if line.startswith("uri=file"):
            lines[index] = 'uri=file://' + video_path

    # To change output-file

    for index, line in enumerate(lines):
        if line.startswith("output-file"):
            lines[index] = 'output-file='+ os.path.join(output_folder_path, model_name+'_'+video_name.split('.')[0]+'_transfer.mp4')
    
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

