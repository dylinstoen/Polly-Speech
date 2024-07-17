# Description

Run Amazon Polly locally on your desktop with this user friendly interface!

![image](https://github.com/user-attachments/assets/454bf0c9-b875-470c-afb5-1ab136a53ab5)

Play audio right inside the app or save it as an mp3

![image](https://github.com/user-attachments/assets/3251c4b9-096b-4cc0-add8-009160dfbae3)

Select between light and dark themes

![image](https://github.com/user-attachments/assets/ac229cef-97ae-4a02-afd0-60accc0bac2a)

Scale the UI to be larger or smaller!

![image](https://github.com/user-attachments/assets/d1d22188-ec11-44b2-aca4-40eed80e0904)

Choose from any of the Amazon Polly natural voices!

![image](https://github.com/user-attachments/assets/d7c177fc-0e87-4798-8c6a-1d4532e6b29d)

## Tutorial

## Step 1: Set Up an AWS Account
1. Create an AWS Account: If you don't already have one, sign up at AWS Home. You'll need to provide your email address, password, contact information, and credit card details.
2. Sign In to the AWS Management Console: Once your account is active, sign in to the AWS Management Console.

## Step 2. Create an IAM User and Assign Policies
1. Navigate to IAM: In the AWS Management Console, open the IAM (Identity and Access Management) service.
2. Create a New User:
    - Click on “Users” and then “Add user”.
    - Enter a user name and select “Programmatic access” as the access type. This provides an access key ID and secret access key for the AWS API, CLI, and SDKs.
3. Attach Policies:
    - Attach the AmazonPollyFullAccess policy to this user to allow full access to Polly.
    - Confirm and create the user.
    - Important: Download or securely store the access key ID and secret access key displayed, as you will not be able to see them again.

## Step 3. Set Up the AWS CLI (Optional)
1. Install the AWS CLI: Download and install the AWS CLI from AWS CLI.
2. Configure the CLI:
    - Run `aws configure` in your command line.
    - Enter the `AWS Access Key ID` and `Secret Access Key` you just created.
    - Set your `default region name` (e.g., `us-east-1`, `us-west-2`).
    - Set the `default output format` as `json`
    
## Step 4: Test Amazon Polly on your command prompt (Optional)
- test amazon polly running this command `aws polly synthesize-speech --output-format mp3 --voice-id Joanna --text "Hello, World" hello.mp3`
- This command will create an MP3 file named hello.mp3 with the spoken text “Hello, World”.

## Step 5. Run Synthesize Speech App!
1. Download the exe located in the `releases` section of this github repo 
2. Double click to run the `synthesize_speech-advanced.exe`
3. A warning should pop up
    - Click `more info`
    - Click `Run anyway`

## Step 6: Add Poly Speech to All Programs in Windows (Optional)
1. Right click on the exe and select `create desktop shortcut` 
2. Cut and paste desktop shortcut to the path below `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`
3. renaming the shortcut will also rename how the app appears when you search for it and it will not break the link
