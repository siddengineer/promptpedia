import json, itertools

# category: (icon_code, list of (title, framework, prompt))
data = {}

def add(cat, items):
    data.setdefault(cat, [])
    data[cat].extend(items)

# ---------- 1. Productivity & Time Management ----------
topics = ["daily routine","morning routine","night routine","weekly planning","time blocking",
"deep work sessions","anti-procrastination system","study routine","burnout-free workload",
"phone addiction reduction","dopamine detox","focus improvement","consistency habit-building",
"habit tracking","monthly planning","Eisenhower Matrix task sorting","30-day discipline challenge",
"exam preparation","weekend reset","ADHD-friendly workflow","energy management","minimalist task system",
"decision-making process","personal productivity dashboard","distraction-free workspace",
"single-tasking practice","work-life balance schedule","commute time usage","meeting-free focus blocks",
"end-of-day shutdown ritual","priority stacking","calendar audit","procrastination root-cause analysis",
"accountability check-in system"]
items = []
for t in topics:
    items.append((f"{t.title()} Builder","RTF",
        f"Act as a productivity coach. First ask me about my goals, schedule, energy levels, and current struggles with {t}. Then design a realistic, personalized {t} I can start using today."))
add("Productivity & Time Management", items)

# ---------- 2. Content Creation & Social Media ----------
topics = ["LinkedIn posts","Instagram captions","YouTube scripts","Twitter/X threads","blog articles",
"carousel slides","content calendars","viral hooks","short-form video scripts","newsletter issues",
"podcast show notes","personal branding statements","content repurposing plans","storytelling posts",
"SEO-optimized articles","case study write-ups","testimonial requests","community engagement replies",
"content batching workflows","Reels/Shorts scripts","thought-leadership posts","comparison posts",
"listicle articles","behind-the-scenes posts","announcement posts","controversial hot-take posts",
"educational carousels","interview-style posts","milestone/celebration posts","FAQ content",
"content audits","cross-platform content plans","evergreen content ideas","trend-jacking posts",
"call-to-action variations"]
items = []
for t in topics:
    items.append((f"{t.title()} Generator","AIDA",
        f"Act as a social media strategist. Ask me about my niche, target audience, tone, and goals. Then create high-engagement {t} using a strong hook, clear value, and a compelling call to action."))
add("Content Creation & Social Media", items)

# ---------- 3. Coding & Development ----------
topics = ["debugging a script","code review","learning a new programming language","building a portfolio project",
"understanding legacy code","writing unit tests","optimizing slow code","designing a database schema",
"building a REST API","learning data structures & algorithms","preparing for coding interviews",
"refactoring messy code","setting up CI/CD","writing clean documentation","containerizing an app with Docker",
"building a CLI tool","learning Git & version control","building a web scraper","creating a chatbot",
"working with regular expressions","learning SQL joins","building a full-stack app","securing an application",
"writing technical specs","estimating a sprint","choosing a tech stack","migrating a legacy system",
"building automation scripts","learning system design","debugging production incidents",
"writing clear commit messages","building a browser extension","learning a new framework",
"performance profiling","building CI pipelines"]
items = []
for t in topics:
    items.append((f"{t.title()} Mentor","RODES",
        f"Act as a senior software engineer mentor. Help me with {t}. Ask clarifying questions about my current skill level and codebase, then guide me step by step with explanations, examples, and best practices rather than just giving the final answer."))
add("Coding & Development", items)

# ---------- 4. Career & Job Search ----------
topics = ["resume writing","LinkedIn profile optimization","mock interviews","HR interview prep",
"technical interview prep","salary negotiation","cover letter writing","portfolio review",
"ATS resume scanning","job search strategy","skill gap analysis","career switching plan",
"freelancing roadmap","networking messages","internship preparation","interview confidence building",
"STAR-format answers","remote job strategy","communication skills training","career decision making",
"job application tracking","30-day interview prep plan","personal branding for job seekers",
"reference letter requests","offer evaluation","first-90-days planning","promotion case building",
"performance review prep","exit interview prep","layoff recovery plan","side income exploration",
"industry pivot roadmap","executive presence coaching","recruiter outreach messages","panel interview prep"]
items = []
for t in topics:
    items.append((f"{t.title()} Coach","RISEN",
        f"Act as a senior career coach. Ask about my background, target role, industry, and timeline. Then guide me through {t} with a step-by-step action plan and specific examples I can use."))
add("Career & Job Search", items)

