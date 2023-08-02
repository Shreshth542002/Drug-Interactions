# Drug-Interactions

This project uses data to predict if two drugs(medicines) will have a side effect if taken simultaneously.

## How to run in dev enviornment

1. Create a new folder

2. Clone the repository in that folder.

3. Create a new virtual enviornment.

   For Windows:
     
       python -m venv virtualenv_name
   
   For Linux:
   
        pip install virtualenv
        virtualenv virtualenv_name
4. Start the virtual enviornment

   For Windows:

        venv\Scripts\Activate.ps1
        
   For Linux:

        source venv/bin/activate
   
5. Install the packages and modules for the project

       pip install -r requirements.txt

6. Create the enviornment variables file and store the path to your dataset file.

   In .env file:

       CSV_FILE_PATH='path/to/your/csv_file.csv'


7. Run the python file

        python Dataset_representation.py
   
