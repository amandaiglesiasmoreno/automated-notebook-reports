import os
from update_data import update_product_csv_with_new_week_data
from execute_notebook import execute_notebook
from convert_notebook_to_html import convert_notebook_to_html
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def main():
    # Step 1: Update the CSV file with new weekly data
    csv_file = 'supermarket_purchases_data.csv'  
    start_date = '2024-02-01' 
    end_date = '2024-02-07'   
    # Define the agent, model, and headers (update these with your actual values)
    agent = 'This is an agent for generating synthetic data.'
    # Set the headers for the API request, including the token for authentication
    token = api_key 
    headers = {
        'Authorization': f'Bearer {token}'
    }
    # Define the model that will be used for generating the synthetic data
    model = "mistral-large-2407"  

    df_combined = update_product_csv_with_new_week_data(csv_file, start_date, end_date, agent, model, headers)

    # Step 2: Execute the Jupyter Notebook
    notebook_name = 'analysis_purchases.ipynb'  # Notebook name
    execute_notebook(notebook_name)

    # Step 3: Convert the Jupyter Notebook to HTML
    notebook_folder = '../notebooks'  # Path to the folder containing the notebook
    convert_notebook_to_html(notebook_folder, notebook_name)

    print("All tasks completed successfully!")

# Ensure the script runs only if executed directly
if __name__ == '__main__':
    main()
