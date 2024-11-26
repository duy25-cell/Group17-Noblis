### Setting Up GNS3

Obtain images of devices that you would like to simulate. 
Open up GNS3, wait for local server to start, and create a project. 
Go to Preferences -> QEMU VM. Create new VM. Name your VM, and hit next. 
Keep default Binary setting, change RAM if you would like to, and hit next. 
Keep or change default console type, and hit next. Hit “New Image,” and browse to the image you want to upload, and allow GNS3 to copy image to the default image directory, then hit Finish. 
Then, hit Edit, go to HDD, and change Disc Interface to SCSI. Go to Network and change adapters to however many you would like, 12 or 16 should be suitable. 
Go to Advanced and add “-no-kvm” to speed up boot process. If this option breaks your image, do not add it. Hit OK, then hit Apply.
