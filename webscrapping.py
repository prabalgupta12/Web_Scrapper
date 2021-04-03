from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.programmableweb.com/category/tools/api"
api_dic = {}
total_api = 0
while True:

    response = requests.get(url)

    data = response.text

    soup = BeautifulSoup(data,'html.parser')

    tapis = soup.find_all("tr",{"class":["odd","even"]})

    for tapi in tapis:

        titles = tapi.find('td',{'class':'views-field'}).text

        absolute_url = "https://www.programmableweb.com" + tapi.find('a').get("href")

        api_cat = tapi.find('td',{'class':'views-field views-field-field-article-primary-category'}).text

        api_desc = tapi.find('td',{'class':'views-field views-field-field-api-description'}).text

        total_api += 1

        api_dic[total_api] = [titles, absolute_url, api_cat, api_desc]

        #print('API Name:', titles, '\nAPI Url:', absolute_url, '\nAPI Cat:', api_cat, '\nAPI Desc:', api_desc)

       

    url_tag = soup.find('a',{'class':'pw_load_more'})

    if url_tag== None:

        break

    elif url_tag.get('href'):

        url= 'https://www.programmableweb.com' + url_tag.get('href')

        print(url)

    else:

        break

total_api = str(total_api)

print("Total APIs:", total_api)

api_dic_df = pd.DataFrame.from_dict(api_dic, orient = 'index', columns = ['API Name','API Url','API Cat', 'API Desc'])

api_dic_df.head()

api_dic_df.to_csv('apiscrapper.csv')
