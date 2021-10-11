import json
import requests
import random
from requests.models import HTTPError
from dhooks import Webhook, Embed

minPlaceVisits = 50
hook = Webhook(
    'WEBHOOK HERE')


class Group_Game_Details:
    def __init__(self, randomid):
        self.r = requests.get(
            'https://games.roblox.com/v2/groups/{0}/games?accessFilter=All&limit=10&sortOrder=Asc'.format(randomid)).json()
        self.GameName = self.r['data'][0]['name']
        self.PlaceVisits = self.r['data'][0]['placeVisits']
        self.GameID = self.r['data'][0]['rootPlace']['id']
        self.GroupID = self.r['data'][0]['creator']['id']
        self.Description = self.r['data'][0]['description']
        self.LastUpdated = self.r['data'][0]['updated']


def Send_To_Discord():
    try:
        Details = Group_Game_Details(random.randrange(1, 9000000))
        print(Details.PlaceVisits)
        if Details.PlaceVisits > minPlaceVisits:
            embed = Embed(
                description='Found a Game!',
                color=0x5CDBF0,
                timestamp='now'
            )

            embed.add_field(
                name='**Game ID**', value=Details.GameID)
            embed.add_field(
                name='**Game Name**', value=Details.GameName)
            embed.add_field(
                name='**Place Visits**', value=Details.PlaceVisits)
            embed.add_field(
                name='**Last Updated**', value=Details.LastUpdated)
            embed.add_field(
                name='**Group ID**', value=Details.GroupID)
            hook.send(embed=embed)

    except IndexError:
        print('No Results')


while True:
    Send_To_Discord()
