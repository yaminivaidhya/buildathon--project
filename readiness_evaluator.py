def evaluate_readiness(score):
    if score < 40:
        return "Beginner"
    elif score < 70:
        return "Intermediate"
    else:
        return "Ready for Interviews"