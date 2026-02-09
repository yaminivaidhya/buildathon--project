def adaptive_learning_plan(missing_skills):
    plan = {}
    for skill in missing_skills:
        plan[skill] = f"Recommended course + practice for {skill}"
    return plan