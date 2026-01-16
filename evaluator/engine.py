from .rules import RULES

OPERATORS = {
    "==": lambda a, b: a == b,
    ">=": lambda a, b: a >= b,
}

class DecisionEngine:
    def __init__(self, attributes):
        self.attributes = attributes
        self.score = 0
        self.reasons = []
        self.triggered_rules = []

    def evaluate(self):
        for rule in RULES:
            if self._matches(rule):
                self.triggered_rules.append(rule["id"])
                self.reasons.append(rule["message"])

                if rule.get("hard_reject"):
                    return self._reject()

                self.score += rule.get("weight", 0)

        return self._finalize()

    def _matches(self, rule):
        value = self.attributes.get(rule["field"])
        return OPERATORS[rule["operator"]](value, rule["value"])

    def _reject(self):
        return {
            "decision": "REJECT",
            "score": 0,
            "reasons": self.reasons,
            "rules_triggered": self.triggered_rules,
        }

    def _finalize(self):
        decision = "APPROVE" if self.score >= 0.5 else "REVIEW"
        return {
            "decision": decision,
            "score": round(self.score, 2),
            "reasons": self.reasons,
            "rules_triggered": self.triggered_rules,
        }
