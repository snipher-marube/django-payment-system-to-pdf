from django.db import models

class Grade(models.Model):
    POSITION_CHOICES = (
        ('Technician', 'Technician'),
        ('Lead Programmer', 'Lead Programmer'),
        ('CTO', 'CTO'),
        ('Manager', 'manager')
    )
    position = models.CharField(max_length=255, choices=POSITION_CHOICES)
    basic_salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    hours = models.PositiveIntegerField(default=0)
    grade_status = models.ForeignKey(Grade, on_delete=models.CASCADE)
    gross_salary = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.gross_salary = (self.hours * self.grade_status.basic_salary)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
