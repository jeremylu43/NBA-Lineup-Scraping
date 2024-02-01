# Gettting Started
This script relies on the `numpy`, `pandas`, and `nba_api` packages. `nba_api` will require Python 3.7+ as well as the `requests` package. The package can be found [here](https://github.com/swar/nba_api).


# Limitations
Because `NBA.com` stores players in lineups with the F. Last Name format, there can be issues with players of the same name. For example, Jalen Williams and Jaylin Williams, teammates of the OKC Thunder can not be distinguished. Another example of Seth and Stephen Curry, who play on the Mavericks and Golden State Warriors, have the same name. So to make sure the lineups selected are correct, it is important to include the team. There is currently no work around for players with the same name format and who are on the same team.
