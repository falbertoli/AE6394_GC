# AE6394_GC

# Hydrogen Infrastructure Dashboard

This project is a **Dash-based web application** designed to visualize and plan hydrogen infrastructure. The dashboard provides insights into compliance, land use, and operational impacts, making it a valuable tool for stakeholders involved in hydrogen infrastructure planning.

---

## **Features**

- **Interactive Dashboard:**

  - Displays key metrics such as land use, compliance, and estimated costs.
  - Includes graphs for fleet composition and land use.
  - Placeholder for an interactive map to show zones, safety buffers, and tank locations.

- **Key Sections:**
  1. **Alerts Section:** Displays critical warnings or success messages.
  2. **Map Section:** Placeholder for an interactive map (to be integrated with Leaflet.js or Plotly maps).
  3. **Key Metrics Section:** Highlights important metrics like land use, compliance, and costs.
  4. **Graphs Section:** Visualizes fleet composition and land use with side-by-side graphs.

---

## **Technologies Used**

- **Python 3.11.11**
- **Dash 2.18.2**
- **Plotly 6.0.0**
- **Dash Bootstrap Components 1.7.1**
- **Font Awesome** (for icons)

---

## **Setup Instructions**

### **1. Clone the Repository**

Clone the repository to your local machine and navigate to the project directory:

```bash
git clone https://github.com/falbertoli/AE6394_GC.git
cd AE6394_GC
```

---

### **2. Set Up a Virtual Environment**

Create and activate a virtual environment to isolate your dependencies:

- **On macOS/Linux:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

---

### **3. Install Dependencies**

Install the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### **4. Run the App**

Run the app locally:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:8050/` in your browser.

---

## **Deployment**

The app is deployed on **Render** and can be accessed via the following link:
[Hydrogen Infrastructure Dashboard](https://ae6394-gc.onrender.com)

---

## **File Structure**

```
AE6394_GC/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── Procfile             # Deployment configuration for Render
├── runtime.txt          # Python version specification
├── README.md            # Project documentation
└── .gitignore           # Files and directories to ignore in Git
```

---

## **Future Improvements**

- Integrate an interactive map using **Leaflet.js** or **Plotly maps**.
- Add more detailed metrics and visualizations.
- Enhance the UI with additional styling and interactivity.
- Add user authentication for secure access.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**

For any questions or feedback, please contact:

- **Name:** [Your Name]
- **Email:** falbertoli3@gatech.edu
- **GitHub:** [falbertoli](https://github.com/falbertoli)
