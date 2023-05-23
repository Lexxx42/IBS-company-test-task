"""This module is used for data generation."""
from dataclasses import dataclass


@dataclass
class Person:
    """Data class for person generation."""
    name: str = ""
    job: str = ""
