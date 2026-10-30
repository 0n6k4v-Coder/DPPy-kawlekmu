<div align="center">

# 📚 Reading Tracker

**A simple command-line application to manage books and track reading progress.**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NVIDIA%20NVIDIA%20API-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="NVIDIA API">
  <img src="https://img.shields.io/badge/LLM-Powered-blueviolet?style=for-the-badge" alt="LLM Powered">
</p>

</div>

---

## ✨ Main Features

- **Add Books** — Add books to your reading list.
- **View Books** — Display all saved books.
- **Update Status** — Change a book's reading status.
- **Remove Books** — Remove books from your list.
- **Search Books** — Find books by title.
- **Reading Progress** — Summarize your reading progress.
- **AI Summary** — Generate reading summaries using an LLM.

**Reading Status:** `Planned` · `Reading` · `Finished`

## 🚀 How to Run

### 1. Install Dependencies

Install Python, then run:

```bash
pip install openai python-dotenv
```

### 2. Configure the API Key

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Add your NVIDIA API key to `.env`:

```dotenv
NVIDIA_API_KEY=your_api_key
```

### 3. Start the Application

Run the following command from the `rush` directory:

```bash
python main.py
```

### 4. Use the Menu

Enter a menu number to select an action. Choose `8` to exit.

---

<div align="center">

**Built with Python 🐍**

</div>