# ---------- 5. Marketing & Branding ----------
topics = ["brand positioning","go-to-market strategy","email marketing campaigns","paid ad copy",
"landing page copy","customer persona development","competitor analysis","pricing strategy",
"referral program design","brand voice guidelines","influencer outreach messages","product launch plan",
"customer retention strategy","upsell/cross-sell campaigns","market segmentation","funnel optimization",
"A/B test ideas","brand naming","tagline creation","press release writing","partnership pitch decks",
"customer journey mapping","loyalty program design","seasonal campaign planning","conversion rate audit",
"social proof strategy","affiliate marketing plan","local marketing strategy","rebranding roadmap",
"marketing budget allocation","growth experiment backlog","onboarding email sequence",
"win-back campaign for churned customers","brand style guide"]
items = []
for t in topics:
    items.append((f"{t.title()} Strategist","CSI-FBI",
        f"Act as a senior marketing strategist. Ask about my product, target audience, budget, and goals. Then build a complete {t} with clear reasoning, structured steps, and measurable outcomes in a table format."))
add("Marketing & Branding", items)

# ---------- 6. Business & Strategy ----------
topics = ["SWOT analysis","PESTLE analysis","business model canvas","competitive analysis",
"startup idea validation","pricing model design","operations workflow design","vendor negotiation",
"risk assessment","business plan writing","investor pitch deck outline","cash flow forecasting",
"process improvement (DMAIC)","feature prioritization (MoSCoW)","OKR setting",
"customer feedback analysis","org chart design","hiring plan","supply chain optimization",
"partnership evaluation","market entry strategy","scaling roadmap","cost-cutting analysis",
"exit strategy planning","board meeting prep","company culture design","remote team management plan",
"crisis communication plan","product roadmap prioritization","customer support workflow design",
"quarterly business review prep","M&A due diligence checklist","franchise expansion plan",
"sustainability strategy"]
items = []
for t in topics:
    items.append((f"{t.title()} Advisor","CRISPE",
        f"Act as an expert startup and business advisor. Ask about my industry, company stage, and objectives. Then walk me through a {t} with practical, realistic recommendations and a clear action plan."))
add("Business & Strategy", items)

# ---------- 7. Education & Learning ----------
topics = ["a new programming concept","a foreign language","a complex science topic","exam material",
"a certification syllabus","public speaking","critical thinking","a new software tool",
"financial literacy basics","a historical topic","a math concept","research methodology",
"a musical instrument","touch typing","memory techniques","speed reading","note-taking systems",
"a professional certification","statistics fundamentals","a new industry from scratch",
"philosophy fundamentals","design fundamentals","writing skills","data literacy",
"a new software framework","project management fundamentals","negotiation skills",
"emotional intelligence","logical reasoning","a college-level course","a soft skill",
"a professional exam like PMP or CFA","a new craft or hobby","teaching a topic to others"]
items = []
for t in topics:
    items.append((f"Learn {t.title()} Step-by-Step","RISEN",
        f"Act as an expert tutor. Ask about my current knowledge level, available time, and learning style. Then teach me {t} step by step with simple explanations, real examples, and practice exercises."))
add("Education & Learning", items)

# ---------- 8. Writing & Copywriting ----------
topics = ["a short story","a personal essay","a persuasive essay","a product description",
"a sales page","an email sequence","a speech","a eulogy","a wedding toast","a poem",
"a children's story","a screenplay scene","a book outline","a nonfiction book chapter",
"a press release","a grant proposal","an apology letter","a complaint letter","a thank-you note",
"a recommendation letter","a bio/about-me page","a FAQ page","a white paper","a case study",
"an op-ed","a memoir excerpt","a video script","a podcast intro script","a toast for a retirement party",
"a company mission statement","a value proposition statement","a tagline","an elevator pitch",
"a testimonial request email"]
items = []
for t in topics:
    items.append((f"Write {t.title()}","PAS",
        f"Act as a professional writer. Ask about the purpose, audience, tone, and key message. Then write {t} that is clear, engaging, and emotionally resonant, using the problem-agitate-solution structure where appropriate."))
add("Writing & Copywriting", items)

