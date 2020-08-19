#Load the GoogleDrive package to access fileNames from gdrive
from google.colab import drive

#Add gdrive as mount point
drive.mount('/gdrive')
%cd /gdrive


