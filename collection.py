import os
import win32security
import time
import csv

def get_owner(file):
    sid = win32security.GetFileSecurity(file, win32security.OWNER_SECURITY_INFORMATION)
    owner_sid = sid.GetSecurityDescriptorOwner()
    name, domain, _ = win32security.LookupAccountSid(None, owner_sid)
    return domain + "\\" + name

#--Collect filepath--

dir_path = input("Enter your filepath: ").strip()

#owner = get_owner(dir_path)

with open('.\CSV\datafile.csv', 'w', newline='') as csvfile:
    fieldnames = ['Path', 'File Name', 'File Owner', 'File Size', 'Created On', 'Last Touch', 'Last Access']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for folder_path, dirs, files in os.walk(dir_path):
        path = folder_path.split(os.sep)
        print((len(path) - 1) * '>', os.path.basename(folder_path))
    
        for file in files:
            file_path = os.path.join(folder_path, file)
            file_stats = os.stat(file_path)
                
            writer.writerow({'Path': folder_path,
                            'File Name': file, 
                            'File Owner': get_owner(file_path), 
                            'File Size': file_stats.st_size, 
                            'Created On': time.ctime(file_stats.st_ctime),
                            'Last Touch': time.ctime(file_stats.st_mtime),
                            'Last Access': time.ctime(file_stats.st_atime)})
