from domain_recommender import recommend_domains

student_degree = input("Enter your degree: ")
student_interests = input("Enter your interests (comma separated): ").split(",")

results = recommend_domains(student_degree, student_interests)

print("\nRecommended Career Domains:")
for domain, score, interests in results:
    print(f"\nDomain: {domain}")
    print(f"Matched Interests: {', '.join(interests)}")
    print(f"Match Score: {score}")