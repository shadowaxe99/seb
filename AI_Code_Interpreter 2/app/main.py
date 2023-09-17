from flask import Flask, request
from agents.agent1 import Agent1
from agents.agent2 import Agent2
from agents.agent3 import Agent3
from utils.analysis import analyze_directory
from utils.openai_api import OpenAIAPI

app = Flask(__name__)

@app.route('/interpret', methods=['POST'])
def interpret_code():
    code = request.json['code']
    agent_name = request.json['agent']
    
    if agent_name == 'agent1':
        agent = Agent1()
    elif agent_name == 'agent2':
        agent = Agent2()
    elif agent_name == 'agent3':
        agent = Agent3()
    else:
        return 'Invalid agent name'
    
    result = agent.interpret(code)
    return result

@app.route('/analyze', methods=['POST'])
def analyze_directory_endpoint():
    directory_path = request.json['directory']
    result = analyze_directory(directory_path)
    return result

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    result = OpenAIAPI.generate_text(prompt)
    return result

if __name__ == '__main__':
    app.run()