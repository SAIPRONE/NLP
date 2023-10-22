# Google Custom Search CLI Tool
![nlp](https://github.com/SAIPRONE/NLP/assets/95390348/27e4c687-9ecd-4423-81c5-fe5278852a71)

This tool enables users to search Google through a custom search engine right from the command line. Written in Python, it tokenizes user queries, sends them to the Google Custom Search API, and then neatly displays the results.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Author](#author)
- [License](#license)

## Installation

1. Ensure you have Python installed on your machine. 
2. Clone this repository:
    ```
    git clone <repository-link>
    ```
3. Install the required dependencies:
    ```
    pip install nltk requests BeautifulSoup4
    ```

## Usage

1. Before running the script, make sure to fill in the `cx` (Programmable Search Engine ID) and `api_key` (Google API Key) variables in the `main()` function.
2. Run the script:
    ```
    python <script-name>.py
    ```
3. Follow the on-screen prompts. Type in your query and press `Enter`.
4. To exit the tool, simply type `exit`.

## Features

- **Tokenizing User Queries**: Breaks down user's queries into individual words using the Natural Language Toolkit (NLTK).
- **Google Custom Search Integration**: Sends the tokenized queries to Google's Custom Search API.
- **Beautiful Output**: Parses and displays search results in a readable and user-friendly manner.

## Author

- Fadi Helal

## License

This project is open-sourced. Feel free to use, modify, and distribute the code. We'd appreciate it if you give credit to the original author.
