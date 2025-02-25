from django.db import models
class ProjectEvaluation(models.Model):
   project_name = models.CharField(max_length=255)
   # Value alanları
   increase_revenue = models.IntegerField(default=0)
   cost_optimization = models.IntegerField(default=0)
   customer_experience = models.IntegerField(default=0)
   regulative = models.IntegerField(default=0)
   strategy = models.IntegerField(default=0)
   value_total = models.IntegerField(default=0)
   # Cost/Complexity alanları
   human_days = models.IntegerField(default=0)
   budget = models.IntegerField(default=0)
   integrations_systems = models.IntegerField(default=0)
   department_processes = models.IntegerField(default=0)
   complexity_total = models.IntegerField(default=0)
   # Genel toplam
   overall_total = models.IntegerField(default=0)
   def __str__(self):
       return f"{self.project_name} - Value: {self.value_total}, Complexity: {self.complexity_total}, Overall: {self.overall_total}"
