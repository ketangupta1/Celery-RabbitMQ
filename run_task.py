from tasks import add

result = add.delay(4,6)

print("Task sent. Waiting for result...")
print(f"Result: {result.get(timeout=10)}")