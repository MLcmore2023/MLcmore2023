import os

# Your data in the form of a list of dictionaries
data = [
    {
        "Session": "D1-M",
        "Lecture": "1. Introduction to AI and ML\n2. Steps in ML project",
        "Lab (up to 2 hours)": "1. Colab setup\n2. Python refresh\n3. Visualization: t-SNE",
        "TA": "Bruce"
    },
    {
        "Session": "D1-A",
        "Lecture": "1. Data preprocessing & EDA with a case study\n2. Performance evaluation",
        "Lab (up to 2 hours)": "1. Data prep: scaling, normalization, imputation\n2. Feature selection\n3. Model evaluation: classification, regression",
        "TA": "Bruce"
    },
    {
        "Session": "D2-M",
        "Lecture": "1. Model training",
        "Lab (up to 2 hours)": "1. Model tune up\n2. Bagging and Boosting\n3. Supply chain example",
        "TA": "Bruce"
    },
    {
        "Session": "D2-A",
        "Lecture": "1. Supervised learning",
        "Lab (up to 2 hours)": "1. Supervised learning",
        "TA": "Ramy"
    },
    {
        "Session": "D3-M",
        "Lecture": "1. Supervised learning",
        "Lab (up to 2 hours)": "1. Supervised learning",
        "TA": "Nathan, Ramy"
    },
    {
        "Session": "D3-A",
        "Lecture": "1. Supervised learning",
        "Lab (up to 2 hours)": "1. Supervised learning",
        "TA": "Ramy"
    },
    {
        "Session": "D4-M",
        "Lecture": "1. Deep learning",
        "Lab (up to 2 hours)": "1. Deep learning",
        "TA": "Nathan, Ramy"
    },
    {
        "Session": "D4-A",
        "Lecture": "1. Deep learning",
        "Lab (up to 2 hours)": "1. Deep learning",
        "TA": "Ramy"
    },
    {
        "Session": "D5-M",
        "Lecture": "1. Deep learning",
        "Lab (up to 2 hours)": "1. Deep learning",
        "TA": "Nathan, Ramy"
    },
    {
        "Session": "D5-A",
        "Lecture": "Evaluation",
        "Lab (up to 2 hours)": "",
        "TA": "Ramy"
    },
    {
        "Session": "D6-M",
        "Lecture": "1. Unsupervised learning",
        "Lab (up to 2 hours)": "1. PCA\n2. K-mean and cluster # optimization (elbow method)",
        "TA": "Ramy"
    },
    {
        "Session": "D6-A",
        "Lecture": "1. Unsupervised learning",
        "Lab (up to 2 hours)": "1. Hierarchical clustering\n2. Soft-clustering (expectation maximization)",
        "TA": "Ramy"
    },
    {
        "Session": "D7-M",
        "Lecture": "1. Markov decision process",
        "Lab (up to 2 hours)": "1. Standard methods for MDP such as PI and VI\n• Formulation: transition probabilities, reward, …\n• Policy evaluation",
        "TA": "Matin"
    },
    {
        "Session": "D7-A",
        "Lecture": "1. MDP\n2. Monte Carlo method",
        "Lab (up to 2 hours)": "1. PI and VI\n2. Monte Carlo method\n• Return computation\n• Generalized Policy Iteration",
        "TA": "Matin"
    },
    {
        "Session": "D8-M",
        "Lecture": "1. Tabular RL",
        "Lab (up to 2 hours)": "1. Tabular RL: Q-learning, SARSA",
        "TA": "Matin"
    },
    {
        "Session": "D8-A",
        "Lecture": "1. Deep RL",
        "Lab (up to 2 hours)": "1. Deep RL: DQN and others",
        "TA": "Matin"
    },
    {
        "Session": "D9-M",
        "Lecture": "1. Policy optimization",
        "Lab (up to 2 hours)": "1. Policy optimization: REINFORCE, DPG, DDPG",
        "TA": "Matin"
    },
    {
        "Session": "D9-A",
        "Lecture": "1. Model-based RL, MARL",
        "Lab (up to 2 hours)": "1. Dyna-Q, MARL",
        "TA": "Matin"
    },
    {
        "Session": "D10-M",
        "Lecture": "2. RL for Applications",
        "Lab (up to 2 hours)": "1. DQN for optimal maintenance, Sim2Real for robotic control",
        "TA": "Matin"
    },
    {
        "Session": "D10-A",
        "Lecture": "Evaluation",
        "Lab (up to 2 hours)": "",
        "TA": "Matin"
    }
]


# Function to create folder and write README.md in it
def create_session_folder(session_data):
    session_name = f"day{session_data['Session'][1:-2].lower()}_"
    print(session_name)
    if session_data['Session'][-1] == "M":
        session_name += "am_morning"
    else:
        session_name += "pm_afternoon"

    os.makedirs(session_name, exist_ok=True)

    readme_content = f"""\
# Session {session_data['Session']}

## Lecture
{session_data['Lecture']}

## Lab (up to 2 hours)
{session_data['Lab (up to 2 hours)']}

## TA
{session_data['TA']}
"""

    with open(os.path.join(session_name, "README.md"), "w") as readme_file:
        readme_file.write(readme_content)

# Loop through the data and create folders with README.md files
for session_data in data:
    create_session_folder(session_data)
