def get_roadmap(domain):
    roadmaps = {
        "UX/UI Design": [
            "Week 1–2: Learn design basics (color theory, typography)",
            "Week 3–4: Learn Figma or Adobe XD",
            "Week 5–6: Practice wireframes & prototypes",
            "Week 7–8: Build portfolio projects",
            "Week 9: Learn UX research basics"
        ],

        "Software Development": [
            "Week 1–2: Programming fundamentals",
            "Week 3–4: Data Structures & Algorithms",
            "Week 5–6: Coding practice",
            "Week 7–8: Mini projects",
            "Week 9: Core CS revision"
        ],

        "Data Science": [
            "Week 1–2: Learn Python basics",
            "Week 3–4: Statistics & probability",
            "Week 5–6: Data analysis with datasets",
            "Week 7–8: Machine learning basics",
            "Week 9: Mini data science projects"
        ]
    }

    return roadmaps.get(domain, ["No roadmap available for this domain"])