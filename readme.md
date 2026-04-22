# Daily Reflection Tree  
**A no-AI evening reflection tool that actually gets you thinking about your day**

## What This Does  
At 7pm when you're fried but know you should reflect, this walks you through structured questions that reveal:  
- Did you own your choices today? *(agency)*  
- Did you give more than you took? *(contribution)*  
- Was your head just about "me" or "us"? *(perspective)*  

**No AI, no randomness, no typing essays**—just pick options, get real insights.

## Folder Structure  
```
├── tree/                 
│   ├── reflection-tree.tsv     # The actual tree (load this!)
│   └── tree-diagram.png       # Visual map of all paths
├── agent/                    # Bonus: runnable Python version
│   └── reflection_tree.py
├── transcripts/              # Sample conversations
│   ├── victim-path.md
│   └── victor-path.md
├── write-up.md              # Why these questions work
└── README.md                ← you are here
```

## Quick Demo (if you have Python)  
```bash
cd agent/
python3 reflection_tree.py
```
Follow the prompts. Try "Tough" day → different path than "Productive".

## How the Tree Works  
1. **Questions** have 3-4 fixed options  
2. **Decision nodes** route you: `Tough|Frustrating → agency probe`  
3. **Signals** tally: `axis1:internal +1`  
4. **Reflections** show your patterns: *"You spotted your choices even on tough days"*  
5. **Summary** reveals your dominant mindset  

**Example flow**: START → *"How was today?"* → *"Tough"* → *"What was your instinct?"* → *"Waited for help"* → *"Fair—tough days pull focus outward. But you made choices..."*

## Tree Format (TSV Columns)  
| id | parentId | type | text | options | target | signal |  
|----|----------|------|------|---------|--------|--------|  
| A1 | START | question | "How was today?" | Tough<em>Productive</em>... | | |  
| D1 | A1 | **decision** | (hidden) | answer=Tough:A1_LOW... | | |  

## ✅ Evaluation Criteria Match  
- **25+ nodes** - 3 axes × (questions + decisions + reflections)  
- **Psych grounded** - Rotter, Dweck, Maslow → real questions  
- **Deterministic** - Same answers = same path always  
- **No moralizing** - Guides, doesn't judge  
- **Progressive** - Axis 1 insight → Axis 2 question  

## Try These Personas  
**"Victim Rob"**: Pick external/blame options → gets gentle agency nudge  
**"Victor Priya"**: Internal/contribution → gets transcendence prompts  

## Built For  
DeepThought Fellowship assignment. Shows I can turn psych research into structured products, not just chatbots.

---

