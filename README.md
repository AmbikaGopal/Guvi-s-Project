Placement App Project:

This project is a full-stack, data-driven Placement Management Dashboard built using:

MySQL for relational database storage

Python for data insertion and logic

Faker for synthetic data generation

Streamlit for an interactive front-end web interface

The platform enables colleges or institutions to evaluate student readiness for placement, analyze technical and soft skills, and monitor placement progress across batches.

📁 Features

✅ Backend & Data Features

MySQL database setup with foreign key constraints

Tables:

Students

Programming

Soft_Skills

Placements

Data Population using the Faker library with: 300 synthetic students

Technical skill profiles (language, problems, mini-projects, etc.)

Soft skills ratings

Placement status, packages, and company info

💻 Frontend - Streamlit Dashboard

Home Navigation Sidebar

Pages:

Students: View student table

Check the Eligibility: Based on programming skills and communication

Technical Skills: Filter by language and view assessments

Companies: Top companies offering highest packages

Analytics: In-depth batch-wise and language-wise performance


🗃️ Database Schema Overview

Students Table: Basic information about students(name, age, email, etc.)

Programming Table: Coding skills and project work of the students

soft_skills: Soft Skills of the student (Communication, leadership, etc.)

placements: Placement status, company details and outcomes os the students

📈 Key Analytics Implemented

📊 Average programming metrics by batch

👨‍💻 Top students by mini-projects or certifications

🔍 Skill-wise and company-wise placement analysis

🏆 Top 10 students by placement package

📅 Year-wise package trend
