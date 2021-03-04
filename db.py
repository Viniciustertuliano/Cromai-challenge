import peewee


db = peewee.SqliteDatabase("data.db")


class Triangulo(peewee.Model):
    """Triangulo model."""

    class Meta:
        database = db

    cateto_a = peewee.DecimalField(null=True, max_digits=4, decimal_places=2)
    cateto_b = peewee.DecimalField(null=True, max_digits=4, decimal_places=2)
    hipotenusa = peewee.DecimalField(null=False,
                                     max_digits=4, decimal_places=2)
