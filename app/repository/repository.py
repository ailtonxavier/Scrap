"""
Ponto de entrada para o pacote de repositórios.

Este módulo expõe as implementações de repositório para que os chamadores
possam importar diretamente do pacote, como em `from repository import WeatherRepository`.
"""

from .weather import WeatherRepository

__all__ = ["WeatherRepository"]
