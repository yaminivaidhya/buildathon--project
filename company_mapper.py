def get_company_types(domain):
    companies = {
        "UX/UI Design": ["Design Agencies", "Startups", "Product Companies"],
        "Data Science": ["MNCs", "FinTech", "AI Startups"],
        "Software Development": ["MNCs", "Product Companies", "Startups"]
    }
    return companies.get(domain, ["Various companies"])