# Gettting Started
This script relies on the `numpy`, `pandas`, and `nba_api` packages. `nba_api` will require Python 3.7+ as well as the `requests` package. The package can be found [here](https://github.com/swar/nba_api).

# Running this Script

# Notes
Offensive Rating and Defensive Rating are calculated differently on websites. This script relies on NBA.com methodology which has tracking data and uses points scored for/against per 100 possessions.
Cumulative Offensive and Defensive Ratings are calculated by estimating total points scored and against. Using a formula described [here](https://hackastat.eu/en/learn-a-stat-possessions-and-pace/#:~:text=not%20real%20values.-,Formula,those%20finished%20at%20regular%20times.), we can approximate Possessions played for a given lineup. Then, the points scored and against can be estimated using offensive and defensive rating along with total possesions. **This script tends to underestimate cumulative offensive and defensive rating**, however, net rating effects are still correct. Thus any data from this script is best used comparatively, rather than selecting singular ratings. 

# Limitations
Because `NBA.com` stores players in lineups with the F. Last Name format, there can be issues with players of the same name. 

For example, **Jalen Williams** and **Jaylin Williams**, teammates of the OKC Thunder can not be distinguished. Another example is **Seth** and **Stephen Curry**, who play on the Mavericks and Golden State Warriors, respectively; to make sure the lineups selected are correct, it is important to include the team in this instance. There is currently no work around for players with the same name format and who are on the same team.
