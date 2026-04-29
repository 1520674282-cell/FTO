def analyze_fto_risk(target_tech, candidate_patent):
    claims = candidate_patent['claims']
    patent_id = candidate_patent['pn']
    
    prompt = f"""
    任务：进行 FTO（自由实施）风险侵权分析。
    目标技术方案：{target_tech}
    对比专利（{patent_id}）权利要求：{claims}

    请根据“全要素原则”分析：
    1. 目标方案是否包含了对比专利独立权利要求中的所有技术特征？
    2. 给出风险等级（高/中/低）。
    3. 给出规避设计建议（Design-around）。
    """
    # 调用 LLM 进行深度推理
    risk_report = call_llm(prompt)
    return risk_report