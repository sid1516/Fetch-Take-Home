# Fetch-Take-Home

## Getting Started

1. Clone the repository onto your local machine.
2. Ensure that you have installed pandas. This can be done with the command 
```console
pip install pandas
```
3. Run main.py with the csv file that you would like to use. Provide a command line argument for the amount that you would like to spend.
   ```console
   python3 main.py <amount>
   ```
4. To change the csv file you are reading, from provide the relative path to the csv file you want on line 26 of main.py. All csv files are located in the data folder. The format can be seen below, as well as information about the csv files.
   ```
   pd.read_csv("./data/same_time_transactions.csv")
   ``` 
   * transactions.csv: example data
   * empty.csv: data with no transactions within the file
   * large_transactions.csv: data that tests large transaction amounts and what happens when the spending amount is less than the transaction amount
   * same_time_transactions.csv: tests multiple transactions ocurring at once
4. Documentation can be found within the python file as well.
