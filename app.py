import streamlit as st

def main():
    st.set_page_config(layout="wide")  # Enables a wider layout
    st.title("LangGraph Workflow Generator")
    
    # Ensure session state variables are initialized
    if 'download_enabled' not in st.session_state:
        st.session_state['download_enabled'] = False
    if 'workflow' not in st.session_state:
        st.session_state['workflow'] = ""
    if 'generate_disabled' not in st.session_state:
        st.session_state['generate_disabled'] = False
    
    # Top right corner download button
    col1, col2 = st.columns([0.8, 0.2])
    with col2:
        st.download_button(
            "Download as PDF", "Generated_Workflow.pdf", disabled=not st.session_state['download_enabled'], help="Download the finalized workflow"
        )
    
    # User input for workflow requirements
    user_input = st.text_area("", placeholder="Describe your workflow requirements:", height=150)
    
    if st.button("Generate Workflow", key="generate_button", help="Click to generate workflow", disabled=st.session_state['generate_disabled']):
        if user_input.strip() and not st.session_state['generate_disabled']:
            st.session_state['workflow'] = f"Generated workflow for: {user_input}"
            st.session_state['download_enabled'] = True  # Enable download after initial requirement is provided
            st.session_state['generate_disabled'] = True  # Disable generate button permanently after first click
        else:
            st.warning("Please enter your workflow requirements.")
    
    # Display generated workflow
    if st.session_state['workflow']:
        st.subheader("Generated Workflow")
        st.write(st.session_state['workflow'])
        
        # Feedback input and button aligned properly
        feedback_col1, feedback_col2 = st.columns([0.8, 0.2])
        feedback = feedback_col1.text_area("", placeholder="Provide feedback to refine the workflow:", height=80)
        
        with feedback_col2:
            if st.button("Submit Feedback", key="feedback_button", help="Submit feedback for workflow refinement"):
                if feedback.strip():
                    st.session_state['workflow'] += f"\nUser Feedback: {feedback}"
                    st.session_state['download_enabled'] = True  # Ensure download is enabled after feedback
                else:
                    st.warning("Please enter feedback before submitting.")
    
if __name__ == "__main__":
    main()