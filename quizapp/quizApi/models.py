from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class AllQuestion(models.Model):
    Fields_choice = [
        ('geo', 'Geography'),
        ('sci', "Science"),
        ('tec', "Technology"),
        ('cur', 'Current Affairs'),
        ('mus', 'Music'),
        ('ent', 'Entertainment'),
        ('his', 'History'),
        ('mat', "Maths"),
        ('lit', "Literature"),
        ('spo', "Sports"),
        ('mix', "Mixed")
    ]

    type_choices = [
        ('MCQ', 'Multiple_Choice'),
        ('txt', 'Text'),
        ('hin', 'Hints')
    ]
    created = models.DateTimeField(
        auto_now_add=True
    )
    creator = models.ForeignKey(
        'auth.User',
        related_name='questions',
        on_delete=models.CASCADE,
    )
    field = models.CharField(
        max_length=100,
        choices=Fields_choice,
        default='mix'
    )
    questionText = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    # answerText = models.CharField(
    #     max_length=200,
    #     null=False,
    #     blank=False
    # )
    questionType = models.CharField(
        max_length=100,
        choices=type_choices,
        default='txt'
    )

    def __str__(self):
        return "{} of {}".format(self.questionText, self.questionType)


class TextQuestion(models.Model):
    answer = models.CharField(
        max_length=50,
        blank=False
    )
    questionInfo = models.OneToOneField(
        AllQuestion,
        on_delete=models.CASCADE,
        related_name='Answer_of',
        limit_choices_to={'questionType': 'txt'}
    )


class Hintquestion(models.Model):
    noOfHints = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    hintA = models.CharField(
        max_length=30,
        blank=False
    )
    hintB = models.CharField(
        max_length=30,
        blank=True
    )
    hintC = models.CharField(
        max_length=30,
        blank=True
    )
    hintD = models.CharField(
        max_length=30,
        blank=True
    )
    hintE = models.CharField(
        max_length=30,
        blank=True
    )
    hintF = models.CharField(
        max_length=30,
        blank=True
    )
    hintG = models.CharField(
        max_length=30,
        blank=True
    )
    hintH = models.CharField(
        max_length=30,
        blank=True
    )
    hintI = models.CharField(
        max_length=30,
        blank=True
    )
    correctAnswer = models.CharField(
        max_length=100,
        blank=False
    )
    questionInfo = models.OneToOneField(
        AllQuestion,
        on_delete=models.CASCADE,
        related_name='Hints_of',
        limit_choices_to={'questionType': 'hin'}
    )

    def __str__(self):
        return "Here are {}, Correct is {}".format(self.noOfHints, self.correctAnswer)


class MCQquestion(models.Model):
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
    questionInfo = models.OneToOneField(
        AllQuestion,
        on_delete=models.CASCADE,
        related_name='Option_of',
        limit_choices_to={'questionType': 'MCQ'}
    )

    def __str__(self):
        return """  Question  : \n
                    Option A  : {}\n
                    Option B  : {}\n
                    Option C  : {}\n
                    Option D  : {}\n
                    CorOption : {}\n
            """.format(
            self.optA,
            self.optB,
            self.optC,
            self.optD,
            self.corrOpt,
        )


# def validate_max(val):
#     if val <= 1 or val > 10:
#         raise ValidationError("{} is not between 1 to 10".format(val))
#     return
