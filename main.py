from domain_recommender import recommend_domains
from roadmap import get_roadmap
from resume_analyzer import analyze_resume
from company_mapper import get_company_types
from readiness_evaluator import evaluate_readiness
from adaptive_learning import adaptive_learning_plan

print("=== CareerCompass System ===")

degree = input("Degree: ")
interests = input("Interests: ").split(",")

domains = recommend_domains(degree, interests)
print("\nRecommended Domains:", domains)

if domains:
    domain = domains[0][0]
    print("\nRoadmap:", get_roadmap(domain))
    print("Companies:", get_company_types(domain))

    role = input("\nTarget Role: ")
    resume = input("Paste Resume: ")

    matched, missing, score = analyze_resume(role, resume)
    print("Matched:", matched)
    print("Missing:", missing)
    print("Score:", score)
    print("Level:", evaluate_readiness(score))

    print("Adaptive Plan:", adaptive_learning_plan(missing))