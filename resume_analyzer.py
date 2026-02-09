def analyze_resume(role, resume_text):
    role_keywords = {
        "data science": [
            "python",
            "statistics",
            "machine learning",
            "pandas",
            "numpy"
        ],
        "software development": [
            "java",
            "python",
            "c++",
            "data structures",
            "algorithms"
        ],
        "ux/ui design": [
            "figma",
            "wireframe",
            "prototype",
            "user research",
            "ui"
        ],
        "marketing analyst": [
            "google analytics",
            "seo",
            "roi",
            "campaign analysis",
            "excel"
        ]
    }

    # normalize inputs
    role = role.lower()
    resume_text = resume_text.lower()

    keywords = role_keywords.get(role, [])

    matched = []
    missing = []

    for keyword in keywords:
        if keyword in resume_text:
            matched.append(keyword)
        else:
            missing.append(keyword)

    score = int((len(matched) / len(keywords)) * 100) if keywords else 0

    return matched, missing, score