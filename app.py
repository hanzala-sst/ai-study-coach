import streamlit as st
from ai_engine import generate_study_plan

st.set_page_config(page_title="AI Study Coach", layout="centered", initial_sidebar_state="collapsed")

# --- HEADER SECTION ---
st.title("🎓 AI Study Coach")
st.markdown("### Your Personal AI Mentor for Success")
st.info("💡 This AI doesn't wait for prompts — it understands you.")
st.divider()

# Step navigation
if "step" not in st.session_state:
    st.session_state.step = 1

if "file_data" not in st.session_state:
    st.session_state.file_data = None

# STEP 1
if st.session_state.step == 1:
    with st.container(border=True):
        st.subheader("🎯 Step 1: What is your goal?")
        goal = st.selectbox("Choose your goal", ["Crack Your Exam", "Improve weak subjects", "Revise syllabus"])

        if st.button("Next", type="primary", use_container_width=True):
            st.session_state.goal = goal
            st.session_state.step = 2
            st.rerun()

# STEP 2
elif st.session_state.step == 2:
    with st.container(border=True):
        st.subheader("📄 Step 2: Upload study material or previous test results (Optional)")
        
        uploaded_file = st.file_uploader("Upload an image (JPG/PNG) or PDF", type=["jpg", "png", "pdf"])
        
        if st.button("Next", type="primary", use_container_width=True):
            if uploaded_file is not None:
                # Placeholder text extraction logic
                st.session_state.file_data = f"[Extracted content from {uploaded_file.name}]"
                st.toast("File processed successfully!", icon="✅")
            else:
                st.session_state.file_data = None
            
            st.session_state.step = 3
            st.rerun()

# STEP 3
elif st.session_state.step == 3:
    with st.container(border=True):
        st.subheader("📝 Step 3: Tell us about your preparation")

        col1, col2 = st.columns(2)
        with col1:
            exam = st.selectbox("Target Exam", ["JEE", "NEET", "Boards"])
        with col2:
            hours = st.slider("Study hours per day", 1, 12, 4)
            
        confidence = st.slider("Confidence level (1 = Low, 10 = High)", 1, 10, 5)

        if st.button("Analyze My Preparation", type="primary", use_container_width=True):
            st.session_state.exam = exam
            st.session_state.hours = hours
            st.session_state.confidence = confidence
            st.session_state.step = 4
            st.rerun()

