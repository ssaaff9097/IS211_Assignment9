import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"

def get_super_bowl_champions():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})


    champions_data = [] 
    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        print([col.text.strip() for col in columns])
        if len(columns) >= 3:
            year = columns[0].text.strip()
            champion = columns[1].text.strip()
            runner_up = columns[2].text.strip()
            champions_data.append((year, champion, runner_up))

    if champions_data: 
        for year, champion, runner_up in champions_data:
            print(f"Year: {year}, Champion: {champion}, Runner-up: {runner_up}")
    else: 
        print("No data found")

if __name__ == "__main__":
    get_super_bowl_champions()
