import unittest
import pandas as pd
import numpy as np
from CODAS import load_data, extract_data, normalize_weighted_matrix, calculate_distances, create_distance_dataframes, calculate_relative_assessment_matrix, rank_alternatives

class TestCODASMethods(unittest.TestCase):

    def setUp(self):
        # Set up the test by loading the codas_input.xlsx file
        self.input_excel_path = 'codas_input.xlsx'

    def test_load_data(self):
        # Test if the function loads data from the codas_input.xlsx file
        df = load_data(self.input_excel_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(df.shape[0], 0)
        self.assertGreater(df.shape[1], 0)

    def test_extract_data(self):
        # Test if the function extracts data correctly from the DataFrame
        df = load_data(self.input_excel_path)
        weights, criteria_types, data, alternatives = extract_data(df)
        self.assertIsInstance(weights, np.ndarray)
        self.assertIsInstance(criteria_types, np.ndarray)
        self.assertIsInstance(data, np.ndarray)
        self.assertIsInstance(alternatives, np.ndarray)

        # Add specific assertions for the extracted data if needed

    def test_normalize_weighted_matrix(self):
        # Test if the function normalizes and applies weights correctly
        df = load_data(self.input_excel_path)
        weights, criteria_types, data, alternatives = extract_data(df)
        normalized_weighted_matrix = normalize_weighted_matrix(data, criteria_types, weights)
        self.assertIsInstance(normalized_weighted_matrix, np.ndarray)

        # Add specific assertions for the normalized weighted matrix if needed

    def test_calculate_distances(self):
        # Test if the function calculates distances correctly
        df = load_data(self.input_excel_path)
        weights, criteria_types, data, alternatives = extract_data(df)
        normalized_weighted_matrix = normalize_weighted_matrix(data, criteria_types, weights)
        euclidean_distances, taxicab_distances = calculate_distances(normalized_weighted_matrix)
        self.assertIsInstance(euclidean_distances, np.ndarray)
        self.assertIsInstance(taxicab_distances, np.ndarray)

        # Add specific assertions for the calculated distances if needed

    def test_create_distance_dataframes(self):
        # Test if the function creates distance DataFrames correctly
        df = load_data(self.input_excel_path)
        weights, criteria_types, data, alternatives = extract_data(df)
        normalized_weighted_matrix = normalize_weighted_matrix(data, criteria_types, weights)
        euclidean_distances, taxicab_distances = calculate_distances(normalized_weighted_matrix)
        euclidean_distances_df, taxicab_distances_df = create_distance_dataframes(alternatives, euclidean_distances, taxicab_distances)
        self.assertIsInstance(euclidean_distances_df, pd.DataFrame)
        self.assertIsInstance(taxicab_distances_df, pd.DataFrame)

        # Add specific assertions for the created distance DataFrames if needed

    def test_calculate_relative_assessment_matrix(self):
        # Test if the function calculates relative assessment matrix correctly
        df = load_data(self.input_excel_path)
        weights, criteria_types, data, alternatives = extract_data(df)
        normalized_weighted_matrix = normalize_weighted_matrix(data, criteria_types, weights)
        euclidean_distances, taxicab_distances = calculate_distances(normalized_weighted_matrix)
        relative_assessment_matrix = calculate_relative_assessment_matrix(euclidean_distances, taxicab_distances)
        self.assertIsInstance(relative_assessment_matrix, np.ndarray)

        # Add specific assertions for the calculated relative assessment matrix if needed

    def test_rank_alternatives(self):
        # Test if the function ranks alternatives correctly
        df = load_data(self.input_excel_path)
        weights, criteria_types, data, alternatives = extract_data(df)
        normalized_weighted_matrix = normalize_weighted_matrix(data, criteria_types, weights)
        euclidean_distances, taxicab_distances = calculate_distances(normalized_weighted_matrix)
        relative_assessment_matrix = calculate_relative_assessment_matrix(euclidean_distances, taxicab_distances)
        rankings = rank_alternatives(relative_assessment_matrix)
        self.assertIsInstance(rankings, np.ndarray)

        # Add specific assertions for the calculated rankings if needed

if __name__ == '__main__':
    unittest.main()
