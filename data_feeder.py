import csv
import json
import sys
from pprint import pprint

f = open('current.json')
teams = json.load(f)

print(
    'team_favorite_id,',
    'favorite_Score,',
    'favorite_OffensiveYards,',
    'favorite_OffensiveYardsPerPlay,',
    'favorite_RushingYards,',
    'favorite_RushingYardsPerAttempt,',
    'favorite_PassingYards,',
    'favorite_PassingYardsPerAttempt,',
    'favorite_PassingInterceptionPercentage,',
    'favorite_TimesSackedPercentage,',
    'favorite_OpponentScore,',
    'favorite_OpponentOffensiveYards,',
    'favorite_OpponentOffensiveYardsPerPlay,',
    'favorite_OpponentRushingYards,',
    'favorite_OpponentRushingYardsPerAttempt,',
    'favorite_OpponentPassingYards,',
    'favorite_OpponentPassingYardsPerAttempt,',
    'favorite_OpponentPassingInterceptionPercentage,',
    'favorite_OpponentTimesSackedPercentage,',
    'favorite_PointDifferential,',
    'favorite_TurnoverDifferential,',
    'favorite_PenaltyYardDifferential,',
    'favorite_TimeOfPossession,',
    'underdog_id,',
    'underdog_Score,',
    'underdog_OffensiveYards,',
    'underdog_OffensiveYardsPerPlay,',
    'underdog_RushingYards,',
    'underdog_RushingYardsPerAttempt,',
    'underdog_PassingYards,',
    'underdog_PassingYardsPerAttempt,',
    'underdog_PassingInterceptionPercentage,',
    'underdog_TimesSackedPercentage,',
    'underdog_OpponentScore,',
    'underdog_OpponentOffensiveYards,',
    'underdog_OpponentOffensiveYardsPerPlay,',
    'underdog_OpponentRushingYards,',
    'underdog_OpponentRushingYardsPerAttempt,',
    'underdog_OpponentPassingYards,',
    'underdog_OpponentPassingYardsPerAttempt,',
    'underdog_OpponentPassingInterceptionPercentage,',
    'underdog_OpponentTimesSackedPercentage,',
    'underdog_PointDifferential,',
    'underdog_TurnoverDifferential,',
    'underdog_PenaltyYardDifferential,',
    'underdog_TimeOfPossession,',
    'actual'
    # 'did_cover'
)

def getUnderdog(game):
    if game['team_favorite_id'] == game['team_home']:
        return game['team_away']
    elif game['team_favorite_id'] == game['team_away']:
        return game['team_home']
    else:
        print(game)
        print >> sys.stderr, "A"
        sys.exit(1)

def getFinal(game):
    home = int(game['score_home'])
    away = int(game['score_away'])
    if game['team_favorite_id'] == game['team_home']:
        return (away - home)
    elif game['team_favorite_id'] == game['team_away']:
        return (home - away)
    else:
        print(game)
        print >> sys.stderr, "A"
        sys.exit(1)

def printStats(team):
    print(
        team['Team'], ",",
        team['Score'], ",",
        team['OffensiveYards'], ",",
        team['OffensiveYardsPerPlay'], ",",
        team['RushingYards'], ",",
        team['RushingYardsPerAttempt'], ",",
        team['PassingYards'], ",",
        team['PassingYardsPerAttempt'], ",",
        team['PassingInterceptionPercentage'], ",",
        team['TimesSackedPercentage'], ",",
        team['OpponentScore'], ",",
        team['OpponentOffensiveYards'], ",",
        team['OpponentOffensiveYardsPerPlay'], ",",
        team['OpponentRushingYards'], ",",
        team['OpponentRushingYardsPerAttempt'], ",",
        team['OpponentPassingYards'], ",",
        team['OpponentPassingYardsPerAttempt'], ",",
        team['OpponentPassingInterceptionPercentage'], ",",
        team['OpponentTimesSackedPercentage'], ",",
        team['PointDifferential'], ",",
        team['TurnoverDifferential'], ",",
        team['PenaltyYardDifferential'], ",",
        team['TimeOfPossession'], ",", end = ' '
    )
        

with open('latest_games.csv', newline='') as csvfile:
    games = csv.DictReader(csvfile)
    for game in games:
        underdog = getUnderdog(game)
        for team in teams:
            # if game['team_favorite_id'] == team['Team'] and game['schedule_season'] == team['Year']:
            if game['team_favorite_id'] == team['Team']:
                # print(team['Team'], ",", end = ' ')
                printStats(team)
        for team in teams:
            if underdog == team['Team']:
                # print(team['Team'])
                printStats(team)
        print(getFinal(game) < float(game['spread_favorite']))

f.close()
