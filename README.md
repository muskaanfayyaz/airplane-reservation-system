```markdown
# ✈️ Airplane Reservation System

Welcome to the **Airplane Reservation System** built using **Streamlit**! This interactive web application allows users to book seats on a flight, view the seating plan, check the fare details, and reset the system.

---

## Features

- **Seat Booking**: Select your seat class (First Class, Business Class, Economy Class), choose the number of seats, and book them instantly.
- **Seating Plan**: View the current seating layout with available and booked seats.
- **Fare Details**: Check the fare for each class along with optional add-ons like extra legroom, in-flight meals, and priority boarding.
- **System Reset**: Reset all seats to available status and start fresh.

---

## 🛠️ Requirements

- Python 3.x
- Streamlit
- Additional dependencies (see `requirements.txt`)

---

## 📝 Installation

To get started with the **Airplane Reservation System**, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/airplane-reservation-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd airplane-reservation-system
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

Your application will be live at `http://localhost:8501/` in your web browser.

---

## 💡 Usage

Once the application is running, you will be presented with the following options:

### 1. **📅 Book Seats**
   - Choose the seat class: **First Class**, **Business Class**, or **Economy Class**.
   - Select the number of seats to book.
   - Optionally, choose add-ons such as **Extra Legroom**, **In-Flight Meal**, and **Priority Boarding**.
   - See a breakdown of the total fare before confirming your booking.

### 2. **🛋️ View Seating Plan**
   - View the current seating layout with available seats (🟩) and booked seats (🟥).
   - The seating plan shows a visual representation of the plane's seating arrangement with detailed information about the rows.

### 3. **💰 View Fare(s)**
   - View the base fare for each seat class and the optional add-ons.
   - Understand what comes with each class (luxury services, food options, seating arrangements, etc.).

### 4. **🔄 System Reset**
   - Reset all seats to available status, useful if you want to start the booking process over.

---

## 🚀 Project Structure

```
airplane-reservation-system/
│
├── main.py               # The main Streamlit app that drives the user interface
├── airplane.py           # Contains the Airplane class and booking logic
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation
```

---

## 📄 Airplane Class Explanation

The `Airplane` class (in **airplane.py**) contains all the logic for:

- **Seat booking** for different classes (First, Business, Economy).
- **Fare calculations** for each class and the optional add-ons.
- **Seating plan management**, including marking booked seats and resetting the system.

The system allows for a dynamic and real-time user experience where available and booked seats are updated instantly.

---

## 🤖 Developed By

**Muskaan Fayyaz**

---

## 🛠️ Dependencies

- **Streamlit**: The framework used to build the web application.
- **Python**: The programming language used for the backend logic.

---

## 🔄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

For questions, issues, or contributions, feel free to contact me via [email](mailto:your-email@example.com) or open an issue on GitHub.

---

**Happy flying with the Airplane Reservation System!** ✈️
```

---

### Breakdown of the README:

1. **Project Overview**: A brief description of what the application does.
2. **Features**: Highlights of the main features available in the app.
3. **Installation**: Step-by-step guide on how to install and run the app, including virtual environment setup.
4. **Usage**: Explains how to interact with the application once it's running, describing each section of the app (e.g., booking seats, viewing fare details).
5. **Project Structure**: A look at the project file organization.
6. **Airplane Class**: A short explanation of the `Airplane` class and its functionality.
7. **Dependencies**: Lists the main libraries and tools used to create the app.
8. **License**: License details (MIT license used in this example).
9. **Contact Information**: How to reach out for questions, issues, or contributions.

### Customizing the README:

Feel free to modify sections such as **Contact** and **License** with your own details. This README should now provide users with everything they need to get started with your Airplane Reservation System and contribute if they wish.
