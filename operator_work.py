import mysql.connector
class operator():
    a=mysql.connector.connect(host="localhost",user="root",password="jamali123",database="nadra")
    cur=a.cursor()
    desc_query="desc new_nadra_database"
    show_query="select * from new_nadra_database"
    cur.execute(desc_query)
    desc = cur.fetchall()
    print("Table Description: ",desc)
    cur.execute(show_query)
    show=cur.fetchall()
    print("Table Is: ",show)

    def inserting(self,name,age,city):
        query_insert=f"insert into new_nadra_database(Name,Age,City)values('{name}',{age},'{city}')"
        self.cur.execute(query_insert)
        self.a.commit()
        print("Value inserted Sccesfully")


    def modify_stru(self,modify):
        if modify==1:
            add_column=input("Enter properly Column Name and datatype & size :")
            add_query=f"alter table new_nadra_database add column {add_column}"
            print("Column Added Sccesfully")
            self.cur.execute(add_query)
            self.a.commit()


        elif modify==2:
            drop_column=input("Which Column You want to drop :")
            drop_query=f"alter table new_nadra_database drop column {drop_column}"
            print("Column Droped Sccesfully")
            self.cur.execute(drop_query)
            self.a.commit()

    def changing_name(self,previous_name,new_name):
        update_query=f"alter table new_nadra_database change {previous_name} {new_name}"
        self.cur.execute(update_query)
        self.a.commit()
        print("Updated Sccesfully")


    def clear_table(self,warning):
        if warning==1:
            user=input("Last Warning it will Not Recover if sure then enter table name :")
            delete_query=f"truncate table {user}"
            self.cur.execute(delete_query)
            self.a.commit()
        elif warning==2:
            print("Your Table Is Safe")
        else:
            print("Invalid Option")

obj=operator()

while True:
    print("How Can I Help You\n1:Insert data\n2:Add or Drop Column\n3:Change Column name\n4:clear table\n5:Exit")
    user=int(input("Select Your Option :"))
    match user:
        case 1:
            name=input("Enter Name :").capitalize()
            age=int(input("Enter Age :"))
            city=input("Enter City :").capitalize()
            obj.inserting(name,age,city)
        case 2:
            modify = int(input("Which modification you want\n1:Add Column\n2:Drop Column :"))
            obj.modify_stru(modify)
        case 3:
            previous_name = input("Enter Column Prevous name :")
            new_name = input("Enter Column New Name with datatype and size :")
            obj.changing_name(previous_name,new_name)

        case 4:
            warning = int(input("Warning Are You Sure YouWant To Delete Table\n1:Yes\n2:no :"))
            obj.clear_table(warning)
        case 5:
            print("Thankyou for using this App")
            break
        case _:
            print("invalid Option")
