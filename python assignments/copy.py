import shutil
  
# use copyfile()
f= open("JohnDeere_file.txt","a+")
f.close()
shutil.copyfile('Delta_file.txt',' JohnDeere_file.txt')