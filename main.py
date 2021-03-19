import logging
import logging.config

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('main')


class Auto:

    def __init__(self, mileage: int, brand: str, release_year: int):
        logger.debug(f'{mileage} | {brand} | {release_year}')
        self.mileage = mileage
        self.brand = brand
        self.release_year = release_year

    def car_years(self) -> int:
        try:
            return 2021 - self.release_year
        except Exception as e:
            logger.error(e)

    def format_brand(self) -> str:
        logger.info('Пользователь вызвал функцию format_brand')
        return f'Auto: {self.brand}'


if __name__ == '__main__':
    cars = [Auto(12314, 'BMW', 2004), Auto(124124, 'Lada', 2013), Auto(123124, 'asdasdasd', '2019')]

    for car in cars:
        print(f'{car.format_brand()} | {car.car_years()}')
