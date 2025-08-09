# setup.py
from setuptools import setup, find_packages

# Load dependencies from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.1",
    author="dammyjosh",
    description="A FlaskStreamlit-based anime recommendation system using Groq AI",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Streamlit",
        "Operating System :: OS Independent",
    ],
)