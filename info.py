import datetime

firstClass = ""
secondClass = ""
thirdClass = ""
fourthClass = ""
fifthClass = ""
sixthclass = ""

tmp = "%H:%M"
# Class running time.. you might have to modify this !
runn_time = (datetime.datetime.strptime(secondClass, tmp) - datetime.datetime.strptime(firstClass, tmp)).seconds


# Put your meeting id, password, name respectively
# You might have more or less subjects .
english = ["meeting_id", "meeting_passwd", "meeting_name"]
biology = ["", "", ""]
physics = ["", "", ""]
maths = ["", "", ""]
hindi = ["", "", ""]
computer = ["", "", ""]
history = ["", "", ""]
geography = ["", "", ""]
economics = ["", "", ""]
