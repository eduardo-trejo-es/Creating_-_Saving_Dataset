import pandas as pd
import yfinance as yf





class DatasetGenerator:
    def RetivingDataPrices_Yahoo(self,From, to,csvFileName,csvFileName_New):
        startDate=From
        endDate= to

        df=yf.download('CL=F',start = startDate, end = endDate,interval='1d',utc=True,threads = True)

        self.SavingDataset(df,csvFileName, csvFileName_New, True)
        
            
    def SavingDataset(self,df,csvFileName, csvFileName_New,Add_to_old):
        #####      Saving Data In CSV file   ####
        if Add_to_old:
            try:
                existing=pd.read_csv(csvFileName, index_col="Date")
                #print(existing)
                #print(type(existing))
                try:
                    existing = existing.append(df)
                except :
                    print("could not be possible to add new rows")
                print("was try")
                print(existing)
                existing.to_csv(path_or_buf=csvFileName_New,index=True)
                
            except :
                
                print("was execpt")
                df.to_csv(path_or_buf=csvFileName_New,index=True)
        else:
            print("The actual data saved")
            df.to_csv(path_or_buf=csvFileName_New,index=True)
            

    def AddColumnWeekDay(self,csvFileName, csvFileName_New):
        df=pd.read_csv(csvFileName, index_col="Date")
        
        dateIndex=[]
        weekday_Name=[]
        weekday_Number=[]
        for i in df.index:
            dateIndex.append(i)
            d_name = pd.Timestamp(i)
            weekday_Name.append(str(d_name.day_name()))
            weekday_Number.append(d_name.dayofweek)
            
        df["DayName"]=weekday_Name
        df["DayNumber"]=weekday_Number

        self.SavingDataset(df,csvFileName, csvFileName_New,False)