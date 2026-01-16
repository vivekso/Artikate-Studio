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
