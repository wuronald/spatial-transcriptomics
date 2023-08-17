import matplotlib.pyplot as plt

# Data from Museum of spatial transcriptomics
museum_data = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 13, 20, 32, 48, 75, 97]

# Data from STOmicsDB
stomics_data = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 14, 21, 34, 51, 79, 101]

# Years from 2003 to 2023
years = list(range(2003, 2023))

# Plot the data
plt.plot(years, museum_data, label="Museum of spatial transcriptomics")
plt.plot(years, stomics_data, label="STOmicsDB")
plt.xlabel("Year")
plt.ylabel("Number of publications")
plt.title("Number of scientific publications mentioning \"spatial transcriptomics\" for the last 20 years")
plt.legend()
plt.show()

