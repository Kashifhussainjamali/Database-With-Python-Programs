class nadra():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",password="jamali123",database="nadra")
    cur=a.cursor()
    # cur.execute("create table karachi(name varchar(25) not null,age integer(8) not null,cnic integer(13)primary key,city varchar(25), constraint check(city='karachi' and age<50))")
    def karachi(self,name,age,cnic,city):
        insert=(f"insert into karachi(name,age,cnic,city)values('{name}',{age},{cnic},'{city}')")
        self.cur.execute(insert)
        self.a.commit()

    def nawabshah(self,name,age,cnic,city):
        insert = (f"insert into nawabshah(name,age,cnic,city)values('{name}',{age},{cnic},'{city}')")
        self.cur.execute(insert)
        self.a.commit()

    def sakrand(self,name,age,cnic,city):
        insert = (f"insert into sakrand(name,age,cnic,city)values('{name}',{age},{cnic},'{city}')")
        self.cur.execute(insert)
        self.a.commit()

    def fetch_karachi(self):
        fetch_query="select * from karachi"
        self.cur.execute(fetch_query)
        result_karachi=self.cur.fetchall()
        print(result_karachi)

    def fetch_nawabshah(self):
        fetch_query="select * from nawabshah"
        self.cur.execute(fetch_query)
        result_nawabshah=self.cur.fetchall()
        print(result_nawabshah)

    def fetch_sakrand(self):
        fetch_query="select * from sakrand"
        self.cur.execute(fetch_query)
        result_sakrand=self.cur.fetchall()
        print(result_sakrand)

obj=nadra()
help=int(input("How Can i help You\n1:Insert Data\n2:Fetch data"))
if help==1:
    user = int(input('''Which city you Want to Insert Data\n1:Karachi\n2:Nawabshah\n3:sakrand\n'''))
    match user:
        case 1:
            name = input("Enter name").capitalize()
            age = int(input("Enter Age* & must be <50 "))
            cnic = int(input("Enter Cnic* Must be Unique and must be 12 digits"))
            city = input("Enter City Must be (karachi)")
            obj.karachi(name, age, cnic, city)
            print("Data Inserted")
        case 2:
            name = input("Enter name").capitalize()
            age = int(input("Enter Age* & must be <50 "))
            cnic = int(input("Enter Cnic* Must be Unique and must be 12 digits"))
            city = input("Enter City Must be (nawabshah)")
            obj.nawabshah(name, age, cnic, city)
            print("Data Inserted")
        case 3:
            name = input("Enter name").capitalize()
            age = int(input("Enter Age* & must be <50 "))
            cnic = int(input("Enter Cnic* Must be Unique and must be 12 digits"))
            city = input("Enter City Must be (sakrand)")
            obj.sakrand(name, age, cnic, city)
            print("Data Inserted")
        case _:
            print("Wrong Option")
elif help==2:
    user_fetch=int(input("Which City Data You want to Fetch\n1:Karachi\n2:Nawabshah\n3:sakrand\n"))
    match user_fetch:
        case 1:
            obj.fetch_karachi()
        case 2:
            obj.fetch_nawabshah()
        case 3:
            obj.fetch_sakrand()
        case _:
            print("wrong Option")
else:
    print("Wrong Option")