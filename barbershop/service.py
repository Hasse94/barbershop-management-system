"""Service model: something the barbershop offers, like a haircut."""

from decimal import Decimal


class Service:
    """A service the barbershop offers, with a name, a price and a duration.

    The price and the active status are protected: they can be read from
    outside the class, but only changed through the methods below, so the
    rules are always checked.
    """

    def __init__(self, name: str, price: Decimal, duration_minutes: int) -> None:
        """Create a service after checking that all data is valid.

        Args:
            name: The service name, e.g. "Haircut". Cannot be empty.
            price: The price in SEK. Must be a Decimal and not negative.
            duration_minutes: How long the service takes. Must be above 0.

        Raises:
            ValueError: If the name is empty, the price is negative,
                or the duration is 0 or less.
            TypeError: If the price is not a Decimal.
        """
        # Validate first, so an invalid Service can never exist.
        if not name or not name.strip():
            raise ValueError("Service name cannot be empty.")
        self._validate_price(price)
        if duration_minutes <= 0:
            raise ValueError("Service duration must be greater than 0 minutes.")

        # Store the data on this object.
        self.name = name.strip()  # Remove extra spaces, e.g. " Haircut " -> "Haircut"
        self.duration_minutes = duration_minutes
        self._price = price  # Private: only changed through update_price()
        self._is_active = True  # Private: only changed through deactivate()

    @property
    def price(self) -> Decimal:
        """The current price. Read-only from outside the class."""
        return self._price

    @property
    def is_active(self) -> bool:
        """Whether the service is currently offered and can be booked."""
        return self._is_active

    def update_price(self, new_price: Decimal) -> None:
        """Change the price while keeping the price rules.

        Args:
            new_price: The new price in SEK.

        Raises:
            TypeError: If the new price is not a Decimal.
            ValueError: If the new price is negative.
        """
        self._validate_price(new_price)
        self._price = new_price

    def deactivate(self) -> None:
        """Stop offering this service without deleting it.

        The service is kept (soft delete) so that past appointments
        can still refer to it.
        """
        self._is_active = False

    @staticmethod
    def _validate_price(price: Decimal) -> None:
        """Check the price rules, used by both __init__ and update_price().

        Keeping the rules in one place means they only need to be
        changed in one place (DRY: Don't Repeat Yourself).

        Raises:
            TypeError: If the price is not a Decimal (floats are not exact for money).
            ValueError: If the price is negative.
        """
        if not isinstance(price, Decimal):
            raise TypeError("Price must be a Decimal.")
        if price < 0:
            raise ValueError("Price cannot be negative.")