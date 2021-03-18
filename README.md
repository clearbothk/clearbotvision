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

Create the  folder `ml/model` (`model` folder in the ml directory).

Download the model files ZIP, extract and put the files in that folder.

[Download from Releases](https://github.com/clearbothk/clearbotvision/releases/download/v0.1/model.zip)

#### Run the module

```shell
python main.py
```

Note: If the above command does not run, make sure the virtual environment is activated.

#### Command Line Reference

|Option   	|Value   	|Description   	|
|---	|---	|---	|
|-v   	|boolean (True/False)   	|Show video frame output. Default: false   	|
|--debug   	|boolean (True/False   	|Switch to debug mode for logs: Default: false   	|
|-m   	|tiny/full   	|Model type to use for detection. Default: full   	|