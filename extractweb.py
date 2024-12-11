import requests
from bs4 import BeautifulSoup
import json
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def fetch_page(url):
    """Fetch the HTML content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching the URL: {e}")
        return None

def extract_links_and_images(html):
    """Extract all links and images from the HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract links
    links = set(a['href'] for a in soup.find_all('a', href=True))
    
    # Extract images
    images = set(img['src'] for img in soup.find_all('img', src=True))
    
    return {
        "links": list(links),
        "images": list(images)
    }

def organize_data(data, base_url):
    """Organize links into internal and external categories."""
    organized = {
        "internal_links": [],
        "external_links": [],
        "images": data["images"],
    }

    for link in data["links"]:
        if base_url in link or link.startswith("/"):
            organized["internal_links"].append(link)
        else:
            organized["external_links"].append(link)

    # Remove duplicates and sort
    organized["internal_links"] = sorted(set(organized["internal_links"]))
    organized["external_links"] = sorted(set(organized["external_links"]))
    organized["images"] = sorted(set(organized["images"]))

    return organized

def save_to_file(data):
    """Save organized data to a JSON file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if not file_path:
        return
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving file: {e}")

def scrape_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    html_content = fetch_page(url)
    if html_content:
        extracted_data = extract_links_and_images(html_content)
        organized_data = organize_data(extracted_data, base_url=url)
        save_to_file(organized_data)

# GUI Setup
app = tk.Tk()
app.title("Page Scraper")
app.geometry("400x200")

frame = tk.Frame(app)
frame.pack(pady=20)

tk.Label(frame, text="Enter URL:").grid(row=0, column=0, padx=5, pady=5)
url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, padx=5, pady=5)

scrape_button = tk.Button(app, text="Scrape URL", command=scrape_url)
scrape_button.pack(pady=10)

app.mainloop()
