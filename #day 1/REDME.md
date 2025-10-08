# 🧮 GUI Calculator — Day 1

A **responsive calculator** built for **Day-1 of the MySirG 100 Days Learning Challenge** using **HTML, CSS, and JavaScript**.  
It features a clean grid layout, a live display, and essential operations — including percent handling and backspace support.

---

## ✨ Features

✅ **Responsive layout** with a large display and neatly spaced `4x4` button grid for quick input.  
✅ **Number keys** `0–9`, **decimal**, and operators `+`, `−`, `×`, `÷`, and **percent (%)**.  
✅ **AC** clears the current expression; **Backspace** removes the last character.  
✅ **Percent logic** replaces `%` with division by `100` before evaluation.  
✅ **Defensive checks** prevent invalid or undefined results from breaking the UI.

---

## 🧠 Tech Stack

| Technology | Purpose |
|-------------|----------|
| **HTML** | Structure and semantic layout of the calculator |
| **CSS** | Grid, spacing, colors, and hover/active effects |
| **JavaScript** | State management, input handling, and expression evaluation |

---

## 📁 Project Structure

├─ calculator.html # Markup and button grid
├─ style.css # Layout, colors, responsiveness
└─ app.js # State, input handling, evaluation


---

## 🚀 Getting Started

1. **Download or clone** this repository.  
2. Open **`calculator.html`** in any modern browser.  
3. That’s it — the calculator runs locally, no extra tools needed!  
4. Modify `style.css` or `app.js` and simply refresh to see live changes.  

---

## 🧾 Usage

➡️ Tap or click digits and operators to build an expression that appears live on the display.  
➡️ Use **AC** to reset, **Backspace** to delete the last character, and **=** to evaluate.  

**Examples:**
| Expression | Result |
|-------------|---------|
| `50% × 2` | `1` |
| `8 ÷ 2` | `4` |
| `5 + 6` | `11` |

---

## ⚙️ Key Logic Notes

- **Percent Handling:**  
  Converts `%` into division by `100` before evaluation.  
  Example:  

a % × b → a × (b / 100)

gives intuitive results like real calculators.

- **Safety Checks:**  
Prevents empty or invalid expressions from breaking the UI.  

---

## 🗺️ Roadmap

🚧 Upcoming Enhancements:
- ⌨️ **Keyboard input** with visual highlights.  
- 💾 **Memory keys** `M+`, `M−`, `MR`, `MC`.  
- 🌙 **Theme toggle** for light/dark mode.  

---

## 🙌 Acknowledgments

Built as part of the **MySirG 100 Days Learning Challenge**,  
with guidance and inspiration from **Saurabh Shukla Sir** and the **Day-1 tutorial**.

---

### 🧡 Author

**Harsh Kushwaha**  
*100 Days Learning Challenge Participant*  
