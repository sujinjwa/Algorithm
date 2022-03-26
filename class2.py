class User:
    def __init__(self, ID="codetree", level=10):
        self.ID = ID
        self.level = level

user = User()
print(f"user {user.ID} lv {user.level}")

ID, level = tuple(input().split())

user1 = User(ID, int(level))

print(f"user {user1.ID} lv {user1.level}")