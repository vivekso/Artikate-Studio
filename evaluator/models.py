import uuid
from django.db import models

class Evaluation(models.Model):
    evaluation_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.CharField(max_length=100)
    payload_hash = models.CharField(max_length=64, unique=True)

    decision = models.CharField(max_length=10)
    score = models.FloatField()

    reasons = models.JSONField()
    rules_triggered = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
