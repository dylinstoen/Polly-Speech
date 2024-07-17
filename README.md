Polly Desktop GUI is a user-friendly desktop application designed to leverage the powerful text-to-speech capabilities of Amazon Polly directly from your desktop. This application simplifies the process of converting text into natural-sounding speech, allowing users to either play the audio directly through their speakers or save it as an MP3 file for later use

---

# How to install

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
    - Set your `default region name` (e.g., `us-east-1`).
    - Set the `default output format` as `json`
    
## Step 4: Test Amazon Polly on your command prompt (Optional)
- test amazon polly running this command `aws polly synthesize-speech --output-format mp3 --voice-id Joanna --text "Hello, World" hello.mp3`
- This command will create an MP3 file named hello.mp3 with the spoken text “Hello, World”.

## Step 5. Run Synthesize Speech App!
1. Download the zip file [github](https://github.com/dylinstoen/Polly-Speech/) 
2. Unzip the `Poly Speech` folder anywhere on the computer
3. Open into it and double click on the `synthesize_speech-advanced.exe` to launch the app Polly Speech local desktop app

## Step 6: Add Poly Speech so its recognized as an official searchable Programs in Windows (Optional)
1. Right click on the exe and select `create desktop shortcut` 
2. Cut and paste desktop shortcut to the path below `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`
3. renaming the shortcut will also rename how the app appears when you search for it and it will not break the link
