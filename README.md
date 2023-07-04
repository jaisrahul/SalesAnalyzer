# SalesAnalyzer
==================================================================
# Introduction
The goal of this project is to provide minimalistic django project template that everyone can use, which just works out of the box and has the basic setup you can expand on.

# Features
Example app with business model.
Separated dev and production settings.
Separated requirements files.

# Prerequisites
Be sure you have the following installed on your development machine:

Python >= 3.7
Git
pip
Virtualenv (virtualenvwrapper is recommended)

# Installing
Step by step commands on how to run this project on your computer

1)- Install Virtualenv

pip install virtualenv
2)- Create Virtualenv

virtualenv env
3)- Activate virtual env

env/Scripts/activate
4)- Install requirements

pip install -r requirements.txt
Note: Above lines are required for first time installation

5)- Execute below commands

python manage.py makemigrations
python manage.py migrate
Note: Above commands should be executed if there is any db level changes
6)- Create superuser for admin access and follow instruction, if not created one
\admin 
username = admin
password = 112233

Running the tests
python manage.py runserver
And the project is ready for use on your computer!

# Requirements
Django==4.2.3
matplotlib==3.7.1
pandas==2.0.3
wsgiref==0.1.2


The task involves analyzing a sample sales dataset, performing data manipulation and analysis using Pandas, and building a Django web application to visualize and interact with the data.

## what i have done in this project:

### Dataset:
* i have make the button to download dataset "sales_data.csv" file. 

### About Data Analysis:
- i have done Calculate the total sales amount for each customer.
- i have done Calculate the total sales amount for each product.
- i have create a view display the data analysis. 


### Django Web Application:
i have create a Django project named "SalesAnalyzer" with an app named "sales."

in The Django project have a single view that displays the following:
- db displayed as a table.
- A bar chart showing the total sales amount for each customer.
- A pie chart showing the distribution of sales by product.
- i have use the Matplotlib library to generate the charts.
- i ensure that the web application is responsive and visually appealing.
---------------------------------------------------------------------

## Deliverables:
- Ipython Jupyter Notebook file:
i have make the file an IPython notebook named "data_analysis.ipynb" containing the data manipulation and analysis notebook code using Pandas.

- My Django project named "SalesAnalyzer" with the necessary files and functions created as per the analysis done in notebook and code to run the web application

- Dataset:
I have created CSV file named "sales_data.csv" containing the sample sales dataset.

- I have commited the complete project on github and i will provide a github link public repository be provided.