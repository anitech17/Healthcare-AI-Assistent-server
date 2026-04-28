from app.db.session import SessionLocal
from app.db.models import Doctor

db = SessionLocal()

doctors = [
    {"name": "Dr. Amit Sharma", "specialty": "Cardiologist", "experience": 12, "latitude": 19.0760, "longitude": 72.8777, "rating": 4.5, "city": "Mumbai"},
    {"name": "Dr. Neha Verma", "specialty": "Dermatologist", "experience": 8, "latitude": 19.0820, "longitude": 72.8850, "rating": 4.2, "city": "Mumbai"},
    {"name": "Dr. Raj Patel", "specialty": "Neurologist", "experience": 15, "latitude": 19.0700, "longitude": 72.8700, "rating": 4.7, "city": "Mumbai"},
    {"name": "Dr. Priya Singh", "specialty": "General Physician", "experience": 6, "latitude": 19.0900, "longitude": 72.8600, "rating": 4.1, "city": "Mumbai"},
    {"name": "Dr. Kunal Mehta", "specialty": "Orthopedic", "experience": 10, "latitude": 19.1000, "longitude": 72.8800, "rating": 4.3, "city": "Mumbai"},
    {"name": "Dr. Sneha Kapoor", "specialty": "Gynecologist", "experience": 9, "latitude": 19.1100, "longitude": 72.8900, "rating": 4.6, "city": "Mumbai"},
    {"name": "Dr. Arjun Nair", "specialty": "Pediatrician", "experience": 7, "latitude": 19.0650, "longitude": 72.8750, "rating": 4.4, "city": "Mumbai"},
    {"name": "Dr. Rakesh Iyer", "specialty": "ENT Specialist", "experience": 11, "latitude": 19.0850, "longitude": 72.8650, "rating": 4.3, "city": "Mumbai"},
    {"name": "Dr. Meera Joshi", "specialty": "Psychiatrist", "experience": 13, "latitude": 19.0950, "longitude": 72.8950, "rating": 4.5, "city": "Mumbai"},
    {"name": "Dr. Vikram Desai", "specialty": "Cardiologist", "experience": 14, "latitude": 19.1200, "longitude": 72.8700, "rating": 4.8, "city": "Mumbai"},
    {"name": "Dr. Anjali Gupta", "specialty": "Dermatologist", "experience": 5, "latitude": 19.0750, "longitude": 72.8550, "rating": 4.0, "city": "Mumbai"},
    {"name": "Dr. Suresh Reddy", "specialty": "Neurologist", "experience": 16, "latitude": 19.1300, "longitude": 72.8800, "rating": 4.9, "city": "Mumbai"},
    {"name": "Dr. Kavita Menon", "specialty": "Gynecologist", "experience": 12, "latitude": 19.1400, "longitude": 72.8600, "rating": 4.6, "city": "Mumbai"},
    {"name": "Dr. Rohit Shah", "specialty": "Orthopedic", "experience": 9, "latitude": 19.1500, "longitude": 72.8750, "rating": 4.2, "city": "Mumbai"},
    {"name": "Dr. Nitin Agarwal", "specialty": "General Physician", "experience": 8, "latitude": 19.1600, "longitude": 72.8900, "rating": 4.3, "city": "Mumbai"},
    {"name": "Dr. Pooja Bansal", "specialty": "Pediatrician", "experience": 6, "latitude": 19.1700, "longitude": 72.8650, "rating": 4.4, "city": "Mumbai"},
    {"name": "Dr. Deepak Kulkarni", "specialty": "ENT Specialist", "experience": 10, "latitude": 19.1800, "longitude": 72.8800, "rating": 4.2, "city": "Mumbai"},
    {"name": "Dr. Alok Mishra", "specialty": "Psychiatrist", "experience": 11, "latitude": 19.1900, "longitude": 72.8700, "rating": 4.5, "city": "Mumbai"},
    {"name": "Dr. Shalini Rao", "specialty": "Cardiologist", "experience": 13, "latitude": 19.2000, "longitude": 72.8600, "rating": 4.7, "city": "Mumbai"},
    {"name": "Dr. Harsh Vardhan", "specialty": "Orthopedic", "experience": 7, "latitude": 19.2100, "longitude": 72.8900, "rating": 4.1, "city": "Mumbai"},
    {"name": "Dr. Tanya Khanna", "specialty": "Dermatologist", "experience": 6, "latitude": 19.2200, "longitude": 72.8750, "rating": 4.2, "city": "Mumbai"},
    {"name": "Dr. Mohit Jain", "specialty": "General Physician", "experience": 9, "latitude": 19.2300, "longitude": 72.8800, "rating": 4.3, "city": "Mumbai"},
    {"name": "Dr. Ritu Saxena", "specialty": "Gynecologist", "experience": 10, "latitude": 19.2400, "longitude": 72.8700, "rating": 4.6, "city": "Mumbai"},
    {"name": "Dr. Aditya Bose", "specialty": "Neurologist", "experience": 12, "latitude": 19.2500, "longitude": 72.8600, "rating": 4.8, "city": "Mumbai"},
]

for doc in doctors:
    existing = db.query(Doctor).filter(Doctor.name == doc["name"]).first()
    if not existing:
        db.add(Doctor(**doc))

db.commit()
db.close()

print("✅ Doctors seeded successfully!")