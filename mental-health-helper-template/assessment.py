# assessment.py - 心理评估工具包

PHQ9_QUESTIONS = [
    "过去两周，有多少时间你感到做事时提不起兴趣或乐趣？",
    "过去两周，有多少时间你感到心情低落、沮丧或绝望？",
    "过去两周，有多少时间你睡眠出现问题（难以入睡/睡得太多）？",
    "过去两周，有多少时间你感到疲倦或缺乏精力？",
    "过去两周，有多少时间你食欲改变（吃太多/吃不下）？",
    "过去两周，有多少时间你觉得自己很糟、失败或让人失望？",
    "过去两周，有多少时间你注意力难以集中（如看书、看电视）？",
    "过去两周，有多少时间你动作迟缓或坐立不安（被别人注意到）？",
    "过去两周，有多少时间你有“死了更好”或伤害自己的想法？"
]

SCORING_MAP = {
    "完全没有": 0,
    "几天": 1,
    "超过一半日子": 2,
    "几乎每天": 3
}

def get_phq9_question(step):
    question = PHQ9_QUESTIONS[step]
    options = "\n".join([
        "🔘 完全没有",
        "🔘 几天",
        "🔘 超过一半日子",
        "🔘 几乎每天"
    ])
    return f"{question}\n\n请选择最符合你情况的一项：\n{options}"

def score_phq9(responses):
    total = 0
    for r in responses:
        # 提取匹配的关键词
        for key in SCORING_MAP:
            if key in r:
                total += SCORING_MAP[key]
                break
        else:
            total += 0  # 默认为0分
    
    if total >= 20:
        level = "⚠️ 重度抑郁倾向（建议立即就医）"
    elif total >= 15:
        level = "🟡 中度抑郁倾向（建议尽快咨询心理医生）"
    elif total >= 10:
        level = "🟠 轻度抑郁倾向（建议关注情绪变化）"
    else:
        level = "🟢 当前情绪状态在正常范围内"

    return total, level
