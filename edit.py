## Script to read a txt file and change a specifig line

def edit_ds_transfer(ds_transfer_path,folder_name)
my_file=open("txt_files/ds_transfer_learning_app_example.txt")
lines= my_file.readlines()
#print(lines)

folder_name="example"

for line in lines:
    if line[:18]=="output-folder-path":
        part_to_change=line.split('/')[-1]
        line=line.replace(part_to_change,folder_name)
        #line_split[-1]=folder_name
        print(line)
        
        #folder_to_save=line.split(/)
        #print(True)

#output-folder-path=/triton_gender/tl_results_id/portal_558_1


def edit_secondary_gie(file, model_folder):
    with open(file) as openfile:
    for line in openfile:
        for part in line.split():
            if "color=" in part:
                print part