RULES = [
    {
        "id": "RULE_1",
        "field": "account_age_days",
        "operator": ">=",
        "value": 90,
        "weight": 0.2,
        "reason": "Account age above threshold"
    },
    {
        "id": "RULE_2",
        "field": "kyc_verified",
        "operator": "==",
        "value": True,
        "weight": 0.3,
        "reason": "KYC verified"
    },
    {
        "id": "RULE_3",
        "field": "country",
        "operator": "in",
        "value": ["IN", "US", "UK"],
        "weight": 0.24,
        "reason": "Low risk country"
    },
    {
        "id": "RULE_4",
        "field": "monthly_volume",
        "operator": ">",
        "value": 500000,
        "weight": 0.0,
        "hard_reject": True,
        "reason": "Monthly volume too high"
    }
]

class DecisionEngine:
    THRESHOLD_APPROVE = 0.5

    def __init__(self, attributes):
        self.attributes = attributes

    def evaluate(self):
        score = 0
        reasons = []
        rules_triggered = []

        for rule in RULES:
            if self._matches(rule):
                rules_triggered.append(rule["id"])
                score += rule.get("weight", 0)
                reasons.append(rule.get("reason", ""))

                if rule.get("hard_reject", False):
                    return {
                        "decision": "REJECT",
                        "score": score,
                        "reasons": reasons,
                        "rules_triggered": rules_triggered
                    }

        decision = "APPROVE" if score >= self.THRESHOLD_APPROVE else "REVIEW"

        return {
            "decision": decision,
            "score": score,
            "reasons": reasons,
            "rules_triggered": rules_triggered
        }

    def _matches(self, rule):
        field = rule.get("field")
        if not field:
            return False
        value = self.attributes.get(field)
        op = rule.get("operator")
        target = rule.get("value")

        if op == "==":
            return value == target
        elif op == ">=":
            return value >= target
        elif op == "<=":
            return value <= target
        elif op == ">":
            return value > target
        elif op == "<":
            return value < target
        elif op == "in":
            return value in target
        return False
