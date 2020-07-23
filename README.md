# DeepMedic-Pipeline

## 1. Introduction

This is a pipeline designed to make running inference on our model that was created using [DeepMedic](https://github.com/deepmedic/deepmedic) *v0.7.4* easier. The model aims to segment White Matter Hyper-Intensities in MRI images of the brain using T1-weighted and FLAIR images.

## 2. Installation and Requirements

### 2.1. CUDA Installation

Although CPU usage is supported, GPU processing is most likely required, especially if working with large amount of data.

Please follow the [guide in DeepMedic](https://github.com/deepmedic/deepmedic/blob/master/documentation/README.md#13-gpu-processing) to set up CUDA and cuDNN.

> Note: As of now, this pipeline is only compatible with CUDA 9.0

### 2.2. Python 3.6

Python 3.6 is required to run this software.

You can create a [Conda environment](https://docs.conda.io/en/latest/) to for this purpose.

#### Creating a Conda Environment

You can create a Conda environment that uses Python 3.6 at a specific directory by using the following command:

`conda create -p path/to/myEnv python=3.6`

> Note: Once you are done using the pipeline, you can deactivate it using the command: `conda deactivate`

### 2.3 Clone Repository

You can download the pipeline through Github by using the following command:

`git clone https://github.com/guswns3396/DeepMedic-Package.git`

### 2.4 Required Data Pre-Processing

In order to run the pipeline without problems, the following two requirements must be met.

#### DeepMedic Guideline

Data must be pre-processed according to [DeepMedic's guidelines](https://github.com/deepmedic/deepmedic/blob/master/documentation/README.md#14-required-data-pre-processing).

#### BIDS Format

Data must be in [BIDS format](https://bids.neuroimaging.io/).

> Ex
> ---
> myDataFolder/
>> subject-01/
>>> anat/
>>>> subject-01_T1W.nii.gz
>>>>
>>>> subject-01_WMH.nii.gz

## 3. Running the Software

### 3.1 How to Run

This is the basic format to run the software:

`python3 wmh_seg_deepmedic.py <option> [pathToData GPU]`

> Note
> ---
> `wmh_seg_deepmedic.py` is located in the pipeline directory
>
> `<option>` : choose among 1~3
>> 1 : Create Virtual Environment
>>
>> 2 : Install Dependencies
>>
>> 3 : Run Inference
>
> `[pathToData GPU]` : arguments needed if <option> is `3`
>> pathToData : refers to path to the directory where the data to run the inference on is located
>> GPU : specifies which GPU to use for inference (if using CPU use `-1`)

### 3.2 Setup

Virtual environment and dependencies must be setup and installed before inference can be run.

_**The setup needs to be run only once.**_

#### Creating Virtual Environment

A virtual environment must be created before installing dependencies.

It can be created with the following command:

`python3 wmh_seg_deepmedic.py 1`

#### Activating Virtual Environment

After creating the virtual environment, you **must activate it** before installing dependencies.

You can activate the virtual environment by using the following command:

`source env/bin/activate`

> Note: After setup / inference virtual environment can be deactivated by using the command: `deactivate`

#### Installing Dependencies

Once the virtual environment is activated, you can install the dependencies using the following command:

`python3 wmh_seg_deepmedic.py 2`

### 3.3 Running Inference

The following steps must be taken to run inference correctly using the pipeline.

#### Verify Pre-Processing

Please verify that the necessary [pre-processing](#24-required-pre-processing) has been done.

#### Activate Virtual Environment

Please [activate the virtual environment](#activating-virtual-environment) before running inference.

#### Run Inference

You can run inference by using the following command:

`python3 wmh_seg_deepmedic.py 3 path/to/data gpuNumber`

> Refer to [this](#31-how-to-run) for more information.

The output will be located in the `output` folder in the pipeline directory

> Note: [Deactivate the virtual environment](#activating-virtual-environment) once done with inference.

## References

[1] Konstantinos Kamnitsas, Christian Ledig, Virginia F.J. Newcombe, Joanna P. Simpson, Andrew D. Kane, David K. Menon, Daniel Rueckert, and Ben Glocker, “Efficient Multi-Scale 3D CNN with Fully Connected CRF for Accurate Brain Lesion Segmentation”, Medical Image Analysis, 2016.

[2] Konstantinos Kamnitsas, Liang Chen, Christian Ledig, Daniel Rueckert, and Ben Glocker, “Multi-Scale 3D CNNs for segmentation of brain Lesions in multi-modal MRI”, in proceeding of ISLES challenge, MICCAI 2015.