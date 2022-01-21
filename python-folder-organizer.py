import os
from pathlib import Path
import shutil
from win10toast import ToastNotifier
from datetime import datetime, timedelta
import send2trash
import PyPDF2
import textract

pathsToClean = []
folders = []

def setup ():
    # path, bool delete after time, bool delete empty folders, bool delete links, bool clean up folders
    newPathToClean(Path(r'C:\\', 'Users', 'Nikolaj Licht', 'OneDrive', 'Skrivebord'), False, True, True, True)
    #newPathToClean(Path(r'C:\\', 'Users', 'Public', 'Desktop'), False, False, True, True)
    newPathToClean(Path(r'C:\\', 'Users', 'Nikolaj Licht', 'Downloads'), True, True, True, True)


    # Foldername, lifetime of files, ...filetypes
    registerFolder("Images", 7, 'jpg', 'jpeg', 'gif', 'png', 'ico')
    registerFolder("Texts", 7,'mobi', 'epub', 'pdf', 'word', 'txt')
    registerFolder("Executables", 7, 'exe', 'msi', 'jar')
    registerFolder("Compressed", 7, 'rar', 'zip', '7z')
    registerFolder("Audio", 7, 'wav', 'mp3')
    registerFolder("Video", 7, 'mpeg', 'mov', 'mp4', 'webm', 'avi', 'avchd', 'm4p', 'mkv')
    registerFolder("Builds", 7, 'apk')
    registerFolder("3D", 7, 'blend', 'blend1', 'blend2', 'fbx', 'obj', 'stl', 'ply', 'dae', '3ds', 'stp', 'ma', 'c4d', 'mb')
    registerFolder("Game Dev", 7, 'shader', 'asset', 'unity', 'cs', 'tscn')
    registerFolder("Web", 7, 'php', 'js', 'scss', 'css', 'html')
    registerFolder("Design", 7, 'ai', 'svg', 'afdesign', 'afphoto', 'afpublisher')
    registerFolder("Fonts", 7, 'otf', 'ttf')
    registerFolder("Programming", 7, 'py', 'rb')

    
def main ():
    setup()
    
    for path in pathsToClean:
        if path["cleanUpPath"]:
            if (path["path"].exists()):
                # Go to paths
                os.chdir(path["path"])


                for folder in folders:
                    #create folder if not exists
                    newFilePath = makeNewFolder(folder['name'])

                    for fileType in folder['fileTypes']:
                        
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

        if path["deleteShortcuts"]:
            deleteShortcuts(path)

    windowsToast()

def makeNewFolder(foldername):
    registerFolderPath = Path.cwd() / foldername
    if not registerFolderPath.is_dir():
        print('Trying to create folder [' + foldername + '] in path:' + str(Path.cwd()))
        os.makedirs(foldername)
        print('Created new folder - ' + foldername)
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

def deleteShortcuts(path):
    if path["path"].exists():
        os.chdir(Path(path["path"]))
        for windowsshortcut in list(Path.cwd().glob('*.lnk')):
            print(windowsshortcut)
            send2trash.send2trash(windowsshortcut.name)

def sortTextsBasedOnContent(path):
    pass
    #go to text folder
    #for each text, check against keyword collection
    #put into folder if match
    #consider where folder should be

    #if path["path"].exists():
        #for folder in folders:
            #if Path(path["path"] / folder["name"]).exists():
                #os.chdir(Path(path["path"] / folder["name"]))
                 
                #for afile in list(Path.cwd().glob('*')):
                    #if os.path.getmtime(str(afile)) < expirationDate:
                        #pass

    #Make this arguemtn optional like sortTextsOnContent=True
    #For each file that is pdf / text use 
    #https://medium.com/better-programming/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f
    #for reading the content, and if the content contains keywords (stored in a seperate file) like name, address, order, invoice
    #put into folder with important information

def registerFolder(name, fileLifeTimeInDays, *args):
    folder = {}
    folder['name'] = name
    folder['fileLifeTime'] = fileLifeTimeInDays
    folder['fileTypes'] = []
    for ft in args:
        folder['fileTypes'].append(ft)
    folders.append(folder)

def newPathToClean(path, deleteFilesAfterTime, deleteEmptyFolders, deleteShortcuts, cleanUpPath):
    newPath = {
            'path': path,
            'deleteFilesAfterTime': deleteFilesAfterTime,
            'deleteEmptyFolders' : deleteEmptyFolders,
            'deleteShortcuts' : deleteShortcuts,
            'cleanUpPath' : cleanUpPath
            }
    pathsToClean.append(newPath)
    print("added path" + str(path))


def windowsToast():
    notificationText = ""
    for path in pathsToClean:
        notificationText = notificationText + str(path["path"]).split(os.sep)[-1] + ', '
    notificationText = notificationText[:-2]
    notificationText = notificationText + " --> clean"
    toaster = ToastNotifier()
    toaster.show_toast("Cleaned up folders for you", notificationText)


main()

