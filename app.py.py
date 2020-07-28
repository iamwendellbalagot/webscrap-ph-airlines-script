import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import string
import random
import os


while(True):
    def get_ph_flights():
        #utilities
        url = 'https://www.philippineairlines.com/en/promotions/myso-ph'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        #locate the target table
        all_tables = soup.find_all('table')
        all_tr = all_tables[1].find('tbody').find_all('tr')


        #get the cell values
        cells = []
        for row in tqdm(all_tr, desc='Pulling the data'):
            cells.append([' '.join(i.get_text().split()) for i in row.find_all('td')])

        ph_flights_df = pd.DataFrame(cells[2:59])
        ph_flights_df['PRICE'] = ph_flights_df[1] + ' ' + ph_flights_df[2]
        ph_flights_df.drop([1,2,3], axis=1, inplace=True)
        ph_flights_df = ph_flights_df.rename(columns={0:'FLIGHTS'})

        print('='*50)
        print('\n DataFrame Succesfully Created.\n')
        print('='*50, '\n')

        #get the data info
        info_ph = ' '.join(cells[0])

        print(info_ph)
            #gernerate random strings
        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        folder_name = id_generator(10)
        folder = os.mkdir(folder_name)

        # %% [code]
        ph_flights_df.to_csv(folder_name + '/' + 'flights.csv')


        print('='*50)
        print('\n DataFrame Succesfully Created.\n')
        print('='*50, '\n')

        print('DATA INFORMATION: \n', '='*50 , '\n',info_ph)

        print('\n\n The data is ready.\n', 'Folder name: ', folder_name)



    def get_int_flights():
        #utilities
        url = 'https://www.philippineairlines.com/en/promotions/myso-ph'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        #locate the target table
        all_tables = soup.find_all('table')
        all_tr = all_tables[1].find('tbody').find_all('tr')


        #get the cell values
        cells = []
        for row in tqdm(all_tr, desc='Pulling the data'):
            cells.append([' '.join(i.get_text().split()) for i in row.find_all('td')])

        int_flights_df = pd.DataFrame(cells[63:101])
        int_flights_df.drop([1,3,5], axis=1, inplace=True)
        int_flights_df.columns = cells[62]
        int_flights_df = int_flights_df.rename(columns={'':'FLIGHTS'})
        info_int = ' '.join(cells[61])

        #gernerate random strings
        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        folder_name = id_generator(10)
        folder = os.mkdir(folder_name)

        # %% [code]
        int_flights_df.to_csv(folder_name + '/' + 'flights.csv')


        print('='*50)
        print('\n DataFrame Succesfully Created.\n')
        print('='*50, '\n')

        print('DATA INFORMATION: \n', '='*50 , '\n',info_int)

        print('\n\n The data is ready.\n', 'Folder name: ', folder_name)



    print('CHOOSE: [PH, INTERNATIONAL, EXIT]')
    inp = input('Type Here: ')
    
    if inp == 'EXIT':
        print('\n..............')
        break

    elif inp == 'PH':
        print('\nPH FLIGHTS \n\n')
        get_ph_flights()
    elif inp == 'INTERNATIONAL':
        print('\nINTERNATIONAL FLIGHTS \n\n')
        get_int_flights()

    elif inp not in ['PH', 'INTERNATIONAL']:
        print('\nYOU ENTERED A WRONG ID\n\n')

