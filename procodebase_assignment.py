 
import tkinter as tk
from tkinter import ttk

# Function to extract insights based on the selected category
def extract_insights():
    story = story_text.get("1.0", tk.END).strip()
    category = category_selector.get()
    insights_display.delete("1.0", tk.END)

    if not story:
        insights_display.insert(tk.END, "Please enter a story to analyze.")
        return

    insights = {
        "Career Guidance": ["career", "job", "resume", "internship", "skills"],
        "Productivity": ["productivity", "focus", "time management", "habit", "routine"],
        "Life Hacks": ["life hack", "shortcut", "efficiency", "simplify", "tip"]
    }

    keywords = insights.get(category, [])
    extracted_insights = []

    for line in story.split('\n'):
        if any(keyword.lower() in line.lower() for keyword in keywords):
            extracted_insights.append(line.strip())

    if extracted_insights:
        insights_display.insert(tk.END, "\n".join(extracted_insights))
    else:
        insights_display.insert(tk.END, f"No insights found for '{category}'.")

# Tkinter GUI
root = tk.Tk()
root.title("Insight Extractor")

# Story Input
tk.Label(root, text="Enter your story:").pack(anchor="w", padx=10, pady=5)
story_text = tk.Text(root, wrap=tk.WORD, height=10, width=50)
story_text.pack(padx=10, pady=5)

# Category Selector
tk.Label(root, text="Select Insight Category:").pack(anchor="w", padx=10, pady=5)
category_selector = ttk.Combobox(root, values=["Career Guidance", "Productivity", "Life Hacks"], state="readonly")
category_selector.pack(padx=10, pady=5)
category_selector.current(0)  # Default selection

# Extract Insights Button
extract_button = tk.Button(root, text="Generate Insights", command=extract_insights)
extract_button.pack(pady=10)

# Insights Display
tk.Label(root, text="Insights:").pack(anchor="w", padx=10, pady=5)
insights_display = tk.Text(root, wrap=tk.WORD, height=10, width=50, state="normal")
insights_display.pack(padx=10, pady=5)

# Run the application
root.mainloop()























