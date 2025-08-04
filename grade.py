m1=int(input("Enter Marks of First Subject:"))
m2=int(input("Enter Marks of Second Subject:"))
m3=int(input("Enter Marks of Third Subject:"))
sum=m1+m2+m3
avg=sum/3
print("Total Marks is",sum)
print("Average marks is",avg)
if avg>=90:
    print("Grade:A+")
elif avg>=80:
    print("Grade:A")
elif avg>=70:
    print("Grade:B")
elif avg>=60:
    print("Grade:C")
elif avg>=50:
    print("Grade:D")
elif avg>=33:
    print("Grade:E")
else:
    print("Fail")
