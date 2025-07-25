import re

# Define the math function tool
def add(a, b):
    return a + b

# Agent class to handle math queries
class MathAgent:
    def __init__(self):
        self.tools = {
            'add': add
        }
    
    def process_query(self, query):
        # Check if the query contains an addition pattern (e.g., "5 + 7")
        addition_pattern = r'(\d+)\s*\+\s*(\d+)'
        match = re.match(addition_pattern, query.replace("What is", "").strip())
        
        if match:
            num1, num2 = map(int, match.groups())
            result = self.tools['add'](num1, num2)
            return f"The result of {num1} + {num2} is {result}"
        else:
            return "Sorry, I can only handle addition queries in the format 'What is X + Y?'"

# Test the agent
def test_math_agent():
    agent = MathAgent()
    test_queries = [
        "What is 5 + 7?",
        "What is 10 + 20?",
        "What is 3 + 9?"
    ]
    
    for query in test_queries:
        print(f"Query: {query}")
        print(f"Response: {agent.process_query(query)}\n")

# Run the tests
if __name__ == "__main__":
    test_math_agent()