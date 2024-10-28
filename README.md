# Top Selling Albums Analysis

This repository is intended for educational purposes. The script analyzes the best-selling albums of all time, providing insights into album release trends, the most frequent artists, and more. The analysis is performed using a dataset of top-selling albums available online, with a focus on showcasing various data manipulation skills using Python's Pandas library. The repository and its content are created for the author's educational purposes.

## Features

 - Column Renaming: Renames columns to Polish equivalents and capitalizes them appropriately.
 - Unique Artists Count: Calculates the number of unique artists present in the dataset.
 - Most Frequent Artists: Identifies the artists with the most album entries on the list.
 - Year Analysis: Determines the year with the most album releases and counts the number of albums released between 1960-1990.
 - Filtering and Sorting: Finds the youngest album and the earliest album from each artist.
 - CSV Export: Saves the final results into a CSV file for further analysis.

## Python Techniques Used

 - DataFrames: Used for storing and manipulating the album data.
 - Groupby Method: Applied to group the dataset by artist to find the earliest album for each artist.
 - Reading HTML Table: Extracts the table of best-selling albums directly from an HTML page.
 - Saving to CSV: Exports the final dataset to a CSV file.
 - Column Manipulation: Includes renaming, dropping columns, and changing column cases.
 - Filtering and Conditional Logic: Filters data based on specified conditions, such as year ranges.

## Installation

1. Clone this repository to your local machine:

    `git clone https://github.com/andy111223/08.2_TopSellingAlbums.git`

2. Navigate to the project directory:

    `cd 08.2_TopSellingAlbums`

3. Install the required dependencies (if not already installed):

    `pip install pandas lxml`

4. Run the script:

    `python3 main.py`

## Requirements

 - Python 3 (tested on Python 3.12)
 - Pandas library (version 2.2.3 or newer)
 - lxml library