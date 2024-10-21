# changed
# from selenium.webdriver.common.by import By
from selenium import webdriver
# from getpass import getpass
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re
import numpy as np
from selenium.common.exceptions import *
#%%
csv_path = r'\Equity.csv'
stocks = pd.read_csv(csv_path)
stocks = stocks[stocks['Security Code'].str.contains ("Mutual Fund")==False]
companies=stocks.index.values.tolist()
companies=companies[3500:4000]
#%%
driver_path=r'C:\Users\m.h.ramachandra.rao\Downloads\New folder (2)\Latest_chrome_driver\chromedriver-win64\chromedriver-win64'
# s = Service(r"C:\Users\m.h.ramachandra.rao\Downloads\New folder (2)\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# s = Service(r"C:\Users\m.h.ramachandra.rao\Downloads\New folder (2)\Latest_chrome_driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
s = Service(driver_path+r"\chromedriver.exe")
#%%
#company codes list
companies = [
    # '532362','500400'
      # '540980'
      # 541337
      '542867'
     # '526009'
    # '500325'
    # '500325'
    ]
#%%
## Xpath of web elements

# Key ratios xpaths
companyname_xpath = '/html/body/div/div[1]/h1'
mc_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[1]/span[2]/span'
cp_xpath = '//*[@id="top-ratios"]/li[2]/span[2]/span'
hp_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[1]'
lp_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[2]'
pe_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[4]/span[2]/span'
bv_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[5]/span[2]/span'
dy_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[6]/span[2]/span'
roce_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[7]/span[2]/span'
roe_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[8]/span[2]/span'
fv_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[9]/span[2]/span'
eps_xpath = '/html/body/main/div[3]/div[3]/div[2]/ul/li[10]/span[2]/span'


## Quarterly results xpaths
header_QR_xpath = r'//*[@id="quarters"]/div[3]/table/thead/tr'
QR_xpath = r'/html/body/main/section[4]/div[3]/table/tbody'

## Profit and Loss xpaths
header_P_L_xpath=r'/html/body/main/section[5]/div[3]/table/thead'
PL_xpath = r'/html/body/main/section[5]/div[3]/table/tbody'

## Balance sheet
header_bal_xpath=r'/html/body/main/section[6]/div[2]/table/thead'
Bal_xpath = r'/html/body/main/section[6]/div[2]/table/tbody'

## Cash flows
header_cash_xpath = r'/html/body/main/section[7]/div[2]/table/thead'
cash_xpath = r'/html/body/main/section[7]/div[2]/table/tbody'

## Ratios
header_ratios_xpath = r'/html/body/main/section[8]/div[2]/table/thead'
ratios_xpath = r'/html/body/main/section[8]/div[2]/table/tbody'

## Share holding pattern
header_share_holding_xpath=r'/html/body/main/section[9]/div[2]/div/table/thead'
share_holding_xpath =r'/html/body/main/section[9]/div[2]/div/table/tbody'

header_pattern = r'[A-z]{3,4}\s\d+'# Header pattern
value_pattern = r'-{0,1}\d+,{0,1}.{0,1}\d{0,5}'
# value_pattern = r'-{0,1}\d+,{0,1}d{0,5}'

time_frame = [2,3,4,6,9]

# res=PL_df.iloc[:,-time_frame[0]-1:]

#%%
start_time = time.time()