# ---------- 9. Data & Analytics ----------
topics = ["exploratory data analysis","a dashboard design","a SQL query optimization","a data cleaning workflow",
"a KPI framework","an A/B test analysis","a cohort analysis","a churn prediction approach",
"a data visualization plan","a survey design","a regression analysis walkthrough","a forecasting model",
"a data pipeline design","an ETL process design","a data quality audit","a customer segmentation model",
"a statistical significance check","a data storytelling narrative","an Excel/Power BI report",
"a metrics tree breakdown","a root-cause analysis of a metric drop","an experiment design",
"a data governance policy","a reporting automation plan","a Python data analysis script walkthrough",
"a funnel drop-off analysis","a data dictionary","an outlier detection approach","a time-series analysis",
"a survey response analysis","a metrics naming convention","a self-serve analytics rollout plan",
"a data storytelling slide deck","an anomaly alerting system design","a customer LTV calculation model"]
items = []
for t in topics:
    items.append((f"{t.title()} Guide","RODES",
        f"Act as a senior data analyst. Ask about my dataset, tools, and business question. Then guide me through {t} with clear steps, explanations of the reasoning, and example outputs in table format."))
add("Data & Analytics", items)

# ---------- 10. Health & Wellness ----------
topics = ["a beginner workout plan","a home workout routine","a stretching routine","a sleep improvement plan",
"a stress management routine","a mindfulness practice","a healthy meal plan","a hydration habit tracker",
"a posture correction routine","a screen-time eye-care routine","an anxiety-coping toolkit",
"a habit-stacking wellness plan","a work-from-home ergonomics setup","a beginner running plan",
"a recovery/rest day plan","a digital detox weekend","a self-care checklist","a journaling practice",
"a gratitude practice","an energy-boosting morning routine","a breathing exercise routine",
"a healthy snacking guide","a step-count improvement plan","a beginner meditation guide",
"a work-stress recovery plan","a beginner yoga routine","a healthy grocery list system",
"a night-shift sleep adjustment plan","an injury-recovery light movement plan","a caffeine reduction plan",
"a family meal-prep system","a desk-worker mobility routine","a travel wellness routine",
"a seasonal-mood (SAD) coping plan","a new-parent self-care plan"]
items = []
for t in topics:
    items.append((f"{t.title()} Planner","CARE",
        f"Act as a certified wellness coach (not a medical professional). Ask about my current habits, constraints, and goals. Then create {t} with realistic, gradual steps and a simple example to follow. Include a note to consult a doctor for personalized medical advice."))
add("Health & Wellness", items)

# ---------- 11. Finance & Money ----------
topics = ["a monthly budget","a debt payoff plan","a savings challenge","an emergency fund plan",
"a beginner investing roadmap","a retirement savings plan","a side-income plan","a subscription audit",
"a financial goal-setting framework","a spending tracker system","a house-buying savings plan",
"a student loan payoff strategy","a freelancer tax preparation checklist","a net-worth tracking system",
"a 50/30/20 budget breakdown","a financial independence roadmap","a wedding budget plan",
"a travel budget plan","a car-buying decision framework","a credit score improvement plan",
"an investment portfolio review checklist","a small business budget","a family budgeting system",
"a college savings plan","a first-job money management guide",
"a rainy-day fund plan","a no-spend month challenge","a bill-negotiation script",
"a passive income exploration plan","an inheritance management plan","a couples budgeting system",
"a teen/young-adult money basics guide","a gig-worker income smoothing plan"]
items = []
for t in topics:
    items.append((f"{t.title()} Assistant","SMART",
        f"Act as a personal finance coach (not a licensed financial advisor). Ask about my income, expenses, and financial goals. Then build {t} using SMART goals with clear milestones and simple, realistic numbers."))
add("Finance & Money", items)

# ---------- 12. Personal Development ----------
topics = ["a self-confidence building plan","a public speaking practice plan","a boundary-setting guide",
"a conflict resolution framework","an active listening practice","a self-reflection journal template",
"a values clarification exercise","a life-vision exercise","a fear-facing action plan",
"a personal SWOT analysis","a growth mindset practice","a self-discipline system",
"a relationship communication guide","a decision journal template","an accountability partner system",
"a limiting-belief reframing exercise","a personal mission statement","a life-balance wheel exercise",
"a resilience-building plan","a gratitude letter","a 5-year vision plan","a habit-replacement plan",
"a self-compassion practice","a comfort-zone expansion challenge","a personal legacy reflection",
"a forgiveness reflection exercise","a personal identity exploration exercise","a courage-building challenge",
"an emotional regulation toolkit","a patience-building practice","a minimalism mindset exercise"]
items = []
for t in topics:
    items.append((f"{t.title()} Coach","TAG",
        f"Act as a personal development coach. Task: help me build {t}. Action: ask about my current situation and challenges first, then create a practical exercise. Goal: help me make real, lasting progress."))
add("Personal Development", items)

