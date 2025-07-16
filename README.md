# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODTECH IT SOLUTIONS

NAME: BINEET BHADANI

INTERN ID: CT04DH2248

DOMAIN: PYTHON 

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

---

## **Task Title: API Integration and Data Visualization**

---

### **Task Description**

The project titled **“API Integration and Data Visualization”** focuses on building a simple yet functional Python application that fetches real-time weather data using an external API and visualizes it using a bar graph. The task combines two critical skills—**consuming external APIs** and **presenting data visually**—to build an interactive and educational tool that demonstrates real-world data processing.

The script begins by prompting the user to input the name of a city. Once entered, it sends an HTTP GET request to the **OpenWeatherMap API**—a globally used RESTful web service that provides weather data for any location on earth. Using a provided API key and specifying metric units, the script queries weather data for the selected city.

Once a successful response is received (status code 200), the JSON payload from the API is parsed to extract:

* **Temperature (°C)**
* **Humidity (%)**
* **Weather Description** (e.g., “clear sky”, “light rain”)

These values are first printed to the terminal for immediate reference. Then, the temperature and humidity are visualized using the `matplotlib` library. The graph plots two bars—one for temperature and another for humidity—each assigned a distinct color for clarity. A dynamic title is applied to the graph that includes the name of the city entered by the user. This provides users with a real-time visual snapshot of the city's weather conditions.

Error handling is also built-in: If the city name is invalid or the API request fails for any reason, the user receives a clear message indicating the failure, helping them correct the input.

---

### **Tools and Technologies Used**

* **Python**:
  Used for the full implementation due to its robust standard library and ecosystem for working with APIs and data visualization.

* **Requests Library**:
  A widely-used Python library to send HTTP requests. Here, it is used to fetch weather data from the OpenWeatherMap API using the GET method.

* **Matplotlib**:
  One of the most powerful and flexible plotting libraries in Python. It is used here to display temperature and humidity data in a visually appealing bar chart.

* **OpenWeatherMap API**:
  A freely accessible public API that provides current weather data, forecasts, and historical data. The API requires an API key for access.

---

### **Editor Platform Used**

The development and testing of this task were performed using **Visual Studio Code (VS Code)**, an open-source code editor that provides rich support for Python, including:

* Real-time error highlighting
* Integrated terminal
* Support for extensions like Python and Jupyter
* Easy integration of Git and source control

Other platforms that can be used to run this script include:

* **Jupyter Notebooks**
* **PyCharm**
* Online environments like **Google Colab** or **Replit**

---

### **Applicability and Use Cases**

This task and the resulting script are highly relevant to several real-world and academic scenarios:

#### **1. Educational Use**:

* An excellent starting point for students learning about API integration, HTTP requests, and JSON data handling.
* Teaches basic data visualization, which is a key part of any data science or analytics curriculum.

#### **2. Weather Monitoring Applications**:

* A lightweight tool for individuals or travelers to quickly check and visualize weather conditions in any city.
* Can serve as the foundation for mobile or desktop apps that offer live weather updates.

#### **3. Data Analytics and Dashboards**:

* This script demonstrates how real-time data can be fetched and presented in a dashboard-friendly format.
* Can be expanded into a larger project that includes multi-day forecasts, historical trends, and comparative graphs.

#### **4. IoT and Smart Devices**:

* Useful in building smart home systems or embedded applications where environmental data like temperature and humidity are crucial for automation.

#### **5. Hackathons and Rapid Prototyping**:

* The task serves as a minimal viable product (MVP) in hackathons where teams need to showcase API usage and real-time data analysis.
* The combination of live data and visuals provides an engaging demo for judges and stakeholders.

---

### **Conclusion**

This **API Integration and Data Visualization** project brings together the two vital aspects of modern programming—interacting with web-based data sources and making that data human-readable through effective visualization. By using tools like `requests` and `matplotlib` along with the OpenWeatherMap API, this project serves as a hands-on, beginner-friendly gateway into real-world Python programming. It provides learners with not just theoretical knowledge, but practical skills that can be scaled into full-fledged data products and applications.

---

### **OUTPUT**:

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/98cf5c31-aab2-45ac-a9aa-9a6a92818337" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/2a5065ac-9ff3-476f-9ca2-efab5e112827" />
