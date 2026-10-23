# AI4I 2020 Dataset - Predictive Maintenance
# This is a synthetic dataset mimicking the AI4I 2020 industrial machine fault dataset
# Columns: Air temperature [K], Process temperature [K], Rotational speed [rpm], 
#          Torque [Nm], Tool wear [min], Machine failure (0=Normal, 1=Fault)

import numpy as np
import pandas as pd
from pathlib import Path

def generate_ai4i_2020_dataset(n_samples=10000, output_path='ai4i_2020_tdd/data/ai4i_2020.csv'):
    """
    Generate AI4I 2020 dataset for predictive maintenance analysis.
    
    Parameters:
    -----------
    n_samples : int
        Number of samples to generate (default: 10000)
    output_path : str
        Path to save the CSV file
    
    Returns:
    --------
    pd.DataFrame
        Generated dataset
    """
    np.random.seed(42)
    
    # Generate normal operating data first
    air_temp = np.random.normal(300, 5, n_samples)  # Air temperature in Kelvin
    process_temp = np.random.normal(350, 8, n_samples)  # Process temperature in Kelvin
    rotational_speed = np.random.normal(1500, 100, n_samples)  # RPM
    torque = np.random.normal(50, 10, n_samples)  # Newton-meters
    tool_wear = np.random.normal(50, 15, n_samples)  # Minutes
    
    # Create machine failure label based on certain conditions
    # Failure when: high temp + high torque + high tool wear
    failure_probability = (
        (air_temp > 310) & 
        (process_temp > 360) & 
        (torque > 60) & 
        (tool_wear > 80)
    ).astype(int)
    
    # Add some randomness to make it realistic
    failure_probability = (
        failure_probability + 
        np.random.binomial(1, 0.1, n_samples)  # 10% random failures
    ) % 2  # Ensure binary 0/1
    
    # Create DataFrame
    df = pd.DataFrame({
        'Air temperature [K]': np.round(air_temp, 2),
        'Process temperature [K]': np.round(process_temp, 2),
        'Rotational speed [rpm]': np.round(rotational_speed, 1),
        'Torque [Nm]': np.round(torque, 2),
        'Tool wear [min]': np.round(tool_wear, 1),
        'Machine failure': failure_probability
    })
    
    # Save to CSV
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    
    print(f"Generated {len(df)} samples AI4I 2020 dataset")
    print(f"Saved to: {output_file}")
    print(f"Machine failure rate: {failure_probability.mean()*100:.1f}%")
    
    return df

# Generate the dataset when module is run directly
if __name__ == '__main__':
    df = generate_ai4i_2020_dataset()