# Cascade 🌊
Cascade is a simple nad lightweight LLM chain builder. It aims at providing:
- Customizable feedback loops for each link of a given link
- High abstraction for maximal flexibility
- Template based chain creation for non programmatic users
- And most importantly a simple and intuitive API

## Get started ! 🏎️

### Chains
Chains are the backbone of Cascade. They are the main object you'll be using to build your LLM chains.
```python
from cascade import Chain
TBC
```
### Conversations
Conversations are simply a list of messages. Alternating between either ```system```, ```assistant``` or ```user``` messages.  They are the main input and output of most building blocks.

### Links
Links are atomic generation steps in the chain. They most often correspond to a single message in a conversation. They are responsible for designing, executing and verifying the output of a given step.
```python

```

### Constraints
Constraints are atomic verification steps that are run against a link output. Constraint are able to issue feedback back to the link to allow the generation steps to be effectively retried until the constraint is satisfied.

### Executors
Executors simply are abstractions of LLM/generative models.

### Super chains
Super chains allow to piece together multiple chains into a single one. This is useful to create complex chains that would otherwise be hard to design. They can be used to create forks (to enable parallel executions for instance), or convergence points (where we merge multiple chain output into one)


## Contribute 🤝

You'll need:
- Python 3.11+
- poetry
- pre-commit

```bash
poetry install
pre-commit install
```
