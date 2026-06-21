# ⚽ Football API (Transfermarkt Dataset)

A live, high-performance REST API built with FastAPI and Python, connected to a cloud-hosted PostgreSQL database. This system serves data for over 5,000+ football players and 450+ clubs in real time.

🚀 **Live Link:** [Explore the Swagger UI API Documentation](https://football-api-production-7cce.up.railway.app/docs)

---

## 🏗️ Tech Stack
* **Backend Framework:** FastAPI (Python)
* **Database:** PostgreSQL
* **Database Driver:** psycopg2
* **Cloud Hosting & Deployment:** Railway

---

## ⚡ Features
* **Live Cloud Database:** Integrated with a production PostgreSQL database on Railway cloud.
* **Auto-Documented:** Interactive documentation automatically built via Swagger UI (`/docs`).
* **Pydantic Validation:** Strict data filtering and request schema checking.
* **Idempotency & Constraints:** Designed with data integrity protections to handle high concurrency seamlessly.

---

## 🛣️ API Endpoints Preview

HTTP Method | Endpoint | Description
GET | / | Health check
GET | /players | Returns top players by market value
GET | /clubs | Returns all clubs
GET | /clubs/{club_name}/players | Returns squad for a specific club
POST | /players/filter | Filter players by position and market value range
GET | /docs | Interactive Swagger API playground
---

## 💻 Local Installation & Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Ahmedkamel552/football-api.git
   cd football-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```
   DATABASE_URL=your_postgresql_connection_string
   ```

5. **Run the development server:**
   ```bash
   uvicorn main:app --reload
   ```

Visit `http://localhost:8000/docs` to explore the API documentation.

---

## 🚀 Deployment on Railway

1. Connect your GitHub repository to Railway
2. Add environment variables in Railway dashboard
3. Deploy automatically on every push

---

## 📊 Dataset

* **5,000+** Professional football players
* **450+** Football clubs
* Real-time data integration with Transfermarkt

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request.

---

**Built with ❤️ by [Ahmed Kamel](https://github.com/Ahmedkamel552)**
