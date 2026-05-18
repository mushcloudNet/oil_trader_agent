import anthropic
import datetime
import os

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def generate_oil_report():
    today = datetime.datetime.utcnow().strftime("%B %d, %Y")

    prompt = f"""Today is {today}.

Please do the following in a single well-structured markdown report:

1. **Oil Market News** – Search the web (OilPrice.com and CNBC Oil) for the latest oil market news today. Summarize the top developments (prices, geopolitical events, supply/demand changes, OPEC updates, etc.).

2. **Technical Sentiment (Investing.com and TradingView)** – Search for Crude Oil WTI technical analysis and sentiment from Investing.com and TradingView. Report the signals across timeframes (1min, 5min, 15min, 30min, hourly, daily, weekly, monthly) — whether they show Strong Buy, Buy, Neutral, Sell, or Strong Sell. Include key indicator readings (RSI, MACD, Moving Averages) if available.

3. **Summary & Outlook** – Provide a brief combined outlook based on the news and technical signals.

Format the report cleanly in markdown with headers, tables where appropriate, and bullet points. Be concise and professional.
"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract text from response
    report_text = ""
    for block in response.content:
        if block.type == "text":
            report_text += block.text

    return report_text


def save_report(report_text):
    today_str = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    filename = f"reports/oil_report_{today_str}.md"

    os.makedirs("reports", exist_ok=True)

    header = f"""# 🛢️ Oil Market Report — {datetime.datetime.utcnow().strftime("%B %d, %Y")}
*Generated automatically via Claude AI + Web Search*

---

"""
    with open(filename, "w") as f:
        f.write(header + report_text)

    print(f"✅ Report saved to {filename}")
    return filename


if __name__ == "__main__":
    print("🔍 Fetching oil news and technical sentiment...")
    report = generate_oil_report()
    save_report(report)
