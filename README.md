# 📰 KhabarKart – AI-Powered Real-Time News Platform

KhabarKart is a Flask-based news aggregation platform designed to make discovering and accessing news easier. It integrates external news APIs with AI-powered information retrieval and provides users with a searchable news feed, account management, and subscription-based access options.

## 🚀 Features

### 🗞️ Real-Time News Aggregation
- Fetches news articles using external News APIs.
- Displays article headlines and descriptions through dynamically generated news cards.
- Provides links to access original news articles.
- Includes a searchable news feed for easier content discovery.

### 🤖 AI-Powered Information Retrieval
- Integrates AI capabilities to assist users in discovering relevant news information.
- Combines external news data with AI-powered information processing.

### 👤 User Authentication
- User registration and login functionality.
- SQLite database for persistent user account management.
- Stores user registration and login-related information.

### 💳 Subscription Management
KhabarKart includes three subscription tiers with differentiated pricing and features.

| Plan | Price | Features |
|---|---:|---|
| Kart | ₹99/month | Daily news, basic personalization, limited Explore section |
| Kart Pro | ₹199/month | Priority content updates, full Explore section, ad-free experience |
| Kart Pro Max | ₹299/month | Early news access, customizable news feed, VIP support |

*Note: The payment interface is simulated and is not connected to a live payment gateway.*

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web application framework |
| SQLite | User account database |
| REST APIs | External news retrieval |
| HTML & CSS | Frontend development |
| JavaScript | Frontend interactions |
| AI integration | Information retrieval and processing |

## 📂 Project Structure

```text
KhabarKart/
│
├── main.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── database/
│   └── SQLite database
│
└── README.md
```

*The structure above is illustrative; adjust it to match the actual project files.*

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd KhabarKart
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask requests
```

Install any additional packages required by your implementation.

### 4. Configure API credentials

Configure your News API key and any AI service credentials using environment variables, according to the integrations used in the project.

Do not commit API keys or passwords to GitHub.

### 5. Run the application

```bash
python main.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:3000/
```

## 🔄 Application Workflow

1. Users register or log in to their accounts.
2. The application retrieves news articles through external APIs.
3. AI capabilities assist with information retrieval and processing.
4. Articles are presented through a searchable news feed.
5. Users can explore the available subscription plans.
6. A simulated payment interface demonstrates the subscription workflow.

## 🔮 Future Improvements

- Integration with a secure, live payment gateway.
- Personalized news recommendations based on user interests.
- Improved AI-powered news summarization.
- News bookmarking and reading history.
- Enhanced user preferences and subscription management.
- Deployment to a cloud hosting platform.

## 👨‍💻 Project

**KhabarKart – AI-Powered News Aggregation & Subscription Platform**

Built using Python, Flask, SQLite, REST APIs and frontend web technologies.

