import subprocess


def test_hello_world_v1():
  subprocess.run(
    ["python", "hello_world.py"]
  )
  with open("hello.txt", "r") as f:
    line = f.read()
    assert line == "Hello World!\n" 
  subprocess.run(
    ["rm", "hello.txt"]
  )
  