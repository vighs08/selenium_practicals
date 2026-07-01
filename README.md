# 🧪 Selenium Practicals

**A hands-on collection of Python + Selenium WebDriver scripts covering the core building blocks of web UI automation.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning%20%2F%20Practice-blue)
![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey)

---

## 📖 About

`selenium_practicals` is a practice repository built while learning **Selenium WebDriver with Python**. Instead of one large framework, it's a library of small, focused scripts — each one isolates a single Selenium concept (locators, waits, alerts, frames, form elements, etc.) so it's easy to reference exactly the technique you need.

Think of it as a **Selenium cookbook**: open the script for the concept you're stuck on, and see a minimal working example.

---

## 🗂️ What's Inside

### 🔍 Locating Elements
| Script | What it demonstrates |
|---|---|
| `printing_ID.py` | Locating elements using the `id` attribute |
| `printing_NAME.py` | Locating elements using the `name` attribute |
| `printing_LINK.py` | Locating elements using link text |
| `printing_CSS_TAG_XPATH.py` | Locating elements via CSS selectors, tag name, and XPath |
| `printing_page_url_title.py` | Fetching the current page URL and title |

### 🖱️ Interacting with Elements
| Script | What it demonstrates |
|---|---|
| `send_keys.py` | Sending text input to fields |
| `filling_form.py` | Filling and submitting a web form end-to-end |
| `checkbox.py` | Working with checkboxes |
| `radio_test.py` | Working with radio buttons |
| `dropdown.py` | Selecting dropdown options (by visible text/value) |
| `dropdown_by_index.py` | Selecting dropdown options by index |
| `sliders.py` | Interacting with slider controls |
| `datepicker.py` | Automating date picker widgets |

### 🧭 Navigation & Browser Control
| Script | What it demonstrates |
|---|---|
| `first_sel.py` | A basic "hello world" Selenium script — launching a browser session |
| `back_forward_refresh.py` | Simulating browser back, forward, and refresh actions |

### 🧱 Frames & Alerts
| Script | What it demonstrates |
|---|---|
| `iframe.py` | Switching into and out of an `<iframe>` |
| `nested_iframe.py` | Handling nested (frame-within-a-frame) structures |
| `alert.py` / `alerts_example.py` | Handling JavaScript alerts, confirms, and prompts |

### ⏱️ Waits & Assertions
| Script | What it demonstrates |
|---|---|
| `implicit_wait.py` | Using Selenium's implicit wait for element synchronization |
| `assert.py` | Writing basic assertions to validate page state |

---

## 🛠️ Tech Stack

- **Language:** Python
- **Library:** [Selenium WebDriver](https://www.selenium.dev/)
- **Browser:** Google Chrome (via `webdriver.Chrome()`)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Google Chrome installed
- ChromeDriver matching your Chrome version (Selenium 4.6+ handles this automatically via Selenium Manager)

### Installation
```bash
git clone https://github.com/vighs08/selenium_practicals.git
cd selenium_practicals
pip install selenium
```

### Run any script
```bash
python printing_ID.py
```
Swap in the filename of whichever concept you want to explore.

---

## 📁 Project Structure
```
selenium_practicals/
├── printing_ID.py
├── printing_NAME.py
├── printing_LINK.py
├── printing_CSS_TAG_XPATH.py
├── send_keys.py
├── filling_form.py
├── checkbox.py
├── radio_test.py
├── dropdown.py
├── dropdown_by_index.py
├── sliders.py
├── datepicker.py
├── iframe.py
├── nested_iframe.py
├── alert.py
├── alerts_example.py
├── implicit_wait.py
├── assert.py
├── back_forward_refresh.py
├── first_sel.py
└── printing_page_url_title.py
```

> 💡 Each script is standalone — there are no shared page objects or a test runner. Open the one you need and read top to bottom.

---

## 🤝 Contributing

This is primarily a personal learning repo, but suggestions, fixes, or additional practice scripts are welcome via pull request.

## 📄 License

No license currently specified. Please reach out to the repository owner for usage permissions.

---

<p align="center">Built while learning Selenium, one script at a time. 🚀</p>
