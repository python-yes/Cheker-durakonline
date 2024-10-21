from durakonline import durakonline

FILE_DIRECTORY: str = "./accounts.txt"

class Checked:
    def __init__(self) -> None:
        self.load_accounts()

    def load_accounts(self) -> int:
        with open(FILE_DIRECTORY, 'r') as file:
            tokens = file.read().split()
        for token in tokens:
            try:
                durak = durakonline.Client(server_id="u3")
                durak.authorization.signin_by_access_token(token)
                user = durak.get_user_info(durak.uid)

                print(f"""
                        Токен: {token}
                        Ник: {user.name}
                        Баланс: {durak.info.get('points')}
                        Рейтинг: {durak.info.get('score')}
                        Победы: {durak.info.get('wins')}
                        Победы за сезон: {durak.info.get('wins_s', 0)}
                    """)
            except:
                print(f"""
                        Токен: {token}
                        Невалидный
                    """)

if __name__ == "__main__":
    script = Checked
    script()
    print("all")