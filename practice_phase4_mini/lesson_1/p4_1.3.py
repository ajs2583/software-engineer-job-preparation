# Yield concepts


def get_test_session():
    print("Opening Test session")
    try:
        yield "session"
    finally:
        print("Closing test session")


gen = get_test_session()

for i in gen:
    print(i)
