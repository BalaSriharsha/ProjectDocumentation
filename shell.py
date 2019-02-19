import os
import sys
from subprocess import call

repofile = open('repositories.txt','r')

repofile_content = list(repofile)
os.chdir("Repositories")
for con in repofile_content:
#    print(con)
    url_branch = con.split(',')
    url = url_branch[0]
#    print(url)
    branch = url_branch[1]
    url_dup = list(url)
    url_dup = url_dup[::-1]
#    print(url_dup)
    dot = url_dup.index('.')
    slash = url_dup.index('/')
    repo_name = []
    for j in range(dot+1,slash):
        repo_name.append(url_dup[j])
    repo_name = repo_name[::-1]
    repo_name="".join(repo_name)
#    print(repo_name)
    if(os.path.isdir("./"+repo_name)==True):
        os.chdir(repo_name)
        os.system("git pull origin "+branch)
        os.chdir("..")
    else:
        os.system("git clone "+url)

repos = []
files = os.listdir()
for i in files:
    repos.append(i)

#migrating to public_docs folder
try:
    os.chdir("../public_docs")
except:
    print("Public Docs Folder not Found")


for i in repos:
    os.system("mkdir "+i)


#migrating to docs folder
try:
    os.chdir("../docs")
except:
    print("Docs folder not found")


for i in repos:
    os.system("mkdir "+i)

#migrating to repositories folder
os.chdir("../Repositories")
for i in repos:
    os.chdir(i)
    try:
        os.system("cp -r public_docs/* ../../public_docs/"+i+"/")
    except:
        print("Public Docs is an Empty Directory")
    try:
        os.system("cp -r docs/* ../../docs/"+i+"/")
    except:
        print("Docs is an Empty Directory")

os.chdir("../../")
#os.system("pwd")
os.system("make html")

os.system("cp -r ./_build/html/* /var/www/html")

