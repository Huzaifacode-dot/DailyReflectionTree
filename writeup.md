# Reflection Tree Design Write-up

## 1. Approach
I wanted to build something that actually feels helpful at 7pm when you're drained but know you should reflect. The tree walks people through three big psychological shifts: from victim/blame thinking → owning your choices → contribution mindset → team/world awareness. 

No free text, no AI guessing—just fixed options that branch predictably. Same answers = same path every time. That's the trust part.

## 2. Question Design  
I spent most time here because questions are the product. They needed to feel like a colleague asking "hey, walk me through your day" not a psych exam. 

Each has 3-4 options, always balanced (2 "healthy" vs 2 "common traps"). Real behaviors, not abstractions.

**Example from Axis 1 (Locus)**:  
*"Recall a challenge today—what mostly caused it?"*  
A) My prep fell short  
B) Timing was off  
C) I adjusted well  
D) Others blocked me  

You immediately see if someone's defaulting to external vs spotting their agency.

I tested these by roleplaying tired employee personas with ChatGPT. Some options got merged when they felt too similar.

## 3. Branching Logic  
Decision nodes are the magic—hidden routing based on prior answers.  

Like the sample: `answer=Productive|Mixed → A1_Q_AGENCY_HIGH` (internal path).  
Tough|Frustrating → external path with gentler probing.  

Each axis tallies signals: `axis1:internal +1` per internal-leaning answer. Summary picks dominant: `if internal > external → "You leaned internal on agency"`.

Rough count: 3 axes × (2 questions + 1 decision + 1 reflection) + bridges + summary = 25+ nodes.

## 4. Psychological Foundations  
**Axis 1** comes straight from Rotter's 1966 Locus of Control scale. Internal items like *"People's misfortunes result from their own mistakes"* became *"My preparation fell short"*. External like *"Without the right breaks..."* → *"Others blocked me."* Added Dweck's growth mindset flavor.

**Axis 2** pits Campbell's 2004 entitlement scale (*"I deserve more regardless of effort"*) against Organ's 1988 citizenship behaviors (*"helping beyond your role"*). Questions surface: *gave extra effort* vs *expected unearned credit*.

**Axis 3** builds on Maslow's late-1960s self-transcendence (peak beyond self-actualization) + Batson's perspective-taking. Shifts frame from *"my stress"* → *"team/customer impact"*.

Wikipedia + original scale PDFs. Simplified heavily for 7pm brains.

## 5. Design Choices  
- **No preaching**. Reflections validate: *"Tough days pull focus outward. Fair. But you made choices too..."*  
- **Conversational flow**. Bridges connect: *"Now that you see your agency, what'd you give today?"*  
- **Progressive**. Axis 1 insight feeds Axis 2 question, etc.  
- **Deterministic only**. No scores, just path-determined reflections.

Tradeoff: Deeper trees (5 options/question) vs shorter paths. Chose shorter—completion > perfection.

## 6. What I'd Improve  
- Multi-day tracking (spot trends week-over-week)  
- Role variants (manager trees vs IC trees)  
- More nuanced signals (internal-but-defensive vs internal-confident)  
- Visual progress bar (you're 60% through Axis 2)

## 7. Part B: Execution (Agent)

A simple CLI-based agent was implemented to execute the decision tree. It reads the TSV structure, traverses nodes deterministically based on user input, and generates reflections and a summary.

This demonstrates how the static decision tree can be translated into an interactive system without relying on LLMs.

## Conclusion  
This was harder than I expected—turning fuzzy psych into click-paths that actually shift thinking. The constraint of *no LLM at runtime* forced better questions. 

Feels like a wise colleague who asks the right questions at the right time. That's the goal.

*(~25 nodes across 3 axes. Code runner + Mermaid diagram in repo.)*