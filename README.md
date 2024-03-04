# NutriGuide

## 👋 Introduction

NutriGuide is a web application designed to help users keep track of the nutritional information of various fruits. Whether you're a health-conscious individual, a nutritionist, or someone simply curious about the nutritional content of your favorite fruits, this app has you covered.

## 🛠️ Tech Stack

- `Python`
- `Django Framework`
- `Google Firebase`
- `Font Awesome icons`

## ✨ Features

- Add a new fruit to the database.
- Search for a particular fruit from the database (currently implemented in the homepage only).
- Render and display the results in a new HTML page.
- Delete the searched item from the database with the help of a single click.
- Edit the nutritional values of a fruit inside the database.


## 🚀 Process

It took me around 2 weeks time to complete NutriGuide completely. As the evaluation of this assignment was based on my knowledge in Django framework, I sticked to working with Django throughtout. But I had options for working with different SQLs. I had always worked with PostgreSQL when it came to Django Full-Stack projects, but I wanted to try something different in this project. Hence, I decided to get started with Firebase, a real-time database provided by Google. And I found it much more easier to implement.

## 📚 Learnings

In this project, I was able to learn about Firebase, a NoSQL database  system developed by Google. I also learnt how to connect the Django framework to a NoSQL database.

🔧 Improvements

- The search option is currently implemented only in the homepage.
- Right now, the website won't respond well in phones.
- The UI design needs more of a professional look.

## 🏃 Running the Project

1. First get started with cloning the repository into your local system.
2. Create a virtual environment.
3. Once the virtual environment is active, install the necessary commands using the command:
    ```bash
    pip install -r requirements.txt
    ```
4. Change the directory to the Django project
5. Run the command to get the Django server running:
    ```bash
    py manage.py runserver
    ```
6. Open a browser and direct to localhost:8000
7. Login using the following credentials:
    ```bash
    username : admin
    password : reon@123
    ```
