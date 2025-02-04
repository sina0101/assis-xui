import sqlite3

def connect_db():
    return sqlite3.connect('/etc/x-ui/x-ui.db')

def extract_id():
    with connect_db() as db:
        cur = db.cursor()
        cur.execute("SELECT id, expiry_time, total FROM client_traffics")
        return list(cur.fetchall())

def add_traffic(trafic_addition, IDs):
    trafic_addition *= 1024 * 1024 * 1000
    with connect_db() as db:
        cur = db.cursor()
        for i in IDs:
            if i[2] > 0:
                cur.execute("UPDATE client_traffics SET total = ? WHERE id = ?", (i[2] + trafic_addition, i[0]))
        db.commit()
    print("✔ Traffic added for all users!")

def add_time(time_day_addition, IDs):
    time_millisec_addition = time_day_addition * 24 * 60 * 60 * 1000
    with connect_db() as db:
        cur = db.cursor()
        for i in IDs:
            if i[1] > 0:
                cur.execute("UPDATE client_traffics SET expiry_time = ? WHERE id = ?", (i[1] + time_millisec_addition, i[0]))
        db.commit()
    print("✔ Time added for all users!")

def add_user():
    uname = input('Enter username: ')
    password = input('Enter password: ')
    with connect_db() as db:
        cur = db.cursor()
        cur.execute("INSERT INTO users (username, password, login_secret) VALUES (?, ?, '')", (uname, password))
        db.commit()
    print(f"✔ Admin '{uname}' added successfully!")

def del_user():
    show_all_admin()
    id_for_delete = input('Enter the ID of the admin to delete: ')
    with connect_db() as db:
        cur = db.cursor()
        cur.execute("DELETE FROM users WHERE id = ?", (id_for_delete,))
        db.commit()
    print("✔ Admin deleted successfully!")

def show_all_admin():
    with connect_db() as db:
        cur = db.cursor()
        cur.execute("SELECT id, username, password FROM users")
        users = cur.fetchall()
    print("+========================================================+")
    print("|                     X-UI Admins                        |")
    print("+========================================================+")
    print(f"| {'ID':^5} | {'Username':^20} | {'Password':^20} |")
    print("+--------------------------------------------------------+")
    for user in users:
        print(f"| {user[0]:^5} | {user[1]:^20} | {user[2]:^20} |")
    print("+========================================================+")

def main():
    IDs = extract_id()
    while True:
        print("+========================================================+")
        print("|               X-UI Admin Panel - Sina0101             |")
        print("+========================================================+")
        print("1- Add traffic for all active users")
        print("2- Add time for all active users")
        print("3- Add ADMIN for panel")
        print("4- Delete ADMIN from panel")
        print("5- Show all ADMINs")
        print("6- Exit")
        choice = input("Enter a number: ")
        
        if choice == "1":
            trafic_addition = int(input("Enter traffic amount (GB): "))
            add_traffic(trafic_addition, IDs)
        elif choice == "2":
            time_day_addition = int(input("Enter duration (Days): "))
            add_time(time_day_addition, IDs)
        elif choice == "3":
            show_all_admin()
            add_user()
        elif choice == "4":
            del_user()
        elif choice == "5":
            show_all_admin()
        elif choice == "6":
            print("Exiting... ✅")
            break
        else:
            print("❌ Invalid choice! Please enter a valid number.")

main()
