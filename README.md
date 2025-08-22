# 🍴 FoodMunch – Interactive Food Ordering App

FoodMunch is a Python + Tkinter-based desktop application that makes food ordering fun and interactive.
Users can log in, set a budget, explore meals by categories, and even play mini-games to earn discounts before placing their order.


**✨ Features**

 🔑 Login & Signup System – Secure entry for users

 💰 Budget-Based Recommendations – Enter your budget and get food suggestions within limit

 🍽️ Food Categories – Choose from multiple categories like:

     Salads 🥗

     Biryani 🍛

     Juices 🥤

     Desserts 🍨

     And more…

 🎮 Mini-Games for Discounts – Win exciting discounts by playing built-in games

 🗂️ SQLite Database Support – Stores user details and order history (mydatabase.db)

 🎨 Tkinter UI – Simple, interactive, and beginner-friendly design
 

**🛠️ Tech Stack**

 Language: Python 🐍

 GUI Framework: Tkinter

 Database: SQLite

 Other: Random/Game logic, SQLAlchemy (if extended)
 


**📂 Project Structure**

FoodMunch/

│── Scripts/                  # Virtual environment scripts

│── __pycache__/              # Cached Python files

│── source/                   # Supporting source files

│── choose.py                 # Food category selection logic

│── hotellogin.py             # Hotel/Food login system

│── main.py                   # Entry point of the application

│── mydatabase.db             # SQLite database (user & orders)

│── new.py                    # Additional features/experimental

│── s.py                      # Supporting script

│── second1.py                # Secondary UI logic

│── secondpage.py             # Navigation page logic

│── signup.py                 # User signup system

│── sql_crud_demo.ipynb       # Notebook demo for SQL CRUD ops

│── t.py                      # Test script

│── try2.py                   # Experimental script

│── pyvenv.cfg                # Virtual environment config

│── README.md                 # Project documentation



**⚡ Getting Started**

  1️⃣ Clone the Repository
  
  git clone https://github.com/Kusuma431/food-munchapp.git
  cd foodmunch

  2️⃣ Install Dependencies

    Make sure you have Python 3.x installed.
    If you’re using a virtual environment:

    python -m venv venv
    source venv/bin/activate   # On Mac/Linux
    venv\Scripts\activate      # On Windows


   Install required packages (Tkinter is usually bundled with Python):

   pip install -r requirements.txt

  3️⃣ Run the Application
   python main.py


**⚙️ Usage Flow**

 🔑 Login / Signup

 💰 Enter your budget

 🍴 Browse food categories and select items

 📊 Track whether selections fit your budget

 🎮 Play mini-games for discounts

 🎉 Confirm your order!


**💡 Future Enhancements**

✅ Add invoice generator (PDF) for placed orders

✅ More categories and meal combos

✅ API integration for real restaurant menus

✅ Mobile app version using Kivy or Flutter
