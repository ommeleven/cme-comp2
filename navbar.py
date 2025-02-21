import streamlit as st

def show_navbar():
    st.markdown("""
    <style>
    /* Hide Streamlit's default menu */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .top-nav {
        background: #1a1a1a;
        overflow: hidden;
        padding: 5px 20px;
        position: relative;  /* Changed from fixed to relative */
        z-index: 999;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 20px;  /* Added margin to move navbar down */
    }

    /* Gradient border effect */
    .gradient-border {
        position: relative;
        border-radius: 0 0 15px 15px;
        background: #1a1a1a;
        padding: 5px 20px;
    }

    .gradient-border::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, 
            #4285f4 0%, 
            #34a853 25%, 
            #fbbc05 50%, 
            #ea4335 75%,
            #4285f4 100%);
    }

    .nav-links {
        display: flex;
        align-items: center;
    }

    .nav-buttons {
        display: flex;
        gap: 10px;
    }

    .top-nav a {
        display: inline-flex;
        align-items: center;
        color: rgba(255, 255, 255, 0.95);
        text-align: center;
        padding: 16px 24px;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        margin: 0 5px;
        border-radius: 8px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }

    .top-nav a:hover {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }

    .nav-button {
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 8px;
    }

    .deploy-button {
        background-color: #1a1a1a;
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .deploy-button:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }

    .main-content {
        background: #1a1a1a;
        min-height: 100vh;
        color: white;
        padding: 20px;
    }

    /* Responsive design */
    @media screen and (max-width: 768px) {
        .top-nav {
            flex-direction: column;
            padding: 10px;
        }
        
        .nav-links, .nav-buttons {
            flex-direction: column;
            width: 100%;
        }
        
        .top-nav a {
            width: 100%;
            margin: 5px 0;
        }
        
        .nav-button {
            width: 100%;
            margin: 5px 0;
            text-align: center;
            justify-content: center;
        }
    }
    </style>

    <div class="gradient-border">
        <div class="top-nav">
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/dashboard">Dashboard</a>
                <a href="/analytics">Analytics</a>
            </div>
            <div class="nav-buttons">
                <a href="/deploy" class="nav-button deploy-button">
                    Deploy
                </a>
            </div>
        </div>
    </div>

    <div class="main-content">
        <!-- Your page content goes here -->
    </div>
    """, unsafe_allow_html=True)

def main():
    show_navbar()
    
    # Get the current page from the URL query parameters
    query_params = st.experimental_get_query_params()
    current_page = query_params.get("page", ["home"])[0]
    
    # Display content based on current page
    if current_page == "home":
        st.title("Welcome to Home")
    elif current_page == "dashboard":
        st.title("Dashboard")
    elif current_page == "analytics":
        st.title("Analytics")

if __name__ == "__main__":
    main()