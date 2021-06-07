from time import sleep
import paramiko
from zipfile import ZipFile
import os.path
from os import path


def get_all_paths(directory):
    
    file_paths = []
    
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root,filename)
            file_paths.append(filepath)

    return file_paths


def main():
    directory = input("Enter what directory you want to zip: ")

    file_paths = get_all_paths(directory)

    print("Following files will be zipped: ")
    for file_name in file_paths:
        print(file_name)

    with ZipFile("backup.zip", "w") as zip:
        for file in file_paths:
            zip.write(file)
    print("\nbackup.zip zipped successfully!\n")


if __name__ == "__main__":
    main()

host = input("Hostname: ")
port = 2222
username = input("Username: ")
password = input("Password: ")


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

sftp = ssh.open_sftp()

def file():
    local_path = "backup.zip"
    remote_path = "/mnt/volume_nyc1_01/" + local_path

    #sftp.put(local_path, remote_path)



    if path.exists(local_path):
        sftp.put(local_path, remote_path)
    else:
        print("Try again")

    print("Uploading...")

    sleep(2)

    print("Uploaded!")

file()

if path.exists("backup.zip"):
    os.remove("backup.zip")
    print("\nbackup.zip removed locally and uploaded to remote server!")
else:
    None


sftp.close()
ssh.close()