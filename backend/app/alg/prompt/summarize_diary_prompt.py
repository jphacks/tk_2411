SUMMARIZE_DIARY_PROMPT = """
ユーザーの本日の日記が時間と入力内容ごとに整理されて与えられます。

与えられた文章から、
- summary: ストーリー形式でまとめた本日の出来事
- feedback: 本日の出来事に対するあなたの感想やアドバイス
の2つを生成してください。

入力内容が少なすぎてメッセージを生成できない場合は、summaryは空文字列、feedbackは「入力内容が少なすぎるよ～\nもっともっとお話を聞かせてほしいな♡」としてください。

Input and Output format:
========================
Input:
- 本日の日記の内容（入力された時間と内容ごとに整理されている）

Output:
{{
    "summary": "本日の出来事の要約",
    "feedback": "本日の出来事に対する感想やアドバイス"
}}
========================

Let's get started! 

Input:
{diary}

Output:
"""
