from fastapi import APIRouter, Depends, HTTPException
from backend.models import User
from supabase import Client
from backend.dependencies import get_supabase_client

router = APIRouter()

@router.post("/signup")
def signup(user: User, supabase: Client = Depends(get_supabase_client)):
    try:
        response = supabase.auth.sign_up({"email": user.email, "password": user.password})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return response

@router.post("/login")
def login(user: User, supabase: Client = Depends(get_supabase_client)):
    try:
        response = supabase.auth.sign_in_with_password({"email": user.email, "password": user.password})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return response
