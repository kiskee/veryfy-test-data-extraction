# Document Information Extraction using Supervised Machine Learning

In this task, the goal is to accurately extract information from a set of documents in a JSON format using supervised machine learning. Here are some steps and assumptions to keep in mind while working on this task.

## Approach

The approach to solving this task involves the following steps:

- Optical Character Recognition (OCR): The documents will need to undergo an OCR process to extract the text.

- Data Cleaning: The extracted text will need to be cleaned and pre-processed before it can be used for training the machine learning model.

- Data Labeling: Each document will need to be labeled with the appropriate tags indicating the location of the required information in the document.

- Feature Extraction: Features need to be extracted from the documents to be used as inputs to the machine learning model.

- Model Training: A supervised machine learning model will need to be trained on the labeled data.

- Model Evaluation: The trained model will need to be evaluated on a test set of documents to ensure accuracy.

- Information Extraction: The trained model will be used to extract the required information from new documents.

## Assumptions

The following assumptions have been made while working on this task:

- The documents are of high quality and can be processed using OCR to extract the text.

- The information to be extracted is consistent across all documents and can be identified using consistent patterns.

- There are enough labeled documents to train a machine learning model effectively.

# Coding Best Practices

- Write modular code that is easy to read, understand, and maintain.

- Use descriptive variable and function names that accurately reflect their purpose.

- Use version control to track changes and collaborate with others.

- Follow coding standards and conventions.

- Write unit tests to ensure the correctness of the code and the machine learning model.

- Optimize the code for performance and efficiency.

- Document the code and provide clear explanations of the algorithm used.


# Usage

## Requeriments

- OS - Used for file handling and management.
- re - Used for regular expression pattern matching and extraction of specific information from the text.
- json - Used for formatting the extracted information into a JSON format.
- veryfi - Used for extracting information from the documents and generating structured data.

Note: Veryfi is a third-party library that needs to be installed separately. It provides a RESTful API for extracting data from documents such as invoices, receipts, and bills. If you choose to use Veryfi, you will need to obtain an API key and follow the documentation provided by the library.

## Programming paradigm

Imperative programming is used to describe the sequence of steps needed to extract the required information from the documents. This involves defining the flow of control, iterating through the documents, and applying regular expression patterns to extract specific information.

Object-oriented programming is used to organize the code into reusable and modular classes, objects, and methods. This helps in creating a maintainable and scalable codebase that is easy to understand and modify.

In addition to imperative and object-oriented programming, functional programming concepts such as pure functions and lambda expressions can also be used in certain parts of the code to improve readability and maintainability.


## Intallation

- Install Python: The first step is to install Python on your machine. You can download and install the latest version of Python from the official website at https://www.python.org/downloads/.

- Install the required libraries: Install the libraries needed for this task using the pip package manager. You can use the following command to install the required libraries:
    ```bash
      pip install os re json veryfi
    ```
- Clone the repository: Clone the repository containing the code for this task using Git. You can use the following command to clone the repository:
     ```bash
      git clone https://github.com/kiskee/veryfy-test-data-extraction.git
    ```
- Run the code: Run the code using a Python interpreter or an integrated development environment (IDE) such as PyCharm or VS Code.

- The script can be run from the command line with the following command:
    ```bash
      python read.py
    ```
    ###  <span style="color:red">Please change the information on the button of the class if you want to use it from the comand line</span>
    ###  <span style="color:red">Please review very well the routes that are delivered to the class to validate</span>
    
    

## Unit test with pytest

To carry out the unit tests, the installation of the pytest library was carried out
```bash
  pip install pytest
```
Execute this line to get the full test report
```bash
  pytest -v
```

```bash
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.2, pytest-7.3.1, pluggy-1.0.0 -- C:\Users\Daniel Medina\Desktop\veryfi_test\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Daniel Medina\Desktop\veryfi_test
collected 8 items                                                                                                                                  

Git/test/test_read.py::test_vendor_name PASSED                                                                                               [ 12%] 
Git/test/test_read.py::test_bill_to_name PASSED                                                                                              [ 25%] 
Git/test/test_read.py::test_bill_to_address PASSED                                                                                           [ 37%] 
Git/test/test_read.py::test_ship_to_name PASSED                                                                                              [ 50%]
Git/test/test_read.py::test_ship_to_address PASSED                                                                                           [ 62%] 
Git/test/test_read.py::test_get_quantity_and_price PASSED                                                                                    [ 75%] 
Git/test/test_read.py::test_get_description PASSED                                                                                           [ 87%] 
Git/test/test_read.py::test_create_json_return PASSED                                                                                        [100%] 

================================================================ 8 passed in 0.43s ================================================================ 
```
## Conclusion
This README file provides an overview of the approach, assumptions, and coding best practices to keep in mind while working on the task of accurately extracting information in a JSON format from a set of documents using supervised machine learning. By following these guidelines, we can ensure that our code is efficient, maintainable, and produces accurate results.

## Author

- [@kiskee(https://github.com/kiskee)