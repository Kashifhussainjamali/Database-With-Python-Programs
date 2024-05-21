import mysql.connector
import sys
class coder():
    a = mysql.connector.connect(host="localhost", user="root", password="jamali123", database="nadra")
    cur = a.cursor()
    def officer(self,name,id,post):
        '''officer=(ali,123,officer)'''
        user=[(name,id,post)]
        self.cur.execute(f"select * from employs_1 where name='{name}'and id={id} and post='{post}'")
        result_officer= self.cur.fetchall()
        if user==result_officer:
            sys.path.insert(1, "C:\\Users\Kashif\Desktop\python database\Task_3\officer")
            import officer_work
        else:
            print("Invalid Name Or Post")
    def operator(self,name,id,post):
        '''operator=(waqar,1234,operator)'''
        user_2=[(name,id,post)]
        self.cur.execute(f"select * from employs_1 where name='{name}'and id={id} and post='{post}'")
        result_operator= self.cur.fetchall()
        if user_2==result_operator:
            sys.path.insert(1, "C:\\Users\Kashif\Desktop\python database\Task_3\operator")
            import operator_work

        else:
            print("Invalid Name Or Post")

obj=coder()
user=int(input("Select Your Post\n1:Officer\n2:operator :"))
if user==1:
    print(obj.officer.__doc__)
elif user==2:
    print(obj.operator.__doc__)

name=input("Enter Your Name :")
id=int(input("Enter your Id :"))
post=input("Enter Your post :")
match user:
    case 1:
        obj.officer(name,id,post)
    case 2:
        obj.operator(name,id,post)
    case _:
        print("Invalid Option")
