# This Program will create CSV file which Contain list of vacancises ublished by ptopjobs.lk website 

# example url " http://topjobs.lk/applicant/vacancybyfunctionalarea.jsp?FA=AGD "


from bs4 import BeautifulSoup as bf
import pandas as pd
import requests
import csv
import ast




def topjobs(url):
    link = requests.get(url).text

    soup = bf(link, 'lxml')

    f = open("jobs.csv","w", newline="")
    row_1 = ("Company_name","Post","Opening_date","Closing_date"," Job_link ")
    writer = csv.writer(f)
    writer.writerow(row_1)

    d = soup.find('div', class_='cate-lister-view')
    date = d.table.find("tr", id="tr0")

    for num in range(0,19):
        data_list_up = d.table.find("tr", id=f"tr{num}")["onclick"].split("createAlert")[1]
        res2 = ast.literal_eval(data_list_up)
        ad_link = f"http://topjobs.lk/employer/JobAdvertismentServlet?rid={res2[0]}&ac={res2[1]}&jc={res2[2]}&ec={res2[3]}&pg=applicant/vacancybyfunctionalarea.jsp',1098,631,'quickvacancysearch_1{res2[4]}"
    
        row_2 = (d.table.find("tr", id=f"tr{num}").h1.text, d.table.find("tr", id=f"tr{num}").h2.text, date.find_all('td', width="14%")[0].text, date.find_all('td', width="14%")[1].text, ad_link)
        writer.writerow(row_2)
        
        print('company name :- ', d.table.find("tr", id=f"tr{num}").h1.text)
        print('Post         :- ', d.table.find("tr", id=f"tr{num}").h2.text)
        print('Opening date :- ', date.find_all('td', width="14%")[0].text)
        print('Closing date :- ', date.find_all('td', width="14%")[1].text)
        print('link :- ', ad_link ,"\n")

    f.close()
    

    
link1 = input("input your top jobs link:-")
 
if __name__ == '__main__':
  topjobs(link1)