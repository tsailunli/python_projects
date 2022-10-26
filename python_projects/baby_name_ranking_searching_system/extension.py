"""
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        items = soup.find_all('table', {'class': 't-stripe'})
        male = None
        female = None
        for item in items:
            line_lst = item.tbody.text.split('\n')
            male = 0
            female = 0
            for ele in line_lst:
                if len(ele) > 3:
                    ele_lst = ele.split(' ')
                    if len(ele_lst) == 4:
                        male_num = ele_lst[1].split(',')
                        female_mun = ele_lst[3].split(',')
                        male += int(''.join(male_num))
                        female += int(''.join(female_mun))
        print(f'Male Number: {male}')
        print(f'Female Number: {female}')


if __name__ == '__main__':
    main()
