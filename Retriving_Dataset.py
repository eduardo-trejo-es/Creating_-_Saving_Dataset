import pandas as pd
import yfinance as yf





def SavingDataPrices(From, to,csvFileName):
    startDate=From
    endDate= to

    df=yf.download('TWTR',start = startDate, end = endDate,interval='1m',utc=True,threads = True)
    
    #####      Saving Data In CSV file   ####

    """columnsNames=["Open","Open","Open","Open","lastTradedVolume"]
    DateIndexName=[]
    columnsValues=[]
    DataGrouped=[]
    for i in prices_Data:
        DateIndexName.append(i["snapshotTime"])
        columnsValues.append(i["openPrice"]["bid"])
        columnsValues.append(i["closePrice"]["bid"])
        columnsValues.append(i["highPrice"]["bid"])
        columnsValues.append(i["lowPrice"]["bid"])
        columnsValues.append(i["lastTradedVolume"])
        DataGrouped.append(columnsValues)
        columnsValues=[]

    df = pd.DataFrame(DataGrouped,index=DateIndexName, columns=columnsNames)"""
     
    try:
        existing=pd.read_csv(csvFileName, index_col="Datetime")
        #print(existing)
        #print(type(existing))
        try:
            existing = existing.append(df)
        except :
            print("could not be possible to add new rows")
        print("was try")
        print(existing)
        existing.to_csv(path_or_buf=csvFileName,index=True)
        
    except :
        
        print("was execpt")
        df.to_csv(path_or_buf=csvFileName,index=True)


SavingDataPrices('2022-09-15', '2022-09-21',"Twttr/TwitterDataCSV.csv")