import argparse
from edit import edit_ds_transfer, edit_secondary_gie

parser = argparse.ArgumentParser(description='Test of gender model in deepstream and its metrics')

parser.add_argument('model_name', type=str, help='model name for testing)
parser.add_argument('secondary', type=str, help='path to the secondary inference config file')
parser.add_argument('video', type=str, help='path to the video for testing')
parser.add_argument('ds_config', type=str, help='path to deepstream config file')
parser.add_argument('out_path_inference', type=str, help='path to save the inference results')

def main():
    args = parser.parse_args()

    edit_secondary_gie(args.secondary, args.model_name)
    edit_ds_transfer(args.ds_config, args.model_name, args.out_path_inference, video )