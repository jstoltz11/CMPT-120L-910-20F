user_req_num = input("Please give a number between 10 and 20 > ")

range_end = int(user_req_num) + 1

def myfunc(x):
    print("The sum of integers between 1 and " + user_req_num + " is: " + str(sum(range(range_end))))
    
myfunc(range_end)