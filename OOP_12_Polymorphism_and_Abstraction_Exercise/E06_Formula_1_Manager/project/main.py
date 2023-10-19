from project.f1_season_app import F1SeasonApp

f1_season = F1SeasonApp()
f1_season.register_team_for_season("Red Bull", 1_000_000)
f1_season.register_team_for_season("Mercedes", 2_000_000)
# f1_season.register_team_for_season("Mercedes", 999_999)
print(f1_season.new_race_results("Nurburgring", 11, 15))
# print(f1_season.new_race_results("Silverstone", 10, 1))