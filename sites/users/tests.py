from django.test import TestCase
from loguru import logger
from faker import Faker
import random
from datetime import date, timedelta

def generate_random_data():
    fake = Faker('ru_RU')
    
    it_positions = ['Python разработчик', 'JavaScript разработчик', 'Web-дизайнер', 'Системный администратор', 'Тестировщик']
    marketing_positions = ['Маркетолог', 'PR-менеджер', 'SMM-специалист', 'Копирайтер', 'SEO-специалист']
    all_positions = it_positions + marketing_positions

    # генерируем случайное имя и фамилию
    name = fake.first_name()
    last_name = fake.last_name()

    # генерируем случайную почту
    email = fake.email()

    # генерируем случайную должность
    position = random.choice(all_positions)

    # генерируем случайный город
    city = fake.city()

    # генерируем случайную дату рождения в диапазоне 18-65 лет
    today = date.today()
    age = random.randint(18, 65)
    birth_date = today - timedelta(days=365*age)

    # возвращаем словарь с сгенерированными данными
    return {'first_name': name, 'last_name': last_name, 'email': email, 'position': position, 'city': city, 'birth_date': birth_date}

logger.debug(str(generate_random_data()))