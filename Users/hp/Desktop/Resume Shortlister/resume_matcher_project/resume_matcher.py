import math

# Function to normalize skills
def normalize_skills(skills):
    skill_aliases = {
        "python": "python",
        "pyhton": "python",
        "java": "java",
        "javascript": "javascript",
        "javascrpit": "javascript",
        "js": "javascript",
        "typescript": "typescript",
        "typescrpit": "typescript",
        "c++": "cpp",
        "cpp": "cpp",
        "r": "r",
        "kotlin": "kotlin",
        "machinelearning": "machine_learning",
        "machine learning": "machine_learning",
        "ml": "machine_learning",
        "sklearn": "machine_learning",
        "deeplearning": "deep_learning",
        "deep learning": "deep_learning",
        "deep-learning": "deep_learning",
        "tensorflow": "tensorflow",
        "pytorch": "pytorch",
        "keras": "keras",
        "nlp": "nlp",
        "bert": "bert",
        "xgboost": "xgboost",
        "feature engineering": "feature_engineering",
        "statistics": "statistics",
        "stats": "statistics",
        "regression": "regression",
        "clustering": "clustering",
        "data-viz": "data_visualization",
        "data visualization": "data_visualization",
        "data viz": "data_visualization",
        "matplotlib": "data_visualization",
        "tableau": "data_visualization",
        "power-bi": "data_visualization",
        "power bi": "data_visualization",
        "powerbi": "data_visualization",
        "pandas": "pandas",
        "numpy": "numpy",
        "react": "react",
        "reacts": "react",
        "reactjs": "react",
        "vue": "vue",
        "vue.js": "vue",
        "vuejs": "vue",
        "redux": "redux",
        "tailwind": "tailwind",
        "html/css": "html_css",
        "html css": "html_css",
        "html": "html_css",
        "css": "html_css",
        "jest": "jest",
        "graphql": "graphql",
        "node.js": "nodejs",
        "nodejs": "nodejs",
        "node js": "nodejs",
        "flask": "flask",
        "spring boot": "spring_boot",
        "springboot": "spring_boot",
        "rest api": "rest_api",
        "rest": "rest_api",
        "restapi": "rest_api",
        "microservices": "microservices",
        "sql": "sql",
        "mysql": "mysql",
        "mysq": "mysql",
        "postgresql": "postgresql",
        "postgres": "postgresql",
        "mongodb": "mongodb",
        "redis": "redis",
        "docker": "docker",
        "kubernetes": "kubernetes",
        "kubernates": "kubernetes",
        "k8s": "kubernetes",
        "ci/cd": "ci_cd",
        "cicd": "ci_cd",
        "ci cd": "ci_cd",
        "aws": "aws",
        "android": "android",
        "firebase": "firebase",
        "algorithms": "algorithms",
        "algoritms": "algorithms",
        "data structure": "data_structures",
        "data structures": "data_structures",
        "competitive programming": "competitive_programming",
        "ui/ux": "ui_ux",
        "ui ux": "ui_ux",
        "figma": "figma",
    }
    normalized_skills = []
    for skill in skills.split(","):
        skill = skill.strip().lower()
        if skill in skill_aliases:
            normalized_skills.append(skill_aliases[skill])
    return normalized_skills

# Function to deduplicate skills
def deduplicate_skills(skills):
    return list(set(skills))

# Function to compute TF-IDF
def compute_tf_idf(resumes):
    tf_idf = {}
    for resume in resumes:
        skills = normalize_skills(resume['skills'])
        skills = deduplicate_skills(skills)
        resume['skills'] = skills  # Update the resume with normalized and deduplicated skills
        tf_idf[resume['id']] = {}
        for skill in skills:
            tf = 1 / len(skills)
            df = 0
            for r in resumes:
                if skill in r['skills']:
                    df += 1
            if df == 0:
                idf = 0
            else:
                idf = math.log(10 / df)
            tf_idf[resume['id']][skill] = tf * idf
    return tf_idf

# Function to compute cosine similarity
def compute_cosine_similarity(tf_idf, job_description):
    similarity = {}
    for resume_id, skills in tf_idf.items():
        dot_product = 0
        magnitude_resume = 0
        magnitude_job = 0
        for skill in job_description['required_skills'] + job_description['preferred_skills']:
            if skill in skills:
                dot_product += skills[skill]
                magnitude_resume += skills[skill] ** 2
            magnitude_job += 1
        magnitude_resume = math.sqrt(magnitude_resume) if magnitude_resume != 0 else 1
        magnitude_job = math.sqrt(magnitude_job)
        similarity[resume_id] = dot_product / (magnitude_resume * magnitude_job) if magnitude_resume * magnitude_job != 0 else 0
    return similarity

# Main function
def main():
    # Define resumes and job descriptions
    resumes = [
        {'id': 1, 'name': 'John', 'skills': 'python, java, c++'},
        {'id': 2, 'name': 'Jane', 'skills': 'python, javascript, html'},
        {'id': 3, 'name': 'Rahul', 'skills': 'java, spring boot, mysql'},
        {'id': 4, 'name': 'Sneha', 'skills': 'python, tensorflow, keras'},
        {'id': 5, 'name': 'Vikram', 'skills': 'c++, algorithms, data structures'},
        {'id': 6, 'name': 'Ananya', 'skills': 'javascript, vue.js, python'},
        {'id': 7, 'name': 'Karan', 'skills': 'python, sklearn, xgboost'},
        {'id': 8, 'name': 'Deepika', 'skills': 'java, android, kotlin'},
        {'id': 9, 'name': 'Aditya', 'skills': 'reactjs, typescript, graphql'},
        {'id': 10, 'name': 'Meera', 'skills': 'python, r, statistics'},
    ]
    job_descriptions = [
        {'id': 1, 'company': 'Kakao', 'role': 'ML Engineer', 'required_skills': ['python', 'machinelearning', 'deeplearning'], 'preferred_skills': ['nlp', 'bert', 'feature_engineering']},
        {'id': 2, 'company': 'Naver', 'role': 'Backend Engineer', 'required_skills': ['java', 'springboot', 'mysql'], 'preferred_skills': ['restapi', 'ci_cd', 'redis']},
        {'id': 3, 'company': 'Line', 'role': 'Frontend Engineer', 'required_skills': ['javascript', 'react', 'vue'], 'preferred_skills': ['nodejs', 'graphql', 'redux']},
    ]

    # Compute TF-IDF
    tf_idf = compute_tf_idf(resumes)

    # Compute cosine similarity
    for job_description in job_descriptions:
        similarity = compute_cosine_similarity(tf_idf, job_description)
        print(f"Job Description: {job_description['company']} - {job_description['role']}")
        print("Similarity:")
        for resume_id, sim in similarity.items():
            print(f"Resume {resume_id}: {sim:.2f}")
        print()

if __name__ == "__main__":
    main()