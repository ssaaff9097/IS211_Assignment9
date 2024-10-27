from bs4 import BeautifulSoup
import requests

url = "https://www.cbssports.com/nfl/stats/"

def get_football_stats():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'TableBase-table'})
    players = []
    for row in table.find_all('tr')[1:21]:
        columns = row.find_all('td')
        if columns: 
            player = {
                'name': columns[0].text.strip(),
                'position': columns[1].text.strip(),
                'team': columns[2].text.strip(),
                'touchdowns': columns[3].text.strip()
            }
            players.append(player)

        for player in players:
            print(f"Player: {player['name']}, Position: {player['position']}, Team: {player['team']}, Touchdowns: {player['touchdowns']}")


if __name__ == "__main__":
    get_football_stats() 