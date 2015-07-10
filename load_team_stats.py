
from csanal import parse_json
import json

# you know this, but TEAMS is a set() list, so no team names can occur twice.
TEAMS = set([])

def load_team_stats():
    '''
    This is a "DOCSTRING"
    if you're wanting to be super rigid about code compliance and coverage
    you'd write a little bit about the function "load_team_stats" here.
    what arguments it takes, what it will return (all functions should return something, even if just True/False, etc.

    takes no arguments.
    returns a dictionary "teams_matches"
    where teams_matches.keys() would return a list of all teams
    and where teams_matches.values() would return a list of all matches where that particular team won.
    '''
    parsed_json = parse_json()
    teams_matches = {}
    # create the set of all team names
    for m in parsed_json['matches']:
        TEAMS.add(m['team_a'])
    # iterate through all teams
    for t in TEAMS:
        # this says 'give me a list of all matches where current team 't' was the winner'
        wins = [w for w in parsed_json['matches'] if t == w['winner']]
        # setdefault is a simple way to assign key-value pairs
        # when we might not be totally sure what keys and values we might be coming across
        teams_matches.setdefault(t, wins)
    return teams_matches

# figure out why this works when you call this file from command line
# ex: 'python load_team_stats.py'
# but not in ipython notebook (i think)
# should learn a little bit about namespaces
# google "name == main trick"
if __name__ == "__main__":
    print 'im running!'
    stats = load_team_stats()
    # json module has a nice 'pretty printer' function when using sort_keys and indent args
    print json.dumps(stats['Fnatic'], sort_keys=True, indent=2)
