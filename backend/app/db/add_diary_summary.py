import os
from datetime import datetime

from app.gcp_settings import db
from app.utils.data_enum import DiaryCollection, DiaryField, RootCollection


def add_diary_summary(
    user_id: str,
    summary: str,
    feedback: str,
    year: int,
    month: int,
    day: int,
):
    """指定した日付の日記の 要約 + フィードバック をDBに保存

    Args:
        user_id (str): LINEユーザーID
        summary (str): LLMによる日記の要約
        feedback (str): LLMによる日記のフィードバック
    """
    date = datetime(year, month, day).strftime("%Y-%m-%d")
    collection_name = os.path.join(
        RootCollection.diary.value, user_id, DiaryCollection.diary.value
    )

    doc_ref = db.collection(collection_name).document(date)
    doc_dict = doc_ref.get().to_dict()
    doc_dict[DiaryField.summary.value] = summary
    doc_dict[DiaryField.feedback.value] = feedback
    doc_ref.set(doc_dict)
    print(f"Summary and feedback added to diary: {date}\nUserID: {user_id}")
