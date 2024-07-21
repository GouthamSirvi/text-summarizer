import streamlit as st
from preprocessing import preprocess_text
from summarization import generate_summary

def main():
    st.title('Text Summarizer Application')
    
    # Text input from user
    user_input = st.text_area("Enter text to summarize:")
    
    if st.button('Generate Summary'):
        # Preprocess the text
        preprocessed_text = preprocess_text(user_input)
        
        # Generate the summary
        summary = generate_summary(preprocessed_text)
        
        # Display the summary
        st.subheader("Summary:")
        st.write(summary)

if __name__ == "__main__":
    main()
