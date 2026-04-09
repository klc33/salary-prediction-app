from src.db.supabase_client import supabase

def save_prediction(data: dict):
    response = supabase.table("predictions").insert(data).execute()
    return response