# ---------- 13. Design & Creativity ----------
topics = ["a logo concept brief","a color palette","a typography pairing","a UI wireframe concept",
"a landing page layout","a mobile app onboarding flow","a design system outline","a mood board brief",
"a packaging design concept","a poster design concept","an icon set concept","a presentation deck design",
"a brand identity concept","a portfolio website layout","an illustration style guide",
"a dashboard UI concept","a dark-mode design adaptation","an accessibility audit checklist",
"a design critique framework","a user persona for design","a wireframe-to-prototype plan",
"an animation/micro-interaction concept","a design handoff checklist","a rebrand mood board",
"a game UI concept","an email template design","a print ad layout concept","a merch design concept",
"a data-visualization style guide","a design system component checklist","an event branding concept"]
items = []
for t in topics:
    items.append((f"{t.title()} Brief","CRISPE",
        f"Act as a senior product designer. Ask about the brand, audience, and platform. Then create {t} with clear rationale, references, and specific creative direction."))
add("Design & Creativity", items)

# ---------- 14. Sales & Negotiation ----------
topics = ["a cold outreach email","a sales discovery call script","an objection-handling guide",
"a follow-up email sequence","a pricing negotiation script","a proposal document outline",
"a demo call script","a closing techniques guide","a referral request script","an upsell pitch",
"a LinkedIn sales message","a lost-deal win-back email","a client onboarding script",
"a contract negotiation checklist","a sales pipeline review framework","a value-based selling pitch",
"a rejection-handling mindset guide","a partnership negotiation script","a renewal conversation script",
"a discovery questionnaire","a competitor comparison talk track","a sales call role-play scenario",
"an account expansion strategy","a negotiation BATNA analysis","a trust-building sales script",
"a discovery-call agenda","a proposal follow-up cadence","a champion-building strategy for enterprise deals",
"a trade-show pitch script","a customer success handoff script","a price-objection rebuttal script"]
items = []
for t in topics:
    items.append((f"{t.title()} Builder","STAR",
        f"Act as a top-performing sales coach. Ask about my product, target customer, and typical objections. Then create {t} with realistic language and confident, non-pushy phrasing."))
add("Sales & Negotiation", items)

# ---------- 15. AI & Prompt Engineering ----------
topics = ["writing better prompts","building a custom GPT persona","structuring multi-step prompts",
"prompt chaining for workflows","building a prompt library","reducing AI hallucinations",
"few-shot prompting examples","zero-shot prompting practice","using system prompts effectively",
"comparing prompt frameworks","debugging a weak prompt","building role-based prompts",
"prompt testing and iteration","using AI for brainstorming","using AI for summarization",
"using AI for translation tasks","using AI as a research assistant","using AI for structured data output",
"prompt engineering for coding tasks","building reusable prompt templates",
"using AI for meeting summaries","using AI as a devil's advocate reviewer","building an AI writing style clone",
"using AI for decision-tree exploration","using AI for interview simulation","chaining prompts for a research pipeline",
"using AI for competitive teardown research","using AI to generate synthetic test data","using AI for tone-shifting existing copy"]
items = []
for t in topics:
    items.append((f"{t.title()} Guide","RTF",
        f"Act as a prompt engineering expert. Explain the key principles behind {t}, then give me 3 example prompts I can adapt for my own use, along with a short explanation of why each works."))
add("AI & Prompt Engineering", items)

# ---------- 16. Language & Text Generation ----------
# Creative writing
items = []
creative_topics = ["a young woman who discovers a magical portal in her attic","a lighthouse keeper who receives mysterious letters",
"a detective solving a crime in a city where it never stops raining","a child who can talk to animals for one day only",
"two rival chefs forced to cook together","a robot experiencing its first snowfall","an astronaut stranded alone on a quiet moon base",
"a small town where everyone shares one dream each night"]
for t in creative_topics:
    items.append((f"Short Story: {t.split(' ')[0].title()} Prompt","CRISPE",
        f"Write a short story (under 800 words) about {t}. Establish a clear tone, a vivid setting, and an ending that resolves the central tension in a satisfying way."))
add("Language & Text Generation", items)

# summarization
items = []
sum_topics = ["a news article on climate change","a research paper's methodology and findings","a long email thread into one clear update",
"a legal contract into plain-language bullet points","a book chapter into a 5-sentence recap","a meeting transcript into action items",
"a technical whitepaper for a non-technical audience","a podcast episode into key takeaways"]
for t in sum_topics:
    items.append((f"Summarize {t.title()}","TAG",
        f"Task: summarize {t}. Action: identify the 3-5 most important points and remove redundant detail. Goal: produce a concise, accurate summary someone could read in under a minute."))
add("Language & Text Generation", items)

# translation
items = []
tr_topics = ["a short paragraph from English to Spanish","a product description from English to French while preserving marketing tone",
"a formal business email from English to Japanese with appropriate honorifics","a casual conversation from English to German",
"a poem from English to Italian while preserving rhythm where possible","a set of instructions from English to Portuguese for clarity"]
for t in tr_topics:
    items.append((f"Translate {t.title()}","RTF",
        f"Act as a professional translator. Translate {t}, preserving meaning, tone, and any culturally specific nuance rather than translating word-for-word."))
add("Language & Text Generation", items)

# dialogue / conversational
items = []
dlg_topics = ["a friendly chatbot helping a user troubleshoot a computer that won't turn on","a customer support agent handling a refund request calmly",
"a study buddy quizzing a student on flashcards","a travel assistant helping someone plan a weekend trip",
"a debate partner arguing the opposing side of a topic respectfully","a job-interview simulator asking follow-up questions"]
for t in dlg_topics:
    items.append((f"Dialogue Simulation: {t.split(' a ')[-1].title() if ' a ' in t else t.title()}","RISEN",
        f"Act as {t}. Stay in character, ask clarifying questions when needed, and keep responses natural and conversational rather than robotic."))
add("Language & Text Generation", items)

# ---------- 17. Question Answering ----------
items = []
open_q = ["Explain the concept of quantum computing and its potential impact on the future of technology",
"Explain how blockchain works and where it's actually useful versus overhyped",
"Explain the causes and consequences of inflation in simple terms",
"Explain how vaccines train the immune system",
"Explain the basics of behavioral economics with everyday examples"]
for t in open_q:
    items.append((f"Open-Ended Explainer: {t.split(' ')[2].title()}","RODES",
        f"{t}. Assume the reader has no technical background, use a real-world analogy, and keep the explanation under 300 words."))
add("Question Answering", items)

items = []
specific_q = ["What are the main causes of deforestation according to the source I provide",
"What are the key differences between two given frameworks or approaches",
"What year did a specific historical event occur, and what led up to it",
"What are the eligibility requirements for a specific program I describe",
"What is the correct formula or method for a specific calculation I describe"]
for t in specific_q:
    items.append((f"Targeted Answer: {t.split(' ')[3].title()}","CARE",
        f"Based only on the context or source text I provide, answer precisely: {t}. If the source doesn't contain the answer, say so rather than guessing."))
add("Question Answering", items)

items = []
mc_q = ["Who wrote a specific well-known novel, given four author options",
"Which historical figure is associated with a specific invention, given four options",
"Which programming language is best suited for a specific use case, given four options",
"Which economic theory best explains a specific scenario, given four options"]
for t in mc_q:
    items.append((f"Multiple Choice Reasoning: {t.split(' ')[0]}","STAR",
        f"{t}. Walk through why each option is right or wrong before giving the final answer, so the reasoning is transparent."))
add("Question Answering", items)

items = []
hyp_q = ["What would happen if humans could travel at the speed of light",
"What would change if every car on Earth were replaced by a self-driving electric vehicle overnight",
"What would happen to the global economy if a universal basic income were introduced",
"What would change about cities if remote work became permanent for 80% of office jobs",
"What would happen if a major ocean current stopped circulating"]
for t in hyp_q:
    items.append((f"Hypothetical Scenario: {t.split(' ')[3].title()}","CRISPE",
        f"{t}? Reason through the first, second, and third-order effects step by step before summarizing the most likely outcomes."))
add("Question Answering", items)

items = []
op_q = ["Do you believe artificial intelligence will eventually surpass human intelligence, and why or why not",
"Is remote work better for productivity than in-office work, and what does the evidence suggest",
"Should social media platforms be regulated more strictly, and what are the tradeoffs",
"Is a four-day work week a net positive for most industries, and what's the counter-argument"]
for t in op_q:
    items.append((f"Balanced Opinion Analysis: {t.split(' ')[2].title()}","PESTLE",
        f"{t}? Present the strongest arguments on both sides before giving a reasoned, clearly-labeled perspective, so I can see the full picture rather than just one side."))
add("Question Answering", items)

