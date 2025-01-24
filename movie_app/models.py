from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=258)

    def __str__(self):  # pyright: ignore
        return self.name

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"


class Movie(models.Model):
    title = models.CharField(max_length=258)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="movies",
    )

    def __str__(self):  # pyright: ignore
        return self.title

    class Meta:  # pyright: ignore
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    def __str__(self):  # pyright: ignore
        return self.movie.title  # pyright: ignore

    class Meta:
        verbose_name = "Rewiew"
        verbose_name_plural = "Rewiews"
