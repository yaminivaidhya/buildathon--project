def recommend_domains(student_degree, student_interests):
    career_domains = {
        "UX/UI Design": {
            "degrees": {"Computer Science", "IT","it","It","computer science","Computerscience","computerscience"},
            "interests": {"Graphic Design", "Creativity", "Story Writing","storywriting","Storywriting","StoryWriting"}
        },
        "Software Development": {
            "degrees": {"Computer Science", "IT"},
            "interests": {"Problem Solving", "Coding", "Logic"}
        },
        "Data Science": {
            "degrees": {"Computer Science", "IT", "Maths"},
            "interests": {"Statistics", "Data Analysis", "Python","Logic"}
        }
    }

    student_interests = set(student_interests)
    recommendations = []

    for domain, data in career_domains.items():
        score = 0

        # Degree match
        if student_degree in data["degrees"]:
            score += 1

        # Interest match
        matched_interests = student_interests & data["interests"]
        score += len(matched_interests)

        if score > 0:
            recommendations.append((domain, score, matched_interests))

    # Sort by best match
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations 