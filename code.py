import pandas as pd

# Read the CSV file
df = pd.read_csv('QTL overlapping.csv')

# Initialize a list to store overlapping pairs
overlaps = []

# Loop through each QTL to check for overlaps
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        # Check if QTLs overlap based on their coordinates
        if (df['chromosome'][i] == df['chromosome'][j] and
            df['start'][i] < df['end'][j] and
            df['start'][j] < df['end'][i]):
            overlaps.append({
                'QTL_1': df['qtl_name'][i],
                'QTL_2': df['qtl_name'][j],
                'Chromosome': df['chromosome'][i],
                'Start_1': df['start'][i],
                'End_1': df['end'][i],
                'Start_2': df['start'][j],
                'End_2': df['end'][j]
            })

# Create a DataFrame for the overlaps
overlap_df = pd.DataFrame(overlaps)

# Save the results to a new CSV file
overlap_df.to_csv('QTL_overlaps.csv', index=False)

print("Overlapping QTLs have been saved to 'QTL_overlaps.csv'.")
