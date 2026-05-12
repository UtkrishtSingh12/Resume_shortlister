# Resume Ranking System



## Table of Contents

- Introduction
- System Overview
- Features
- Technical Details
- Installation and Usage
- Example Use Cases
- Future Improvements
- Conclusion

---

## Introduction

The Resume Ranking System is a Python-based application designed to match candidates with job descriptions based on their resume content. This project aims to provide a efficient and accurate way to shortlist candidates for a particular job opening.

---

## System Overview

The system works by computing TF-IDF vectors for each resume and job description, and then calculating the cosine similarity between them. The candidates are ranked based on their similarity scores, with the top 3 candidates being selected for each job description.

---

## Features

- Multi-word phrase matching: The system prioritizes matching multi-word phrases over single-word matches to improve accuracy.
- Synonym and typo handling: The system uses a SKILL_ALIASES mapping to handle synonyms and typos in resume skills.
- TF-IDF vector computation: The system computes TF-IDF vectors for each resume and job description to calculate similarity scores.
- Cosine similarity calculation: The system calculates the cosine similarity between resume and job description vectors to rank candidates.
- Top 3 candidate selection: The system selects the top 3 candidates for each job description based on their similarity scores.

---

## Technical Details

- Native Python libraries: The system uses only native Python libraries, including numpy and scipy, to ensure efficiency and simplicity.
- Exact formulas: The system uses exact formulas provided to ensure accuracy and consistency.
- Shared vocabulary: The system builds a shared vocabulary from all resume skills to improve matching accuracy.

---

## Installation and Usage

To install and use the Resume Ranking System, follow these steps:

1. Clone the repository using git clone.
2. Install the required libraries using pip install -r requirements.txt.
3. Run the system using python main.py.
4. Provide the job description and resume files as input.
5. The system will output the top 3 candidates for each job description.

---

## Example Use Cases

- Job description: "Software Engineer with expertise in Python and machine learning."
- Resume files: ["resume1.pdf", "resume2.pdf", "resume3.pdf"]
- Output: The system will output the top 3 candidates for the job description, along with their similarity scores.

---

## Future Improvements

- Handling ties in ranking: The system can be improved to handle ties in ranking candidates by using additional metrics, such as candidate experience or education.
- Optimizing cosine similarity logic: The system can be improved to optimize the cosine similarity logic for better matching by using techniques, such as word embeddings or topic modeling.

---

## Conclusion

The Resume Ranking System is a efficient and accurate way to match candidates with job descriptions based on their resume content. The system uses TF-IDF vectors and cosine similarity to rank candidates, and provides a simple and easy-to-use interface. With future improvements, the system can be even more effective in shortlisting candidates for job openings. 📊💻
