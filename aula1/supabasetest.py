from supabase import create_client, Client

def getProfiles():

    url = "https://gwciamwzymavzshvqitu.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd3Y2lhbXd6eW1hdnpzaHZxaXR1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzQ1MDY1ODMsImV4cCI6MTk5MDA4MjU4M30.RMM_741CnTS-I-MOdZLBLv4AZCxL-M9OTB0olJ7Zrok"
    supabase: Client = create_client(url, key)

    return supabase.table('profiles').select("*").execute()