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

db.user.insert({
    "username": 1,
    "password":"64ef9fb87f9bd92144e366b59861cde62dbb006ee14e539c93d5eabf9fa9f8be",
    "is_enabled":true
})
