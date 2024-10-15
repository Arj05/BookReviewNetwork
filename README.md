# Goodreads Reviewers Scraper and Network Visualizer

This project scrapes reviewers from Goodreads who have commented on the same book and builds a network graph of their interactions. It provides a visual representation of how users who review the same book are connected, offering insights into the reviewer community for that specific book.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Visualization Example](#visualization-example)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

The tool scrapes reviewers' names from Goodreads review pages of a specific book, such as *Pride and Prejudice*. It then builds a network graph where reviewers are represented as nodes, and connections (edges) are drawn between them if they have commented on the same book. This visualization helps analyze patterns in the reviewer community and their shared interest in the book.

## Features

- **Web Scraping**: Scrapes reviewer information from multiple Goodreads review pages.
- **Graph Construction**: Automatically constructs a graph based on shared reviews for the same book.
- **Pagination**: Handles multiple pages of reviews to gather more comprehensive data.
- **Visualization**: Displays the network of reviewers with visual nodes and edges using graph visualization techniques.
- **Graph Export**: Saves the final graph as an image file for further use or analysis.

## Installation

To install the required dependencies and set up the project, follow these steps:

1. **Clone the Repository**: Download the project from the repository.
   ```bash
   git clone https://github.com/your_username/goodreads-reviewer-network.git

2. **Set Up the Project**: Set the book URL you want to scrape. For example, to scrape Pride and Prejudice, use the following line in a notebook cell: book_url = 'https://www.goodreads.com/book/show/1885.Pride_and_Prejudice'

## Usage
Once the dependencies are installed and the project is set up, follow these steps in Jupyter Notebook:

1. **Prepare the Goodreads Book UR**L: Open a notebook cell and set the book_url variable to the Goodreads URL of the book you want to scrape.
   book_url = 'https://www.goodreads.com/book/show/1885.Pride_and_Prejudice'

2. **Run the Scraper**: Execute the notebook cell that contains the scraping logic. The scraper will iterate through multiple pages of reviews (up to 5 pages by default), collect reviewers' names, and display progress for each page.

3. **Graph Building and Visualization**: After scraping, the graph will be built, showing the connections between reviewers. You can visualize the network in the notebook or save the graph as an image file.

4. **Visualize the Graph**: Use the following function to visualize or save the graph in your Jupyter Notebook:
visualize_graph(G, book_title, save_as='reviewers_graph.png')


## Technologies Used
-Python: Core programming language used for scraping and graph building.
-Selenium: For web scraping Goodreads pages.
-BeautifulSoup4: To parse HTML and extract relevant data (reviewers).
-NetworkX: For building and manipulating the graph of reviewers.
-Matplotlib: For visualizing the reviewer network graph.
