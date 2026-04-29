def main_fto_pipeline(doc_path):
    # Step 1: 解析文档
    raw_text = parse_document(doc_path)
    
    # Step 2: 蒸馏关键词
    distilled_data = distill_technical_features(raw_text)
    print(f"提取特征：{distilled_data}")
    
    # Step 3: 检索平台调用
    searcher = PatentSearcher(api_key="YOUR_KEY", api_secret="YOUR_SECRET")
    results = searcher.execute_search(distilled_data['keywords'], distilled_data['ipc'])
    
    # Step 4: 循环进行风险比对并生成报告
    final_reports = []
    for patent in results:
        risk_analysis = analyze_fto_risk(raw_text, patent)
        final_reports.append({
            "patent_id": patent['pn'],
            "analysis": risk_analysis
        })
    
    return final_reports