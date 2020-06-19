from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Project(models.Model):
    projectName = models.CharField(
        max_length=250, 
        unique=True, 
        blank=False
    )
    projectDescription = models.CharField(
        max_length=1000, 
        blank=True,
        null=True
    )
    projectCreator =  models.ForeignKey(
        'auth.User',
        related_name='projects',
        on_delete=models.CASCADE,
    )
    organization = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )



class QuestionSet(models.Model):
    setName = models.CharField(
        max_length=250, 
        unique=True, 
        blank=False
    )
    setDescription = models.CharField(
        max_length=1000, 
        blank=True,
        null=True
    )
    setCreator =  models.ForeignKey(
        'auth.User',
        related_name='sets',
        on_delete=models.CASCADE,
    )
    setProject = models.ManyToManyField(
        Project,
        related_name="Sets",
    )
    parentSet = models.ManyToManyField(
        'self', 
        symmetrical=True,
        related_name='ChildSets',
        blank = True
    )



class TextQuestion(models.Model):
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

    answer = models.CharField(
        max_length=50,
        blank=False
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    creator = models.ForeignKey(
        'auth.User',
        related_name='Textquestions',
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
    questionSet = models.ManyToManyField(
        QuestionSet,
        related_name="SetQuestionsText",
    )
    def __str__(self):
        return " 'Answer' : '{}' ".format(self.answer)


class Hintquestion(models.Model):
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
    hintJ = models.CharField(
        max_length=30,
        blank=True
    )
    correctAnswer = models.CharField(
        max_length=100,
        blank=False
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    creator = models.ForeignKey(
        'auth.User',
        related_name='Hintquestions',
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
    questionSet = models.ManyToManyField(
        QuestionSet,
        related_name="SetQuestionsHint",
    )

    def __str__(self):
        return " 'noOfHints' : '{}', 'hintA': '{}', 'hintB': '{}', 'hintC': '{}', 'hintD': '{}', 'hintE': '{}', 'hintF': '{}', 'hintG': '{}','hintH': '{}','hintI': '{}', 'correctAnswer' : '{}' ".format(
            self.noOfHints,
            self.hintA,
            self.hintB,
            self.hintC,
            self.hintD,
            self.hintE,
            self.hintF,
            self.hintG,
            self.hintH,
            self.hintI,
            self.correctAnswer)


class MCQquestion(models.Model):
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

    created = models.DateTimeField(
        auto_now_add=True
    )
    creator = models.ForeignKey(
        'auth.User',
        related_name='MCQquestions',
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
    questionSet = models.ManyToManyField(
        QuestionSet,
        related_name="SetQuestionsMCQ",
    )


    def __str__(self):
        return """ 'optA' : '{}','optB' : '{}','optC' : '{}','optD' : '{}','corrOpt' : '{}' """.format(
            self.optA,
            self.optB,
            self.optC,
            self.optD,
            self.corrOpt,
        )

