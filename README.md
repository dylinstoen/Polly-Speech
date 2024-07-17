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

## Step 1: Set Up Your AWS Account
- **Sign Up**: Head over to AWS Home to create your account. You’ll need to provide some basic info like your email, password, contact details, and credit card.
- **Log In**: Once you’ve set up your account, log into the AWS Management Console.

## Step 2: Create an IAM User
- **Open IAM**: From the AWS Management Console, navigate to the IAM (Identity and Access Management) service.
- **Add a New User**:
  - Click “Users”, then “Add user”.
  - Choose a user name and select “Programmatic access” for API, CLI, and SDK access.
- **Attach Policies**:
  - Give the user AmazonPollyFullAccess for full Polly capabilities.
  - Finish up and **don’t forget** to save the access key ID and secret access key shown. You won’t see them again!

## Step 3: Set Up AWS CLI (Optional)
- **Install AWS CLI**: Download and install it from AWS CLI.
- **Configure the CLI**:
  - Run `aws configure` in your command prompt.
  - Input your AWS Access Key ID and Secret Access Key.
  - Set your default region, like `us-east-1`, and output format as `json`.

## Step 4: Try Out Amazon Polly (Optional)
- Run `aws polly synthesize-speech --output-format mp3 --voice-id Joanna --text "Hello, World" hello.mp3` in your command prompt to create an MP3 file saying "Hello, World".

## Step 5: Run Synthesize Speech App!
- **Download and Run**:
  - Grab the exe from the `releases` section on this GitHub repo.
  - Open it, and if a warning pops up, click `more info` and then `Run anyway`.

## Step 6: Add Polly Speech to All Programs in Windows (Optional)
- **Create a Shortcut**:
  - Right-click the exe and choose `create desktop shortcut`.
  - Move the shortcut to `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`.
  - Renaming the shortcut will change how it appears in search results without breaking the link.

