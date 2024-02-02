# Gettting Started
This script relies on the `numpy`, `pandas`, and `nba_api` packages. `nba_api` will require Python 3.7+ as well as the `requests` package. The package can be found [here](https://github.com/swar/nba_api).

# Running this Script

The script is run in terminal as:

> python lineup_scrape.py -i "included players" -e "excluded players" -t TEAM -m minimum

For `included` and `excluded players`, you must include them as a comma separated list, with the name in F. Last Name convention. These fields are optional, so no inputs will simply pull every lineup on NBA.com. The `team` field will specify lineups from only a specific team. By default, having no team will simply pull every lineup with the specified restrictions. Finally `minimum` will filter lineups to a minimum minutes played. The default value is 0, which will give ALL lineups

**Example 1:** To see every lineup with Joel Embiid and Tyrese Maxey, and without Nicolas Batum, you would enter:
 
`python lineup_scrape.py -i "J. Embiid, T. Maxey" -e "N. Batum`
and get the results:
```
  GROUP_NAME TEAM_ABBREVIATION    MIN    POS    PFOR     PAG  OFF_RATING  DEF_RATING  NET_RATING    PACE
 -1      Total               PHI  456.0  958.0  1083.0  1057.0       113.0       110.3         2.7  100.84
 Full results saved to lineup_results.csv
```

The full results, which include all the lineups with Embiid and Maxey and no Batum will be saved to the file `lineup_results.csv`.

**Example 2:** To see every Raptors lineup that played at least 10 minutes together, including OG Anunoby and Scottie Barnes, and without Pascal Siakam and Gradey Dick,  you would enter:

`python lineup_scrape.py -i "O. Anunoby, S. Barnes" -e "P. Siakam, G. Dick' -t TOR -m 10` and get the results:

```
GROUP_NAME TEAM_ABBREVIATION    MIN    POS   PFOR    PAG  OFF_RATING  DEF_RATING  NET_RATING   PACE
-1      Total               TOR  145.5  298.0  319.0  296.0       107.0        99.3         7.7  98.31
Full results saved to lineup_results.csv
```

Note there may be some unexepcted/conflicting outputs, check the **Limitations** section for more.

# Notes
Offensive Rating and Defensive Rating are calculated differently on websites. This script relies on NBA.com methodology which has tracking data and uses points scored for/against per 100 possessions.


Cumulative Offensive and Defensive Ratings are calculated by estimating total points scored and against. Using a formula described [here](https://hackastat.eu/en/learn-a-stat-possessions-and-pace/#:~:text=not%20real%20values.-,Formula,those%20finished%20at%20regular%20times.), we can approximate total possessions played for a given lineup. Then, the points scored and against can be estimated using offensive and defensive rating along with total possesions. **This script tends to underestimate cumulative offensive and defensive rating**, however, net rating effects are still correct. Thus any data from this script is best used comparatively, rather than selecting singular ratings. 

# Limitations
Because `NBA.com` stores players in lineups with the F. Last Name format, there can be issues with players of the same name. 

For example, **Jalen Williams** and **Jaylin Williams**, teammates of the OKC Thunder can not be distinguished. Another example is **Seth** and **Stephen Curry**, who play on the Mavericks and Golden State Warriors, respectively; to make sure the lineups selected are correct, it is important to include the team in this instance. There is currently no work around for players with the same name format and who are on the same team.
