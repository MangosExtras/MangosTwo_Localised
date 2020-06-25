# python3 py3MangosAddAllLangs_linux.py
import os

# select setting :
declaraction1 = """
*** will auto install all language Pakage ***
    only support python3 && linux.

# need <<<<<<<<<<<<<<<<<<
did you already have MangosTwo_Localised.git?
if haven't:
    please Ctrl+C; then
    git clone --recurse-submodules https://github.com/MangosExtras/MangosTwo_Localised.git

# how to use:
    python3 py3MangosAddAllLangs_linux.py
    
    
***all select can't null;***

# after setting
after install final.
goto rewrite mangosd.conf 

#    DBC.Locale
# DBC Language Settings
# 0 = English; 1 = Korean; 2 = French; 3 = German; 4 = Chinese; 5 = Taiwanese; 6 = Spanish;
# 255 = Auto Detect (Default)

example chinese : 
        DBC.Locale = 4


# other    
test environment : debian10, mysql8.0, gcc-8, python3.6, 2018-10-07; 
bug : QQ32686647; skype:fevefun@hotmail.com
test server : www.gamefunc.top

Thanks Mangos and everyone.
my english not good.
"""
print(declaraction1)


# setting other
path = input("enter your MangosTwo_Localised folder PATH(like: /root/MangosTwo_Localised/ ) : ")
path = path.strip()
if path[-1] != "/":
    path = path + "/"

selectSqlType = input("select you sql type Number(1=mysql, 2=mariaDB) (enter: 1 or 2) : ")
sqlHost = input("database connect Address is(like: 192.168.1.1 or 127.0.0.1) : ")
sqlPort = input("database connect Port is(like: 3306) : ")
sqlUserName = input("database connect UserName is(like: mangos or root) : ")
two_worldDBName = input("input worldDB in SQL's name(like: two_world or mangos2)  : ")

if len(path) < 2 or len(selectSqlType) == 0 or len(sqlHost) == 0 or len(sqlPort) == 0 or len(sqlUserName) == 0 or len(two_worldDBName) == 0:
    raise TypeError("all select must enter")


# get sql connect secert and set sqlExecCMD
if selectSqlType == "1":
    print("enter your sql connect PASSWORD ")
    secretCMD = "mysql_config_editor set --login-path=local --host={sqlHost} --port={sqlPort} --user={sqlUserName} --password --skip-warn".format(sqlHost=sqlHost, sqlPort=sqlPort, sqlUserName=sqlUserName)
    os.system(secretCMD)
    print(secretCMD)
    sqlExecCMD = "mysql --login-path=local -q -s " + two_worldDBName + " <  "
elif selectSqlType == "2":
    mariaPassword = intput ( "input your sql connect PASSWORD : ")
    sqlExecCMD = "mysql -h{sqlHost} -P{sqlPort} -u{sqlUserName} -p{mariaPassword}  {zero_worldDBName}  <  ".format(sqlHost=sqlHost, sqlPort=sqlPort, mariaPassword=mariaPassword, two_worldDBName=two_worldDBName)
else:
    raise TypeError("dbType Fail , when select sql Type must input 1 or 2 only")
    

# process start
for baseDBset in ["1_LocaleTablePrepare.sql", "2_Add_NewLocalisationFields.sql", "3_InitialSaveEnglish.sql"]:
    os.system(sqlExecCMD + path + baseDBset)
    print(sqlExecCMD + path + baseDBset)


# install language all folder
path2 = path + "Translations/" 
TranslationsALL = os.listdir(path2)
langFolders = []

for fName in  TranslationsALL:
    if os.path.isdir(path2 + fName) is True:
        langFolders.append(fName)
        
for langF in langFolders:
    path3 = path2 + langF + "/"
    files = os.listdir(path3)
    
    for filename in files:
        if os.path.isdir(path3 + filename) is True or filename.rsplit(".", 1)[1].lower() != "sql":
            continue
        else:
            print(sqlExecCMD  + path3 + filename)
            os.system(sqlExecCMD  + path3 + filename)


FinalSTR = """
*** all install final ok***

then:
    *** goto rewrite mangosd.conf ***
    
    #    DBC.Locale
    # DBC Language Settings
    # 0 = English; 1 = Korean; 2 = French; 3 = German; 4 = Chinese; 5 = Taiwanese; 6 = Spanish;
    # 255 = Auto Detect (Default)

    example chinese : (DBC.Locale = 4)

restart mangos server ;

bug : QQ32686647; skype:fevefun@hotmail.com



"""
print(FinalSTR)
