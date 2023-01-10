from anonfile import AnonFile
from colorama import Fore
from pathlib import Path
import sys
import os 
anonfiles = AnonFile()


print(Fore.GREEN +"""
 █████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗██╔══██╗██╔══██╗╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██║  ██║███████║ ╚███╔╝ 
██╔══██║██║╚██╗██║██║   ██║██║  ██║██╔══██║ ██╔██╗ 
██║  ██║██║ ╚████║╚██████╔╝██████╔╝██║  ██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
""")

print(Fore.RED+"┌――――――┬―――――――――――――――――――┐")
print("| [1]  | ✶ "+Fore.YELLOW+"Download Files"+Fore.RED+"  |")         
print("| [2]  | ✶ "+Fore.YELLOW+"Upload Files "+Fore.RED+"   |")         
print("└――――――┴―――――――――――――――――――┘")
print()
print()
choice = input(Fore.GREEN + "[?] Enter choice > ")


# DOWNLOAD FILES FROM anonfiles.com
if choice == "1":
    target_dir = Path.home().joinpath('Downloads')
    os.system('cls')
    files_link = input("Enter link > ")
    input(Fore.YELLOW+"[INFO]" + "Ready ? (press enter) ")
    filename = anonfiles.download(files_link, path=target_dir)
    print(Fore.YELLOW+ "[INFO] "+filename)


# UPLOAD FILES TO anonfiles.com
if choice == '2':
    os.system('cls')
    path = input(Fore.YELLOW + "[+]"+Fore.RED+" > Enter Path to the file > ")
    input(Fore.YELLOW+"[INFO]" +Fore.GREEN+ " Ready ? (press enter) ")
    os.system('cls')
    files_upload = anonfiles.upload(path, progressbar=True)
    print(files_upload.url.geturl())
    input()
else:
    os.system('cls')
    print("[INFO] : Invalid Files")