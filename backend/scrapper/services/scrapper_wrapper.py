import requests
from bs4 import BeautifulSoup


def fetch_data():
    url = 'https://coinmarketcap.com/'

    html = requests.get(url).content

    data = BeautifulSoup(html, 'html5lib')

    table = data.find('tbody')

    final_data = []

    for row in table.findAll('tr')[:10]:
        temp_dict = {}
        each_row_data = row.findAll('td')
        for col in range(len(each_row_data)):
            if col == 2:
                temp_dict['name'] = each_row_data[col].find('p', attrs = {'class':"sc-14rfo7b-0 lhJnKD", 'color':"text", 'data-sensors-click':"true", 'font-size':"1", 'font-weight':"semibold"}).text
            elif col == 3:
                temp_dict['price'] = float(each_row_data[col].text.replace('$', '').replace(',', ''))
            elif col == 4:
                temp_dict['one_hour'] = each_row_data[col].text
            elif col == 5:
                temp_dict['twentyfour_hour'] = each_row_data[col].text
            elif col == 6:
                temp_dict['seven_day'] = each_row_data[col].text
            elif col == 7:
                temp_dict['market_cap'] = each_row_data[col].find('span', attrs = {'class':"sc-1ow4cwt-1 ieFnWP", 'data-nosnippet':"true"}).text
            elif col == 8:
                temp_dict['volume'] = each_row_data[col].find('p', attrs = {'class':"sc-14rfo7b-0 fVSMmK font_weight_500", 'color':"text", 'data-sensors-click':"true", 'font-size':"1"}).text
            elif col == 9:
                temp_dict['suppy'] = each_row_data[col].text
            else:
                pass

        temp_dict['current_top_10'] = True
        final_data.append(temp_dict)

    return final_data
