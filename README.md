# tanX Project

## Overview

This project processes and analyzes customer order data from an `orders.csv` file. It performs the following tasks:
- Computes total revenue generated by the online store for each month.
- Computes total revenue generated by each product.
- Computes total revenue generated by each customer.
- Identifies the top 10 customers by revenue.

The project is implemented in Python and uses the pandas library for data manipulation. It includes unit tests to ensure functionality and is Dockerized for easy deployment and testing.

## Project Structure

Here's the project structure in a bash format, based on the provided image:

```sh
tanx_project/
├── .venv/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── customer_revenue.csv
├── docker-compose.yml
├── Dockerfile
├── monthly_revenue.csv
├── orders.csv
├── product_revenue.csv
├── README.md
├── requirements.txt
└── top_10_customers.csv
```


## Setup and Installation

### Prerequisites

- Docker Desktop installed on your machine. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).
- Docker Compose (included with Docker Desktop).

### Steps

1. **Clone the Repository**

   ```sh
   git clone https://github.com/devgupta2619/tanx_project.git
   cd tanx_project
   ```

2. **Create the orders.csv File**

   Ensure you have a sample `orders.csv` file in the root directory of the project. You can use the following sample data:

   ```csv
   order_id,customer_id,order_date,product_id,product_name,product_price,quantity
   1,1,2023-01-01,1,Product A,100,1
   2,2,2023-01-10,2,Product B,200,1
   3,1,2023-02-01,1,Product A,150,1
   ```

3. **Build the Docker Image**

   ```sh
   docker-compose build
   ```

4. **Run the Application**

   ```sh
   docker-compose up app
   ```

   This will execute the main application and display the computed revenues.

5. **Run Tests**

   To run the unit tests, use the following command:

   ```sh
   docker-compose up test
   ```

## File Descriptions

- **app/main.py**: Contains the main application logic for reading data, computing revenues, and printing results.
- **tests/test_main.py**: Contains unit tests for verifying the correctness of the application logic.
- **Dockerfile**: Specifies the environment for running the application. It installs dependencies and sets up the container.
- **docker-compose.yml**: Defines services for running the application and tests. It also sets up volumes and dependencies.
- **requirements.txt**: Lists Python libraries required for the project.

## Running the Project Locally

If you prefer to run the project locally without Docker, you can set up a virtual environment and install dependencies manually:

1. **Create and Activate a Virtual Environment**

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

2. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```sh
   python app/main.py
   ```

4. **Run Tests**

   ```sh
   python -m unittest discover -s tests
   ```

## Troubleshooting

- **Docker Not Running**: Ensure Docker Desktop is running and properly configured. Restart Docker Desktop if necessary.
- **Version Compatibility**: Ensure Docker and Docker Compose are up-to-date and compatible with the project configuration.
- **File Not Found**: Verify that `orders.csv` is present in the root directory of the project.

## Output

The Output for the main function are stored in seprate CSV files(customer_revenue.csv,monthly_revenue.csv,product_revenue.csv,top_10_customers.csv) and a demo video of project has been uploaded along side project for reference.
