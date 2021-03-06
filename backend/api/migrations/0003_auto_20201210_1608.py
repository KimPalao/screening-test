# Generated by Django 3.1.4 on 2020-12-10 16:08

from django.db import migrations


def fill_values_and_principles(apps, schema_editor):
    values = [
        "Individuals and Interactions Over Processes and Tools",
        "Working Software Over Comprehensive Documentation",
        "Customer Collaboration Over Contract Negotiation",
        "Responding to Change Over Following a Plan",
    ]

    principles = [
        "Customer satisfaction through early and continuous software delivery",
        "Accommodate changing requirements throughout the development process",
        "Frequent delivery of working software",
        "Collaboration between the business stakeholders and developers throughout the project",
        "Support, trust, and motivate the people involved",
        "Enable face-to-face interactions",
        "Working software is the primary measure of progress",
        "Agile processes to support a consistent development pace",
        "Attention to technical detail and design enhances agility",
        "Simplicity",
        "Self-organizing teams encourage great architectures, requirements, and designs",
        "Regular reflections on how to become more effective",
    ]

    Value = apps.get_model("api", "Value")
    Principle = apps.get_model("api", "Principle")
    for value in values:
        Value.objects.create(text=value)
    for principle in principles:
        Principle.objects.create(text=principle)


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_auto_20201210_1521"),
    ]

    operations = [migrations.RunPython(fill_values_and_principles)]
