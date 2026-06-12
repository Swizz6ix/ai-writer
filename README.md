# ai-writer
A small agent demostration for my students, a parameterized text generation system:

Input → Prompt Template → LLM (Gemini) → Output UI

Users control:
* Tone (professional, casual, persuasive…)
* Audience (beginners, executives…)
* Format (email, blog post, tweet…)

# What This Project Teaches
This mini-project encodes core GenAI engineering patterns:
- Prompt templating
- Input parameterization
- UI → LLM pipeline design
- Separation of concerns (UI vs logic vs API)
- Deterministic control over stochastic outputs

# System Architecture
```
[Streamlit UI]
     ↓
[Input Form]
     ↓
[Prompt Builder]
     ↓
[Gemini API Client]
     ↓
[Response Parser]
     ↓
[Output Renderer]
```

# Environment and dependencies
**conda environment**

*Create Conda and activate conda environment*

<mark style="background-color: yellow;">Create conda environment</mark>
`conda create -n ai-writer python=3.10`

<mark style="background-color: yellow;">Activate conda environment</mark>
`conda activate ai-writer`

<mark style="background-color: yellow;">Install Environment packages</mark>
`conda env create -f environment.yml`

**dependencies**
1. genai
2. python-dotenv
3. streamlit

**Install Dependencies**
`pip install -r requirements.txt`

**dependencies**
```
ai-writing-assistant/
│
├── app.py
├── prompt_builder.py
├── gemini_client.py
├── .env
└── requirements.txt
└── environment.yml
```

# Test Scenarios
Use structured test cases:

Case 1
- Input: “Announce a new AI course”
- Tone: Professional
- Audience: Executives
- Format: Email

Case 2
- Input: “Explain blockchain”
- Tone: Casual
- Audience: Beginners
- Format: Blog Post

# Features Improvement Ideas
These turn this from a demo → real product:

✅ 1. Multi-step generation
- Outline → Expand → Refine

✅ 2. Editable prompt preview
- Let users see and tweak the prompt

✅ 3. Tone intensity slider
- Slightly professional → Very formal

# ⚠️ Common Pitfalls
- ❌ Overly vague prompts → weak output
- ❌ No constraints → inconsistent tone
- ❌ Hardcoding everything → no flexibility
- ❌ Ignoring latency/errors → bad UX

# Deliverable Checklist
Students should end up with:

- ✅ Working Streamlit app
- ✅ Modular code (client + prompt builder)
- ✅ Configurable inputs (tone, audience, format)
- ✅ Clean generated outputs
- ✅ Error handling

# Run the App
`streamlit run app.py`