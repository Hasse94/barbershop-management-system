"""Tests for the Service class."""

from decimal import Decimal

import pytest

from barbershop.service import Service


# ---------- Creating a service ----------

def test_create_valid_service():
    """A service with valid data stores everything and starts active."""
    service = Service("Haircut", Decimal("300"), 30)

    assert service.name == "Haircut"
    assert service.price == Decimal("300")
    assert service.duration_minutes == 30
    assert service.is_active is True


def test_name_is_stripped():
    """Extra spaces around the name are removed."""
    service = Service("  Beard trim  ", Decimal("150"), 15)

    assert service.name == "Beard trim"


def test_free_service_is_allowed():
    """A price of exactly 0 is valid (edge case: the rule is 'not negative')."""
    service = Service("Consultation", Decimal("0"), 10)

    assert service.price == Decimal("0")


# ---------- Validation: bad data is rejected ----------

def test_empty_name_raises_error():
    with pytest.raises(ValueError):
        Service("", Decimal("300"), 30)


def test_name_with_only_spaces_raises_error():
    with pytest.raises(ValueError):
        Service("   ", Decimal("300"), 30)


def test_negative_price_raises_error():
    with pytest.raises(ValueError):
        Service("Haircut", Decimal("-1"), 30)


def test_float_price_raises_type_error():
    """Floats are not exact for money, so only Decimal is accepted."""
    with pytest.raises(TypeError):
        Service("Haircut", 300.0, 30)


def test_zero_duration_raises_error():
    with pytest.raises(ValueError):
        Service("Haircut", Decimal("300"), 0)


# ---------- Encapsulation: protected data ----------

def test_price_is_read_only():
    """The price can't be set directly, only through update_price()."""
    service = Service("Haircut", Decimal("300"), 30)

    with pytest.raises(AttributeError):
        service.price = Decimal("1")


def test_update_price_changes_price():
    service = Service("Haircut", Decimal("300"), 30)

    service.update_price(Decimal("350"))

    assert service.price == Decimal("350")


def test_update_price_with_negative_keeps_old_price():
    """A rejected update must not change the price."""
    service = Service("Haircut", Decimal("300"), 30)

    with pytest.raises(ValueError):
        service.update_price(Decimal("-50"))

    assert service.price == Decimal("300")


def test_deactivate_makes_service_inactive():
    service = Service("Haircut", Decimal("300"), 30)

    service.deactivate()

    assert service.is_active is False