from app.gcp_settings import db
from app.utils.data_enum import RootCollection, UserField


def add_user_analization(
    user_id: str,
    personality: str,
    strength: str,
    weakness: str,
) -> tuple[str, str]:
    """ユーザーの性格・強み・弱みをDBに保存"""
    user_ref = db.collection(RootCollection.user.value).document(user_id)
    user_dict = user_ref.get().to_dict()

    user_dict[UserField.personality.value] = personality
    user_dict[UserField.strength.value] = strength
    user_dict[UserField.weakness.value] = weakness

    user_ref.set(user_dict)
    print(f"User Personality and Strength and Weakness added to User: {user_id}")