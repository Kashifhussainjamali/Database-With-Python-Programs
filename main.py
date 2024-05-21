class joinings():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",password="jamali123",database="kashif")
    cur=a.cursor()
    print("-" * 40, "Software_Developers", "-" * 40)
    table_1="select * from Software_Developer"
    cur.execute(table_1)
    sd_table=cur.fetchall()
    for x in sd_table:
        print(x)

    print("-"*40,"Shopping","-"*40)
    table_2="select * from shopping"
    cur.execute(table_2)
    s_table=cur.fetchall()
    for y in s_table:
        print(y)
    demo="-"*40+"Your Results"+"-"*40

    def inner(self,id,name):
        inner_query=f"select * from Software_Developer as d inner join shopping as s on s.id={id} and d.name='{name}'"
        self.cur.execute(inner_query)
        print(self.demo)
        inner_result=self.cur.fetchall()
        self.a.commit()
        print(inner_result)

    def left_joining(self,id,name):
        left_query=f"select * from Software_Developer as d left join shopping as s on s.id={id} and d.name='{name}'"
        self.cur.execute(left_query)
        left_result = self.cur.fetchall()
        self.a.commit()
        print(self.demo)
        for x in left_result:
            print(x)

    def right_joining(self,id,name):
        right_query=f"select * from Software_Developer as d right join shopping as s on s.id={id} and d.name='{name}'"
        self.cur.execute(right_query)
        right_result = self.cur.fetchall()
        self.a.commit()
        print(self.demo)
        for x in right_result:
            print(x)

    def full_join(self,id_1,id_2,name_1,name_2):
        full_query=(f'''select * from Software_Developer as d right join shopping as s on s.id={id_1} and d.name='{name_1}'
                        union
                        select * from Software_Developer as d left join shopping as s on s.id={id_2} and d.name='{name_2}' ''')
        print(self.demo)
        self.cur.execute(full_query)
        full_result=self.cur.fetchall()
        self.a.commit()
        for x in full_result:
            print(x)

    def view(self,table_name,column_1,column_2):
        create_view=f"create view {table_name} as select {column_1},{column_2} from Software_Developer"
        self.cur.execute(create_view)
        view_query=f"select * from {table_name}"
        self.cur.execute(view_query)
        result=self.cur.fetchall()
        self.a.commit()
        for x in result:
            print(x)


obj=joinings()
while True :
    print("*"*100)
    user=int(input('''Select Your Option\n1:Inner Joining\n2:Left Joining\n3:Right Joining\n4:Full Joining\n5:Create a view\n6:End Here :'''))
    match user:
        case 1:
            name = input("Enter Name Which You want To connect :")
            id = int(input("Enter Id Connecting With Name :"))
            obj.inner(id,name)
        case 2:
            name = input("Enter Name Which You want To connect :")
            id = int(input("Enter Id Connecting With Name :"))
            obj.left_joining(id,name)
        case 3:
            name = input("Enter Name Which You want To connect :")
            id = int(input("Enter Id Connecting With Name :"))
            obj.right_joining(id,name)
        case 4:
            name = input("Enter Name Which You want To connect :")
            id = int(input("Enter Id Connecting With Name :"))
            name_2=input("Enter 2nd Name :")
            id_2 = int(input("Enter 2nd ID : "))
            obj.full_join(id_1=id,name_1=name,id_2=id_2,name_2=name_2)
        case 5:
            table_name=input("Set table name")
            column_1=input("Enter 1st Column Name :")
            column_2=input("Enter 2nd Column Name :")
            obj.view(table_name,column_1,column_2)
        case 6:
            print("Thankyou For Using this Software")
            break
        case _:
            print("Wrong Option")