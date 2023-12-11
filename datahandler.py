import pandas as pd
import os as os
import datetime as dt
import random

def make_path(dir_p,file_p):
    return os.path.join(os.getcwd(),dir_p,file_p)

def make_days_2_date(days):
    return pd.to_datetime(days,unit='D',origin='1899-12-30').date()

def is_wd_equal(date1,date2):
    return date1.weekday() == date2.weekday()

def get_wd_df(df,clock):
    return df[df.apply(lambda row: is_wd_equal(make_days_2_date(row['날짜']),clock),axis=1)]

class datahandler:
    raw_p = "raw"
    parsed_p = "parsed"
    excel_p = "에버랜드데이터셋11_static.xlsx"
    sheets = 3
    csv_paths = []
    key_list = []
    csv_p = "exceldata_sheet"
    key_p = "keywords.log"

    df_await = None
    df_route = None
    df_route1 = None
    df_route2 = None

    def __init__(self):
        self.get_csv_paths()
        self.df_await = self.read_csv(0)
        self.df_route1 = self.read_csv(1)
        self.df_route2 = self.read_csv(2)
        self.key_list = self.df_await.columns[3:].to_list()
        self.use_route(1)

    def update(self):
        self.make_excel_2_csv()
        self.write_key()

    def use_route(self,num):
        if num == 1: self.df_route = self.df_route1
        elif num == 2: self.df_route = self.df_route2

    def get_csv_paths(self):
        for i in range(self.sheets):
            self.csv_paths.append('exceldata_sheet'+ str(i) + '.csv')

    def make_excel_2_csv(self):
        for i in range(self.sheets):
            excel_data = pd.read_excel(make_path(self.raw_p,self.excel_p), sheet_name = i)
            excel_data.to_csv(make_path(self.parsed_p,self.csv_paths[i]))

    def read_csv(self,i):
        return pd.read_csv(make_path(self.parsed_p,self.csv_paths[i]))

    def write_key(self):
        file = open(make_path(self.parsed_p,self.key_p),"w",encoding='utf-8')
        for key in self.key_list:
            file.write(key + "\n")

    def get_await_time(self,target : str,clock=dt.datetime.today()):
        df = self.df_await
        df_wd = get_wd_df(df,clock)
        h = clock.hour
        # if clock.minute < 30: h -= 1
        if h < 10 or h >18: return -1
        new = dt.time(hour=h,minute=30)
        row_of_new = df_wd.iloc[:,2][df_wd.iloc[:,2]==str(new)].index.to_list()[0]
        return float(df.loc[row_of_new,target])

    def get_route_time(self,start,end):
        df = self.df_route
        row_of_start = df.iloc[:,1][df.iloc[:,1]==start].index.to_list()[0]
        return float(df.loc[row_of_start,end])

    def get_ride_time(self,target):
        return 5.0