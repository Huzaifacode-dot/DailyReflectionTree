# Daily Reflection Tree

**A simple, no-AI reflection tool that helps you actually think through your day**

## What This Does

At the end of a long day—when you're tired but know you should reflect—this walks you through a set of structured questions to help you notice patterns in how you think and act:

* Did you take ownership of your actions? *(agency)*
* Did you contribute or mostly expect? *(contribution)*
* Were you focused only on yourself or also on others? *(perspective)*

**No AI, no randomness, no long typing**—just choose options and get clear, consistent insights.

---

## Folder Structure

```
├── tree/                 
│   ├── reflection-tree.tsv     # Main decision tree
│   └── tree-diagram.png        # Visual flow of the tree
├── agent/                    
│   └── reflection_tree.py      # Runnable CLI version
├── transcripts/              
│   ├── victim-path.md
│   └── victor-path.md
├── write-up.md                # Design explanation
└── README.md                  
```

---

## Quick Demo (Python)

From the root folder:

```bash
python agent/reflection_tree.py
```

Follow the prompts.
Try answering differently (e.g., “Tough” vs “Productive”) to see how the path changes.

---

## How the Tree Works

1. You answer questions with fixed options
2. Your answers determine the path (no randomness)
3. Signals track patterns across three axes
4. Reflections highlight what your responses suggest
5. A summary shows your overall tendency

**Example flow**:
START → “How was today?” → “Tough” → “What was your instinct?” → “Waited for help” → reflection → next axis

---

## Tree Format (TSV Columns)

| id | parentId | type     | text             | options                 | target | signal |
| -- | -------- | -------- | ---------------- | ----------------------- | ------ | ------ |
| A1 | START    | question | "How was today?" | Tough | Productive ...  |        |        |
| D1 | A1       | decision | (hidden)         | answer=Tough:A1_LOW ... |        |        |

---

## Why This Works

* **Deterministic** – same answers always lead to the same outcome
* **Grounded in psychology** – based on ideas like locus of control and perspective-taking
* **Practical** – designed for real end-of-day reflection, not theory
* **Non-judgmental** – it nudges, not lectures

---

## Try These Personas

* **“Victim Rob”** → chooses external/blame options → gets gentle prompts toward ownership
* **“Victor Priya”** → chooses internal/contribution options → gets deeper reflection

---

## Built For

Created as part of the DeepThought Fellowship assignment to demonstrate how psychological concepts can be translated into structured, deterministic systems—not just AI-driven conversations.

---
