import time


class SleepTimer:
    """Classe responsável por gerenciar pausas (sleep) no sistema."""

    def wait_minutes(self, minutes: int):
        """
        Aguarda um número específico de minutos antes de continuar a execução.

        Args:
            minutes (int): O número de minutos que o sistema deve aguardar.
        """
        seconds = minutes * 60
        print(f"Aguardando {seconds} segundos até o próximo ciclo...")
        time.sleep(seconds)
