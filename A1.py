my_list=[]
my_list= [1000,500,2000]
my_list= list((1000,2000))
my_list= list(range(1,6))


marks = [100, 200, 300, 400, 500]
#print(marks[0])
#print(marks[-2])    
#print(int(marks[-1]))      #0,1,2...right side se input print karta hai , -1,-2,-3...left side se input print karta h

student_list = ["John", "Jane", "Jim", "Jill"]
student_list.remove("Jim")  # This will remove "Jim" from the list
#print(student_list)  # Output: ['John', 'Jane', 'Jill']


#print("Total marks:", sum(marks))  # Output: Total marks: 1500



#TUPLE
DATA = ('KARTAVYA','64','DA','BTECH')
#print(DATA[2])
#print(DATA[-2])

#FOR LOOP
s = 0
for i in range(2, 21 , 2):
    #print(i)
    s= s + i

#print("Sum of even numbers from 2 to 20:", s)

#While Loop
i=1
while i<=10:
    #print(i)
    i+=1

i=2
while i<=20:
    #print(i)
    i+=2

password = ""
while password != "ABCD":
    password = input("Enter the password: ")
    if password != "ABCD":
        print("Access DENIED!")
    else:
        print("Access GRANTED!")
    