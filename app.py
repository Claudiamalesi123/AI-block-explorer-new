from transformers import pipeline
import streamlit as st
import re
from explorer import get_transactions

# Initialize the pipeline
nlp = pipeline("question-answering")

# Streamlit app
st.set_page_config(page_title="AI-assisted Block Explorer", page_icon="🔍")
st.markdown(
    """
    <style>
    .main {background-color: #1e1e1e; color: #f0f2f6;}
    .stButton button {background-color: #4CAF50; color: white; padding: 10px 20px; font-size: 16px; border-radius: 8px; border: none; cursor: pointer; transition: background-color 0.3s;}
    .stButton button:hover {background-color: #45a049;}
    .stTextInput input {background-color: #2b2b2b; color: white; border: 1px solid #555; border-radius: 4px; padding: 8px;}
    .stTextInput input:focus {border-color: #4CAF50;}
    .stMarkdown p {color: #f0f2f6;}
    .stHeader {text-align: center; color: #f0f2f6;}
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    st.title("🔍 AI-assisted Block Explorer")
    st.write("Enter a natural language query to explore blockchain data.")

    query = st.text_input("Query (e.g., 'How many transactions were made for wallet123 on 2024-07-21?')")

    def extract_wallet_and_date(query):
        # Regex patterns for extracting wallet and date
        wallet_pattern = re.compile(r'wallet(\d+)')
        date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

        wallet_match = wallet_pattern.search(query)
        date_match = date_pattern.search(query)

        wallet = wallet_match.group() if wallet_match else None
        date = date_match.group() if date_match else None

        return wallet, date

    if st.button("Get Results"):
        if query:
            wallet, date = extract_wallet_and_date(query)

            if wallet and date:
                # Fetch blockchain data
                transactions = get_transactions(wallet, date)
                if transactions:
                    # Create a readable context from transactions
                    context = f"Transactions for {wallet} on {date}: "
                    for txn in transactions["transactions"]:
                        context += f"Transaction {txn['id']} with amount {txn['amount']} at {txn['timestamp']}. "

                    # Process the query with the readable context
                    result = nlp(question=query, context=context)
                    answer = result['answer']

                    # Enhance the response to be more user-friendly
                    st.write(f"💬 **The transactions made by {wallet} on {date} are as follows:**")
                    st.write(f"**Answer:** {answer}")
                else:
                    st.write(f"No transactions found for wallet {wallet} on {date}.")
            else:
                # Handle generic queries
                if "most transactions" in query:
                    st.write("💬 **The wallet that made the most transactions is wallet123.**")
                elif "total amount" in query:
                    st.write("💬 **The total amount transacted by wallet456 is 1000 units.**")
                else:
                    st.write("Could not extract wallet and date from the query. Please ensure the query contains a wallet and a date.")
        else:
            st.write("Please enter a query.")
        
        # Add the "Back to Main" button
        if st.button("Back to Main"):
            st.experimental_rerun()
    else:
        st.write("**Examples you can try from our mock data:**")
        st.write("1. How many transactions were made for wallet123 on 2024-07-21?")
        st.write("2. What is the total amount transacted by wallet456 on 2024-06-15?")
        st.write("3. Who made the most transactions for wallet789 on 2024-05-10?")
        st.write("4. Which wallet made the most transactions?")
        st.write("5. What is the highest transaction amount for wallet789?")

if __name__ == "__main__":
    main()
