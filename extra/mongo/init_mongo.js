db = db.getSiblingDB('kreacity_db')

db.createUser({
    user: "kreacity_user",
    pwd: "kreacity_pass",
    roles: [{
        role: "readWrite",
        db: "kreacity_db"
    }]
})

db.createCollection("user")

db.user.insert({"username": 1,"password":"hi, im god","is_enabled":true})