# Cost Savings Visualization 📊

This Python script visualizes the cost savings between two vehicle sellers based on pricing data provided in a CSV file. The visualization is presented as a horizontal bar chart, where bars are color-coded to indicate which seller offers better prices.

## Features

- **Data Handling**: The script processes data from a CSV file, handles missing values, and ensures that all numerical data is correctly formatted.
- **Custom Visualization**: Utilizes `matplotlib` and `seaborn` to create a clean and informative bar chart with a professional style.
- **Color-Coded Bars**: Green bars indicate Seller A is cheaper, and red bars indicate Seller B is cheaper.
- **Detailed Labels**: Each bar is labeled with the number of vehicles that correspond to the price difference.
- **PDF Export**: The generated plot is saved as a high-resolution PDF file.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ivezeh/cost-savings-visualization.git
   cd cost-savings-visualization
   ```
2. **Prepare the Data:

- Ensure you have a CSV file named `table.csv` in the root directory of the project.
- The CSV file should contain at least the following columns:
  - `number of vehicles`
  - `price seller A`
  - `price seller B`

3. **Run the Script:
  ```bash
 python analysis.py
  ```

4. **Output:
   - The script will generate a horizontal bar chart displaying the cost savings between the two sellers.
   - The plot will be saved as cost_benefit.pdf in the project directory.




This README provides a comprehensive overview of your project, including features, installation instructions, usage, and the code itself. You can replace placeholder text like "yourusername" and "your-email@example.com" with your actual GitHub username and contact information.

