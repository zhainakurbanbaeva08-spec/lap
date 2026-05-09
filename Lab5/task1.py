class User:
    def __init__(self, id_user: int, name: str, email: str):
        self._id=id_user
        self._name=name.strip().title()
        email_lower=email.lower()
        if '@' not in email_lower:
            raise ValueError("Некорректный формат: email должен содержать '@'")
        self._email=email_lower
    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"
    def __del__(self):
        print(f"User {self._name} deleted")

u=User(1, "john doe", "John@Example.com")
u2=User(2, "zhaina kurbanbayeva", "zhaina.kurbanbayeva@narxoz.kz")
print(u)
print(u2)