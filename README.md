# Summary

This set of instructions refers to an array of Bash and Python scripts used in production in the Digital Imaging Unit. Included are instructions for setup, running the scripts, and various considerations for running the scripts in a mac environment connected to networked storage. The scripts referred to below were designed to efficiently move files around the lab or to and from the server, rename files to Image ID from capture sequence and vice versa, or to create derivatives from files intended for the repository. The setup instructions described below have been completed on all DIU computers at the time of this writing, but have been written out here for reference in case steps need to be retraced in the future. 

[Session Merger](#bookmark=id.7upfm3mpw9ob)

[Upload](#bookmark=kix.gmv8p7i4oipp)

[Sequencer](#bookmark=kix.3fmyvt42e5a1)

[Renamer](#bookmark=id.898vujkuzsed)

[Denamer](#bookmark=id.io00epgevn6d)

[PDF Maker](#bookmark=id.tqi13t9mp977)

[Move to RTG](#bookmark=id.jdb91g57te1)

[Transfer](#bookmark=id.1fydidbctiz7)

[Setup Instructions](#bookmark=id.oyb2v1ktz1y3)

# Using the Scripts

## Session Merger

Session Merger is a python script that uses rsync to merge all Capture files from one Capture One session to another. This script is designed to be used before files have been processed and does not copy over any files from the Selects, Output, or Trash folders from a session. The goal in writing this script was to streamline the process of merging sessions without relying on Finder/OSX merge functionality which can be problematic and will overwrite files if there are any duplicate filenames. The script will work to combine any two in-progress sessions, but was primarily intended to make session merging simpler on the book scanner.

 1. Open Terminal

 2. Type **sessionmerger**

 3. When prompted to drag in your Capture folder, drag the Capture folder from your Capture One session that you'd like to work with after the merge and press return.

 4. When prompted to drag in your Capture folder again, drag the Capture folder from the session where your additional files to be merged are located and press return

 5. The script will then use rsync to merge all captures and settings files from the second Capture One session into the first.

Things to Consider:

 * You'll need two sessions handy that you'd like to merge.

 * Session merger works recursively and will grab everything in the Capture folder you'd like to move, including all settings files (crops, moire adjustments, neutral balance, etc.)

 * You may have better luck merging sessions if Capture One is closed. Having it open can confuse the connection to the new settings files 

 * If you need to merge two sessions on two different computers, it may be easiest to first upload the Capture folder from one session to the server. Sessions can then be merged directly from the server.

## Upload

Upload is a bash script that uses rsync to copy all files in a directory to another directory. This script is designed to be used as a shortcut to the common rsync command for uploading files to the server. The command replaced by this shortcut is as follows: 

**rsync -ratvhP /path/to/directory/with/files/* [target]**

Once files have been uploaded and verified by rsync, this script takes the directory of tif files on the server as input and creates jpeg copies with a long dimension of 3500 pixels. Jpeg derivatives are then moved to a subfolder within the original directory with the name "QC". Because files uploaded by the DIU can be large in size and number, Finder and Bridge may have difficulty loading icon previews efficiently enough to allow for a quick look at crops, rotations, etc. This script is designed to create a folder of derivatives from finalized and uploaded files that can be scrolled through quickly when performing quality control at the icon level.

> 1. Open Terminal

> 2. Type **upload**

> 3. When prompted to drag in your output folder, drag the output folder from your Capture One session (or any other folder with files you'd like to move to the server) into Terminal and press return

> 4. When prompted to drag in your destination folder, drag the folder from the server where you'd like your files to be transferred. Press return and your files will be uploaded.

> 5. Once upload is complete and verified, jpeg copies of all tif files will be created within the directory and then moved to a QC folder.

Things to Consider:

> * You'll need to create your destination folder on the server 

> * Upload works recursively and will grab everything in the folder you'd like to move, including files in subfolders. This means the CaptureOne folder within your Output folder will move to the server when uploading. This will work to your advantage if you'd like to upload an entire session to the server.

> * Upload sets permissions for the destination folder and all files uploaded so that everyone can read, write, and execute the files. 

> * The -a flag will preserve original timestamps after upload

> * The Imagemagick command that creates derivatives will only convert tif files. Jpeg derivatives will be named according to the tif files they are cut from. Tifs can be named by capture sequence or Image ID.

> * Jpegs will be created for both s and u files.

> * S files with a long edge shorter than 3500 pixels will be upconverted to 3500 pixels. This will have no effect at the icon view, but will be pixelated when enlarged. If you need to take a closer look at a file, open the tif. 

## Sequencer

Similar to Renamer, Sequencer is a Python script that takes a directory as input and renames the files within that directory. However, Sequencer is designed for a specific use case when there are gaps in the file naming sequence before renaming to Image IDs (as when an extra capture is found during QC and deleted from the server or local Output folder). 

> 1. Open Terminal

> 2. Type **sequencer**

> 3. When prompted to enter directory, drag the folder with your files into Terminal and press return

Things to Consider:

> * Sequencer will rename tifs or jpegs. Files must be named by capture sequence and be appended with either an 's' or a 'u'. Files without 's' or 'u' will not be resequenced.

> * Tifs and jpegs should be in separate folders. The script will exit without resequencing if both file types are present in your folder.

> * When naming your files by capture sequence, make sure there are no leading zeros in the file names. Use a 1-digit batch renamer in Capture One or in Better Finder to rename large batches of files to capture sequence.

> * Double check that your images match the capture sequence on the work order. 

## Renamer

Renamer is a Python script that takes a directory as input and renames the files within that directory, exchanging capture sequence for Capture IDs. Use this script to rename files at the end of the quality control process when all images named by capture sequence correctly match captures on a work order.

> 1. Open Terminal

> 2. Type **renamer**

> 3. When prompted to enter directory, drag the folder with your files into Terminal and press return

> 4. When prompted to enter Image IDs, go to your work order and click the Copy all Capture IDs link. This copies all image IDs on the work order to the clipboard in a comma-separated list. 

> 5. Return to Terminal and paste your Image IDs. Press return. 

Things to Consider:

> * Renamer will rename tifs or jpegs. Tifs must be named by capture sequence and be appended with either an "s" or a "u". Jpegs must be named by capture sequence only.

> * When naming your files by capture sequence, make sure there are no leading zeros in the file names. Use a 1-digit batch renamer in Capture One or in Better Finder to rename large batches of files to capture sequence.

> * Double check that your images match the capture sequence on the work order. 

> * Double check that the number of images uploaded is twice the number of captures on your work order, if uploading s and u files. If not, make certain that only the uploaded files are needed to complete the work order.

> * Be sure to remember to complete the renaming step in the workflow before moving files to RTG. Otherwise, we'll end up with a lot of 1s.tif, 1u.tif, 2s.tif, etc. files in the repository with no linked metadata.

> * Make sure that no spaces are present between elements of the directory file name. Use underscores in place of spaces. The Renamer process will fail when spaces are present.

## Denamer

Denamer is the undo for Renamer. Denamer is a Python script that takes a directory as input and renames the files within that directory from Image ID to capture sequence. Once files have been renamed by mapping across rows in the work order, it may not be simple to batch rename by another method if any capture sequence or Image IDs are nonsequential. Use denamer if necessary at the end of the quality control process if all images named by Image ID need to be converted back to capture sequence, e.g., when a new capture needs to be added in the middle of the capture sequence.

> 1. Open Terminal

> 2. Type **denamer**

> 3. When prompted to enter directory, drag the folder with your files into Terminal and press return

> 4. When prompted to enter Image IDs, go to your work order and click the Copy all Capture IDs link. This copies all image IDs on the work order to the clipboard in a comma-separated list. 

> 5. Return to Terminal and paste your Image IDs. Press return. 

Things to Consider:

> * Note you will still need to enter Image IDs even though the final output will be a directory of files named according to capture sequence. Entering Image IDs is necessary to create the correct mapping across the rows of the work order.

> * Denamer will rename tifs or jpegs. Tifs must be named by Image ID and be appended with either an "s" or a "u". Jpegs must be named by Image ID only.

> * Double check that your images named by Image ID match the capture sequence on the work order. 

> * Double check that the number of images uploaded is twice the number of captures on your work order, if uploading s and u files. If not, make certain that only the uploaded files are needed for denaming.

> * Make sure that no spaces are present between elements of the directory file name. Use underscores in place of spaces. The Denamer process will fail when spaces are present.

## PDF Maker

PDF Maker is a Bash script that creates pdf files for public order delivery, often for full book scans. The script takes a directory of tif files as input and creates jpeg copies with a long dimension of 1600 pixels before creating a pdf from the jpegs. Pdfs are moved into ice.repo.nypl.org/ifs/ice/PDF_Storage where they can be retrieved by Permissions for delivery. 

> 1. Open Terminal

> 2. Type **pdfmaker**

> 3. When prompted to enter directory, drag the folder with your files into Terminal and press return

> 4. Jpeg derivatives of all s files will be created within the directory and a pdf will be created from these jpegs. 

> 5. The pdf will take the name of the directory dragged into Terminal

> 6. The pdf will be moved into ice.repo.nypl.org/ifs/ice/PDF_Storage

> 7. All jpegs in the folder will be deleted

Things to Consider:

> * Pdf maker will only create jpegs from s files. Files must be tifs.

> * Images in the pdf will be ordered numerically according to filename. Pdf maker will work after files have been named by Image ID, but if Image IDs are out of sequence so it will be in the pdf. Pdf maker is best used when images are still named by capture sequence. Use denamer if necessary.

> * Jpegs created from tifs named by capture sequence are given leading zeros to avoid strict alphabetical ordering issues, giving all jpegs 4-digit filenames. If files are named with Image ID or have filenames longer than 4-digits, the logic does not apply. 

## Move to RTG

Move to RTG is a bash script that uses rsync to move all tif files in a directory to to the ready to go folder for processing. This script is designed to eliminate drag and drop Finder transfers for files with an immediate deadline (all other files should be moved to rtg via nightly cron job). The script will not move jpegs, CaptureOne folders, or files with Image IDs with less than 5-digits and will provide feedback when your folder has no tif files or your files need to be renamed. The script also removes source files. The command replaced by this shortcut is as follows:

**rsync -rtvhP --remove-source-files [source files] [target]**

> 1. Open Terminal

> 2. Type **movetortg**

> 3. When prompted to drag in your folder to send to rtg, drag your folder from the server with files that have passed QC into Terminal and press return

> 4. All tif files with filenames longer than 4-digits will be moved to the rtg folder for processing

Things to Consider:

> * Jpegs, files with 4-digit or fewer filenames, and CaptureOne folders are excluded

> * Movetortg is set to work work recursively, so files in subfolders will also move to rtg if a parent folder is dragged into the Terminal window. 

> * Source files are removed from original folder

## Transfer

Transfer is a python script that uses scp (secure copy) to copy all files in a directory to another computer. The script will copy files between any two computers in the DIU, including the SASB workstation. Files can either be moved from another computer to the computer you're currently working on, or vice versa. The script will guide you through the process to help you specify which directories will be moved to which location. 

> 1. Open Terminal

> 2. Type **transfer**

> 3. You'll be asked whether the files you'd like to move are on the computer you're currently working on. Answer y or n (not case sensitive).

> 4. If you answer y, you'll be asked to drag in the folder you'd like to move

> 5. You'll then be asked which computer you'd like to move the folder to and you're provided with a list of computer nicknames. Type in the nickname of the computer you'd like to move your files to exactly as you see it printed in the dialog and press return

> 6. Next, you'll be given a list of hard drives on the remote computer. Copy and paste the name of the hard drive you'd like to send the files to and press return

> 7. Your files will copy to the remote computer

> 8. If you answered n to the first question, you'll be asked instead for the name of the computer where the files you'd like to transfer are located. Type the nickname of the computer into Terminal exactly as you see it and press return

> 9. Copy and paste the name of the hard drive where your files live and press return

> 10. Copy and paste the name of the folder you'd like to copy and press return

> 11. Drag in the folder from the computer you're working on where you'd like the files to copy to and press return

> 12. Your files will copy to your computer

Things to Consider:

> * If you're copying a directory from another computer to the computer you're currently working on, you'll need to create your destination folder if not copying to the root of the drive. You can drag this folder into the Terminal window in the last step.

> * Transfer works recursively and will grab everything in the folder you'd like to move, including files in subfolders and the folder itself. 

> * You can exit at any time by hitting Control+C, even if files have already started to transfer.

> * Permissions are set recursively to full read, write, and execute to prevent permissions problems when transferring sessions.

# Setup Instructions 

### Placing scripts in /usr/local/bin

The scripts are stored on ICE (ice.repo.nypl.org/ifs/ice) under Info/Scripts. Scripts will need to be copied into your usr/local/bin before they can be used. The usr/local/bin is a safe space to call scripts from and is included in the folders that Terminal searches when commands are run (your PATH). Navigate to the usr/local/bin by using the Go to Folder function in Finder or using the Shift+Command+G key combination and entering "/usr/local/bin". If Finder says the folder can't be found, you'll need to create it. Navigate to /usr first and then create a new folder called "local". Navigate to the local folder and create another folder within it with the name "bin". Alternatively, you can type **cd /usr** in Terminal to change the directory to /usr and press return. Then type **mkdir local** to make a local folder and press return. Type **cd local** to change the directory to local and press return. Then type **mkdir bin** to create a bin folder.

### Adding Executable Permission

Scripts will need executable permission added to the files in order to run them, if the permission hasn't been added already. To test this, you can drag the script into Terminal and press return. Terminal will give you a Permission denied error if the script is not executable. To add executable permission type **chmod +x** into Terminal and then drag in your script and press return. Terminal will give you a new Bash prompt and your script should now be ready to go.

### Creating Aliases

Nicknames can be created for scripts or Bash command you use often by editing your Bash profile in a Terminal application called Nano (or Vim if you wish). Nano is a command line text editor that can edit system files. To edit your bash profile, type **nano .bash_profile** in Terminal and press return. There may be aliases already set up on your computer, in which case you'll see some text in Nano. If no aliases have been set up, your Nano screen will be blank. In order to create a new alias, you'll need to add a basic equivalency statement to the .bash_profile using the following example as a pattern: 

**alias renamer="/usr/local/bin/renamer.py" **

In this example we're telling Terminal that we'd like to run the renamer.py script, which is located in the usr/local/bin, by typing "renamer" into Terminal. You may want to leave yourself a note about the alias being added to Terminal in case it becomes unclear in the future. To do this, write a note above the script and convert it to a comment by beginning with #. Comments are not read by the system. See the following as an example:

**#adding alias to terminal to call renamer script from /usr/local/bin**

Once the statement has been added to the profile, press Control+x and then press Y when asked about saving the modified buffer and then press return to write to the .bash_profile system file. Type **source .bash_profile** to load the new alias for immediate use. Now, when you type **renamer** in Terminal, the script will run without any further input. 

### Installing Dependencies

Many of the scripts included here require additional applications to be installed through Terminal before they can be run. The renamer, denamer, and file transfer scripts rely entirely on Python or Bash, which are preinstalled in MacOS. However, the QC and pdfmaker scripts rely on ImageMagick and GNU parallel, both of which will need to be installed before those scripts can be run. ImageMagick is a powerful command line image editing application and GNU parallel is a shell tool that will allow multiple processes to be run on multiple cores of a single computer or across multiple computers at once. The simplest way to install ImageMagick and GNU parallel is through Homebrew, which is a command line package installer. Homebrew has a rather large library of precompiled packages (known as formula in Homebrew world) available on Github that can be downloaded and installed using the **brew install** command. Homebrew installs applications in their own folders in usr/local/Cellar folder and provides symbolic links in /usr/local. In other words, Homebrew installs command line applications in a way that can be easily undone and will not affect preinstalled applications. As of July 2017, Homebrew can be installed by pasting the following into Terminal:

**/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"**

Once Homebrew installation is complete, Homebrew can be used to install ImageMagick and GNU parallel. To install ImageMagick, type **brew install imagemagick** into Terminal and press return. To install GNU parallel, type **brew install parallel** and press return. After these applications have been installed, commands specific to ImageMagick or parallel can be run through a normal Terminal bash prompt or called by a script. Homebrew is not required beyond this point to run the applications. It's worth noting that GNU parallel will run a reminder to cite GNU parallel in any programs that rely on its usage. The reminder can be silenced by typing **parallel --citation** into a bash prompt. The program will then ask you to type **will cite** to turn off the reminder.

6/29/18 update - Upload has been rewritten as a python script with new dependencies, tqdm and joblib. These will need to be installed using pip (install instructions found at: [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)). After installing pip, tqdm and joblib can be installed with the **pip install** command. The pip install command may need to be preceeded by a **sudo -H**. The Session Merger script is also new as of 6/29/18 and also requires tqdm and joblib.

### SSH Keys

Transfer relies on shared ssh keys in order to connect to other machines on the network. Static IP addresses have been assigned (with assistance from ITG) to each DIU computer to facilitate seamless connections. A list of these IP addresses can be found at **ice.repo.nypl.org/ifs/ice/Info/Network/DIU_IP_Addresses.csv**. Instructions for sharing ssh keys between computers on the network can be found here: **[https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2). **Keys must be shared in both directions between all machines. Password verification can be turned off by modifying the sshd_config file as discussed in the ssh key sharing instructions linked above. 

