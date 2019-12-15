import sqlite3 as lite

# functionality 

class DatabaseManager(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('crash.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF EXISTS crashtb(Id INTEGER PRIMARY KEY AUTOINCREMENET, name TEXT, desc TEXT,price TEXT,is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("unable to create DB")
            
    def insert_data(self,data):

        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO crashtb(name, desc, price, is_private)VALUES(?,?,?)",data)
            return True
     
        except Exception:
            return False

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM crashtb")
                return cur.fetchall
        
        except Exception:
            return False
    
    def delete_data(self,id):
        try:
            with con: 
                cur = con.cursor()
                sql = "DELETE FROM crashtb WHERE id = ?"
                cur.execute(sql,[id])
                return True
        except Exception:
            return False


# TODO: interface

def main():
    print("*"*40)
    print("\n ::crash management")
    print("\n")
    db = DatabaseManager()
    print("#"*40)
    print("\nUser Manual\n")
    print("1.Insert a course")
    print("2.Show all course")
    print("3.Delete a course")
    print("#"*40)

    choice = input("\n Enter a choice :")

    if choice == "1":
        name = input("\n enter course name :")
        desc = input("\n enter course desc :")
        price = input("\n enter course price :")
        # is_private = input("\n is this course private :")

        if db.insert_data([name,desc,price]):
            print("Course Added :)")
        else:
            print("OOPS Something is wrong")

    elif choice == "2":
        print("\nCourse list")
        for index,item in enumerate(db.fetch_data()):
            print("\nCourse ID :"+ str(item[0]))
            print("\nCourse Name :"+ str(item[1]))
            print("\nCourse Desc :"+ str(item[2]))
            print("\nCourse Price :"+ str(item[3]))
            # private = 'Yes' if item[4] else 'NO'
            # print("\nCourse Private :"+ private)
    
    elif choice == "3":
        record_id = input("Enter the course ID")
        if db.delete_data(record_id):
            print("Course Deleted ")
        else:
            print("oops something went wrong")
    else:
        print("BAD Choice")



if __name__ == '__main__':
    main()

    