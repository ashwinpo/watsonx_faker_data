# Synthetic Data Generator

The Synthetic Data Generator is a powerful and user-friendly tool that generates tailored synthetic datasets from natural language descriptions. Built using Streamlit, Faker, and the WatsonX AI Language Model, this application simplifies the process of creating custom datasets for testing, demos, and exploratory projects.

## Features

- Generate synthetic datasets based on natural language descriptions
- Utilize the Faker library for realistic and diverse data generation
- Leverage the WatsonX AI Language Model for advanced language understanding
- Seamlessly integrate the generated code into your development workflow
- Create unique datasets on-demand, eliminating the need for manual data curation

## Installation

1. Clone the repository: `git clone https://github.com/your-username/synthetic-data-generator.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the necessary environment variables:
- Create a `.env` file in the project root directory
- Add the following variables to the `.env` file:
  ```
  IAM_KEY=your-watsonx-ai-iam-key
  PROJECT_ID=your-watsonx-ai-project-id
  ```
- Replace `your-watsonx-ai-iam-key` and `your-watsonx-ai-project-id` with your actual WatsonX AI credentials

4. Run the Streamlit application: `streamlit run app.py`

## Usage

1. Open the Synthetic Data Generator application in your web browser
2. Enter a natural language description of the dataset you want to generate
3. Click the "Generate Dataset" button
4. The application will generate the Python code using the WatsonX AI Language Model and display it in the code block
5. The generated code will be executed, and the resulting synthetic dataset will be displayed as a pandas DataFrame

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Faker](https://faker.readthedocs.io/) - Python library for generating realistic fake data
- [WatsonX AI](https://www.ibm.com/cloud/watsonx-ai) - Advanced language understanding capabilities
- [Streamlit](https://streamlit.io/) - Python library for building interactive web applications
