"""This module is used for generating data for tests."""
from faker import Faker
from data import Person

faker_en = Faker('EN')
Faker.seed()


def generated_person():
    """
    Generation person data with Faker library.
    :returns: person generator object.
    """
    yield Person(
        name=faker_en.first_name(),
        job=faker_en.job()
    )
