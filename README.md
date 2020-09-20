## Driver drowsiness detection - Setup and Installation

You need to have anaconda installed on your system :)

### Step 1: Update conda 
```bash
conda update conda
```
### Step 2: Update anaconda 
```bash
conda update anaconda 
```
### Step 3: Clone the github repository
```bash
git clone https://github.com/ShobhitRathi/DrowsyRide
```

### Step 4: Create a virtual environment
```bash 
conda create -n env_dlib 
```
### Step 5: Activate the virtual environment 
```bash 
conda activate env_dlib
```
### Step 6: Install dlib 
```bash 
conda install -c conda-forge dlib 
```
If all these steps are completed successfully, then dlib will be installed in the virtual environment <b>env_dlib</b>. Make sure to use this environment to run the entire project. 
### Step 7: Installing packages
```bash
pip install -r requirements.txt
```

### Step 8: Running the webserver!
```bash
python app.py
```
And the app runs on the localhost of port 5000, And you can visit, and see it!

### Step to deactivate the virtual environment 
```bash 
conda deactivate 
```

