# create dictionary
bir_thaday = { 
    "darshan":"09/10/2008",
    "dhanush": "24/10/2009",
}
print(type(bir_thaday))
# accessing dictionary
print(bir_thaday.get("sudeep","not found")) # safe access
#adding who developer
bir_thaday["sudeep"] = "09/9/1997"
print(bir_thaday)

#updating dict rechck and correct
bir_thaday["sudeep"] = "05/9/1997"
print(bir_thaday)

#removing by using pop and del
#x = bir_thaday.pop("sudeep")
#print(x)



#by using del
#del bir_thaday["sudeeep"]
x = bir_thaday.pop("sudeep")
print(x)
print(bir_thaday)