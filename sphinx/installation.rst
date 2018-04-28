Installation Instruction
=========================
 	 
Download and Install Python and Pip (If you already have Python 3.6 skip to Step 2)

1-Follow [this link](https://www.python.org/) to the Python Software Fondation Website.
   
2-Navagate to the Downloads button and select the Python 3.x. installer that matches your Operating System.  Alternatively, you can navagate to their full [list of downloads](https://www.python.org/downloads/) and select the download link of the Python Version you wish to download. The list of available packages and installers for various operating systems are listed at the bottom of the version download page.
   
3- Download and run the installer following the installer's prompts.
   
 Once installed you should be able to type `python` into your console's command line and have it return something similar to:

   Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.

   
If you are running Windows and recieve the following error:  `‘python’ is not recognized as an internal or external command`  you can follow [this post](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/) in order to manually add the keyword 'python' to the PATH Environment Variable.
   
2. Clone the Repo

Navigate your console to your desired install folder and enter:

   git clone https://github.com/Rhernandez513/open_source_computing.git

   
Check to ensure you have the most up-to-date files using:
   ```
   git status
   ```
   
Installing Packages from Requirements.txt

Check to ensure you have Pip 9.0.1 or later installed by entering the following into your console command line:
   ```
   pip -V
   ``` 
   
   If you are running and older version of Pip you can enter in the following command to update:
   ```
   python -m pip install --upgrade pip
   ```
   
Navigate to directory containing the `requirements.txt`. The directory should be something like:

   `C:\...\open_source_computing\project1`
   
 From there enter the command: 
   ```
   pip install -r requirements.txt
   ```

This will install the required packages listed in the text document. You can check if you have all the correct packages by entering:
   ```
   pip list
   ```

4. Running the Application using manage.py

 Navagate your console to the Project Root Folder which should contain the file 'manage.py'
   
 Enter this command to launch the local server:
   ```
   python manage.py runserver
   ```
   
   To access the application, open up your web browser and navagate to `localhost:8000`
   