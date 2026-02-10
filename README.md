# Manga Downloader

Use Python web scraping to download manga from nhentai.net and save it to a specified folder.

## About

This project is a Python-based tool designed to automate the process of downloading manga. It utilizes `requests` and `BeautifulSoup` to scrape manga content, retrieving high-quality images from nhentai.net while maintaining the correct page order.

Users can choose to run the script via Python or download the standalone executable file.

- **Releases (EXE)**: [Download latest release](https://github.com/sky9154/MangaDownloader/releases)

- **Repository**: [GitHub Repository](https://github.com/sky9154/MangaDownloader)

## Screenshots

![Demo](/assets/docs/demo.png)

## Features

- **Web Scraping**: Retrieves high-quality images from nhentai.net while maintaining the correct page order using requests and BeautifulSoup.

- **Download Management**: Downloads manga content as images to a user-defined directory using multithreading for faster performance.

- **PDF Conversion**: Allows users to save the downloaded manga automatically as a PDF.

## Getting Started

### Prerequisites

To run the source code, you need:

- Python 3.x

- pip (Python package installer)

_(Note: If you use the executable file from Releases, you do not need to install Python dependencies.)_

### Installation

**1. Clone repo**

```bash
git clone https://github.com/sky9154/MangaDownloader.git
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

This command will install required packages like `requests` and `beautifulsoup4`.

**3. Configuration (Optional)** You can configure the settings using the setting.ini file:

```ini
[Download]
max_workers = 3
delay = 1
```

This allows you to set the maximum number of threads (`max_workers`) and the delay between each request (`delay`).

**4. Run application**
```bash
python app.py
```

## Folder Structure

```
MangaDownloader/
├── assets/
│   └── images/         # Application resources (icons, cover images)
├── functions/          # Core logic (downloader, config, threading)
├── layout/             # UI Layout definitions
├── widgets/            # Custom UI components (buttons, input fields)
├── app.py              # Main application entry point
├── requirements.txt    # Python dependencies
└── setting.ini         # User configuration settings
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.