import pandas as pd
import numpy as np
import argparse
from nba_api.stats.endpoints import leaguelineupviz

parser = argparse.ArgumentParser(description='Given requirements, collect all lineups and display aggregate information')
parser.add_argument('-i', '--include', help='Players you want to include in F. Last Name format., and comma separated')
parser.add_argument('-e', '--exclude', help='Players you want to exclude in F. Last Name format., and comma separated')
parser.add_argument('-t', '--team', help='Team you want (if player was on multiple teams during season)')
parser.add_argument('-m', '--min', help='Minimum minutes played for lineup (0 is default)')
args = parser.parse_args()



def obtain_lineup_data(minute_min):
    endpoint = leaguelineupviz.LeagueLineupViz(minutes_min = minute_min)
    lineups = endpoint.get_data_frames()[0]
    lineups = lineups[['GROUP_NAME', 'TEAM_ABBREVIATION', 'MIN', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'PACE']]
    lineup_concat = []
    for lineup in lineups['GROUP_NAME']:
        lineup_concat.append([i.strip() for i in lineup.split(' - ')])
    lineups.loc[:, 'POS']= np.floor(lineups['PACE']/48 * lineups['MIN'])
    lineups.loc[:, 'PFOR']= np.floor(lineups['OFF_RATING'] * lineups['POS']/100)
    lineups.loc[:, 'PAG']= np.floor(lineups['DEF_RATING'] * lineups['POS']/100)
    return(lineups)

def main(include, exclude, team, min):
    if include is None:
        include = []
    else:
        include = include.split(', ')
    if exclude is None:
        exclude = []
    else:
        exclude = exclude.split(', ')
    if min is None:
        min = 0
        
    lineups = obtain_lineup_data(min)

    subset = lineups
    if team is not None:
        subset = lineups[lineups['TEAM_ABBREVIATION'] == team]
    for player in include:
        subset = subset[[player in lineup for lineup in subset['GROUP_NAME']]]
    for player in exclude:
        subset = subset[[player not in lineup for lineup in subset['GROUP_NAME']]]

    if len(subset.index) > 0:
        results = pd.DataFrame({'GROUP_NAME': 'Total',
                           'TEAM_ABBREVIATION': list(subset['TEAM_ABBREVIATION'])[0],
                           'MIN' : np.sum(subset['MIN']),
                           'POS' : np.sum(subset['POS']),
                           'PFOR' : np.sum(subset['PFOR']),
                           'PAG' : np.sum(subset['PAG']),
                           'OFF_RATING' : np.round(np.sum(subset['PFOR']) * 100/(np.sum(subset['POS'])), 1),
                           'DEF_RATING' : np.round(np.sum(subset['PAG']) * 100/(np.sum(subset['POS'])), 1),
                           'NET_RATING' : np.round((np.sum(subset['PFOR']) - np.sum(subset['PAG'])) * 100/(np.sum(subset['POS'])), 1),
                           'PACE': np.round(np.sum(subset['POS'])/np.sum(subset['MIN']) * 48, 2)},  index = [-1])
        final = pd.concat([results, subset])
        final.to_csv('lineup_results.csv')
        print(results)
        print('Full results saved to lineup_results.csv')
    else:
        results = pd.DataFrame()
        print('Your results are empty! Make sure your inputs are correct (Names are correct, and have space between each, team abbreviation is correct).')
        print('Alternatively, your minutes requirement may be too high, try lowering it.')
    
    
if __name__ == "__main__":
    main(args.include, args.exclude, args.team, args.min)