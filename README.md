```markdown
# CODAS Method User Guide

The **CODAS (COmbinative Distance-based Assessment)** method is a technique used to solve multi-criteria decision-making problems. This method ranks alternatives by calculating distances between them and creating a relative assessment matrix.

## Requirements

To run this project, you will need the following requirements:
- Python (3.x)
- Flask
- Pandas
- NumPy
- A web browser

## Application Structure

```
flask_app/
├── uploads/
├── CODAS.py
├── app.py
└── templates/
    └── index.html
```

## Installation

To run the project, follow these steps:
1. Clone the repository or download the ZIP file of the project.
2. Navigate to the directory where you cloned or downloaded the file.
3. (Optional) Create and activate a virtual environment in the main directory.
4. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
5. Navigate to the main directory and start the Flask application:
   ```bash
   python app.py
   ```

## Usage

When the project is running, navigate to `localhost:5000` in a web browser to see the interface. You can use this interface to apply the CODAS method.

- On the homepage, use the 'Choose File' button to upload an Excel file.
- After uploading the file, click on the 'Upload' button.
- The results and processed data will be displayed at the bottom of the page.
input Excel:
![image](https://github.com/mertmetin1/Excel-CODAS-WEB-App/assets/98667673/97815bbe-312a-476d-a2b2-51df475fc13c)

GUI:
![image](https://github.com/mertmetin1/Excel-CODAS-WEB-App/assets/98667673/cbe3151c-ed6f-4e8a-8d66-48842380a3f5)

EXport Excel:
![image](https://github.com/mertmetin1/Excel-CODAS-WEB-App/assets/98667673/726e5da7-d0e7-4be7-839e-a2c235168d57)

## Notes

- During the file upload process, an 'uploads' folder is created, and the uploaded file is saved to this folder.
- The project requires the necessary libraries to be installed.

## Tests

The tests included in the project can be used to verify that the code is functioning correctly. To run the tests, navigate to the main directory of the project in the terminal and execute the following command:
```bash
python test.py
```

## Module Descriptions

### app.py

Contains the Flask application and creates the web interface.

- **index()**
  - Renders the homepage, which is the page users visit to upload files.
- **upload()**
  - Performs the file upload process. When the user uploads a file, this function is executed. It saves the uploaded file to the 'uploads' folder, then calls the `codas_method` function to process this file. Finally, it converts the uploaded Excel file to a DataFrame, converts it to an HTML table, and renders an HTML page with this table along with the results and any possible errors.
- **codas_method(file_path)**
  - Processes the uploaded Excel file and applies the CODAS method. It redirects to the `codas_method` function in the `CODAS.py` file. This function takes the data from the uploaded Excel file, applies the CODAS method, and returns the results. These results are returned as a normalized data matrix, Euclidean and Manhattan distances, a relative assessment matrix, and alternative rankings.

### CODAS.py

Contains functions implementing the CODAS method.

- **load_data(input_excel_path)**
  - **Purpose:** To load data from an Excel file.
  - **Parameters:** `input_excel_path` (str): Path of the Excel file to be loaded.
  - **Return Value:** `df` (pandas DataFrame): DataFrame containing the data from the Excel file.
  - **Function:** Reads the specified Excel file and returns the data inside it as a DataFrame. If the file is not found or an error occurs, it provides an appropriate error message and returns None.

- **extract_data(df)**
  - **Purpose:** To extract necessary data from the Excel DataFrame.
  - **Parameters:** `df` (pandas DataFrame): DataFrame containing the data obtained from the Excel file.
  - **Return Value:**
    - `weights` (numpy ndarray): An array containing weights.
    - `criteria_types` (numpy ndarray): An array containing criterion types.
    - `data` (numpy ndarray): An array containing the data matrix.
    - `alternatives` (numpy ndarray): An array containing alternatives.
  - **Function:** Extracts weights, criterion types, data matrix, and alternatives from the given DataFrame. Assigns the extracted data to respective variables and returns them. In case of any error, it provides an appropriate error message and returns the variables as None.

- **normalize_weighted_matrix(data, criteria_types, weights)**
  - **Purpose:** To normalize the data matrix and apply weights.
  - **Parameters:**
    - `data` (numpy ndarray): An array containing the data matrix.
    - `criteria_types` (numpy ndarray): An array containing criterion types.
    - `weights` (numpy ndarray): An array containing weights.
  - **Return Value:** `normalized_weighted_matrix` (numpy ndarray): Normalized and weighted data matrix.
  - **Function:** Normalizes the data matrix and applies weights according to criterion types. Uses different normalization methods for each criterion type (e.g., maximum or minimum). Returns the normalized data matrix. In case of any error, it provides an appropriate error message and returns None.

- **calculate_distances(normalized_weighted_matrix)**
  - **Purpose:** To calculate Euclidean and Manhattan distances.
  - **Parameters:** `normalized_weighted_matrix` (numpy ndarray): Normalized and weighted data matrix.
  - **Return Value:**
    - `euclidean_distances` (numpy ndarray): An array containing Euclidean distances.
    - `manhattan_distances` (numpy ndarray): An array containing Manhattan distances.
  - **Function:** Calculates ideal negative values from the normalized data matrix. Calculates Euclidean and Manhattan distances. Returns the distance of each alternative from the ideal negative values. In case of any error, it provides an appropriate error message and returns the variables as None.

- **create_distance_dataframes(alternatives, euclidean_distances, manhattan_distances)**
  - **Purpose:** To create distance dataframes for alternatives.
  - **Parameters:**
    - `alternatives` (numpy ndarray): An array containing alternatives.
    - `euclidean_distances` (numpy ndarray): An array containing Euclidean distances.
    - `manhattan_distances` (numpy ndarray): An array containing Manhattan distances.
  - **Return Value:**
    - `euclidean_distances_df` (pandas DataFrame): DataFrame containing Euclidean distances.
    - `manhattan_distances_df` (pandas DataFrame): DataFrame containing Manhattan distances.
  - **Function:** Creates DataFrames from the given distance arrays. Returns a DataFrame for each alternative containing Euclidean and Manhattan distances. In case of any error, it provides an appropriate error message and returns the DataFrames as None.

- **calculate_relative_assessment_matrix(euclidean_distances, manhattan_distances)**
  - **Purpose:** To calculate the relative assessment matrix.
  - **Parameters:**
    - `euclidean_distances` (numpy ndarray): An array containing Euclidean distances.
    - `manhattan_distances` (numpy ndarray): An array containing Manhattan distances.
  - **Return Value:** `relative_assessment_matrix` (numpy ndarray): An array containing the relative assessment matrix.
  - **Function:** Calculates the relative assessment matrix using Euclidean and Manhattan distances. Returns the relative assessment matrix for each alternative compared to other alternatives. In case of any error, it provides an appropriate error message and returns None.

- **rank_alternatives(relative_assessment_matrix)**
  - **Purpose:** To rank alternatives based on assessment sums.
  - **Parameters:** `relative_assessment_matrix` (numpy ndarray): An array containing the relative assessment matrix.
  - **Return Value:** `rankings` (numpy ndarray): An array containing the rankings of alternatives.
  - **Function:** Ranks alternatives based on assessment sums. Returns an array containing the rankings of each alternative. In case of any error, it provides an appropriate error message and returns None.

- **codas_method(input_excel_path)**
  - **Purpose:** To apply the CODAS method.
  - **Parameters:** `input_excel_path` (str): Path of the Excel file.
  - **Return Value:**
    - `normalized_weighted_matrix_df` (pandas DataFrame): DataFrame containing the normalized and weighted data matrix.
    - `euclidean_distances_df` (pandas DataFrame): DataFrame containing Euclidean distances.
    - `manhattan_distances_df` (pandas DataFrame): DataFrame containing Manhattan distances.
    - `relative_assessment_matrix_df` (pandas DataFrame): DataFrame containing the relative assessment matrix.
    - `rankings` (numpy ndarray): An array containing the rankings of alternatives.
  - **Function:** Loads the provided Excel file and extracts the necessary data. Normalizes the data matrix and applies weights. Calculates Euclidean and Manhattan distances, and creates DataFrames for them. Calculates the relative assessment matrix. Ranks alternatives based on assessment sums. Returns the results of all these operations along with relevant variables. Provides an appropriate error message and returns the variables as None in case of any error.

## Unit Tests

### test.py

Contains unit tests for verifying the functionality of the CODAS method implementation.

- **test_load_data()**
  - **Purpose:** Verifies the `load_data()` function. This function loads data from an Excel file. The test checks whether the function correctly loads data from the specified Excel file.

- **test_extract_data()**
  - **Purpose:** Verifies the `extract_data()` function. This function extracts necessary data from the Excel DataFrame. The test checks whether the function correctly extracts weights, criterion types, data matrix, and alternatives.

- **test_normalize_weighted_matrix()**
  - **Purpose:** Verifies the `normalize_weighted_matrix

()` function. This function normalizes the data matrix and applies weights. The test checks whether the function correctly normalizes the data matrix and applies weights according to criterion types.

- **test_calculate_distances()**
  - **Purpose:** Verifies the `calculate_distances()` function. This function calculates Euclidean and Manhattan distances. The test checks whether the function correctly calculates distances from the ideal negative values.

- **test_create_distance_dataframes()**
  - **Purpose:** Verifies the `create_distance_dataframes()` function. This function creates distance dataframes for alternatives. The test checks whether the function correctly creates distance dataframes.

- **test_calculate_relative_assessment_matrix()**
  - **Purpose:** Verifies the `calculate_relative_assessment_matrix()` function. This function calculates the relative assessment matrix. The test checks whether the function correctly calculates the relative assessment matrix.

- **test_rank_alternatives()**
  - **Purpose:** Verifies the `rank_alternatives()` function. This function ranks alternatives based on assessment sums. The test checks whether the function correctly ranks alternatives.

These unit tests ensure the reliability and accuracy of the CODAS method implementation by validating each function's behavior against expected outcomes. Running these tests helps maintain code quality and assures that any changes made to the codebase do not introduce unintended errors.

