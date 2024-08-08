from xagent import XAgent, XAgentClient, XAgentEvalConfig
from xagent.tools import XSerpGoogleSearch

# Modified function to initialize the XAgent
def xagent_factory():
    # Initialized XAgent with required configurations
    xagent = XAgent(
        model_name="gpt-3.5-turbo",
        temperature=0,
        tools=[XSerpGoogleSearch()],
        system_message="Your system message here",
        output_parser="Your output parser here",
        max_iterations=5,
        verbose=True,
        handle_parsing_errors="Check your output and make sure it conforms!"
    )
    return xagent

# Initialized the agent
agent = xagent_factory()

# Initialized the client using XAgent's client class
client = XAgentClient()

# Evaluation configuration using XAgent's configuration class
eval_config = XAgentEvalConfig(
    evaluators=[
        "qa",
        XAgentEvalConfig.Criteria("helpfulness"),
        XAgentEvalConfig.Criteria("conciseness"),
    ],
    input_key="input",
    eval_llm=XAgent(model_name="gpt-3.5-turbo", temperature=0.5),
)

# Running evaluation on the dataset with XAgent
chain_results = client.run_on_dataset(
    dataset_name="test-dataset",
    llm_or_chain_factory=xagent_factory,
    evaluation=eval_config,
    concurrency_level=1,
    verbose=True,
)