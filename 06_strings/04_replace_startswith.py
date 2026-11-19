filename = "report_final.pdf"
print(filename.replace("_", " "))
print(filename.replace("final", "draft"))
print(filename.endswith(".pdf"))
print(filename.startswith("report"))

email = "student@lspu.edu.ph"
if email.endswith(".edu.ph") and "@" in email:
    print("Looks like a valid school email")
