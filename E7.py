import shutil
name=input('Enter zip file name: ')
directory=input('Enter file directory: ')
shutil.make_archive(name,'zip',directory)