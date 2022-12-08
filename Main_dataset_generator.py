from Retriving_Dataset import *

dataSet_Gen= DatasetGenerator()

#dataSet_Gen.RetivingDataPrices_Yahoo('2000-08-23', '2000-11-25',"/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/testClass.csv","/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/testClass.csv")

#dataSet_Gen.AddColumnWeekDay("/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/CRUDE_OIL_DataCSV.csv", "/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/CRUDE_OIL_WeekDayNum.csv")



#Generate new FFT columns done :)
"""Column=['Open','High','Low','Close','Adj Close','Volume']
frec=[10,50,100]

for i in Column:
    for j in frec:
        dataSet_Gen.Add_ColumsFourier_Transform(j,i, "/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/CRUDE_OIL_Dataand_FFT_10_50_100.csv","/Users/eduardo/Desktop/Creating_-_Saving_Dataset/CRUDE_OIL/CRUDE_OIL_Dataand_FFT_10_50_100.csv")      
"""