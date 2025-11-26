"""Repository package entrypoint.

Expose repository implementations from this module so callers can import
`from repository import WeatherRepository`.
"""

from .weather import WeatherRepository

__all__ = ["WeatherRepository"]
