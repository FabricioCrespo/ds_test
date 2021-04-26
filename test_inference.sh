#Change config files
python3 main.py  model_cam_55x_00 gender_portal/gender.txt  ../../../../../../samples/streams/557-20a/557-20a-6pm.mp4 ds_transfer_learning_app_example.txt /triton_gender/tl_results_id
#Run deepstream-app for evaluation
../../deepstream-transfer-learning-app -c ds_transfer_learning_app_example.txt
