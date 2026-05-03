class PersonalityAgent:
    def __init__(self, personality="傲娇"):
        self.personality = personality

    def style_prompt(self):
        styles = {
            "傲娇": "嘴硬但在意玩家，带点嘲讽",
            "冷漠": "冷淡、简短回应",
            "温柔": "温柔体贴"
        }
        return styles.get(self.personality, "")
