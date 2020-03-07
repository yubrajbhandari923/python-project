from django.db import models

# Create your models here.


class MCQquestion(models.Model):
    Fields_choice = [
        ('sci', "Science"),
        ("mat", "Maths"),
        ("lit", "Literature"),
        ("spo", "Sports"),
        ('mix', "Mixed")
    ]
    created = models.DateTimeField(
        auto_now_add=True
    )
    mainQuestion = models.CharField(
        max_length=150,
        blank=False
    )
    field = models.CharField(
        max_length=3,
        choices=Fields_choice,
        default='mix'
    )
    optA = models.CharField(
        max_length=30,
        blank=False
    )
    optB = models.CharField(
        max_length=30,
        blank=False
    )
    optC = models.CharField(
        max_length=30,
        blank=False
    )
    optD = models.CharField(
        max_length=30,
        blank=False
    )
    corrOpt = models.CharField(
        max_length=1,
        blank=False
    )
    creator = models.ForeignKey(
        'auth.User',
        related_name='questions',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return """Question  : {}\n
                  Option A  : {}\n
                  Option B  : {}\n
                  Option C  : {}\n
                  Option D  : {}\n
                  CorOption : {}\n
                  Created_by: {}\n
                  Created_on: {}\n
        """.format(
            self.mainQuestion,
            self.optA,
            self.optB,
            self.optC,
            self.optD,
            self.corrOpt,
            self.creator,
            self.created
        )
