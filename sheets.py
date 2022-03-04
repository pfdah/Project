import os
import xlsxwriter
import pandas
import datetime


def insert_attendance(test_name):
    sub = "Attendance"
    if  len(os.listdir('./attendance')) < 1:
        workbook = xlsxwriter.Workbook("./attendance/Attendance.xlsx")
        print("Creating Spreadsheet with Title: " + sub)
        sheet = workbook.add_worksheet() 
        sheet.write(0,0,"SN.")
        sheet.write(0,1,"Name")
        sheet.write(0,2,"Attn")
        sheet.write(0,3,"Date")
        sheet.write(0,4,"P.Days")
        sheet.write(0,5,"T.Days")
        pos = 1
        for i in test_name:
            sheet.write(pos,0,pos)
            sheet.write(pos,1,i)
            sheet.write(pos,2,0)
            sheet.write(pos,3,0)
            sheet.write(pos,4,0)
            sheet.write(pos,5,0)
            pos += 1
        #print(datetime.datetime.now().date())
        workbook.close() 
    print("Done.")
    return
def close_attendance():
    print("Attendance Closed for the Day")
    df = pandas.read_excel('./attendance/Attendance.xlsx',index_col=0)
    df["T.Days"] += 1
    df.to_excel('./attendance/Attendance.xlsx')
    
#mark_attendance("Bill Gates")
def mark_attendance(person):
    print("Attendance Process Started")
    names = os.listdir('./train_img')
    if (person in names):
        df = pandas.read_excel('./attendance/Attendance.xlsx',index_col=0)
        print(df)
        df.loc[df['Name'] == person, 'Attn'] = 'P'
        df.loc[df['Name'] == person, 'Date'] = datetime.datetime.now().date()
        df.loc[df['Name'] == person, 'P.Days'] += 1
        df.to_excel('./attendance/Attendance.xlsx')
        print(df)
    else:
        print("Person is not enrolled")
    print("Attendace Process Completed")
