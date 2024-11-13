import pandas as pd
import numpy as np
import os

def perform_statistical_analysis(df, output_dir='data'):
    # Logaritmikus transzformáció előtti statisztikai elemzés
    stats_data = {
        'Column': [],
        'Mean': [],
        'Median': [],
        'Standard Deviation': [],
        'Variance': [],
        'Min': [],
        'Max': []
    }
    
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            stats_data['Column'].append(column)
            stats_data['Mean'].append(np.mean(df[column]))
            stats_data['Median'].append(np.median(df[column]))
            stats_data['Standard Deviation'].append(np.std(df[column]))
            stats_data['Variance'].append(np.var(df[column]))
            stats_data['Min'].append(np.min(df[column]))
            stats_data['Max'].append(np.max(df[column]))

    # Eredmények DataFrame-be
    stats_df = pd.DataFrame(stats_data)
    
    # Eredmények mentése CSV fájlba
    output_path = os.path.join(output_dir, 'statistical_analysis_before_log.csv')
    stats_df.to_csv(output_path, index=False)
    print(f"Statisztikai elemzés mentve a következő fájlba: {output_path}")

    return stats_df
