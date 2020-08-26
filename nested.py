ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
def friend_counter(a_dict):
  friends = 0
  for friend in a_dict["friends"]:
    friends += 1
  return friends


print(ramit["friends"][0]["email"])
print(ramit["friends"][1]["interests"][1])
print(friend_counter(ramit))
