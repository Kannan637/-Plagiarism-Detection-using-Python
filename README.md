# Plagiarism Detection Using Python

## 📌 Project Overview

This project is a simple **Plagiarism Detection System** developed using Python. It compares the contents of two text files and calculates the similarity percentage between them using Python's built-in `difflib` library.

The project is useful for understanding the basics of text comparison and similarity analysis. It can be used to compare assignments, documents, or any text-based files.

---

## 🚀 Features

* Compare two text files.
* Calculate similarity percentage.
* Easy to understand and implement.
* Uses Python's built-in `difflib` module.
* Lightweight and beginner-friendly.

---

## 🛠️ Technologies Used

* Python 3
* `difflib` module
* Google Colab / Jupyter Notebook / VS Code

---

## 📂 Project Structure

```text
Plagiarism-Detection/
│
├── Demo#1.txt
├── Demo#2.txt
├── plagiarism_detection.py
└── README.md
```

---

## 📝 Sample Code

```python
from difflib import SequenceMatcher

with open("Demo#1.txt") as file1, open("Demo#2.txt") as file2:

    file1_data = file1.read()
    file2_data = file2.read()

    similarity = SequenceMatcher(
        None,
        file1_data,
        file2_data
    ).ratio()

    print(f"Plagiarism Detection: {similarity * 100:.2f}%")
```

---

## ▶️ How It Works

1. Open the two text files.
2. Read their contents as strings.
3. Use `SequenceMatcher()` from `difflib` to compare the texts.
4. Calculate the similarity ratio.
5. Convert the ratio into a percentage.
6. Display the plagiarism percentage.

---

## 📊 Example

### Demo#1.txt

```text
Python is one of the most popular programming languages.
It is easy to learn and widely used.
```

### Demo#2.txt

```text
Python is among the most popular programming languages.
It is simple to learn and widely used.
```

### Output

```text
Plagiarism Detection: 82.45%
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/plagiarism-detection.git
```

2. Navigate to the project directory:

```bash
cd plagiarism-detection
```

3. Run the Python file:

```bash
python plagiarism_detection.py
```

---

## 🔍 Limitations

* Works only with plain text (`.txt`) files.
* Cannot detect paraphrased content accurately.
* Sensitive to changes in word order.
* Not suitable for large-scale plagiarism detection systems.

---

## 🚀 Future Enhancements

* Support for PDF and DOCX files.
* Compare multiple files simultaneously.
* Use Natural Language Processing (NLP) techniques.
* Add a graphical user interface (GUI).
* Highlight matching sentences or paragraphs.

---

## 👨‍💻 Author

**Kannan C**

* AI Creative Executive
* Graphic Designer
* Motion Graphic Designer
* UI Designer
* Python & Web Development Enthusiast

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify it for educational purposes.
