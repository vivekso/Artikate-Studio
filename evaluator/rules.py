RULES = [
    {
        "id": "RULE_1",
        "field": "account_age_days",
        "operator": ">=",
        "value": 90,
        "weight": 0.2,
        "message": "Account age above threshold"
    },
    {
        "id": "RULE_2",
        "field": "kyc_verified",
        "operator": "==",
        "value": False,
        "hard_reject": True,
        "message": "KYC not verified"
    }
]
