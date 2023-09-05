from database import session
from models import Audition, Role


def print_audition_details(audition):
    print(f"Audition ID: {audition.id}")
    print(f"Actor: {audition.actor}")
    print(f"Location: {audition.location}")
    print(f"Phone: {audition.phone}")
    print(f"Hired: {audition.hired}")
    print(f"Role ID: {audition.role_id}")
    print()


def print_role_details(role):
    print(f"Role ID: {role.id}")
    print(f"Character Name: {role.character_name}")
    print()


audition1 = Audition(actor="Actor 1", location="Location 1", phone=1234567890)
role1 = Role(character_name="Character 1")

audition2 = Audition(actor="Actor 2", location="Location 2", phone=9876543210)
role2 = Role(character_name="Character 2")


audition1.role = role1
audition2.role = role2


session.add_all([audition1, role1, audition2, role2])
session.commit()


print("All Auditions:")
all_auditions = session.query(Audition).all()
for audition in all_auditions:
    print_audition_details(audition)


print("\nAll Roles:")
all_roles = session.query(Role).all()
for role in all_roles:
    print_role_details(role)


role1_hired_auditions = session.query(Audition).filter_by(role_id=role1.id, hired=True).all()
if role1_hired_auditions:
    print(f"\nHired Auditions for Role '{role1.character_name}':")
    for audition in role1_hired_auditions:
        print_audition_details(audition)
else:
    print(f"\nNo auditions have been hired for Role '{role1.character_name}'.")


session.close()
