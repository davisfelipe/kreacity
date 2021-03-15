db.createUser({
    user: "kreacity_user",
    pwd: "kreacity_pass",
    roles: [{
        role: "readWrite",
        db: "kreacity_db"
    }]
})
