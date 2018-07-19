#encoding:utf-8

point = int(input("Pls. insert your point: "))

if point >= 60:
    if point >= 70:
        if point >= 80:
            if point >= 90:
                print("Class A")
            else:
                print("Class B")
        else:
            print("Class C")
    else:
        print("Class D")
else:
    print("Class E")