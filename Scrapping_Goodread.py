#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[2]:


pip install requests beautifulsoup4 networkx matplotlib


# In[4]:


import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt

# Function to extract unique reviewers and book title from the HTML content
def extract_reviewers_and_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    reviewers = set()

    # Locate the book title
    title_tag = soup.select_one('h1#bookTitle')
    book_title = title_tag.text.strip() if title_tag else "Pride and Prejudice"  # Default to the known book title

    # Locate the reviews section and iterate through the reviews
    for review in soup.select('article'):
        user_tag = review.select_one('section.ReviewerProfile__info a')
        if user_tag:
            user_name = user_tag.text.strip()
            reviewers.add(user_name)
    
    return reviewers, book_title

# Function to scrape Goodreads with pagination
def scrape_goodreads_reviews(base_url, max_pages=5):
    all_reviewers = []  # List to collect all sets of reviewers from each page
    current_page = 1
    book_title = None
    while current_page <= max_pages:
        url = f"{base_url}?page={current_page}"
        response = requests.get(url)
        
        if response.status_code == 200:
            html_content = response.content
            reviewers_on_page, book_title = extract_reviewers_and_title(html_content)
            all_reviewers.append(reviewers_on_page)  # Store reviewers from this page
            
            # Print progress
            print(f"Scraped page {current_page}, found {len(reviewers_on_page)} reviewers")
            current_page += 1
        else:
            print(f"Failed to fetch page {current_page}. Status code: {response.status_code}")
            break  # Stop if there's an error fetching the page
    
    return all_reviewers, book_title

# Function to build a graph from the collected reviewers
def build_graph(reviewer_lists, book_title):
    G = nx.Graph()
    
    # Add two parent nodes for the book title
    G.add_node(f"Book: {book_title}")
    G.add_node(f"Title: {book_title}")

    # Create edges between all reviewers in the same list
    for reviewers in reviewer_lists:
        reviewer_list = list(reviewers)  # Convert the set to a list
        for i in range(len(reviewer_list)):
            for j in range(i + 1, len(reviewer_list)):
                G.add_edge(reviewer_list[i], reviewer_list[j])  # Create a connection between two reviewers

        # Connect each reviewer to both book nodes
        for reviewer in reviewer_list:
            G.add_edge(reviewer, f"Book: {book_title}")
            G.add_edge(reviewer, f"Title: {book_title}")

    return G

# Function to visualize the graph with the book title as the central node
def visualize_graph(G, book_title):
    plt.figure(figsize=(12, 12))
    
    # Define positions for the nodes
    pos = nx.spring_layout(G)  # Use spring layout for the graph

    nx.draw_networkx_nodes(G, pos, node_size=100, node_color='blue', alpha=0.6)
    nx.draw_networkx_edges(G, pos, alpha=0.2)
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
    
    plt.title(f"Connections between reviewers and the book '{book_title}'")
    plt.axis('off')
    plt.show()

# Main code execution
if __name__ == "__main__":
    # URL of the Goodreads book reviews page
    book_url = 'https://www.goodreads.com/book/show/1885.Pride_and_Prejudice'
    
    # Scrape reviews (scraping up to 5 pages as an example)
    reviewer_lists, book_title = scrape_goodreads_reviews(book_url, max_pages=5)
    
    # Build the graph from the collected reviewer data
    G = build_graph(reviewer_lists, book_title)
    
    # Visualize the connections with the book title as the central nodes
    visualize_graph(G, book_title)


# In[6]:


import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt

# Function to extract unique reviewers and book title from the HTML content
def extract_reviewers_and_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    reviewers = set()

    # Locate the book title
    title_tag = soup.select_one('h1#bookTitle')
    book_title = title_tag.text.strip() if title_tag else "Pride and Prejudice"  # Default to the known book title

    # Locate the reviews section and iterate through the reviews
    for review in soup.select('article'):
        user_tag = review.select_one('section.ReviewerProfile__info a')
        if user_tag:
            user_name = user_tag.text.strip()
            reviewers.add(user_name)
    
    return reviewers, book_title

# Function to scrape Goodreads with pagination
def scrape_goodreads_reviews(base_url, max_pages=5):
    all_reviewers = []  # List to collect all sets of reviewers from each page
    current_page = 1
    book_title = None
    while current_page <= max_pages:
        url = f"{base_url}?page={current_page}"
        response = requests.get(url)
        
        if response.status_code == 200:
            html_content = response.content
            reviewers_on_page, book_title = extract_reviewers_and_title(html_content)
            all_reviewers.append(reviewers_on_page)  # Store reviewers from this page
            
            # Print progress
            print(f"Scraped page {current_page}, found {len(reviewers_on_page)} reviewers")
            current_page += 1
        else:
            print(f"Failed to fetch page {current_page}. Status code: {response.status_code}")
            break  # Stop if there's an error fetching the page
    
    return all_reviewers, book_title

# Function to build a graph from the collected reviewers
def build_graph(reviewer_lists, book_title):
    G = nx.Graph()
    
    # Add two parent nodes for the book title
    G.add_node(f"Book: {book_title}")
    G.add_node(f"Title: {book_title}")

    # Create edges between all reviewers in the same list
    for reviewers in reviewer_lists:
        reviewer_list = list(reviewers)  # Convert the set to a list
        for i in range(len(reviewer_list)):
            for j in range(i + 1, len(reviewer_list)):
                G.add_edge(reviewer_list[i], reviewer_list[j])  # Create a connection between two reviewers

        # Connect each reviewer to both book nodes
        for reviewer in reviewer_list:
            G.add_edge(reviewer, f"Book: {book_title}")
            G.add_edge(reviewer, f"Title: {book_title}")

    return G

# Function to visualize the graph with the book title as the central node
def visualize_graph(G, book_title, save_as=None):
    plt.figure(figsize=(12, 12))
    
    # Define positions for the nodes
    pos = nx.spring_layout(G)  # Use spring layout for the graph

    nx.draw_networkx_nodes(G, pos, node_size=100, node_color='blue', alpha=0.6)
    nx.draw_networkx_edges(G, pos, alpha=0.2)
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
    
    plt.title(f"Connections between reviewers and the book '{book_title}'")
    plt.axis('off')
    
    if save_as:
        plt.savefig(save_as)  # Save the figure
        print(f"Graph saved as '{save_as}'")
    else:
        plt.show()  # Show the graph if no file name is provided

# Main code execution
if __name__ == "__main__":
    # URL of the Goodreads book reviews page
    book_url = 'https://www.goodreads.com/book/show/1885.Pride_and_Prejudice'
    
    # Scrape reviews (scraping up to 5 pages as an example)
    reviewer_lists, book_title = scrape_goodreads_reviews(book_url, max_pages=5)
    
    # Flatten the list of sets to get unique reviewers
    unique_reviewers = set()
    for reviewers in reviewer_lists:
        unique_reviewers.update(reviewers)

    # Print the unique reviewers
    print(f"\nUnique reviewers for the book '{book_title}':")
    for reviewer in unique_reviewers:
        print(reviewer)

    # Build the graph from the collected reviewer data
    G = build_graph(reviewer_lists, book_title)
    
    # Specify the filename for saving the graph
    filename = 'reviewers_graph.png'  # You can change the file name and extension as needed
    
    # Visualize the connections with the book title as the central nodes and save the graph
    visualize_graph(G, book_title, save_as=filename)


# In[ ]:





# In[ ]:




