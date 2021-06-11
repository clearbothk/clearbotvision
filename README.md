# Clearbot Vision Module

### Setup guide

#### Requirements

- Python 3.6
- USB Camera/webcam

#### Setup environment

Using `virtualevn`:

If you don't have virtualenv installed:

```shell
pip install virtualenv --user
```

In the project directory, setup the virtual environment:

```shell
virtualenv .venv -p python3
```

Use the environment while working on the project:

Linux:

```shell
source .venv/bin/activate
```

Windows (using Command Prompt)

```shell
cd .venv/Scripts
activate.bat
cd ..\..
```

Install Python dependencies using:

```shell
pip install -r requirements.txt
```

#### Download model files

There are two models in this project: YOLO and Mask R-CNN.

The model folders must be created in `ml/yolo/model` and `ml/detectron/model`.

Please find the models in the release.

#### Run the module

```shell
python main.py
```

Please refer to the options available for the command below.

Note: If the above command does not run, make sure the virtual environment is activated.

#### Command Line Reference

| Option  | Value                | Description                                                                        |
| ------- | -------------------- | ---------------------------------------------------------------------------------- |
| -v      | boolean (True/False) | Show video frame output. Default: false (only available for yolo model)            |
| --debug | boolean (True/False  | Switch to debug mode for logs: Default: false (only available for the yolo model)  |
| -m      | detectron/yolo       | Model type to use for detection. Default: full                                     |
| -s      | full/tiny            | Model type to use for detection. Default: full (only available for the YOLO model) |
