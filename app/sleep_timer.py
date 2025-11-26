import time


class SleepTimer:
    def wait_minutes(self, minutes: int):
        seconds = minutes * 60
        print(f"Aguardando {seconds} segundos até o próximo ciclo...")
        time.sleep(seconds)