# ---------- Additional Code Generation prompts (extends Coding & Development) ----------
items = []
code_extra = [
    ("Code Completion", "Write a function to calculate the factorial of a given number in [language], with a partial snippet I provide as the starting point."),
    ("Code Translation", "Translate this code snippet from [source language] to [target language], preserving functionality, idioms, and readability rather than a literal line-by-line port."),
    ("Code Optimization", "Analyze this code for performance bottlenecks and suggest specific optimizations, explaining the expected impact of each change."),
    ("Code Debugging", "Here is code that throws an error. Identify the root cause, explain why it happens, and show the corrected version with a brief explanation."),
    ("Code Explanation Line-by-Line", "Explain this unfamiliar code line by line in plain language, calling out any non-obvious logic or edge cases."),
    ("Test Generation", "Write a comprehensive set of unit tests for this function, covering typical inputs, edge cases, and invalid inputs."),
    ("API Design Review", "Review this API design for consistency, naming, and RESTful best practices, and suggest improvements."),
]
for title, prompt in code_extra:
    items.append((title, "RTF", f"Act as a senior software engineer. {prompt}"))
add("Coding & Development", items)

# ---------- 18. Image Generation (safe, non-identity, no real people) ----------
items = []
photoreal = [
    "a sunset over the ocean with palm trees silhouetted against the sky",
    "a misty pine forest at dawn with sunlight breaking through the trees",
    "a cozy mountain cabin interior with a crackling fireplace on a snowy night",
    "a bustling farmers market stall piled with fresh produce in soft morning light",
    "a vintage motorcycle parked on a cobblestone street in an old European town",
    "a steaming bowl of ramen on a wooden table with chopsticks and soft steam rising",
    "a modern minimalist kitchen with marble countertops and warm pendant lighting",
    "a field of lavender stretching toward distant purple mountains at golden hour",
]
for t in photoreal:
    items.append((f"Photorealistic Scene: {t.split(' ')[1].title()}","CARE",
        f"Generate a photorealistic image of {t}. Specify natural lighting, realistic textures, and a believable depth of field, avoiding an overly artificial or plastic look."))
add("Image Generation", items)

items = []
artistic = [
    "an impressionist painting of a bustling city street with people walking under umbrellas in the rain",
    "a Japanese ukiyo-e style print of a wave crashing against a rocky shore",
    "an Art Deco poster of a train arriving at a grand 1920s station",
    "a watercolor illustration of a quiet countryside cottage surrounded by wildflowers",
    "a cyberpunk-style neon cityscape at night with rain-slicked streets",
    "a Studio Ghibli-inspired scene of a floating island with a small windmill",
]
for t in artistic:
    items.append((f"Artistic Style Image: {t.split(' ')[2].title()}","CRISPE",
        f"Generate an image in the style of {t}. Specify the art movement or technique clearly, along with color palette and mood, so the style comes through distinctly."))
add("Image Generation", items)

items = []
abstract = [
    "the concept of hope, using bright colors and flowing shapes",
    "the feeling of nostalgia, using muted tones and soft blurred forms",
    "the idea of connection, using interwoven lines and geometric patterns",
    "the concept of chaos transforming into order, using contrasting textures",
    "the passage of time, using layered translucent shapes and gradients",
]
for t in abstract:
    items.append((f"Abstract Concept Image: {t.split(',')[0].title()}","AIDA",
        f"Generate an abstract image representing {t}. Focus on composition, color theory, and emotional tone rather than literal or figurative representation."))
add("Image Generation", items)

items = []
editing = [
    "changing the background of a landscape photo to a starry night sky with a full moon",
    "removing a distracting object from a product photo and filling the space naturally",
    "converting a daytime street photo into a realistic golden-hour version",
    "adding realistic rain and reflections to an outdoor scene photo",
    "upscaling a low-resolution image while preserving natural detail and texture",
    "recoloring a room photo to show a different wall paint color realistically",
]
for t in editing:
    items.append((f"Image Editing Task: {t.split(' ')[0].title()}","TAG",
        f"Task: {t}. Action: describe the exact change needed while keeping everything else in the image untouched. Goal: a seamless, realistic edit with no visible artifacts."))
add("Image Generation", items)

