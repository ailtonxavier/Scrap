class Singleton(type):
    """
    Metaclasse que implementa o padrão de design Singleton.

    Garante que qualquer classe que a utilize tenha apenas uma única instância
    durante todo o ciclo de vida da aplicação.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Controla a criação de instâncias.

        Se a classe (cls) ainda não tiver uma instância criada, cria uma nova
        e a armazena. Caso contrário, retorna a instância já existente.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
