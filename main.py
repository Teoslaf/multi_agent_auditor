from textwrap import dedent
from agents import CustomAgents
from tasks import SecurityAuditTasks
from crewai import Crew
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def read_contract_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == "__main__":
    # Check if API key is loaded
    if not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY not found in .env file")
        exit(1)
        
    print("## Welcome to Smart Contract Security Audit Crew")
    print("----------------------------------------------")
    contract_path = "test.sol" 
    
    try:
        # Read contract code
        contract_code = read_contract_file(contract_path)
        
        # Initialize agents
        agents = CustomAgents()
        security_expert = agents.security_vulnerability_expert()
        business_analyst = agents.business_logic_analyzer()
        white_hat = agents.white_hat_hacker()
        doc_specialist = agents.documentation_specialist()
        
        # Initialize tasks
        tasks = SecurityAuditTasks()
        task1 = tasks.initial_vulnerability_scan(security_expert, contract_code)
        task2 = tasks.business_logic_review(business_analyst, contract_code, "#{task1.output}")
        task3 = tasks.exploit_scenario_analysis(white_hat, contract_code, "#{task1.output}\n#{task2.output}")
        task4 = tasks.final_report_compilation(doc_specialist, "#{task1.output}\n#{task2.output}\n#{task3.output}")
        
        # Create and run the crew
        crew = Crew(
            agents=[security_expert, business_analyst, white_hat, doc_specialist],
            tasks=[task1, task2, task3, task4],
            verbose=True
        )
        
        result = crew.kickoff()
        
        print("\n\n########################")
        print("## Security Audit Report:")
        print("########################\n")
        print(result)
        
    except FileNotFoundError:
        print(f"Error: Could not find contract file at {contract_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
