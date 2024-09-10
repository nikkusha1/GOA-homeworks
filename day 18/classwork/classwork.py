str1 = "Hello world"    # გარდაქმნის ყველა ასოს დიდ ასოებად.
print(str1.lower())

str1 = "HellO wOrld"    #გარდაქმნის ყველა ასოს პატარა ასოებად.
print(str1.upper())

str1 = "HEllO WorLd"    #პირველ ასოს გარდაქმნის დიდ ასოთ და დანარჩენ ასოებს პატარა ასოებად.
str1 = str1.capitalize()
print (str1)

str1 = "Hello WorlD"   #დიდ ასოებს პატარა ასოებად გარდაქმნის, ხოლო პატარა ასოებს დიდ ასოებად.
str1 = str1.swapcase()
print(str1)

str1 = "Hello wOrld"   #პოულობს ასოს სტრინგში, თუ ვერ იპოვა, აბრუნებს -1.
print (str1.find("g"))


str1 = "hello"    #აბრუნებს სტრინგის სიგრძეს.
length = len(str1)
print(length)


text = "hello world"   #
position = text.index("world")
print(position) 

list = [1, 2, 3]  #ბოლო ელემენტს უმატებს ელემენტს
list.append(4)
print(list)  







