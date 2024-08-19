"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1)
        assert product.quantity == 999

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


@pytest.fixture
def cart():
    return Cart()


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_cart_add(self, cart, product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 5)
        assert cart.products[product] == 6


    def test_cart_remove_single(self, cart, product):
        cart.add_product(product, 4)
        cart.remove_product(product, 1)
        assert cart.products[product] == 3
        cart.remove_product(product, 3)
        assert product not in cart.products


    def test_cart_clear_all(self, cart, product):
        cart.add_product(product, 5)
        cart.clear()
        assert len(cart.products) == 0


    def test_cart_total_price(self, cart, product):
        cart.add_product(product, 3)
        assert cart.get_total_price() == 300


    def test_cart_buy_more(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()


    def test_cart_buy(self, cart, product):
        cart.add_product(product, 3)
        cart.buy()

        assert product.quantity == 997
        assert len(cart.products) == 0