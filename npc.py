from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

from agents.memory_agent import MemoryAgent
from agents.personality_agent import PersonalityAgent
from agents.decision_agent import DecisionAgent

client = OpenAI(api_key=OPENAI_API_KEY)

class NPC:
    def __init__(self, name="NPC"):
        self.name = name
        self.memory = MemoryAgent()
        self.personality = PersonalityAgent("傲娇")
        self.decision = DecisionAgent()

    def respond(self, player_input):
        memories = self.memory.search(player_input)
        action = self.decision.decide(player_input)

        prompt = f"""
NPC: {self.name}

性格: {self.personality.style_prompt()}
记忆: {memories}
玩家: {player_input}
状态: {action}

生成自然回复：
"""

        res = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9
        )

        reply = res.choices[0].message.content

        self.memory.add_memory(player_input)
        self.memory.add_memory(reply)

        return reply
