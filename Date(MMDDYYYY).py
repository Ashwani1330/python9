date= input("Enter date in numerals (DDMMYYYY): ")
months={'01':'January', '02':'Ferbruary', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':"November",'12':"December"}
month_num=date[2:4]
month_name=months[month_num]
date_num=date[0:2]
Year_num=date[4:9]
print("\n \t Entered Date:")
print("\n \t",month_name, date_num+",",  Year_num)