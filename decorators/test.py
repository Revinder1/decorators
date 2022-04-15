import requests



TOKEN = '2619421814940190'


class Character:
    def __init__(self, token, name):
        self.token = token
        self.name = name

    def char_intelligence(self):
        char_url = f'https://superheroapi.com/api/{self.token}/search/{self.name}'
        resp = requests.get(char_url)
        return int(resp.json()['results'][0]['powerstats']['intelligence'])



def smartest_hero(first, second, third):
    new_dict = dict()
    new_dict[first.name] = first.char_intelligence()
    new_dict[second.name] = second.char_intelligence()
    new_dict[third.name] = third.char_intelligence()
    sorted_list = sorted(new_dict.items(), key=lambda i: i[1])
    return f'Самый умный супер герой: {sorted_list[-1][0]}, его intelligence: {sorted_list[-1][1]}'


if __name__ == '__main__':
    Hulk = Character(TOKEN, 'Hulk')
    Captain = Character(TOKEN, 'Captain America')
    Thanos = Character(TOKEN, 'Thanos')
    print(smartest_hero(Hulk, Captain, Thanos))

