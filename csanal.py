import json
import requests
csgo_json = requests.get("http://csgo.hvalrossen.dk/")
parsed_json = json.loads(csgo_json.text)
"""%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
from pandas.io.json import json_normalize
normalized_json = json_normalize(parsed_json['matches'])""" #will use this later
def tvt(team1,team2):
    
    matches = []
    h2hmatches = []
    team1wins = []
    team2wins = []
    team1h2h = []
    team2h2h = []
    team1h2hpercent = []
    team2h2hpercent = []
    for m in parsed_json['matches']:
        if m['team_a'] == team1 or m['team_b'] == team1 or m['team_a'] == team2 or m['team_b'] == team2:
            matches.append(m)
    for h in parsed_json['matches']:
        if h['team_a'] == team1 and h['team_b'] == team2 or h['team_a'] == team2 and h['team_b'] == team1:
            h2hmatches.append(h)
    team1wins = [x for x in matches if x['winner'] == team1]
    team2wins = [x for x in matches if x['winner'] == team2]
    team1h2h = [x for x in h2hmatches if x['winner'] == team1]
    team2h2h = [x for x in h2hmatches if x['winner'] == team2]
    team1h2hpercent = round(float(len(team1h2h)) / float(len(h2hmatches)),3)
    team2h2hpercent = round(float(len(team2h2h)) / float(len(h2hmatches)),3)
    print '{0} {1}{2}{3}{4}: {5}'.format("Total",team1," vs ",team2," matches",len(h2hmatches))
    print '{0} {1}: {2}'.format(team1,"head to head wins",len(team1h2h))
    print '{0} {1}: {2}{3}'.format(team1,"head to head win percentage",team1h2hpercent*100, "%")
    print '{0} {1}: {2}'.format(team2,"head to head wins",len(team2h2h))
    print '{0} {1}: {2}{3}'.format(team2,"head to head win percentage",team2h2hpercent*100, "%")
        
def team_win_percentage(team):
    
    matches = []
    losses = []
    ties = []
    for m in parsed_json['matches']:
        if m['team_a'] == team or m['team_b'] == team:
            matches.append(m)
    wins = [x for x in matches if x['winner'] == team]
    losses = [x for x in matches if x['winner'] != team] and [x for x in matches if x['winner'] != '_NONE_']
    ties = [x for x in matches if x['winner'] == '_NONE_']
    print float(len(wins)) / float(len(losses))
