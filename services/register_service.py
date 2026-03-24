class RegisterService:
    def __init__(self):
        self.storage = {} #fake DB

    #o'rganish uchun vaqtinchalik shu yechimga kelindi
    async def save_user(self, user_id: int, name: str, age: int):
        self.storage[user_id] = {
            "name": name,
            "age": age
        }
        return self.storage[user_id]
