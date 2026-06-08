import os

import mysql.connector
from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "database": os.environ["DB_NAME"],
}

PAGE = """
<!doctype html>
<html lang="ru">
<head><meta charset="utf-8"><title>Lab Docker</title></head>
<body>
  <h1>Список задач</h1>
  {% if error %}<p style="color:red">{{ error }}</p>{% endif %}
  <form method="post">
    <input name="name" placeholder="Название задачи" required>
    <button type="submit">Добавить</button>
  </form>
  <ul>
  {% for task in tasks %}
    <li>{{ task }}</li>
  {% endfor %}
  </ul>
</body>
</html>
"""


def connection():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        db = connection()
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL)")

        if request.method == "POST":
            cursor.execute("INSERT INTO tasks(name) VALUES (%s)", (request.form["name"],))
            db.commit()
            cursor.close()
            db.close()
            return redirect("/")

        cursor.execute("SELECT name FROM tasks ORDER BY id DESC")
        tasks = [row[0] for row in cursor.fetchall()]
        cursor.close()
        db.close()
        return render_template_string(PAGE, tasks=tasks, error=None)
    except mysql.connector.Error as exc:
        return render_template_string(PAGE, tasks=[], error="База данных недоступна: " + str(exc))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
