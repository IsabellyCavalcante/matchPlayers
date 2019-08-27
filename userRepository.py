class UserRepository():

    def __init__(self):
        self.users = {
            0: {
                "name": "Isabelly Cavalcante",
                "age": 25,
                "accepting_invitations": "y",
                "own_games": ["Dead of Winter", "Sagrada", "Abyss"],
                "interest_games": ["Azul", "7 Wonders"]
            }
        }

    def create_user(self, user):
        user_id = int(max(self.users.keys())) + 1
        self.users[user_id] = user

        return self.users.get(user_id)

    def has_user(self, user_id):
        return user_id in self.users

    def get_user(self, user_id):
        return self.users[user_id]

    def remove_user(self, user_id):
        self.users.pop(user_id)

    def get_users(self):
        return self.users
