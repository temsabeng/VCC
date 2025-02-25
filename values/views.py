from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ProjectEvaluation
@csrf_exempt
def project_evaluation_view(request):
   if request.method == "POST":
       try:
           data = json.loads(request.body.decode("utf-8"))  # JSON verisini al
           # Formdan gelen veriler
           project_name = data.get("project_name", "Unnamed Project")
           increase_revenue = int(data.get("increase_revenue", 0))
           cost_optimization = int(data.get("cost_optimization", 0))
           customer_experience = int(data.get("customer_experience", 0))
           regulative = int(data.get("regulative", 0))
           strategy = int(data.get("strategy", 0))
           value_total = sum([increase_revenue, cost_optimization, customer_experience, regulative, strategy])
           human_days = int(data.get("human_days", 0))
           budget = int(data.get("budget", 0))
           integrations_systems = int(data.get("integrations_systems", 0))
           department_processes = int(data.get("department_processes", 0))
           complexity_total = sum([human_days, budget, integrations_systems, department_processes])
           overall_total = value_total + complexity_total  # Toplam hesaplama
           # Veritabanına kayıt
           project = ProjectEvaluation.objects.create(
               project_name=project_name,
               increase_revenue=increase_revenue,
               cost_optimization=cost_optimization,
               customer_experience=customer_experience,
               regulative=regulative,
               strategy=strategy,
               value_total=value_total,
               human_days=human_days,
               budget=budget,
               integrations_systems=integrations_systems,
               department_processes=department_processes,
               complexity_total=complexity_total,
               overall_total=overall_total
           )
           return JsonResponse({"message": "Project successfully saved!", "project_id": project.id}, status=201)
       except Exception as e:
           return JsonResponse({"error": str(e)}, status=400)
   last_project = ProjectEvaluation.objects.order_by("-id").first()
   return render(request, "values/project_evaluation.html", {"last_project": last_project})