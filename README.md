# Description

- Run Amazon Polly right on your desktop locally using this amazing user friendly interface!
- Setup AWS and Amazon Polly to configure with this app and any future apps you want to make all in this one stop shop tutorial!

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
    - From the AWS Management Console, go to to the IAM (Identity and Access Management) service.
    - Click `Users`
    - Click `Add user`
    - **Attach Policies**:
        - Give the user AmazonPollyFullAccess for full Polly capabilities.
        - Finish up and **don’t forget** to save the access key ID and secret access key shown. You won’t see them again!

3. **Set Up AWS CLI (Optional)**
    - Download and install `AWS CLI.exe` from the AWS CLI website.
    - Open a command prompt on your desktop
    - Run `aws configure` in your command prompt.
    - Input your AWS Access Key ID and Secret Access Key.
    - Set your default region, like `us-east-1`, and output format as `json`.

4. **Run Synthesize Speech App!**
    - Grab the exe from the `releases` section on this GitHub repo.
    - Open it, and if a warning pops up, click `more info` and then `Run anyway`.

5. Add Polly Speech to All Programs in Windows (Optional)
    - Right-click on the `exe` and choose `create desktop shortcut`.
    - Move the shortcut to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`.
    - Renaming the shortcut will change how it appears in search results without breaking the link.
 
### Troubleshooting

1. install python and the programs dependencies packages
    - install python `3.11.7`
    -  `pip install boto3`
    -  `pip install pygame`
    -  `pip install customtkinter`
    -  `pip install io`
    -  `pip install pyinstaller`
    -  Download the .py file
    -  'pyinstaller --onefile --windowed text_to_speech.py'

2. install `visual studio build tools 2022`
    - in the main install menu check on to install `Desktop development with C++`
    - in `individual components` check on to install `MSVC v142 - VS 2019 C++ x64/x86 build tools`
    - open `edit the system enviorment variables` and then under `System` open up `path`
    - under `path` add
        - `C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64`
        - `C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64`