# STEP 4 (AI)
elif st.session_state.step == 4:
    with st.spinner("Analyzing your preparation..."):
        file_info = f"Extracted Data: {st.session_state.file_data}" if st.session_state.file_data else "Extracted Data: None provided"

        user_input = f"""
        Goal: {st.session_state.goal}
        Exam: {st.session_state.exam}
        Hours: {st.session_state.hours}
        Confidence: {st.session_state.confidence}
        {file_info}
        """

        if "study_plan_result" not in st.session_state:
            st.session_state.study_plan_result = generate_study_plan(user_input)

    result = st.session_state.study_plan_result

    if "### Study Plan" in result:
        parts = result.split("### Study Plan")
        analysis_part = parts[0].replace("### AI Analysis", "").strip()
        plan_part = parts[1].strip()
        
        with st.container(border=True):
            st.subheader("🧠 AI Analysis")
            st.markdown(analysis_part)
        
        with st.container(border=True):
            st.subheader("📊 Your Study Plan")
            st.markdown("### Study Plan\n" + plan_part)
    else:
        with st.container(border=True):
            st.subheader("🧠 AI Analysis & Study Plan")
            st.markdown(result)

    st.divider()

    # --- WEAKNESS SECTION ---
    st.subheader("🔍 Understand Your Weakness")
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            weak_subject = st.selectbox(
                "Select a subject to analyze:",
                ["Physics", "Chemistry", "Mathematics"],
                label_visibility="collapsed"
            )
        with col2:
            explain_btn = st.button("Explain My Weakness", use_container_width=True)

        # Initialize state
        if "weakness_explanation" not in st.session_state:
            st.session_state.weakness_explanation = None

        if "weakness_loading" not in st.session_state:
            st.session_state.weakness_loading = False

        # Button click
        if explain_btn:
            st.session_state.weakness_loading = True
            st.session_state.weakness_explanation = None

        # Run AI when loading
        if st.session_state.weakness_loading:
            with st.spinner(f"Analyzing {weak_subject} weakness..."):
                from ai_engine import client

                prompt = f"""
You are an elite AI Study Coach.

Student Data:
{user_input}

Focus only on the subject: {weak_subject}

Explain in depth:
1. Why the student is weak
2. Conceptual gaps
3. Common mistakes
4. Step-by-step improvement
5. What to STOP doing
"""

                models_to_try = [
                    "models/gemini-2.5-flash",
                    "models/gemini-flash-latest",
                    "models/gemini-pro-latest"
                ]

                explanation = None

                for model_name in models_to_try:
                    try:
                        response = client.models.generate_content(
                            model=model_name,
                            contents=prompt,
                        )
                        explanation = response.text
                        break
                    except Exception:
                        continue

                st.session_state.weakness_explanation = explanation or "⚠️ AI busy. Try again."
                st.session_state.weakness_loading = False

        # Show result
        if st.session_state.weakness_explanation:
            st.markdown("---")
            st.subheader("📌 Weakness Explanation")
            st.markdown(st.session_state.weakness_explanation)
            st.success("Analysis complete!", icon="✅")

    st.divider()

    # --- NEW FEATURE: UPDATE MY PROGRESS ---
    st.subheader("📈 Update Your Progress")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            progress_hours = st.slider("Hours studied today", 0, 12, 4)
        with col2:
            progress_subject = st.selectbox("Which subject did you focus on?", ["Physics", "Chemistry", "Mathematics"], key="prog_subj")
            
        progress_difficulty = st.text_area("What difficulty did you face today?", placeholder="e.g. Struggled with Thermodynamics formulas")

        if "progress_feedback" not in st.session_state:
            st.session_state.progress_feedback = None

        if "progress_loading" not in st.session_state:
            st.session_state.progress_loading = False

        if st.button("Update My Plan", use_container_width=True):
            st.session_state.progress_loading = True
            st.session_state.progress_feedback = None

        if st.session_state.progress_loading:
            with st.spinner("Updating your study plan..."):
                from ai_engine import client
                
                prompt = f"""
You are an elite AI Study Coach.

Student's Original Data:
{user_input}

Today's Progress:
- Hours studied today: {progress_hours}
- Subject focused on: {progress_subject}
- Difficulties faced: {progress_difficulty}

Please generate an updated progress report:
1. Updated study plan for tomorrow
2. Adjusted priorities
3. What to improve tomorrow
4. Mistakes in today's approach
"""

                models_to_try = [
                    "models/gemini-2.5-flash",
                    "models/gemini-flash-latest",
                    "models/gemini-pro-latest"
                ]

                feedback = None
                for model_name in models_to_try:
                    try:
                        response = client.models.generate_content(
                            model=model_name,
                            contents=prompt,
                        )
                        feedback = response.text
                        break
                    except Exception:
                        continue

                st.session_state.progress_feedback = feedback or "⚠️ AI busy. Try again."
                st.session_state.progress_loading = False

        if st.session_state.progress_feedback:
            st.markdown("---")
            st.subheader("🔄 Updated Plan & Feedback")
            st.markdown(st.session_state.progress_feedback)
            st.success("Plan updated successfully!", icon="✅")

    st.divider()

    # --- NEW FEATURE: INSTANT ACTION MODE ---
    st.subheader("⚡ Instant Action Mode")
    with st.container(border=True):
        if "instant_action" not in st.session_state:
            st.session_state.instant_action = None

        if "instant_loading" not in st.session_state:
            st.session_state.instant_loading = False

        if st.button("What Should I Do Right Now?", type="primary", use_container_width=True):
            st.session_state.instant_loading = True
            st.session_state.instant_action = None
            
        if st.session_state.instant_loading:
            with st.spinner("Finding the best task for you right now..."):
                from ai_engine import client
                
                # Incorporate progress if available
                progress_context = ""
                if st.session_state.get("progress_feedback"):
                    progress_context = f"\nLatest Progress:\n- Hours studied today: {progress_hours}\n- Subject focused on: {progress_subject}\n- Difficulties faced: {progress_difficulty}"
                
                prompt = f"""
You are an elite AI Study Coach.

Student Data:
{user_input}{progress_context}

The student needs a VERY SPECIFIC immediate task to do RIGHT NOW.
Keep it SHORT and ACTIONABLE. No long explanations.

Output format:
### Immediate Action Plan
- Task: (Specific chapter/topic/problem)
- Duration: (e.g., 30 min, 1 hour)
- Goal: (What should be achieved)
- Why this matters: (Short reason based on student's profile)
"""
                models_to_try = [
                    "models/gemini-2.5-flash",
                    "models/gemini-flash-latest",
                    "models/gemini-pro-latest"
                ]

                action = None
                for model_name in models_to_try:
                    try:
                        response = client.models.generate_content(
                            model=model_name,
                            contents=prompt,
                        )
                        action = response.text
                        break
                    except Exception:
                        continue

                st.session_state.instant_action = action or "⚠️ AI busy. Try again."
                st.session_state.instant_loading = False

        if st.session_state.instant_action:
            st.markdown("---")
            st.subheader("🚀 Your Next Move")
            st.markdown(st.session_state.instant_action)

    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Start Over", use_container_width=True):
            st.session_state.clear()
            st.rerun()