url_1 = 'https://www.screener.in/company/'
# url_2 = '/consolidated/'
url_2='#quarters'
j=1
final= pd.DataFrame()
list=[]
for i in companies:
    
    print(f'Run: {j}, company: {i}')
    j=j+1
    url = url_1+str(i)+url_2
    driver=webdriver.Chrome(service=s)
    driver.get(url)
    
    
    #Start of key ratios
    try:
        company_name = driver.find_element('xpath',companyname_xpath).text
    except ValueError:
        company_name = ''
    try:
        market_cap = float(''.join((driver.find_element("xpath",mc_xpath).text).split(',')))        
    except ValueError:
        market_cap = ''
        
    try:
        current_price= float(''.join((driver.find_element("xpath",cp_xpath).text).split(',')))
    except ValueError:
        current_price = ''
    
    try:
        hp_price = float(''.join((driver.find_element("xpath",hp_xpath).text).split(',')))
    except ValueError:
        hp_price = ''
    
    try:
        lp_price = float(''.join((driver.find_element("xpath",lp_xpath).text).split(',')))
    except ValueError:
        lp_price = ''
    
    try:
        pe = float(''.join((driver.find_element("xpath",pe_xpath).text).split(',')))
    except ValueError:
        pe = ''
    
    try:
        bv = float(''.join((driver.find_element("xpath",bv_xpath).text).split(',')))
    except ValueError:
        bv=''
        
    try:
        div_yeild = float(''.join((driver.find_element("xpath",dy_xpath).text).split(',')))
    except ValueError:
        div_yeild=''
        
    try:
        roce = float(''.join((driver.find_element("xpath",roce_xpath).text).split(',')))
    except ValueError:
        roce=''
        
    try:
        roe = float(''.join((driver.find_element("xpath",roe_xpath).text).split(',')))
    except ValueError:
        roe=''
        
    try:
        face_val = float(''.join((driver.find_element("xpath",fv_xpath).text).split(',')))
    except ValueError:
        face_val=''
    
    
    list_values=[i,company_name,market_cap,current_price,hp_price,lp_price,pe,bv,div_yeild,roce,roe,face_val]
    df = pd.DataFrame({'company_code':[],'company_name':[],'market_cap':[],'current_price':[],'52wk_High':[],'52wk_low':[],'PE_ratio':[],'Book_value':[],'Dividend':[],'ROCE':[],'ROE':[],'Face_value':[]})
    df.loc[len(final)]=list_values
    final = final.append(df,ignore_index=False)
    #End of Key ratios
    
    
    # Quartely results
    try:
        QR_header=driver.find_element('xpath',header_QR_xpath).text
        QR_df=pd.DataFrame(columns=['columns']+re.findall(header_pattern,QR_header))
        
        table = driver.find_element('xpath',QR_xpath).text
        QR_df_values = table.splitlines()
        
        sales            = ["".join([i for i in QR_df_values[0] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[0].replace(",","").replace("%","").split(" ") if i.isnumeric()==True] #[float(i) for i in QR_df_values[0].replace(",","").split(" ")[2:]]
        expenses         = ["".join([i for i in QR_df_values[1] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[1].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        operating_profit = ["".join([i for i in QR_df_values[2] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[2].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        OPM              = ["".join([i for i in QR_df_values[3] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[3].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        other_income     = ["".join([i for i in QR_df_values[4] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[4].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        interest         = ["".join([i for i in QR_df_values[5] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[5].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        depreciation     = ["".join([i for i in QR_df_values[6] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[6].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        Profit_before_tax= ["".join([i for i in QR_df_values[7] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[7].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        
        Tax_rate         = ["".join([i for i in QR_df_values[8] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[8].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        Net_profit       = ["".join([i for i in QR_df_values[9] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[9].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
        eps              = ["".join([i for i in QR_df_values[10] if i.isnumeric()==False])] + [float(i) for i in QR_df_values[10].replace(",","").replace("%","").split(" ") if i.isnumeric()==True]
    
    except NoSuchElementException:
        print(f'Issue with this company {i}')
        
        QR_df = pd.DataFrame(columns=['columns']+[])
        sales = ['Sales +'] + []
        expenses = ['Expenses +']+[]
        operating_profit = ['Operating Profit']+[]
        OPM=['OPM%']+ []
        other_income=['Other Income +']+[]
        interest=['Interest']+[]
        depreciation =['Depreciation']+[]
        Profit_before_tax=['Profit Before Tax']+[]
        Tax_rate =['Tax %']+ []
        Net_profit=['Net Profit +']+ []
        eps=['EPS in Rs']+[]
        
    try:
        QR_df.loc[len(QR_df)]=sales
    except ValueError:
        print(f'This company {i} is having issue in Sales')
    
    try:
        QR_df.loc[len(QR_df)]=expenses
    except ValueError:
        print(f'This company {i} is having issue in expenses')
    
    try:
        QR_df.loc[len(QR_df)]=operating_profit
    except ValueError:
        print(f'This company {i} is having issue in operating_profit')
    
    try:
        QR_df.loc[len(QR_df)]=OPM
    except ValueError:
        print(f'This company {i} is having issue in OPM')
    
    try:
        QR_df.loc[len(QR_df)]=other_income
    except ValueError:
        print(f'This company {i} is having issue in other_income')
    
    try:
        QR_df.loc[len(QR_df)]=interest
    except ValueError:
        print(f'This company {i} is having issue in interest')
    
    
    try:
        QR_df.loc[len(QR_df)]=depreciation
    except ValueError:
        print(f'This company {i} is having issue in depreciation')
    
    try:
        QR_df.loc[len(QR_df)]=Profit_before_tax
    except ValueError:
        print(f'This company {i} is having issue in Profit_before_tax')
        
    try:
        QR_df.loc[len(QR_df)]=Tax_rate
    except ValueError:
        print(f'This company {i} is having issue in Tax_rate')
        
    try:
        QR_df.loc[len(QR_df)]=Net_profit
    except ValueError:
        print(f'This company {i} is having issue in Net_profit')
    
    try:
        QR_df.loc[len(QR_df)]=eps
    except ValueError:
        print(f'This company {i} is having issue in eps')
    
    # driver.quit()
end_time = time.time()

total_time =start_time-end_time
