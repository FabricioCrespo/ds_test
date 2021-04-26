# Automatization for test gender models in deepstream-app

First, we have to download the epoch of the model we want to test from the Digits port.
This model will be in .tar.gz format, then we have to extract the model and we will have
a ton of file for deployment. We just need to focus in 3 of them:

1. deploy.prototxt
2. snap_xxx.caffemodel
3. labels.txt

We have to do the following changes:
1. We have to change the name of snap_xxx.caffemodel to modelgender.caffemodel
2. Then we have to edit the labels file to format the content to DS. Example:
labels.txt original:
```
female
male
```
DS format labels.txt:
```
female; male
```

We move the model folder to gender_portal insisde the docker in the configs section od the DS app.
After that we excecute the python file to edit configs according to our model. Then, we run:

```python
python3 main.py --model_name --secondary -- video --ds_config --out_path_inference

positional arguments:
  model_name          model name for testing
  secondary           path to the secondary inference config file
  video               path to the video for testing
  ds_config           path to deepstream config file
  out_path_inference  path to save the inference results
```

fter that, we just need to excecute the deepstream app:

```
../../deepstream-transfer-learning-app -c ds_transfer_learning_app_example.txt
```
We can find the inference results in the path we provide in --out_path_inference. After that, we need
to run an script to obtain the metrics of our infered model.

We need to run the following command:
```
python evaluate_model.py --csv_path <file.csv> --json_path <file.json> --model_name <model_name>
```
where:
```
Input:
--csv_path -> csv file path with the infered results
--json_path -> json file path with the ground truth labels from cloud annotations.
Output:
The script generates 6 files:
1. ground_truth_general.csv -> Table with cleaned ground truth results for male and female.
2. inference_general.csv ->  Table with cleaned inferenced results for male and female.
3. general_comparison.csv -> Table with inferenced, ground truth and comparison results for male and female.
4. female_comparison.csv -> Table with inferenced, ground truth and comparison results only for female. 
5. male_comparison.csv -> Table with inferenced, ground truth and comparison results only for male.
6. model_name_report.txt -> Report with multiple results:
                            Global:
                            Results based on individual images.
                            Grouped by Person_Id No Weighted:
                            Results based on Person_Id
                            Grouped by Person_Id Weighted:
                            Results based on Person_Id weighted according to occurrence
```
