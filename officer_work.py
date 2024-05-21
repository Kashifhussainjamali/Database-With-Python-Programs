import mysql.connector
class officer():
    a = mysql.connector.connect(host="localhost", user="root", password="jamali123", database="nadra")
    cur = a.cursor()
    desc_query = "desc new_nadra_database"
    show_query = "select * from new_nadra_database"
    cur.execute(desc_query)
    desc = cur.fetchall()
    print("Table Description: ", desc)
    cur.execute(show_query)
    show = cur.fetchall()
    print("Table Is: ", show)

    def show_des_wise(self,col_name):
        name_query=f"select {col_name} from new_nadra_database"
        self.cur.execute(name_query)
        names=self.cur.fetchall()
        for x in names:
            print(x)

    def maxormin_value(self,min_or_max):
        max_query=f"select {min_or_max}(age) from new_nadra_database"
        self.cur.execute(max_query)
        max=self.cur.fetchall()
        print(f"The {min_or_max} Age is :{max}")

    def city(self,city):
        city_query=f"select * from new_nadra_database where city='{city}'"
        self.cur.execute(city_query)
        city=self.cur.fetchall()
        for x in city:
            print(x)

    def avg(self):
        avg_query="select avg(age) from new_nadra_database"
        self.cur.execute(avg_query)
        avg=self.cur.fetchall()
        print("The Average is:",avg)


obj=officer()
while True:
    user=int(input("How Can I help you\n1:Show Single Column\n2:Show Max or Min age\n3:Show Citywise\n4:Show Avg of age :"))
    if user==1:
        col_name = input("Which Column You want to display :")
        obj.show_des_wise(col_name)
    elif user==2:
        min_or_max = input("Min or Max value of age :")
        obj.maxormin_value(min_or_max)
    elif user==3:
        city = input("insert city name")
        obj.city(city)
    elif user==4:
        obj.avg()
    else:
        print("Wrong Option")
