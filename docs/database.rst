Modèles de la base de données
=============================

Profile Model
-------------

.. code-block:: python

    class Profile(models.Model):
        """
        Represent the profile of a user.

        Fields :
            user (OneToOneField): One-to-one relationship to Django User class.
            favorite_city (CharField): Favorite city of the user.

        Methods:
            __str__(): Return a string representation of the profile in the format
                "<User.username>"
        """
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        favorite_city = models.CharField(max_length=64, blank=True)
        
        def __str__(self):
            return self.user.username


Address Model
-------------

.. code-block:: python

    class Address(models.Model):
        """
        Represents a physical address, typically used for storing location details.

        Fields:
            - number (PositiveIntegerField): The building or house number (must be
                between 1 and 9999).
            - street (CharField): The street name or address line (up to
                64 characters).
            - city (CharField): The city or locality (up to 64 characters).
            - state (CharField): The state or region code
                (must be 2 characters, e.g., 'CA' for California).
            - zip_code (PositiveIntegerField): The postal code (must be between
                1 and 99999).
            - country_iso_code (CharField): The ISO code of the country (must be
                3 characters, e.g., 'USA' for United States).

        Meta:
            verbose_name (str): The singular name for the model ('Address').
            verbose_name_plural (str): The plural name for the model ('Addresses').

        Methods:
            __str__(): Returns a string representation of the address in the
            format: "<number> <street>".
        """

        number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
        street = models.CharField(max_length=64)
        city = models.CharField(max_length=64)
        state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
        zip_code = models.PositiveIntegerField(
            validators=[MaxValueValidator(99999)]
        )
        country_iso_code = models.CharField(
            max_length=3, validators=[MinLengthValidator(3)]
        )

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.number} {self.street}"


Letting Model
-------------

.. code-block:: python

    class Letting(models.Model):
        """
        Represent a property listed for rent

        Fields :
            title (Charfield): name of the property listed (up to 256 characters)
            address (OneToOneFiled): One-to-one relationship to an address.
                Represent the address of the property

        Methods:
            __str__(): Return a string representation of the property in the format
                "<title>"
        """

        title = models.CharField(max_length=256)
        address = models.OneToOneField(Address, on_delete=models.CASCADE)

        def __str__(self):
            return self.title

