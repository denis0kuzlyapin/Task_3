from abc import ABC, abstractmethod


class LoginStrategy(ABC):
    #Абстрактный класс для стратегии авторизации
    
    @abstractmethod
    def login(self, email: str, password: str):
        #Выполнить авторизацию
        pass
    
    @abstractmethod
    def is_logged_in(self) -> bool:
        #Проверить, что авторизация прошла успешно
        pass