# ---------- Additional Prompt Engineering Strategy prompts (extends AI & Prompt Engineering) ----------
items = []
strategy_extra = [
    ("Zero-Shot Prompting Practice", "Give me a direct instruction (no examples) for [task], and explain why zero-shot works well for this kind of task versus few-shot."),
    ("Few-Shot Example Design", "Help me design 3 strong input-output example pairs to teach the AI a consistent style or format for [task], before it sees the real prompt."),
    ("Chain-of-Thought Prompt Design", "Rewrite this prompt to explicitly ask the AI to reason step by step before giving a final answer, for [task]."),
    ("Zero-Shot Chain-of-Thought", "Show me how to add a simple 'let's think step by step' style instruction to a zero-shot prompt for [task], and explain when this technique helps most."),
    ("Prompt Specificity Audit", "Review this vague prompt and rewrite it to be specific: define the desired length, format, audience, and tone explicitly."),
    ("Multi-Turn Conversation Design", "Help me design a multi-turn prompt flow for [task] where the AI asks clarifying questions before producing a final output."),
    ("Prompt Format Comparison", "Compare how [task] performs with a natural-language question versus a structured, field-based prompt, and recommend which to use."),
]
for title, prompt in strategy_extra:
    items.append((title, "RTF", f"Act as a prompt engineering coach. {prompt}"))
add("AI & Prompt Engineering", items)

