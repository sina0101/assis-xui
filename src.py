import sqlite3

db=sqlite3.connect('/etc/x-ui/x-ui.db')
#db=sqlite3.connect('xui.db')
cur=db.cursor()



def extact_id():
    
    IDs=cur.execute(""" SELECT id  , expiry_time ,total  FROM client_traffics""")
    IDs=list(IDs)
    
    return IDs


def add_trafic(trafic_addition,IDs):
    trafic_addition=trafic_addition*1024*1024*1000
    for i in IDs:
        
        if i[2]>0:
            cur.execute("""UPDATE client_traffics SET total=?  WHERE id = ?""",(i[2]+trafic_addition,i[0]))


    db.commit()
    


def add_time(time_day_addition,IDs):
    time_milisecend_addition=time_day_addition*24*60*60*1000
    for i in IDs:
        if i[1]>0:
            cur.execute("""UPDATE client_traffics SET expiry_time=? WHERE id=?""",(time_milisecend_addition+i[1],i[0]))

    db.commit()
    

def add_user():
    uname=input('please input username: ')
    password=input('please input password: ')
    cur.execute("""INSERT INTO users (username , password ,login_secret) VALUES(?,?,?)""",(uname,password,''))

    db.commit()

    

def del_user():
    show_all_admin()
    id_for_delete=input('please input id for admin you will be delete: ')
    cur.execute("""DELETE FROM users WHERE id=?""",(id_for_delete,))

    db.commit()
    

def show_all_admin():

    users=cur.execute("""SELECT id,username,password FROM users""")
    

    print("+============================================================================+")
    print("|==============================    X-UI Users   POWER BY SINA0101  ============================|")
    print("|==============================    github : SINA0101  ============================|")
    print("+============================================================================+")
    header = "| {:^5} | {:^20} | {:^20} |".format('ID', 'Username', 'Password')
    separator = "+{:-^7}+{:-^22}+{:-^22}+".format('', '', '')
    print(separator)
    print(header)
    
    for user in users:
        print("| {:^5} | {:^20} | {:^20} |".format(user[0], user[1], user[2]))
        


    

IDs=extact_id()
def start():
    
    print("+============================================================================+")
    print("|==============================    X-UI ASSIS - POWER BY SINA0101    ============================|")
    print("|==============================    github : SINA0101  ============================|")
    print("+============================================================================+")

    print ('1-add traffic for all active users')
    print ('2-add time for all active users')
    print ('3-add user ')
    print ('4-delete user ')
    print ('5-show all user')
    print ('6-exit')
    inp1=int(input('enter a number: '))
    if inp1 not in [1,2,3,4,5,6]:
        print ('please enter 1 or 2 or 3 or 4 or 5 or 6') 
        exit
    else:
        return inp1
inp1=start()



if inp1==1:
    trafic_addition=int(input('enter how many GB??'))
    add_trafic(trafic_addition,IDs)
    print ('added traffic for all users...')


if inp1==2:
    time_day_addition=int(input('enter how many DAYs??'))
    add_time(time_day_addition,IDs)
    print ('added time for all users...')


if inp1==3:
    show_all_admin()
    add_user()

if inp1==4:
    del_user()

if inp1==5:
    show_all_admin()

if inp1==6:
    exit
