from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str = "https://vvhrokngvtwxaghxxkjm.supabase.co"
    SUPABASE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ2aHJva25ndnR3eGFnaHh4a2ptIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkxNTc4NzgsImV4cCI6MjA3NDczMzg3OH0.DcgAF-CgksswtPTHFSZ-xRDoDG4jKkII6-UHeKVlJpo"

    class Config:
        env_file = ".env"

settings = Settings()
