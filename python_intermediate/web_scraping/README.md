# Python Intermediate — Dragon Find Quotes

This project is part of my second–semester learning path in Computer Science, focusing on practical web scraping and terminal interaction.  
The goal is to build confidence with HTTP requests, HTML parsing, CLI workflows, and defensive programming through a real, functioning tool.

---

## Overview

Dragon Find Quotes is a command-line application that retrieves and displays quotes from `http://quotes.toscrape.com/`.  
The script requests pages from the website, parses their HTML structure, extracts quote blocks, and allows the user to browse them interactively through a paginated menu system.

The program also includes a minimal interface layer with typed-text output, colored formatting, and contextual feedback to simulate a more dynamic terminal experience.

---

## Core Features

### HTTP Requests  
The script uses `requests.get()` with built-in timeout and status checks. Each page is validated before parsing, and network-related exceptions are handled to prevent program crashes.

### HTML Parsing  
BeautifulSoup (`html.parser`) is used to locate quote containers, extract the quote text and authors, and detect whether a “Next” pagination button is available.

### Pagination System  
If the target page contains a next-page link, the application automatically stores it and allows the user to continue navigating forward until the final page is reached.

### Interactive Menu  
All interaction takes place inside a loop that refreshes the screen, shows available quotes, and waits for user input.  
The user can:
- select a quote number to view details  
- move to the next page  
- exit the program  

### Terminal Feedback  
The script uses:
- a typewriter-style printing function  
- color formatting through Colorama  
- screen clearing for cleaner updates  

---

## File Structure

**dragon_quotes.py**  
Main script containing:
- the web-scraping logic  
- the pagination mechanism  
- the CLI interface  
- error handling and formatted output  

---

## How It Works

1. The program accesses the base URL and downloads the page.  
2. It parses the HTML and extracts all `<div class="quote">` blocks.  
3. It checks whether a next-page button exists and stores its relative URL.  
4. The menu is displayed, showing the number of available quotes.  
5. The user interacts with the menu until choosing to exit.

---

## Requirements

Install the required dependencies: `pip install requests beautifulsoup4 colorama`

---

## Learning Goals

This project strengthens skills related to:

- handling HTTP communication  
- parsing structured HTML documents  
- managing user input in terminal applications  
- building loops with stateful navigation  
- applying structured error handling  
- organizing logic within maintainable functions  

It also serves as an introduction to transforming basic scripts into more complete and user-facing software.

---

## Future Improvements

Potential areas for expansion include:

- storing selected quotes in a local database  
- filtering quotes by tags  
- adding backward navigation  
- exporting pages or quotes as text files  

This project represents an early but significant step in applying Python to real interactive tasks, re