# ---------- 19. Resume Writing & ATS Optimization ----------
items = [
    ("Professional Summary Enhancement", "CARE",
     "Generate a compelling professional summary for a marketing professional with 5 years of experience in digital marketing, highlighting success in driving online engagement and lead generation. Adapt the same approach for other professions and experience levels."),
    ("Skill Highlighting", "TAG",
     "Craft a list of key skills for a software developer resume, focusing on programming languages (such as Python and JavaScript), software development methodologies (such as Agile and Scrum), and relevant tools (such as Git and Docker)."),
    ("Achievement Bullet Points", "STAR",
     "Generate achievement-oriented bullet points for a sales manager's resume, highlighting accomplishments like exceeding sales targets, leading successful client negotiations, and implementing strategies that resulted in revenue growth."),
    ("Industry-Specific Buzzwords", "RTF",
     "Create industry-specific buzzwords and phrases suitable for a finance professional's resume, emphasizing expertise in financial analysis, risk management, and compliance with regulatory standards."),
    ("Project Descriptions", "STAR",
     "Draft concise project descriptions for an IT project manager's resume, showcasing successful project implementations, budget management, team leadership, and stakeholder communication."),
    ("Education and Certifications Optimization", "TAG",
     "Optimize the education and certifications section of a healthcare professional's resume, including relevant degrees, licenses, certifications (such as CPR certification), and ongoing professional development activities."),
    ("Personal Statement Refinement", "CARE",
     "Refine the personal statement section of a recent graduate's resume, emphasizing passion for the industry, relevant experiences from internships or projects, and career aspirations aligned with a company's mission."),
    ("ATS Resume Fixer", "RTF",
     "Make my resume pass [Job Title] computer screening by adding exact keywords from the job posting. Remove fancy formatting that blocks scanning software. Use simple bullet points and standard section names. Apply the 2-page rule and show which file format works best.\n\nJob description: [Paste or attach Job Description]\nMy resume: [Paste or attach Resume]"),
    ("Results-Based Bullet Writer", "STAR",
     "Change my [Job Title] job duties into impressive results using the PAR method (Problem-Action-Result). Show how I solved problems, saved money, or improved processes. Write a comparison showing weak versus strong bullet examples.\n\nMy resume: [Paste or attach Resume]\nTarget role: [Paste or attach Job Description]"),
    ("Value Proposition Summary", "AIDA",
     "Write an opening summary for [Role] using the 30-second rule that makes recruiters want to read more. Start with years of experience and the biggest career achievement. Include key skills and clear career goals. Write 3 different versions for various experience levels and rate their appeal.\n\nMy resume: [Paste or attach Resume]\nJob target: [Paste or attach Job Description]"),
    ("Skills Hierarchy Builder", "TAG",
     "List my abilities for [Job Title] using the T-shaped skills model in order of what employers value most. Separate hard skills from soft skills. Remove old skills that would lower my chances, and add new ones from job trends. Show which skills match perfectly with job requirements.\n\nMy resume: [Paste or attach Resume]\nJob needs: [Paste or attach Job Description]"),
    ("Leadership Impact Showcase", "STAR",
     "Show my leadership wins for [Role Level] using the STAR method, including team sizes led and results achieved. Add examples of developing people and improving team performance. Create stories that prove I can handle bigger leadership roles.\n\nMy resume: [Paste or attach Resume]\nTarget job: [Paste or attach Job Description]"),
    ("Career Pivot Helper", "CRISPE",
     "Connect my work from [Current Field] to [New Industry] using the transferable skills bridge by showing how my skills solve their common problems. Research what challenges the new field faces and explain my relevant experience. Add learning steps that show a serious commitment to career change.\n\nMy resume: [Paste or attach Resume]\nNew goal: [Paste Target Role]"),
    ("Education ROI Maximizer", "CARE",
     "Format my educational details for [Career Stage] using the relevance filter, highlighting courses and projects that fit job needs. Include active certifications and ongoing learning. Connect academic work to real business value.\n\nMy resume: [Paste or attach Resume]\nRole focus: [Paste or attach Job Description]"),
    ("Job Gap Builder", "STAR",
     "Write a positive explanation for my work break between [Start Date] and [End Date] using the growth story framework, focusing on learning and development. Include volunteer work, courses taken, or projects completed during time off.\n\nMy timeline: [Paste Work History]\nTarget position: [Paste or attach Job Description]"),
    ("Multi-Target Resume Creator", "RISEN",
     "Create one resume template that works well for [Job A], [Job B], and [Job C] using the core-flex approach by finding shared requirements. Build sections that highlight different strengths for each job type. Include easy customization steps and a quick change checklist for different applications.\n\nMy resume: [Paste or attach your Resume]\nJob options: [Paste 3 Job Descriptions]"),
    ("Project Portfolio Builder", "STAR",
     "List my important projects for [Industry] using the impact storytelling method, showing goals set, work done, and results delivered. Include my exact role, tools used, and business impact created. Add teamwork examples and creative solutions found.\n\nMy projects: [Paste Project List]\nJob requirements: [Paste or attach Job Description]"),
    ("Full ATS Resume Rewrite Walkthrough (Multi-Step)", "RISEN",
     "Run a full multi-turn resume rewrite as an expert resume writer, one step at a time, waiting for my replies between steps:\n"
     "1) Adopt the persona of an expert resume writer experienced with FAANG hiring.\n"
     "2) Confirm the task: write a strong ATS-friendly resume proving I'm the best candidate, using the resume and job description I'll share. Don't edit yet.\n"
     "3) Set guardrails: never invent experience or results, avoid em dashes, and ask clarifying questions first.\n"
     "4) Pull major accomplishments from my performance reviews that fit the resume.\n"
     "5) Flag which of my existing bullet points read as tasks rather than accomplishments.\n"
     "6) Suggest ways to add measurable results or outcomes to weak bullet points.\n"
     "7) Suggest realistic metrics I could add to specific bullet points, then offer 2-3 stronger variations of each.\n"
     "8) Write an ATS- and human-readable skills section based on the updated resume.\n"
     "9) Write a 3-line objective statement from my top achievements and career goal, then tighten it further.\n"
     "10) Write a professional summary under three lines from my work experience, then tighten it further.\n"
     "11) Finally, roleplay as a modern ATS trained on Greenhouse/Lever/Taleo-style filtering logic: critically assess whether the finished resume would be shortlisted against the job description, give a yes/no verdict, and list at least 10 specific red or yellow flags if it would not be shortlisted."),
    ("Personality-Driven Resume Builder Workflow", "RISEN",
     "Run a two-phase resume-building session:\n\n"
     "PHASE 1 — Understanding Yourself:\n"
     "1) Ask me 10 questions about how I approach problems, teamwork, and deadlines, then summarize my professional working style in three lines.\n"
     "2) Take all my achievements, projects, and work experiences I share and store them as my base resume data set.\n\n"
     "PHASE 2 — Building the Resume:\n"
     "3) Adopt the persona of an expert resume writer who helps early-career professionals land roles at top companies, writing in a confident, human tone.\n"
     "4) From the job description I share, identify the 20 keywords and competencies my resume should reflect.\n"
     "5) Rewrite my bullet points from the base data set to naturally include those keywords without sounding forced.\n"
     "6) Review the draft against the job description and flag weak or unclear areas, suggesting ways to make achievements more measurable.\n\n"
     "BONUS — Resume Clusters: from the same base data set, create three tailored resume versions for three different target roles, each highlighting the most relevant achievements and skills for that role."),
]
add("Resume Writing & ATS Optimization", items)

# flatten into final list
out = []
pid = 1
for cat, items in data.items():
    for title, framework, prompt in items:
        out.append({
            "id": pid,
            "category": cat,
            "title": title,
            "framework": framework,
            "prompt": prompt
        })
        pid += 1

print("Total prompts:", len(out))
print("Categories:", list(data.keys()))
for cat, items in data.items():
    print(cat, len(items))

with open("prompts.json", "w") as f:
    json.dump(out, f, indent=2)
