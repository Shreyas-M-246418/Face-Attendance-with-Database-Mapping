import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL': url'})

ref=db.reference('attendance')

data = {
    "111":
        {
            "name":"Shreyas",
            "school":"C&It",
            "branch":"Ai&Ml",
            "vaild_till":2025,
            "total_attendance":7,
            "year":3,
            "last_attendance_time":"2024-3-29 20:16:06"
        },
    "110":
        {
            "name":"Ratan Tata",
            "school":"Cse",
            "branch":"Ai&Ds",
            "vaild_till":2026,
            "total_attendance":10,
            "year":2,
            "last_attendance_time":"2024-3-29 20:32:06"
        },
    "112":
        {
            "name":"Elon",
            "school":"EEE",
            "branch":"ECE",
            "vaild_till":2024,
            "total_attendance":4,
            "year":4,
            "last_attendance_time":"2024-3-29 20:43:06"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
