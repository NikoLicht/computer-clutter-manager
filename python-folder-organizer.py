import os
from pathlib import Path
import shutil
from win10toast import ToastNotifier
from datetime import datetime, timedelta
import send2trash

pathsToClean = []
folders = []

def setup ():
    # path, should delete after time, should delete empty folders
    newPathToClean(Path(r'C:\\', 'Users', 'Nikolaj Licht', 'Downloads'), True, True)
    newPathToClean(Path(r'C:\\', 'Users', 'Nikolaj Licht', 'Desktop'), False, True)

    # Foldername, lifetime of files, ...filetypes
    newFolder("Images", 7, 'jpg', 'jpeg', 'gif', 'png', 'ico')
    newFolder("Texts", 7, 'pdf', 'word', 'txt')
    newFolder("Executables", 7, 'exe', 'msi', 'jar')
    newFolder("Compressed", 7, 'rar', 'zip', '7z')
    newFolder("Audio", 7, 'wav', 'mp3', 'webm', 'mov')
    newFolder("Builds", 7, 'apk')

    
def main ():
    setup()
    
    for path in pathsToClean:
        if (path["path"].exists()):
            # Go to paths
            os.chdir(path["path"])


            for folder in folders:
                #create folder if not exists
                newFilePath = makeNewFolder(folder['name'])

                for fileType in folder['fileTypes']:
                    print(fileType)
                    
                    for messyFile in list(path["path"].glob('*.' + fileType)):
                        messyPath = Path(messyFile)
                        shutil.move(messyPath, newFilePath / messyPath.name)
                        print(messyFile)

        else:
            print('could not find path: ' + str(path["path"]))

        if path["deleteFilesAfterTime"]:
            deleteOldFiles(path)

        if path["deleteEmptyFolders"]:
            deleteEmptyFolders(path)

    windowsToast()

def makeNewFolder(foldername):
    newFolderPath = Path.cwd() / foldername
    if not newFolderPath.is_dir():
        os.makedirs(foldername)
        print('successfully created new folder')
    else:
        print('folder ' + foldername + ' already exists, no new folder added')
    
    return Path(Path.cwd() / foldername)

def deleteOldFiles(path):
    if path["path"].exists():
        for folder in folders:
            expirationDate = (datetime.today() - timedelta(days = folder["fileLifeTime"])).timestamp()
            if Path(path["path"] / folder["name"]).exists():
                os.chdir(Path(path["path"] / folder["name"]))
                 
                for afile in list(Path.cwd().glob('*')):
                    if os.path.getmtime(str(afile)) < expirationDate:
                        print ("deleting File " + afile.name)
                        send2trash.send2trash(afile.name)

def deleteEmptyFolders(path):
    if path["path"].exists():
        for folder in folders:
            if Path(path["path"] / folder["name"]).exists():
                os.chdir(path["path"])
                if not os.listdir(path["path"] / folder["name"]):
                    print("deleting folder " + str(path["path"] / folder["name"]))
                    os.rmdir(path["path"] / folder["name"])

def newFolder(name, fileLifeTimeInDays, *args):
    folder = {}
    folder['name'] = name
    folder['fileLifeTime'] = fileLifeTimeInDays
    folder['fileTypes'] = []
    for ft in args:
        folder['fileTypes'].append(ft)
    folders.append(folder)

def newPathToClean(path, deleteFilesAfterTime, deleteEmptyFolders):
    newPath = {
            'path': path,
            'deleteFilesAfterTime': deleteFilesAfterTime,
            'deleteEmptyFolders' : deleteEmptyFolders
            }
    pathsToClean.append(newPath)


def windowsToast():
    notificationText = ""
    for path in pathsToClean:
        notificationText = notificationText + str(path["path"]).split(os.sep)[-1] + ', '
    notificationText = notificationText[:-2]
    notificationText = notificationText + " --> clean"
    toaster = ToastNotifier()
    toaster.show_toast("Cleaned up folders for you", notificationText)


main()

