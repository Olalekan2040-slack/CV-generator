PRD.md
Project Title: Django CV Maker MVP
Document Version: 1.0
1. Project Overview
1.1 Product Summary
The Django CV Maker is a web application that enables users to input personal and professional information, select a CV template, and generate a visually appealing CV in PDF format. The app will satisfy MVP requirements by offering basic template options, user authentication, and downloadable CVs.

1.2 Objective
To create a functional MVP for a CV generator web app, allowing users to create a professional CV based on pre-designed templates in a user-friendly, accessible way.

2. Target Audience
Job seekers
Freelancers
Students looking to apply for internships or job positions
3. Product Requirements
3.1 Key Features for MVP
User Registration and Authentication

Sign-up and log-in functionality.
Password reset and account recovery options.
User Profile Management

Option to enter and save personal and professional details.
Edit and update information as needed.
CV Template Selection

Display 2-3 CV templates for users to choose from.
Preview feature to see how the CV will look with their information.
CV Generation and Download

Use Django templates to format the CVs.
Export the CV in PDF format.
Allow users to download the generated CV.
Basic Dashboard

Show saved CVs, allowing users to select a template, and edit or delete CVs.
Responsive Design

Ensure the app is optimized for both desktop and mobile devices.
4. Technical Requirements
4.1 Frontend Stack
HTML, CSS (for styling), and Bootstrap for responsive design.
JavaScript for any dynamic elements (e.g., template preview).
4.2 Backend Stack
Django (latest stable version) for server-side logic and database interaction.
Django REST Framework (optional for future API use).
4.3 Database
SQLite (for MVP); migrate to PostgreSQL if scaling becomes necessary.
4.4 PDF Generation
Use a library like WeasyPrint, ReportLab, or xhtml2pdf to generate downloadable PDFs from Django templates.
4.5 Version Control
Use Git for source control with GitHub or GitLab for remote repository management.
5. Development Steps
5.1 Project Setup
Set up the Django project and Git repository

Initialize Django project with necessary configurations.
Create Git repository and commit initial setup.
Create User Authentication Module

Set up Django’s authentication system for sign-up, login, and password reset functionality.
Implement secure password storage using Django’s built-in hashing mechanisms.
5.2 User Profile Management
Design Profile Models

Create Django models for user information (personal details, work experience, education, skills, etc.).
Implement views and forms for user profile creation and editing.
Create Profile Pages

Build profile creation/editing forms and views.
Design pages using Bootstrap for responsive layouts.
5.3 CV Template Selection
Build Template Selection Page

Create models and views to display available CV templates.
Enable template preview to show a snapshot of what the user’s CV would look like.
Template Design

Develop HTML templates for each CV layout option using Django’s templating system.
Include placeholders for user data (e.g., {{ user.name }}, {{ user.experience }}).
5.4 CV Generation and Download
Integrate PDF Library

Choose and integrate a PDF generation library (e.g., WeasyPrint).
Ensure HTML templates are compatible with PDF conversion.
Build Download Functionality

Add a "Download" button that triggers PDF generation.
Implement backend logic to generate and serve the PDF for download.
5.5 Dashboard and User Management
Build Basic Dashboard

Create a dashboard page showing saved CVs and options to create a new CV, edit existing information, or delete records.
Error Handling and User Feedback

Ensure informative error messages for validation (e.g., missing fields).
Include flash messages to confirm successful actions (e.g., “Profile Updated”).
5.6 Responsive and User-Friendly Design
Responsive Styling
Ensure mobile-friendly design using Bootstrap.
Test across various screen sizes and browsers.
5.7 Testing and Quality Assurance
Unit Testing

Write unit tests for critical features like CV generation, authentication, and form submissions.
Integration Testing

Test the end-to-end flow of creating, editing, generating, and downloading a CV.
5.8 Deployment
Set Up Deployment Environment

Set up a hosting environment (e.g., Heroku or DigitalOcean).
Ensure database connections and static file handling.
Push to Production

Push the final MVP build to the production environment.
Conduct final tests and fix any issues that arise.
6. Future Scope
Once the MVP is validated, the following features can be added in future iterations:

More customizable templates with color and font options.
API to integrate with LinkedIn for profile import.
Premium templates and subscription plans.
Analytics on CV views and downloads.
7. Timeline and Milestones
Milestones
Week 1: Project setup, authentication, and user profile.
Week 2: Template design and selection functionality.
Week 3: CV generation and PDF download.
Week 4: Dashboard, styling, and final testing.
Week 5: Deployment and feedback collection.
Estimated Completion Time
5 Weeks

8. Success Metrics
User Engagement: Number of users signing up and generating CVs.
Template Downloads: Track the number of CVs downloaded.
User Retention: Percentage of users returning to edit or create new CVs.
9. Risk Analysis
PDF Generation Compatibility: Some CSS might not render correctly in PDFs.
Mitigation: Use compatible CSS libraries and test thoroughly.
User Authentication Security: Potential for unauthorized access.
Mitigation: Use Django’s built-in security features and follow best practices for user data protection.