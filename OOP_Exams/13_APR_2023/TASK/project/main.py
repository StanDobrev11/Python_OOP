from project.robots_managing_app import RobotsManagingApp

app = RobotsManagingApp()
print(app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(app.service_price('ServiceRobotsWorld'))
print(app.service_price('ServiceTechnicalsWorld'))

print(str(app))

print(app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(app.service_price('ServiceRobotsWorld'))
print(app.service_price('ServiceTechnicalsWorld'))

print(str(app))
