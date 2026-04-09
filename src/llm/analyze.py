import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ollama import chat  # <- use chat function, not Ollama class

def generate_analysis(predictions: pd.DataFrame):
    """
    predictions: DataFrame with columns:
      - job_title
      - predicted_salary
      - other features if needed
    """

    # Step 1: Simple chart
    plt.figure(figsize=(8, 5))
    sns.barplot(data=predictions, x='job_title', y='predicted_salary')
    plt.xticks(rotation=45)
    plt.title('Predicted Salary by Job Title')
    plt.tight_layout()
    chart_path = "salary_chart.png"
    plt.savefig(chart_path)
    plt.close()

    # Step 2: Convert DataFrame to text for LLM
    text_input = predictions.to_string(index=False)

    # Step 3: Create prompt
    prompt = f"""
You are a data analyst. Here is the predicted salary dataset:

{text_input}

Please generate a written analysis of the salary landscape. 
Highlight which job titles have higher salaries, trends with remote ratio or company size, 
and any other interesting insights. Refer to the chart saved as '{chart_path}'.
"""

    # Step 4: Call LLM (Ollama)
    response = chat(model="llama3", messages=[{"role": "user", "content": prompt}])

    # Step 5: Return analysis and chart path
    return {
        "narrative": response['content'],
        "chart_path": chart_path
    }