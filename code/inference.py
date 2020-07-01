import os
import pathlib
import shutil

# display required BIDS format
def displayBIDS() -> None:
	print("Please make sure the data is organized in the following fashion")
	print("myDataFolder/")
	print("\tSubject1/")
	print("\t\tanat/")
	print("\t\t\tSubject1_T1W.nii.gz")
	print("\t\t\tSubject1_FLAIR.nii.gz")

# modify modelConfig.cfg
def modifyMC() -> None:
	# path to package directory
	path = pathlib.Path(__file__).parent.parent.absolute()
	# get modelConfig.cfg path
	path_mc = str(path)
	path_mc += "/deepmedic/inference_model/config/model/modelConfig.cfg"
	# find stop & append index
	with open(path_mc,'r') as file:
		content = file.read()
	index1 = content.find("folderForOutput = ")
	index2 = content.find("#  ================ MODEL PARAMETERS")
	# modify modelConfig.cfg output folder
	path_o = str(path) + "/deepmedic/inference_model/output/"
	with open(path_mc,'w') as file:
		print(content[:index1 + len("folderForOutput = ")] + "\"" + path_o + "\"" + "\n", file=file)
		print(content[index2:], file=file)

# modify testConfig.cfg
def modifyTC() -> None:
	# path to package directory
	path = pathlib.Path(__file__).parent.parent.absolute()
	# get testConfig.cfg path
	path_tc = str(path) + "/deepmedic/inference_model/config/test/testConfig.cfg"
	# find stop & append index
	with open(path_tc,'r') as file:
		content = file.read()
	index1 = content.find("folderForOutput = ")
	substr = "#  [Optional] Path to a saved model, to load parameters from in the beginning of the session. If one is also specified using the command line, the latter will be used."
	index2 = content.find(substr)
	# modify testConfig.cfg output folder
	path_o = str(path) + "/deepmedic/inference_model/output/"
	with open(path_tc,'w') as file:
		print(content[:index1 + len("folderForOutput = ")] + "\"" + path_o + "\"" + "\n", file=file)
		print(content[index2:], file=file)

# get list of subjects
def getSubjects(path: "path to directory of data") -> list:
	subjects = []
	dirlist = os.listdir(str(path))
	for file in dirlist:
		if os.path.isdir(str(path) + "/" + file):
			subjects.append(file)
	subjects.sort()
	return subjects

# modify names of prediction
def modifyPred(subjects: "list of subjects") -> None:
	# get path to pred cfg
	path = pathlib.Path(__file__).parent.parent.absolute()
	path_pd = str(path) + "/deepmedic/inference_model/config/test/testNamesOfPredictions.cfg"
	# open cfg file for writing
	with open(path_pd,'w') as file:
		# write for each subject
		for subject in subjects:
			name = subject + "_WMH.nii.gz"
			print(name, file=file)

# modify test channels & prediction
def modifyCfgs(path: "path to directory of data") -> None:
	# get path to channel cfg
	path_cfg = pathlib.Path(__file__).parent.parent.absolute()
	# channel cfgs
	path_flair = str(path_cfg) + "/deepmedic/inference_model/config/test/test_flair.cfg"
	path_t1w = str(path_cfg) + "/deepmedic/inference_model/config/test/test_t1w.cfg"
	path_cfgs = [path_flair, path_t1w]
	# get all subjects
	subjects_all = getSubjects(path)
	subjects = []
	# make sure t1w and flair images are both present
	for subject in subjects_all:
		image_path = str(path) + "/" + subject + "/anat"
		hasT1W = os.path.isfile(image_path + "/" + subject + "_T1W.nii.gz")
		hasFLAIR = os.path.isfile(image_path + "/" + subject + "_FLAIR.nii.gz")
		if hasT1W and hasFLAIR:
			subjects.append(subject)
		else:
			print("Missing required image(s) for subject: " + subject)
	# modify channel cfgs
	modalities = ["FLAIR", "T1W"]
	for i in range(0, len(path_cfgs)):
		with open(path_cfgs[i],'w') as file:
			for subject in subjects:
				img = str(path) + "/" + subject + "/anat/" + subject + "_" + modalities[i] + ".nii.gz"
				print(img, file=file)
	# modify pred cfg
	modifyPred(subjects)

# run inference
def runInf(path_dm: "path to deepmedic", path_data: "path to data") -> None:
	

	# prepare different parts of command
	path_d = getPathToDM()
	run = path_d + "deepMedicRun"
	model = "-model " + os.getcwd() + "/config/model/modelConfig.cfg"
	test = "-test " + os.getcwd() + "/config/test/testConfig.cfg"
	load = "-load " + os.getcwd() + "/output/saved_models/train_t1w+flair/"
	load += "model_t1w+flair.train_t1w+flair.final.2019-11-01.11.44.09.274761.model.ckpt"
	# ask for which GPU to use
	dev = "-dev cuda" + input("Which GPU # to use? ")
	# run command for inference
	os.system(run + " " +  model + " " + test + " " +  load + " " + dev + " >& out.txt &")
	print("Running inference. You can check the progress using 'cat out.txt | less'")
	print("Or 'ps aux | grep -i myUserName' to check if the process is still running")
