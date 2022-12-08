import pandas as pd
import yfinance as yf

import numpy as np
import matplotlib.pyplot as plt

import cmath

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
        
    def Add_ColumsFourier_Transform(self,periodic_Components_num,column_to_use, Origin_File_Path,Destiny_File_Path):
        csvFileName=Origin_File_Path
        df=pd.read_csv(csvFileName, index_col="Date")
        
        Colum_Used=column_to_use

        data_FT = df[Colum_Used]
        
        
        dateIndex=[]
        for i in data_FT.index:
            dateIndex.append(i)
            
            
        array_like=np.asarray(data_FT).tolist()
        The_fft = np.fft.fft(array_like)
        fft_df =pd.DataFrame({'fft':The_fft})
        fft_df['absolute']=fft_df['fft'].apply(lambda x: np.abs(x))
        fft_df['angle']=fft_df['fft'].apply(lambda x: np.angle(x))
        fft_list = np.asarray(fft_df['fft'].tolist())
        
        
        Periodic_Components_Num=periodic_Components_num

        fft_list_m10= np.copy(fft_list); 
        fft_list_m10[Periodic_Components_Num:-Periodic_Components_Num]=0
        data_fourier=np.fft.ifft(fft_list_m10)
        
        Magnitud=[]
        Angle=[]
        for i in data_fourier:
            magnitud, angle=cmath.polar(i)
            Magnitud.append(magnitud)
            Angle.append(angle)
        
        df["FFT_Mag_{}_{}".format(Colum_Used,periodic_Components_num)]=Magnitud
        df["FFT_Angl_{}_{}".format(Colum_Used,periodic_Components_num)]=Angle     
        self.SavingDataset(df,Origin_File_Path, Destiny_File_Path, False)
        