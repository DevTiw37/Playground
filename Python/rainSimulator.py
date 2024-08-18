def should_go_outside():
  """Decides whether to go outside based on weather and umbrella availability."""

  is_raining = True  # Replace with a function to check actual weather if needed
  have_umbrella = False  # Replace with a function to check umbrella availability if needed

  if is_raining:
    if have_umbrella:
      print("Go outside!")
    else:
      print("Wait a while.")
  else:
    print("Go outside!")

if __name__ == "__main__":
  should_go_outside()