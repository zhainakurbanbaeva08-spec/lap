class User:
    def __init__(self, id_user, name, email):
        self._id = int(id_user)
        self._name = name.strip().title()
        email_lower = email.strip().lower()
        if '@' not in email_lower:
            raise ValueError("Некорректный формат: email должен содержать '@'")
        self._email = email_lower

    @classmethod
    def from_string(cls, data: str):
        parts = data.split(',')
        if len(parts) != 3:
            raise ValueError("Строка должна содержать 3 элемента")
        return cls(parts[0], parts[1], parts[2])

    def __repr__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

u = User.from_string("2, Alice Wonderland , alice@wonder.com")
print(u)