# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODTECH IT SOLUTIONS

NAME: BINEET BHADANI

INTERN ID: CT04DH2248

DOMAIN: PYTHON 

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

---

### **Task Description: Weather Forecasting and Visualization Tool**

This project involves developing a **weather forecasting and visualization script** that fetches real-time weather data for a given city using an external API and presents the results through a simple bar graph using Python. The program serves both educational and practical purposes, demonstrating real-time API integration, data parsing, visualization, and user interaction via terminal input.

#### **Key Functionalities:**

1. **User Input**:
   The script prompts the user to input a city name. It automatically trims and capitalizes the input to ensure accuracy and consistency in API requests.

2. **API Integration**:
   The script connects to the **OpenWeatherMap API**, a popular free source for real-time global weather data. The API call uses:

   * City name
   * A valid API key
   * Metric units for standardized temperature reporting

3. **Data Retrieval and Parsing**:
   Upon a successful request (HTTP status code 200), the program extracts key weather parameters such as:

   * **Temperature (°C)**
   * **Humidity (%)**
   * **Weather Description** (e.g., "light rain", "clear sky")

4. **Data Display**:
   The results are printed in the terminal for quick reference. Then, using the **Matplotlib** library, the temperature and humidity are plotted as a vertical bar graph with appropriate labels and colors, offering a visual representation of current weather conditions.

5. **Error Handling**:
   If the API request fails (e.g., due to an invalid city name), a user-friendly error message is displayed.

---

### **Tools Used**

* **Python**:
  The entire script is written in Python due to its readability, strong community support, and vast collection of libraries for data manipulation and visualization.

* **Requests Library**:
  This library simplifies HTTP requests and is used to interact with the OpenWeatherMap API.

* **Matplotlib Library**:
  This powerful plotting library is used to create a bar chart for visualizing temperature and humidity.

* **OpenWeatherMap API**:
  An external RESTful weather API that provides real-time weather data based on city name input.

---

### **Editor Platform Used**

This script was developed and tested on **Visual Studio Code (VS Code)**, a widely-used open-source code editor. VS Code provides:

* Syntax highlighting
* Integrated terminal
* Git support
* Code linting and debugging
  These features make it ideal for quick development and testing of lightweight scripts like this one.

Alternatively, the code can also be run using:

* **Jupyter Notebooks** 
* **PyCharm**
* **Online IDEs** like Replit or Google Colab

---

### **Applicability and Use Cases**

This weather visualization tool has various practical and educational applications:

#### **1. Educational Use**:

* Introduces students to **API integration**, one of the most important concepts in modern software and data development.
* Demonstrates how to **fetch, parse, and visualize** external data.
* Great for beginner programmers learning how to interact with web services and libraries like Matplotlib.

#### **2. Real-World Utility**:

* Can be used by individuals needing quick weather updates directly via terminal.
* Forms the basis of more complex **weather dashboards** or **IoT applications**, such as integrating weather data into smart home devices.

#### **3. Expandability**:

* Can be extended to include forecasts, wind speed, or historical weather trends.
* Could be part of a larger **data analysis or machine learning project** focusing on climate trends or agriculture applications.

#### **4. Developer Practice**:

* Sharpens skills in handling **JSON data** from APIs.
* Reinforces **error handling** and **conditional logic**.
* Builds understanding of **basic data visualization principles**.

---

### **Conclusion**

This task showcases the integration of external data sources with real-time processing and visualization. It not only demonstrates foundational programming skills but also introduces students and developers to the power of API-driven applications. Through a few lines of Python code, users can transform raw weather data into a meaningful and interactive experience.

---

### **OUTPUT**:

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/98cf5c31-aab2-45ac-a9aa-9a6a92818337" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/2a5065ac-9ff3-476f-9ca2-efab5e112827" />
