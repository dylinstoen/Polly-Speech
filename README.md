# Description

Run Amazon Polly right on your desktop using this amazingly simple app!

![image](https://github.com/user-attachments/assets/454bf0c9-b875-470c-afb5-1ab136a53ab5)

Play audio right inside the app or save it as an mp3!

![image](https://github.com/user-attachments/assets/ac229cef-97ae-4a02-afd0-60accc0bac2a)

Switch between light and dark themes!

![image](https://github.com/user-attachments/assets/9e428c8a-d39a-4750-90fb-6d76dac93fed)

Scale the UI to be larger or smaller!

![image](https://github.com/user-attachments/assets/d1d22188-ec11-44b2-aca4-40eed80e0904)

Choose from any of the Amazon Polly natural voices!

![image](https://github.com/user-attachments/assets/d7c177fc-0e87-4798-8c6a-1d4532e6b29d)

## Tutorial

1. **Set Up Your AWS Account**
    - **Sign Up**: Head over to AWS Home to create your account. You’ll need to provide some basic info like your email, password, contact details, and credit card.
    - **Log In**: Once you’ve set up your account, log into the AWS Management Console.

2. **Create an IAM User**
    - From the AWS `Console Home` screen (can access this screen by clicking the `AWS` logo in the top left corner) look to the right of the logo for a `search` bar
    - In the search bar type `"iam"` in the search box and then click on the result that just says `IAM` under the `Services` category following the picture below

![image](https://github.com/user-attachments/assets/e2c1e91a-8635-4d9c-bdef-3ed54b0a316c)


- Once inside the `Identiy and Access Management (IAM)` homepage look to the left and you should see a sidebar full of options, under the `Access management` category click on `Users` like in the picture below

![image](https://github.com/user-attachments/assets/a232be4a-9935-47ab-9847-df52f458574e)


- To the right click on `Create user` like in the picture below

![image](https://github.com/user-attachments/assets/7bf6476d-44ca-4cf7-9541-4f2d74922ec4)

- Give the user a name and then click `Next`
- Under `Set permissions` and `Permission options` there's 3 options, toggle on the rightmost option which should say `Attach policies directly`
- After the `Permission options` there's the `Permissions policies` where under that category, check on `AmazonPollyFullAccess` (and optionally toggle on `AdministratorAccess`, `AWSCompromisedKeyQuarantineV2` for more control)
- Click `Next` and then `Create user`

 
3. **Set Up AWS CLI (Optional)**
    - **Attach Security Credentials**:
        - After creating a user, we should be back in the `users` directory
        - Open into the user you just created by clicking on there name
        - Now once your inside the user that you just created in **step 2**, look in the middle of the dashboard and find the 4 tab options (`Permissions Groups`, `Tags`, `Security credentials`, `Access Advisor`)
        - Once you found the tabs, click on the `Security credentials` tab
        - Under `Access Keys (0)` click `Create Access key`
        - Click `Command Line Interface (CLI)`, check on `I understand...`
        - (DON'T click on `Done`!) Instead, to the left of `Done` click `Download .csv file` which saves both access keys for us to use on the next step (if you forgot the keys, forgot to save the keys, and you don't have access to the .csv then creating a new `access key` pair should give you a new valid pair of access key/secrete values to use on the next step)
    - **Install and Configure AWS ClI**:
    - Download and install `AWS CLI.exe` by following this link to the [AWS CLI website](https://aws.amazon.com/cli/) then click on whats boxed in red from the picture below matching the system your on.

  ![image](https://github.com/user-attachments/assets/c240daa5-a143-4d75-b444-93ef1b76c066)
 
 
- After installing AWS CLI:
    - Open a command prompt on your desktop
    - Run `aws configure` in your command prompt.
    - Input your AWS Access Key ID and Secret Access Key (if you forgot look at the `username_access.cvs` file you saved earlier)
    - Set your default region, like `us-east-1`, and output format as `json`.

4. **Run Synthesize Speech App!**
    - Grab the exe from the `releases` section on this GitHub repo.
    - Open it, and if a warning pops up, click `more info` and then `Run anyway`.

5. Add Polly Speech to All Programs in Windows (Optional)
    - Right-click on the `exe` and choose `create desktop shortcut`.
    - Move the shortcut to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`.
    - Renaming the shortcut will change how it appears in search results without breaking the link.
 
### Troubleshooting

1. build local version of program
    - install python `3.11.7`, then in the terminal run the following `pip` commands
        -  `pip install boto3`
          -  `pip install pygame`
          -  `pip install customtkinter`
          -  `pip install io`
          -  `pip install pyinstaller`
    -  Download the `synthesize_speech-advanced.py` file
      -  open up the terminal in the directory of the python file you just downloaded, run the following command
        -  `pyinstaller --onefile --windowed text_to_speech.py`
    - Inside the same folder as your python file should be a `Dist`, open it up and there should be your local build of `synthesize_speech-advanced.exe`

3. if the `synthesize_speech-advanced.exe` build failed continue below
   - install `visual studio build tools 2022` and the rest of the programs dependcies
       - in the main install menu check on to install `Desktop development with C++`
        - in `individual components` check on to install `MSVC v142 - VS 2019 C++ x64/x86 build tools`
        - open `edit the system enviorment variables` and then under `System` open up `path`
        - under `path` add
          - `C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64`
            - `C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64`
            -  open up the terminal in the directory of the python file you downloaded in step 1, then run the following command again
              -  `pyinstaller --onefile --windowed text_to_speech.py`
          - Inside the same folder as your python file should be a `Dist`, open it up and there should be your local build of `synthesize_speech-advanced.exe`
