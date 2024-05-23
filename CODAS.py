import pandas as pd
import numpy as np

def load_data(input_excel_path):
    """
    Excel dosyasından verileri yükler.
    """
    try:
        df = pd.read_excel(input_excel_path, sheet_name=0)
        return df
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return None
    except Exception as e:
        print("Beklenmeyen bir hata oluştu:", str(e))
        return None

def extract_data(df):
    """
    Excel veri çerçevesinden gerekli verileri çıkarır.
    """
    try:
        weights = df.iloc[0, 1:].values
        criteria_types = df.iloc[1, 1:].values
        data = df.iloc[2:, 1:].values
        alternatives = df.iloc[2:, 0].values
        return weights, criteria_types, data, alternatives
    except Exception as e:
        print("Veri çıkarılırken bir hata oluştu:", str(e))
        return None, None, None, None

def normalize_weighted_matrix(data, criteria_types, weights):
    """
    Veri matrisini normalize eder ve ağırlıkları uygular.
    """
    try:
        normalized_weighted_matrix = np.zeros_like(data, dtype=float)
        for i, criterion_type in enumerate(criteria_types):
            if criterion_type.upper() == 'MAX':
                normalized_weighted_matrix[:, i] = data[:, i] / data[:, i].max() * weights[i]
            elif criterion_type.upper() == 'MIN':
                normalized_weighted_matrix[:, i] = data[:, i].min() / data[:, i] * weights[i]
        return normalized_weighted_matrix
    except Exception as e:
        print("Normalizasyon işlemi sırasında bir hata oluştu:", str(e))
        return None

def calculate_distances(normalized_weighted_matrix):
    """
    Öklid ve Taksi mesafelerini hesaplar.
    """
    try:
        ideal_negative = normalized_weighted_matrix.min(axis=0)
        euclidean_distances = np.sqrt(((normalized_weighted_matrix - ideal_negative) ** 2).sum(axis=1))
        taxicab_distances = np.abs(normalized_weighted_matrix - ideal_negative).sum(axis=1)
        return euclidean_distances, taxicab_distances
    except Exception as e:
        print("Mesafe hesaplama sırasında bir hata oluştu:", str(e))
        return None, None

def create_distance_dataframes(alternatives, euclidean_distances, taxicab_distances):
    """
    Alternatifler için mesafe veri çerçeveleri oluşturur.
    """
    try:
        euclidean_distances_df = pd.DataFrame({'Alternative': alternatives, 'Euclidean Distance': euclidean_distances})
        taxicab_distances_df = pd.DataFrame({'Alternative': alternatives, 'Taxicab Distance': taxicab_distances})
        return euclidean_distances_df, taxicab_distances_df
    except Exception as e:
        print("Mesafe veri çerçevesi oluşturulurken bir hata oluştu:", str(e))
        return None, None

def calculate_relative_assessment_matrix(euclidean_distances, taxicab_distances):
    """
    Göreceli değerlendirme matrisini hesaplar.
    """
    try:
        phi = 0.02
        relative_assessment_matrix = np.zeros((len(euclidean_distances), len(euclidean_distances)))
        for i in range(len(euclidean_distances)):
            for j in range(len(euclidean_distances)-2):
                if i != j:
                    relative_assessment_matrix[i, j] = (euclidean_distances[i] - euclidean_distances[j]) + \
                        phi * (euclidean_distances[i] - euclidean_distances[j]) * (taxicab_distances[i] - taxicab_distances[j])
        return relative_assessment_matrix
    except Exception as e:
        print("Göreceli değerlendirme matrisi hesaplanırken bir hata oluştu:", str(e))
        return None

def rank_alternatives(relative_assessment_matrix):
    """
    Alternatifleri değerlendirme toplamlarına göre sıralar.
    """
    try:
        assessment_sums = relative_assessment_matrix.sum(axis=1)
        rankings = assessment_sums.argsort()[::-1] + 1  # Daha yüksek değerler tercih edilir
        return rankings
    except Exception as e:
        print("Alternatifler sıralanırken bir hata oluştu:", str(e))
        return None

def codas_method(input_excel_path):
    """
    CODAS yöntemini uygular.
    """
    try:
        df = load_data(input_excel_path)
        if df is None:
            return None, None, None, None, None, None, None
        weights, criteria_types, data, alternatives = extract_data(df)
        if any(var is None for var in [weights, criteria_types, data, alternatives]):
            return None, None, None, None, None, None, None
        normalized_weighted_matrix = normalize_weighted_matrix(data, criteria_types, weights)
        if normalized_weighted_matrix is None:
            return None, None, None, None, None, None, None
        euclidean_distances, taxicab_distances = calculate_distances(normalized_weighted_matrix)
        if any(var is None for var in [euclidean_distances, taxicab_distances]):
            return None, None, None, None, None, None, None
        euclidean_distances_df, taxicab_distances_df = create_distance_dataframes(alternatives, euclidean_distances, taxicab_distances)
        relative_assessment_matrix = calculate_relative_assessment_matrix(euclidean_distances, taxicab_distances)
        if relative_assessment_matrix is None:
            return None, None, None, None, None, None, None
        rankings = rank_alternatives(relative_assessment_matrix)
        if rankings is None:
            return None, None, None, None, None, None, None
        
        normalized_weighted_matrix_df = pd.DataFrame(normalized_weighted_matrix, columns=criteria_types)
        relative_assessment_matrix_df = pd.DataFrame(relative_assessment_matrix, columns=alternatives, index=alternatives)
        normalized_weighted_matrix_min_values = normalized_weighted_matrix.min(axis=0)

        return normalized_weighted_matrix_df, euclidean_distances_df, taxicab_distances_df, relative_assessment_matrix_df, rankings, relative_assessment_matrix.sum(axis=1), normalized_weighted_matrix_min_values
    except Exception as e:
        print("CODAS yöntemi uygulanırken bir hata oluştu:", str(e))
        return None, None, None, None, None, None, None

