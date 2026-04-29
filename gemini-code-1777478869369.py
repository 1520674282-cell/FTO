import openai # 或使用其他 LLM SDK

def distill_technical_features(text):
    prompt = f"""
    你是一名资深专利代理人。请阅读以下技术方案，并提取用于专利检索的关键信息：
    1. 核心技术关键词（中英文对照，5-10个）
    2. 预测可能的 IPC 分类号（前3位）
    3. 技术特征分解（Feature Breakdown）

    技术方案：{text}
    """
    # 模拟 LLM 调用
    response = client.chat.completions.create(
        model="gemini-1.5-flash", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content