from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import EvaluationRequestSerializer
from .models import Evaluation
from .engine import DecisionEngine
from .utils import hash_payload

class EvaluateAPIView(APIView):
    def post(self, request):
        serializer = EvaluationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payload = serializer.validated_data
        payload_hash = hash_payload(payload)

        existing = Evaluation.objects.filter(payload_hash=payload_hash).first()
        if existing:
            return Response(self._response(existing))

        engine = DecisionEngine(payload["attributes"])
        result = engine.evaluate()

        evaluation = Evaluation.objects.create(
            user_id=payload["user_id"],
            payload_hash=payload_hash,
            decision=result["decision"],
            score=result["score"],
            reasons=result["reasons"],
            rules_triggered=result["rules_triggered"],
        )

        return Response(self._response(evaluation), status=201)

    def _response(self, evaluation):
        return {
            "decision": evaluation.decision,
            "score": evaluation.score,
            "reasons": evaluation.reasons,
            "rules_triggered": evaluation.rules_triggered,
            "evaluation_id": str(evaluation.evaluation_id),
            "timestamp": evaluation.created_at.isoformat(),
        }
